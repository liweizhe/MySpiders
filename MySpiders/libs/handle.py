import pymysql
from pymongo import MongoClient
from MySpiders.libs.tables import SALARY, COMPANY_NATURE, SCALE, WELFARE, WORK_NATURE, EXPERIENCE, EDUCATION, INDUSTRY,\
    JOB_KEYS, COMPANY_KEYS
from MySpiders.libs.time_usage import time_usage
import json
from pymysql.err import IntegrityError

DROP_TABLE = "DROP TABLE IF EXISTS {};"

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS {} (
    {}_id INT(2) PRIMARY KEY,
    content CHAR(30) NOT NULL 
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
INSERT_TABLE = """
INSERT INTO {} ({}_id, content) VALUES (%s, %s)
"""

CREATE_JOB = """
DROP TABLE IF EXISTS job;
CREATE TABLE IF NOT EXISTS job(
    id INT(8) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    time VARCHAR(255),
    contact VARCHAR(255),
    Tel VARCHAR(255),
    address VARCHAR(255),
    company VARCHAR(255),
    age VARCHAR(255),
    location VARCHAR(255),
    schedule VARCHAR(255),
    welfare VARCHAR(255),
    response_and_require  VARCHAR(255),
    company_id INT(8),
    salary_id INT(8),
    nature_id INT(8),
    education_id INT(8),
    experience_id INT(8)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

CREATE_COMPANY = """
DROP TABLE IF EXISTS company;
CREATE TABLE IF NOT EXISTS company(
    id INT(8) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    info VARCHAR(1024),
    contact VARCHAR(255),
    Tel VARCHAR(255),
    address VARCHAR(255),
    job VARCHAR(255),
    email VARCHAR(255),
    scale_id INT(8),
    nature_id INT(8),
    industry_id INT(8)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""


def reverse(dict_impl=SALARY):
    tmp_dict = dict()
    for k in dict_impl:
        tmp_dict[dict_impl.get(k)] = k
    # print(json.dumps(tmp_dict, indent=4, ensure_ascii=False).encode('utf8').decode())


def dict_to_list(dict_impl):
    tmp_list = []
    for k in dict_impl:
        tmp_list.append((dict_impl.get(k), k))
    return tmp_list


def insert(table_name, dict_name):
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='xmrc', charset='utf8')
    cursor = conn.cursor()
    cursor.execute(DROP_TABLE.format(table_name))
    cursor.execute(CREATE_TABLE.format(table_name, table_name))
    cursor.executemany(INSERT_TABLE.format(table_name, table_name), dict_to_list(dict_name))
    cursor.execute("SELECT * FROM {}".format(table_name))
    data = cursor.fetchall()
    print('-' * 30, table_name, '-' * 30)
    for d in data:
        print(d)
    print('-' * 30, table_name, '-' * 30)
    cursor.close()
    conn.commit()
    conn.close()


def insert_tables():
    insert(table_name='salary', dict_name=SALARY)
    insert(table_name='scale', dict_name=SCALE)
    insert('welfare', WELFARE)
    insert('work_nature', WORK_NATURE)
    insert('experience', EXPERIENCE)
    insert('education', EDUCATION)
    insert('company_nature', COMPANY_NATURE)
    insert('industry', INDUSTRY)


@time_usage
def update_company(d='xmrc', c='company'):
    collection = MongoClient()[d][c]
    docs = collection.find({}, {'_id': False})
    for doc in docs:
        # COMPANY_NATURE, SCALE, WELFARE, Work_NATURE, EXPERIENCE, EDUCATION, INDUSTRY
        assign_by_dict(doc, 'scale', SCALE)
        assign_by_dict(doc, 'nature', COMPANY_NATURE)
        assign_by_dict(doc, 'industry', INDUSTRY)
        collection.update_one({'id': doc['id']}, {'$set': doc})


@time_usage
def update_job(d='xmrc', c='job'):
    collection = MongoClient()[d][c]
    docs = collection.find({}, {'_id': False})
    for doc in docs:
        # WELFARE, Work_NATURE, EXPERIENCE, EDUCATION
        # assign_by_dict(doc, 'welfare', WELFARE)
        assign_by_dict(doc, 'nature', WORK_NATURE)
        assign_by_dict(doc, 'education', EDUCATION)
        assign_by_dict(doc, 'experience', EXPERIENCE)
        collection.update_one({'id': doc['id']}, {'$set': doc})


@time_usage
def link_job_company(d='xmrc', c1='company', c2='job'):
    company_collectiion = MongoClient()[d][c1]
    job_collection = MongoClient()[d][c2]
    docs = company_collectiion.find({}, {'_id': False})
    for doc in docs:
        for job_id in doc.get('job'):
            tmp_doc = job_collection.find_one({'id': job_id}, {'_id': False})
            if tmp_doc:
                tmp_doc['company_id'] = doc.get('id')
                job_collection.update_one({'id': tmp_doc['id']}, {'$set': tmp_doc})


def assign_by_dict(source_dict, key, data_dict):
    value = source_dict.get(key)
    # print(value)
    if source_dict.get(key) is None:
        return
    else:
        for k in data_dict:
            # print(k, value)
            if k in value:
                source_dict['{}_id'.format(key)] = data_dict[k]
                # print('{}_id'.format(key), data_dict[k])


@time_usage
def select_by_keys(d='xmrc', c='job', selector=JOB_KEYS, limit_flag=True):
    conn = pymysql.connect(host='localhost', user='root', password='123456', database='xmrc', charset='utf8')
    cursor = conn.cursor()
    connection = MongoClient()[d][c]
    if limit_flag:
        docs = connection.find({}, selector).limit(20)
    else:
        docs = connection.find({}, selector)
    for doc in docs:
        for k in selector:
            if doc.get(k):
                continue
            doc[k] = None
        doc.pop('_id', None)
        # if c == 'company' and doc.get('logo'):
        #     doc['logo'] = str(doc.get('logo'), encoding='utf-8')
        sql = get_insert_keys(doc, table_name=c) + get_insert_values(doc)
        # print(sql)
        try:
            cursor.execute(sql)
        except IntegrityError as e:
            print(e)
        # print(json.dumps(doc, indent=4, ensure_ascii=False).encode('utf-8').decode())
    cursor.close()
    conn.commit()
    conn.close()


def get_insert_keys(dict_impl, table_name='job'):
    sql = 'INSERT INTO {} ('.format(table_name)
    for k in dict_impl:
        sql += k + ','
    # print(sql)
    sql = sql[:-1]
    sql += ') '
    return sql


def get_insert_values(dict_impl):
    sql = 'VALUES ('
    for k in dict_impl:
        if dict_impl.get(k):
            # if isinstance(dict_impl.get(k), int):
            #     sql += '{},'.format(dict_impl.get(k))
            # else:
            #     sql += '"{}",'.format(dict_impl.get(k))
            sql += '"{}",'.format(str(dict_impl.get(k)))
        else:
            sql += '"",'

    sql = sql[:-1]
    sql += ');'
    return sql


@time_usage
def remove_redundant(d='xmrc', c='job'):
    collection = MongoClient()[d][c]
    if c == 'job':
        key = 'company_id'
    else:
        key = 'job'
    docs = collection.find()
    i = 0
    for doc in docs:
        if not doc.get(key):
            collection.delete_one({'id': doc.get('id')})
            i += 1
    print(i)


if __name__ == '__main__':
    # reverse()
    # insert(table_name='salary')
    # insert_tables()
    # update_company()
    # update_job()
    # link_job_company()
    # select_by_keys()
    # select_by_keys(c='company', selector=COMPANY_KEYS)
    # get_insert_keys(JOB_KEYS)
    # print(get_insert_values(JOB_KEYS))
    # select_by_keys(c='job', selector=JOB_KEYS, limit_flag=False)
    # select_by_keys(c='company', selector=COMPANY_KEYS, limit_flag=False)
    # select_by_keys(c='job', selector=JOB_KEYS)
    # select_by_keys(c='company', selector=COMPANY_KEYS)
    # remove_redundant()
    # remove_redundant(c='company')
    pass
