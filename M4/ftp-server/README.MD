```
目录结构
ftp-server/                             #项目主目录
├── ftp_client                          #客户端程序
│   ├── core                            #客户端核心代码目录
│   │   └── socket_class.py             #客户端核心代码
│   ├── __init__.py
│   └── userdata                        #用户家目录地址
│       └── zhoutao
│           ├── 1.txt
│           ├── 2.txt
│           └── 800.img
├── ftp_server                          #服务器端核心程序
│   ├── conf                            #服务器端配置文件
│   │   ├── __init__.py
│   │   └── userdb.json                 #服务器端数据库文件
│   ├── core
│   │   ├── __init__.py
│   │   ├── mysocketserver.py           #服务器核心代码
│   ├── __init__.py
│   └── userdata                        #服务器端存储
│       └── zhoutao
│           ├── 2.txt
│           ├── 800.img
│           ├── dir
│           ├── dir1
│           │   ├── dir1.txt
│           │   └── dir2
│           │       └── dir2.txt
│           ├── seektest.py
│           └── test.txt
├── __init__.py
├── README.mkd
├── start_ftp_client.py               #客户端启动文件
└── start_ftp_server.py               #服务器端启动文件


操作example:
请先登录
username:zhoutao
password:123456
欢迎zhoutao来到ftpserver

        【帮助信息】：
        可执行命令：
        ls：      查看目录内容
        cd：      切换目录
        get：     下载文件
        put：     上传文件
        help: 查看帮助文件

[zhoutao@127.0.0.1]userdata/zhoutao:ls
2.txt
test.txt
dir1
seektest.py
dir
[zhoutao@127.0.0.1]userdata/zhoutao:cd dir1
[zhoutao@127.0.0.1]userdata/zhoutao/dir1:ls
dir2
dir1.txt
[zhoutao@127.0.0.1]userdata/zhoutao/dir1:cd dir2
[zhoutao@127.0.0.1]userdata/zhoutao/dir1/dir2:ls
dir2.txt
[zhoutao@127.0.0.1]userdata/zhoutao/dir1/dir2:cd ..
[zhoutao@127.0.0.1]userdata/zhoutao/dir1:cd ../dir
[zhoutao@127.0.0.1]userdata/zhoutao/dir:ls
[zhoutao@127.0.0.1]userdata/zhoutao/dir:cd ../dir1
[zhoutao@127.0.0.1]userdata/zhoutao/dir1:ls
dir2
dir1.txt
[zhoutao@127.0.0.1]userdata/zhoutao/dir1:cd ..
[zhoutao@127.0.0.1]userdata/zhoutao:ls
2.txt
test.txt
dir1
seektest.py
dir
[zhoutao@127.0.0.1]userdata/zhoutao:put 800.img
====================================================================================================>100%file:800.img put   done
[zhoutao@127.0.0.1]userdata/zhoutao:put 150.img
====================================================================================================>100%file:150.img put   done
[zhoutao@127.0.0.1]userdata/zhoutao:put 100.img
not enough space pls called administrators #触发磁盘配额
[zhoutao@127.0.0.1]userdata/zhoutao:pwd
userdata/zhoutao


#断点续传
[zhoutao@127.0.0.1]userdata/zhoutao:get 800.img
===========>11%^CTraceback (most recent call last): #ctrl+c 程序中断，中断前传递了%11
zt@zt-All-Series:~/PycharmProjects/51cto_python_homework/M4/ftp-server$ python3.5 start_ftp_client.py
请先登录
username:zhoutao
password:123456
欢迎zhoutao来到ftpserver

        【帮助信息】：
        可执行命令：
        ls：      查看目录内容
        cd：      切换目录
        get：     下载文件
        put：     上传文件
        help: 查看帮助文件

[zhoutao@127.0.0.1]userdata/zhoutao:get 800.img #再次登录get 开始断点续传
文件800.img未传完，开始断点续传
====================================================================================================>100%file:800.img get  done




```