# 文件主目录

###　目录结构
```
kcb 
├── conf 配置文件目录
│   ├── __init__.py
│   ├── settings.py　				＃存放学校ｐｉｃｋｌｅ序列化后的对象文件
├── core
│   ├── __init__.py
│   ├── lessons.py					＃课程类文件
│   ├── main.py						＃主逻辑交互文件
│   ├── schools.py					＃学校类文件
│   ├── students.py					＃学生类文件
│   ├── techers.py					＃老师类文件
│   ├── write_read_obj.py			＃ｐｉｃｋｌｅ序列化反序列化类
├── db
│   ├── bj_school					＃保存的学校序列化文件
│   ├── __init__.py
│   └── sh_school					＃保存的学校序列化文件
├── __init__.py
├── KCB.py							＃程序入口文件
├── README.MD
└── views							＃视图目录
    ├── __init__.py
    ├── manager_view.py				＃后台管理视图
    ├── stu_view.py					＃学生视图
    ├── techer_view.py				＃老师视图


```

###　　学生操作演示
```
        请选择管理视图
        １：学生视图
        ２：教师视图
        ３：管理视图
        
:>1
当前校区如下bj_school
当前校区如下sh_school
请选择校区:sh_school 
/home/zt/PycharmProjects/51cto_python_homework/M3/kcb/db/sh_school
{'linux_s2': {'lesson_name': 'linux', 'techername': 'techer_bb', 'students': []}, 'linux_s1': {'lesson_name': 'linux', 'techername': 'techer_cc', 'students': [['stu002', '99']]}}
请输入新学员姓名:stu003
<kcb.core.schools.School object at 0x7f82d4fd4eb8>
请输入学费:1200000
{'stu002': 0}
{'stu002': 0, 'stu003': 1200000}
是否需要现在选择班级Y/Ny
当前可选班级为:linux_s2
当前可选班级为:linux_s1
选择班级linux_s2
{'linux_s2': {'lesson_name': 'linux', 'techername': 'techer_bb', 'students': [['stu003', None]]}, 'linux_s1': {'lesson_name': 'linux', 'techername': 'techer_cc', 'students': [['stu002', '99']]}}

```
###　　老师操作演示

```
        请选择管理视图
        １：学生视图
        ２：教师视图
        ３：管理视图
        
:>2
请输入讲师姓名：techer_cc

             1:查看学员花名册
             2：选择授课班级
            
请选择操作1
学生姓名:stu002 ,学生成绩:99
是否修改学生成绩:Y/Ny
选择学生:stu002
从新设定分数90
学生stu002 原成绩99　成绩修改为90
{'linux_s1': {'lesson_name': 'linux', 'students': [['stu002', '90']], 'techername': 'techer_cc'}, 'linux_s2': {'lesson_name': 'linux', 'students': [['stu003', None]], 'techername': 'techer_bb'}}

             1:查看学员花名册
             2：选择授课班级
            
请选择操作
```

###　　管理操作演示
```
        请选择管理视图
        １：学生视图
        ２：教师视图
        ３：管理视图
        
:>3
当前校区 sh_school
当前校区 bj_school
请选择校区进行操作：sh_school

        请选择管理功能
        １：创建讲师
        ２：创建班级
        ３：创建课程
        4:推出
    　　　　　
请选择管理功能：1
添加老师，请输入老师姓名:techer_tom

        请选择管理功能
        １：创建讲师
        ２：创建班级
        ３：创建课程
        4:推出
    　　　　　
请选择管理功能：2
您要创建的班级名称:linux_s3
课程如下linux
课程如下python
班级关联课程:linux
班级:linux_s3 成功关联课程内容linux
当前学校老师如下
['techer_cc', 'techer_bb', 'techer_tom']
techer_id:	0 techer_name:	techer_cc
techer_id:	1 techer_name:	techer_bb
techer_id:	2 techer_name:	techer_tom
请输入老师工号ID：2
{'linux_s1': {'lesson_name': 'linux', 'students': [['stu002', '90']], 'techername': 'techer_cc'}, 'linux_s3': {'lesson_name': 'linux', 'students': [], 'techername': 'techer_tom'}, 'linux_s2': {'lesson_name': 'linux', 'students': [['stu003', None]], 'techername': 'techer_bb'}}

        请选择管理功能
        １：创建讲师
        ２：创建班级
        ３：创建课程
        4:推出
    　　　　　
请选择管理功能：3
课程名:java
课程价格:20
课程周期:1mouth
java 20 1mouth

        请选择管理功能
        １：创建讲师
        ２：创建班级
        ３：创建课程
        4:推出
    　　　　　
请选择管理功能：4

        请选择管理视图
        １：学生视图
        ２：教师视图
        ３：管理视图
        
```
