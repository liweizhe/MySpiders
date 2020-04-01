from pymongo import MongoClient
import re
from MySpiders.libs.time_usage import time_usage
from MySpiders.libs.tables import FORMATED_SALARY


@time_usage
def analyse_salary(d='xmrc', c='job'):
    collection = MongoClient()[d][c]
    query = {
        # '$limit': 10
    }
    docs = collection.find(query, {'_id': 0})
    pattern_range = re.compile(r'(?<=参考月薪： )\d+-\d+\.?')
    pattern_top = re.compile(r'(?<=-)\d+\.?')
    salary_set = set()
    formated_salary = FORMATED_SALARY
    salary_id = 0
    salary_range = formated_salary[salary_id]
    for doc in docs:
        salary = doc.get('salary')
        if not salary:
            doc['salary_id'] = salary_id
            doc['salary_range'] = salary_range
            collection.update_one({'id': doc['id']}, {'$set': doc})
            continue
        salary = pattern_range.findall(salary)
        if salary:
            top_salary = int(pattern_top.findall(salary[0])[0])
            salary_set.add(top_salary)
            if top_salary < 1000:
                salary_id = 0
                salary_range = formated_salary[salary_id]
            elif top_salary <= 3000:
                salary_id = 1
                salary_range = formated_salary[salary_id]
            elif top_salary <= 5000:
                salary_id = 2
                salary_range = formated_salary[salary_id]
            elif top_salary <= 8000:
                salary_id = 3
                salary_range = formated_salary[salary_id]
            elif top_salary <= 10000:
                salary_id = 4
                salary_range = formated_salary[salary_id]
            elif top_salary <= 12000:
                salary_id = 5
                salary_range = formated_salary[salary_id]
            elif top_salary <= 15000:
                salary_id = 6
                salary_range = formated_salary[salary_id]
            elif top_salary <= 20000:
                salary_id = 7
                salary_range = formated_salary[salary_id]
            elif top_salary <= 30000:
                salary_id = 8
                salary_range = formated_salary[salary_id]
            else:
                salary_id = 9
                salary_range = formated_salary[salary_id]
        doc['salary_id'] = salary_id
        doc['salary_range'] = salary_range
        collection.update_one({'id': doc['id']}, {'$set': doc})
        # print(doc['_id'])
        # for k in doc:
        #     print(k, doc.get(k))
    for salary in salary_set:
        print(salary)


# @time_usage
def analyse_set(db_name='xmrc', clt_name='job', key='welfare', split_char='、'):
    collection = MongoClient()[db_name][clt_name]
    # docs = collection.find().limit(1000)
    docs = collection.find()
    pattern = re.compile(r'(?<=： )[\s\S]+')
    tmp_set = set()
    tmp_dict = {}
    for doc in docs:
        # print(doc.get(key))
        data = doc.get(key)
        if data:
            # print(data)
            data = pattern.findall(data)
            if data:
                data = data[0]
                data_list = data.split(split_char)
                for d in data_list:
                    if not tmp_dict.get(d):
                        tmp_dict[d] = 1
                    else:
                        tmp_dict[d] += 1
                    tmp_set.add(d)
    # for s in tmp_set:
    #     print(s)
    w = sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True)
    i = 0
    for l in w:
        i += 1
        print('    \''+l[0]+'\': ' + str(i)+',  # ' + str(l[1]))


if __name__ == '__main__':
    # analyse_salary()
    analyse_set()
    # analyse_set(key='nature')
    # analyse_set(key='experience')
    # analyse_set(key='education')
    # analyse_set(clt_name='company', key='nature', split_char='/')
    # analyse_set(clt_name='company', key='industry', split_char='、')
    # analyse_set(clt_name='company', key='scale')
    # analyse_set(key='age')
    pass


