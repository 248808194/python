当然此表你在文件存储时可以这样表示
  name  , age ,phone, dep,year
1,Alex Li,22,13651054608,IT,2013-04-01


id,name,age,phone,dep,year
1,zhoutao,22,18964381759,qt,2015-08-12
2,zhoutao1,23,18864381759,bt,2014-07-12
3,zhoutao2,24,18764381759,at,2013-06-12
4,zhoutao3,25,18664381759,ct,2012-05-12
5,zhoutao4,26,18564381759,it,2011-04-12


读取文件，生成一个dict 格式
{
 idvalue: {
        name: alex,
        age: 22.phone: 13985421571,
        dep: IT,
        year: 2013-04-01
    }
 idvalue: {
        name: alex,
        age: 22.phone: 13985421571,
        dep: IT,
        year: 2013-04-01
    }
}

主函数判断输入
	select 开头
	调用select 函数
		函数内判断:
			判断1：在select 和 from 之间 的字符串放在一个列表中，如果大于1 逐个去匹配，如果小于 1 判断是否为 * 号，如果不为* 也放在列表中 par_list =  [ "name","age" ]
				判断1-2：有没有where 如果有 将where 后面的字符串分别放入到一个列表中，Example: wherepar_list = [ age, ">","22" ]
					如果没有where 直接通过par_list 查出数据
					如果有where 将 wherepar_list 中的参数拿出来查出数据
			函数结束最后将零时列表，字典等清空.
	update 开头
		调用 update 函数
			过滤出set 和 where 之间的值 放入update_dict = {"detp":"it","dep":"it"}
			遍历循环update_dict和 old_dict做对比，如果符合条件则更新old_dict
		更新完成后将old_dict 循环写入到文件中去


	insert 开头
		调用 insert 函数
			先统计出id 将最大的ID拿出来＋１，为插入的ｉｄ做准备
			INSERT INTO table SET name = zhoutao,age = 22,phone = 111111,dep = IT,year = 2014-10-20
			将ｉｎｓｅｒｔ　组合成字典insert_dict = {'name':'zhoutao','age':'22','dep':'it','phone':'18964381759','year':'20140123'}
			检查ｉｎｓｅｒｔ　中的ｐｈｏｎｅ是否存在与old_dict 有则报告已经存在
			没有，将insert_dict 插入　ＩＤ　组合成一个新字典，更新到old_dict下去
			将ｏｌｄ_dict 更新到文件中去



	delete 开头
		调用del 函数 匹配ID 然后删除old_dict 的一个子字典
		将old_dict  写入到文件中去


{'age': None, 'phone': None, 'dep': None, 'year': None, 'name': None}
请输入增删改查语句:select * from info where age > 25
123
6 {'age': '27', 'phone': '18964381259', 'dep': 'IT', 'year': '2018-04-06', 'name': 'Alex5 Li'}
2 {'age': '23', 'phone': '18964381659', 'dep': 'IT', 'year': '2014-04-02', 'name': 'Alex1 Li'}
4 {'age': '25', 'phone': '18964381459', 'dep': 'IT', 'year': '2016-04-04', 'name': 'Alex3 Li'}
3 {'age': '24', 'phone': '18964381559', 'dep': 'IT', 'year': '2015-04-03', 'name': 'Alex2 Li'}
5 {'age': '26', 'phone': '18964381359', 'dep': 'IT', 'year': '2017-04-05', 'name': 'Alex4 Li'}


请输入增删改查语句:select name,age from info where age > 22
123
name Alex5 Li
age 27
name Alex4 Li
age 26
name Alex3 Li
age 25
name Alex1 Li
age 23
name Alex2 Li
age 24

select name,age from info where age = 25
['name', 'age']
name Alex3 Li
age 25

请输入增删改查语句:select name,age from info where age < 25
['name', 'age']
name Alex1 Li
age 23
name Alex Li
age 22
name Alex2 Li
age 24

select name,age from info where phone like 188
['phone', 'like', '188']
like
name Alex4 Li
age 26

select * from info where dep like CC
['dep', 'like', 'CC']
like
6 {'dep': 'CC', 'age': '27', 'name': 'Alex5 Li', 'year': '2018-04-06', 'phone': '18964381259'}




update info set dep=t1t where age=22v



insert INTO table SET name = zhoutao1,age = 22,phone = 111111,dep = IT,year = 2014-10-20


请输入增删改查语句:delete info where id=6
6