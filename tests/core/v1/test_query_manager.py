
from core.v1.query_manager import QueryManager


def test_query_manager_lifecycle():
    expected = True

    statement = "SELECT 1"
    actual = QueryManager.query(statement)
    assert expected == actual
