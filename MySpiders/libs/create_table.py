import pymysql
from pymongo import MongoClient
from MySpiders.libs.tables import SALARY, COMPANY_NATURE, SCALE, WELFARE, WORK_NATURE, EXPERIENCE, EDUCATION, INDUSTRY,\
    JOB_KEYS, INSERT_TABLE, CREATE_TABLE, DROP_TABLE, SCHEDULE
from MySpiders.libs.time_usage import time_usage
from pymysql.err import IntegrityError, DataError, InternalError
import re


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
    conn = pymysql.connect(host='localhost', user='root', password='', database='xmrc', charset='utf8')
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
    insert('schedule', SCHEDULE)


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
def select_by_keys(d='xmrc', c='job', selector=JOB_KEYS, limit=0):
    conn = pymysql.connect(host='localhost', user='root', password='', database='xmrc', charset='utf8')
    cursor = conn.cursor()
    connection = MongoClient()[d][c]
    if limit > 0:
        docs = connection.find({}, selector).limit(limit)
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
        # sql = get_insert_keys(doc, table_name=c) + get_insert_values(doc)
        # print(sql)
        sql = get_insert_sql(dict_impl=doc, table_name=c)
        # print(sql)
        try:
            cursor.execute(sql)
        except IntegrityError as e:
            print(e)
            # print(sql)
        except DataError as e:
            print(e)
            # print(sql)
        except InternalError as e:
            print(e)
            # print(sql)
        # print(json.dumps(doc, indent=4, ensure_ascii=False).encode('utf-8').decode())
    cursor.close()
    conn.commit()
    conn.close()


def get_insert_sql(dict_impl, table_name='job'):
    keys = 'INSERT INTO {} ('.format(table_name)
    values = 'VALUES ('
    age_pattern = re.compile('\d+')
    time_pattern = re.compile('\d+-\d+-\d+')
    for k in dict_impl:
        value = dict_impl.get(k)
        if 'age' == k:
            keys += 'age_lower,age_upper,'
            if value:
                ages = age_pattern.findall(value)
                values += '{},{},'.format(ages[0], ages[1])
            else:
                values += 'NULL,NULL,'
            continue
        if 'time' == k:
            keys += 'date_lower,date_upper,'
            if value:
                times = time_pattern.findall(value)
                try:
                    values += '"{}","{}",'.format(times[0], times[1])
                except IndexError:
                    print(value, times)
                    values += 'NULL,NULL,'
            else:
                values += 'NULL,NULL,'
            continue

        keys += k + ','
        if value:
            if isinstance(value, str):
                if '职位要求:' in value:
                    lst = value.split(':')
                    value = ':'.join(lst[1:])

                    if value:
                        value = value.strip()
                        values += '"{}",'.format(value)
                    else:
                        values += 'NULL,'
                    continue
                if '：' in value:
                    lst = value.split('：')
                    value = '：'.join(lst[1:])
                    value = value.strip()
                    # value = value.strip('\r\n')
                    if value:
                        # if k == 'response_and_require' and len(value) <= 10:
                        #     print(value)
                        values += '"{}",'.format(value)
                    else:
                        values += 'NULL,'
                else:
                    values += '"{}",'.format(value)
            else:
                values += '"{}",'.format(value)
        else:
            values += 'NULL,'
    # print(sql)
    keys = keys[:-1]
    keys += ') '
    values = values[:-1]
    values += ');'
    return keys + values


@time_usage
def analyse_job(d='xmrc', c='job', key='welfare', table=WELFARE):
    collection = MongoClient()[d][c]
    docs = collection.find({}, {'_id': False})
    for doc in docs:
        value = doc.get(key)
        if value:
            tmp_lst = []
            for k in table:
                if k in value:
                    tmp_lst.append(table[k])
            doc[key] = tmp_lst
            collection.update_one({'id': doc['id']}, {'$set': doc})


@time_usage
def create_job_linked_table(d='xmrc', c='job', key='welfare', limit=0):
    collection = MongoClient()[d][c]
    if limit > 0:
        docs = collection.find().limit(limit)
    else:
        docs = collection.find()
    conn = pymysql.connect(host='localhost', user='root', password='', database='xmrc', charset='utf8')
    cursor = conn.cursor()
    j_id = 'job_id'
    k_id = '{}_id'.format(key)
    table_name = 'job_{}'.format(key)

    for doc in docs:
        lst = doc.get(key)
        if lst and isinstance(lst, list):
            job_id = doc.get('id')
            for l in lst:
                tmp_dict = dict()
                tmp_dict[k_id] = l
                tmp_dict[j_id] = job_id
                sql = get_insert_sql(tmp_dict, table_name)
                try:
                    cursor.execute(sql)
                except Exception as e:
                    print(e)
                    print(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # reverse()
    # insert(table_name='salary')
    # insert_tables()
    # update_company()
    # update_job()
    # link_job_company()
    # select_by_keys(limit=0)
    # select_by_keys(c='company', selector=COMPANY_KEYS, limit=0)
    # select_by_keys(c='job', selector=JOB_KEYS, limit_flag=False)
    # select_by_keys(c='job', selector=JOB_KEYS)
    # select_by_keys(c='company', selector=COMPANY_KEYS)
    # remove_redundant()
    # remove_redundant(c='company')
    # analyse_job()
    # analyse_job(key='schedule', table=SCHEDULE)
    # create_job_linked_table(limit=0)
    # create_job_linked_table(key='schedule', limit=0)
    pass
