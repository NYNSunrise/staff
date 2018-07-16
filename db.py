# coding:utf-8

import pymysql
#连接数据库
conn = pymysql.connect(
    database = 'impc',
    host = '172.18.1.77',
    port = 3306,
    user = 'root',
    password ='lan123456',
    charset = 'utf8'
)

#获取游标对象:用来执行SQl语句
cursor = conn.cursor()

#增加数据的函数
def insert(insert_sql,params,flag=True):
    '''
    增加一条数据到数据库中
    :param insert_sql:要执行的SQL语句
    :param params: 序列数据[列表|元组]
    :flag params: True表示增加一条数据；False表示增加多少数据
    :return: 返回执行了多少行数据
    '''
    if flag:
        rows = cursor.execute(insert_sql,params)
    else:
        rows = cursor.executemany(insert_sql,params)
    conn.commit()
    return rows
#查询
def select(sql, params):
    '''从数据库中查询指定的数据'''
    cursor.execute(sql, params)
    result = cursor.fetchall()
    return result

#释放资源
def free():
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()


if __name__ == "__main__":
    sql = "insert into jp_tsukuba (id,email) values(%s,%s)"
    r = insert(sql,(222,y ),flag=True)
    print("增加了{}条数据到数据库".format(r))