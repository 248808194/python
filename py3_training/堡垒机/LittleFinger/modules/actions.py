#_*_coding:utf-8_*_
__author__ = 'Alex Li'


from conf import settings
from conf import action_registers
from modules import utils


def help_msg(): #输入错误帮助函数,
    '''
    print help msgs
    :return:
    '''
    print("\033[31;1mAvailable commands:\033[0m") #打印出未知的命令行参数,
    for i in action_registers.actions: #循环的便利action_registers.actions字典
        print("\t",i)

def excute_from_command_line(argvs):
    if len(argvs) < 2: #计算传入的长度,如果小于2就打印help_msg函数,并且退出
        help_msg()
        exit()
    if argvs[1] not in action_registers.actions: #如果传入的参数１　不在action_registers.actions 字典ｋｅｙ　下  则调用utils.print_err 打印所输命令不不存在．
        utils.print_err("Command [%s] does not exist!" % argvs[1], quit=True) #
    action_registers.actions[argvs[1]](argvs[1:]) # 如果存在，获取到传入参数相对于的ｖａｌｕｅ函数，传入参数（参数为列表第０［程序文件名］个除外的所有参数）



