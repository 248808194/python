```python
ATM/　 # 程序主目录
├── bin
│   ├── atm.py  执行程序　程序执行从这里开始
│   └── __init__.py
├── conf　＃　存放一些配置文件
│   ├── __init__.py
│   └── settings.py　配置文件程序
├── core　＃　主要程序逻辑
│   ├── account.py　　账户操作相关　还款，取款，消费等
│   ├── authz.py　账户认证模块
│   ├── db_handlers.py　＃　读取，写入用户配置文件等
│   ├── historys.py　＃　保存账户的历史信息等
│   ├── __init__.py
│   ├── logger.py　日志记录模块
│   ├── main.py　＃　主程序逻辑交互
│   ├── managers.py　＃　后台管理模块
├── db
│   ├── accounts　＃　db/account/*.json　存放用户数据文件等
│   │   └── zhoutao.json
│   └── __init__.py
├── logs　＃　日志记录目录，保存类型为/account/years/mouth/{access.log,tran.log} # access.log 登录日志，tran.log 消费日志
│   ├── __pycache__
│   └── zhoutao
│       ├── 2017
│       │   ├── 01
│       │   │   ├── access.log
│       │   │   └── tran.log
│       │   └── 02
│       │       ├── access.log
│       │       └── tran.log
│       └── 2018
│           └── 01
│               ├── access.log
│               └── tran.log
└── 购物商城  # 原来的ｓｈｏｐｉｎｇｍａｉｌ　程序接入
    ├── login.py
    ├── prodlist.json
    ├── userdb
    ├── zhoutao_cart_histtory
    └── 购物车.png

 程序说明
	用户登录ａｔｍ　可进行常规操作如商城购物．还款，取款，打印账单等操作
```
