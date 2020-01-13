import random

from pymysql import *


conn = connect(host='localhost', port=3306, user='root', password='123456',
               database='heyuyang', charset='utf8')

cs1 = conn.cursor()
try:
    # for i in range(10,99):
    #     cs1.execute("insert into test_index(id, name)values(0,'嘿嘿%d')" % i)

    for i in range(100000):
        cs1.execute("insert into t_index(id, name ,age)values(0,'哈哈%d', %d)" % (i, random.randint(15, 90)))

    conn.commit()
    print("添加成功")

except Exception as e:
    conn.rollback()
    print(e)
cs1.close()
conn.close()


# mysql  事务 ACID
"""
用于处理操作量大，复杂度高的数据
A原子性 事务不可在分割
C一致性 数据库必须从一个一致性状态到另一个一致性状态
I隔离性 在事务最终提交之前所做的操作 对其他事务不可见
D持久性  一旦事务提交，则其所作的修改会永久保存在数据库，即使数据库崩溃也不会丢失
开启事务begin start transaction;
提交 commit
"""

# mysql 视图 view
"""
作用: 方便查询,保护数据,提高代码重用性,让数据更加清晰
创建视图 create view 视图名称  as 查询结果
视图使用 select * from 视图
删除视图 drop view 视图名称;
查看视图定义 : show create view 视图名称

"""

# mysql 索引 index
"""
set profiling=1 开始操作即使
查看操作时间 show profiles;
作用: 加快查询效率
什么时候加  数据量大，字段常用    数据表主键自动作为索引
创建索引 creat index 索引名称 on 表名(列名[非int加长度]);
查看索引 show index from 表名;
删除索引 drop index 索引名称 on 表名;
"""