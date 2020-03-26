import json
import pymysql
from pymongo import MongoClient
from MySpiders.libs.tables import SALARY, COMPANY_NATURE, SCALE, WELFARE, WORK_NATURE, EXPERIENCE, EDUCATION, INDUSTRY
from MySpiders.libs.time_usage import time_usage

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


def reverse(dict_impl=SALARY):
    tmp_dict = dict()
    for k in dict_impl:
        tmp_dict[dict_impl.get(k)] = k
    print(json.dumps(tmp_dict, indent=4, ensure_ascii=False).encode('utf8').decode())


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


if __name__ == '__main__':
    # reverse()
    # insert(table_name='salary')
    # insert_tables()
    # update_company()
    # update_job()
    link_job_company()
    pass
