```
目录结构：
├── core
│   ├── __init__.py
│   └── SSH.py #主逻辑类文件
├── db
│   ├── db_dict.py
├── __init__.py
├── README.MD
└── start_manager.py #启动程序


=================列表如下:==================
1.1.1.3
1.1.1.2
1.1.1.1
选择操作的主机或者主机组:1.1.1.2 1.1.1.1 1.1.1.3
此次操作的主机如下 ['1.1.1.2', '1.1.1.1', '1.1.1.3']

            请选择
            1：执行参数
            2：上传文件
            3：下载文件:

:1
请输入命令:/sbin/ifconfig eth0
1.1.1.2
 eth0      Link encap:Ethernet  HWaddr 00:50:56:BA:2E:59
          inet addr:1.1.1.2  Bcast:180.153.238.255  Mask:255.255.255.128
          inet6 addr: fe80::250:56ff:feba:2e59/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:12670861348 errors:0 dropped:0 overruns:0 frame:0
          TX packets:119405244 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1075106199576 (1001.2 GiB)  TX bytes:122508199367 (114.0 GiB)


1.1.1.1
 eth0      Link encap:Ethernet  HWaddr 00:50:56:BA:11:39
          inet addr:1.1.1.1  Bcast:180.153.238.255  Mask:255.255.255.128
          inet6 addr: fe80::250:56ff:feba:1139/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:12654829420 errors:0 dropped:0 overruns:0 frame:0
          TX packets:110594637 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1073735872786 (999.9 GiB)  TX bytes:112986780994 (105.2 GiB)


1.1.1.3
 eth0      Link encap:Ethernet  HWaddr 00:50:56:BA:13:9E
          inet addr:1.1.1.3  Bcast:180.153.238.255  Mask:255.255.255.128
          inet6 addr: fe80::250:56ff:feba:139e/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:12701625971 errors:0 dropped:0 overruns:0 frame:0
          TX packets:148658136 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1081462615508 (1007.1 GiB)  TX bytes:156923585274 (146.1 GiB)


执行完毕

            请选择
            1：执行参数
            2：上传文件
            3：下载文件:

:/tmp/sshtest.txt /tmp/sshtest.txt
命令不存在，从新输入

            请选择
            1：执行参数
            2：上传文件
            3：下载文件:

:2
输入本地文件 服务器文件Example：localfile remotefile:/tmp/sshtest.txt /tmp/sshtest.txt
执行完毕

            请选择
            1：执行参数
            2：上传文件
            3：下载文件:

:1
请输入命令:ls /tmp/sshtest.txt
1.1.1.2
 /tmp/sshtest.txt

1.1.1.3
 /tmp/sshtest.txt

1.1.1.1
 /tmp/sshtest.txt

执行完毕

            请选择
            1：执行参数
            2：上传文件
            3：下载文件:

:ls -lh /tmp/sshtest.txt
命令不存在，从新输入

            请选择
            1：执行参数
            2：上传文件
            3：下载文件:

:1
请输入命令:ls -lh /tmp/sshtest.txt
1.1.1.2
 -rw-rw-r-- 1 zhoutao zhoutao 0 4月  12 16:54 /tmp/sshtest.txt

1.1.1.3
 -rw-rw-r-- 1 zhoutao zhoutao 0 4月  12 16:55 /tmp/sshtest.txt

1.1.1.1
 -rw-rw-r-- 1 zhoutao zhoutao 0 4月  12 16:55 /tmp/sshtest.txt

执行完毕

            请选择
            1：执行参数
            2：上传文件
            3：下载文件:

:3
输入本地文件 服务器文件Example： remotefile localpath:/tmp/sshtest.txt /home/zt/sshtset.txt
执行完毕

            请选择
            1：执行参数
            2：上传文件
            3：下载文件:


```