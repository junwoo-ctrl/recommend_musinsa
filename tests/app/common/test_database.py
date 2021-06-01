
from dataset import Database as database_obj

from server.common.database import Database


def test_database_lifecycle():
    
    dbw = Database()
    
    # initlialize properties
    assert dbw.config
    assert dbw.url
    assert db2.db

    # get_db()
    db_obj = dbw.get_db()
    assert isinstance(db_obj, database_obj)

    # _pint()
    expected = True
    actual = db._ping()
    assert expected == actual

    # query()
    expected = True

    statement = 'select 1'
    acutal = db.query(statement)
    assert expected == actual
