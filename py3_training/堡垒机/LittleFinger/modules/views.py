#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from modules import models
from modules.db_conn import engine,session
from modules.utils import print_err,yaml_parser
from modules import common_filters
from modules import ssh_login
def auth(): # 认证模块,
    '''
    do the user login authentication
    :return:
    '''
    count = 0
    while count <3:
        username = input("\033[32;1mUsername:\033[0m").strip()
        if len(username) ==0:continue
        password = input("\033[32;1mPassword:\033[0m").strip()
        if len(password) ==0:continue
        user_obj = session.query(models.UserProfile).filter(models.UserProfile.username==username,
                                                            models.UserProfile.password==password).first()
        if user_obj: #如果用户名密码能吵到，则返回一个user_obj对象
            return user_obj
        else:
            print("wrong username or password, you have %s more chances." %(3-count-1)) #　否则ｃｏｕｎｔ　＋１　继续ｗｈｉｌｅ　
            count +=1
    else:
        print_err("too many attempts.")

def welcome_msg(user): #欢迎函数
    WELCOME_MSG = '''\033[32;1m
    ------------- Welcome [%s] login LittleFinger -------------
    \033[0m'''%  user.username
    print(WELCOME_MSG)



def log_recording(user_obj,bind_host_obj,logs):
    '''
    flush user operations on remote host into DB
    :param user_obj:
    :param bind_host_obj:
    :param logs: list format [logItem1,logItem2,...]
    :return:
    '''
    print("\033[41;1m--logs:\033[0m",logs)

    session.add_all(logs)
    session.commit()

def start_session(argvs): #　登录系统
    print('going to start sesssion ')
    user = auth() #调用用户认证模块　ｕｓｅｒ　＝　ｒｅｔｕｒｎ　的user_obj　
    if user:
        welcome_msg(user)
        print(user.bind_hosts) #返回ｕｓｅｒid user hostname，未分组主机
        print(user.groups) #返回　有分组的足记
        exit_flag = False #设定一个标志位
        while not exit_flag: #此ｗｈｉｌｅ　为打印出用户管理的所有机器，包括分组未分组
            if user.bind_hosts:
                print('\033[32;1mz.\tungroupped hosts (%s)\033[0m' %len(user.bind_hosts) ) #打印出未分组主机
            for index,group in enumerate(user.groups): #打印出以分组主机
                print('\033[32;1m%s.\t%s (%s)\033[0m' %(index,group.name,  len(group.bind_hosts)) )

            choice = input("[%s]:" % user.username).strip() #让用户选择输入
            if len(choice) == 0:continue
            if choice == 'z': #如果输入ｚ
                print("------ Group: ungroupped hosts ------" ) #　
                for index,bind_host in enumerate(user.bind_hosts): #打印出未分组的机器
                    print("  %s.\t%s@%s(%s)"%(index,
                                              bind_host.remoteuser.username,
                                              bind_host.host.hostname,
                                              bind_host.host.ip_addr,
                                              ))
                print("----------- END -----------" )
            elif choice.isdigit(): #如果选择的是数字
                choice = int(choice)
                if choice < len(user.groups):
                    print("------ Group: %s ------"  % user.groups[choice].name ) #打印出分组机器
                    for index,bind_host in enumerate(user.groups[choice].bind_hosts):
                        print("  %s.\t%s@%s(%s)"%(index,
                                                  bind_host.remoteuser.username,
                                                  bind_host.host.hostname,
                                                  bind_host.host.ip_addr,
                                                  ))
                    print("----------- END -----------" )

                    #host selection
                    while not exit_flag: #此ｗｈｉｌｅ　选择相应主机操作
                        user_option = input("[(b)back, (q)quit, select host to login]:").strip()
                        if len(user_option)==0:continue
                        if user_option == 'b':break # 选择ｂ，ｂｒｅａｋ跳出循环，
                        if user_option == 'q': #选择ｑ修改标志位为ｔｒｕｅ跳出大循环
                            exit_flag=True
                        if user_option.isdigit(): #如果选择的是数字
                            user_option = int(user_option)
                            if user_option < len(user.groups[choice].bind_hosts) :
                                print('host:',user.groups[choice].bind_hosts[user_option]) #打印出ｈｏｓｔ　
                                print('audit log:',user.groups[choice].bind_hosts[user_option].audit_logs) #打印出ｌｏｇ
                                ssh_login.ssh_login(user,
                                                    user.groups[choice].bind_hosts[user_option], #具体操作主机的对象
                                                    session,
                                                    log_recording) #执行ssh_login.ssh_login 传入ｕｓｅｒ.obj,主机ｉｐ地址，ｓｅｓｓｉｏｎ　， log_recording函数
                else:
                    print("no this option..")


