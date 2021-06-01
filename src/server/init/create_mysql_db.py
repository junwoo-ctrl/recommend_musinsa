import random
from typing import List, Dict
from clize import run

from server.common.database import Database
from server.util.tools import EnvTool


CREATE_RECOMMEND_TABLE_QUERY = """
    CREATE TABLE {env}.recommend_store (
        `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
        `recommend_word` text,
        PRIMARY KEY (`id`),
        FULLTEXT INDEX ngram_idx(`recommend_word`) WITH PARSER ngram
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""


def init_db_scheme():
    statement = CREATE_RECOMMEND_TABLE_QUERY.format(env=EnvTool.get_env())
    dbw = Database()
    try:
        resp = dbw.query(statement)
        print(resp)
    except Exception as e:
        print(str(e))


def upload_data():
    default_mock_data = {'recommend_word': 'nike'}
    mock_data_set: List[Dict] = get_mock_data_set(default_mock_data)

    dbw = Database()
    table_name = 'recommend_store'
    try:
        table = dbw.db[table_name]
        table.insert_many(mock_data_set)
    except Exception as e:
        print(str(e))
    finally:
        dbw.close()


def get_mock_data_set(default_mock_data: Dict[str, str]):
    keyword = list(default_mock_data.values())[0]

    iter_num = 50
    ret = []
    for x in range(iter_num):
        postfixed_keyword: str = get_random_postfixed_keyword(keyword)
        prefixed_keyword: str = get_random_postfixed_keyword(keyword)
        infixed_keyword: str = get_random_infixed_keyword(keyword)

        ret.append({'recommend_word': postfixed_keyword})
        ret.append({'recommend_word': prefixed_keyword})
        ret.append({'recommend_word': infixed_keyword})
    return ret


def get_random_postfixed_keyword(keyword: str):
    length = random.randint(1, 8)
    all_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    generated_random_string = '.'.join((random.choice(all_alphabets)) for x in range(length))
    return keyword + generated_random_string


def get_random_prefixed_keyword(keyword: str):
    length = random.randint(1, 8)
    all_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    generated_random_string = '.'.join((random.choice(all_alphabets)) for x in range(length))
    return generated_random_string + keyword


def get_random_infixed_keyword(keyword: str):
    length = random.randint(1, 8)
    all_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    generated_random_string_1 = '.'.join((random.choice(all_alphabets)) for x in range(length))

    length = random.randint(1, 8)
    generated_random_string_2 = '.'.join((random.choice(all_alphabets)) for x in range(length))
    return generated_random_string_1 + keyword + generated_random_string_2
 

if __name__ == '__main__':
    run({
        'init_db_scheme': init_db_scheme,
        'upload_data': upload_data,
    })