def stop_server(argvs):
    pass

def create_users(argvs): #　创建堡垒机本机用户
    '''
    create little_finger access user
    :param argvs:
    :return:
    '''
    if '-f' in argvs: #先判断有没有-f参数
        user_file  = argvs[argvs.index("-f") +1 ] #通过ｉｎｄｅｘ计算出－ｆ的索引值，在通过＋１　获得ｕｓｅｒｆｉｌｅ
    else:
        print_err("invalid usage, should be:\ncreateusers -f <the new users file>",quit=True)

    source = yaml_parser(user_file) #通过ｙａｍｌ＿ｐａｒｓｅｒ将文件序列化为字典赋值给ｓｏｕｒｃｅ
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.UserProfile(username=key,password=val.get('password'))
            if val.get('groups'):
                groups = session.query(models.Group).filter(models.Group.name.in_(val.get('groups'))).all()
                if not groups:
                    print_err("none of [%s] exist in group table." % val.get('groups'),quit=True)
                obj.groups = groups
            if val.get('bind_hosts'):
                bind_hosts = common_filters.bind_hosts_filter(val)
                obj.bind_hosts = bind_hosts
            #print(obj)
            session.add(obj)
        session.commit()


def create_groups(argvs): #创建主机组
    '''
    create groups
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        group_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreategroups -f <the new groups file>",quit=True)
    source = yaml_parser(group_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.Group(name=key)
            if val.get('bind_hosts'):
                bind_hosts = common_filters.bind_hosts_filter(val)
                obj.bind_hosts = bind_hosts

            if val.get('user_profiles'):
                user_profiles = common_filters.user_profiles_filter(val)
                obj.user_profiles = user_profiles
            session.add(obj)
        session.commit()


def create_hosts(argvs): #创建主机
    '''
    create hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        hosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new hosts file>",quit=True)
    source = yaml_parser(hosts_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.Host(hostname=key,ip_addr=val.get('ip_addr'), port=val.get('port') or 22)
            session.add(obj)
        session.commit()


def create_bindhosts(argvs): #创建主机，用户，等对应关系
    '''
    create bind hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        bindhosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new bindhosts file>",quit=True)
    source = yaml_parser(bindhosts_file)
    if source:
        for key,val in source.items():
            #print(key,val)
            host_obj = session.query(models.Host).filter(models.Host.hostname==val.get('hostname')).first()
            assert host_obj
            for item in val['remote_users']:
                print(item )
                assert item.get('auth_type')
                if item.get('auth_type') == 'ssh-passwd':
                    remoteuser_obj = session.query(models.RemoteUser).filter(
                                                        models.RemoteUser.username==item.get('username'),
                                                        models.RemoteUser.password==item.get('password')
                                                    ).first()
                else:
                    remoteuser_obj = session.query(models.RemoteUser).filter(
                                                        models.RemoteUser.username==item.get('username'),
                                                        models.RemoteUser.auth_type==item.get('auth_type'),
                                                    ).first()
                if not remoteuser_obj:
                    print_err("RemoteUser obj %s does not exist." % item,quit=True )
                bindhost_obj = models.BindHost(host_id=host_obj.id,remoteuser_id=remoteuser_obj.id)
                session.add(bindhost_obj)
                #for groups this host binds to
                if source[key].get('groups'):
                    group_objs = session.query(models.Group).filter(models.Group.name.in_(source[key].get('groups') )).all()
                    assert group_objs
                    print('groups:', group_objs)
                    bindhost_obj.groups = group_objs
                #for user_profiles this host binds to
                if source[key].get('user_profiles'):
                    userprofile_objs = session.query(models.UserProfile).filter(models.UserProfile.username.in_(
                        source[key].get('user_profiles')
                    )).all()
                    assert userprofile_objs
                    print("userprofiles:",userprofile_objs)
                    bindhost_obj.user_profiles = userprofile_objs
                #print(bindhost_obj)
        session.commit()


def create_remoteusers(argvs): # 创建远程用户
    '''
    create remoteusers
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        remoteusers_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_remoteusers -f <the new remoteusers file>",quit=True)
    source = yaml_parser(remoteusers_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models.RemoteUser(username=val.get('username'),auth_type=val.get('auth_type'),password=val.get('password'))
            session.add(obj)
        session.commit()


def syncdb(argvs):
    print("Syncing DB....")
    models.Base.metadata.create_all(engine) #创建所有表结构
