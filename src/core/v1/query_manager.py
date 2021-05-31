
from collections import OrderedDict
from typing import Any, List

from src.core.interfaces.abstract_query_manager import AbstractQueryManager as AQM
from src.app.common.database import Database


class QueryManager(AQM):
    
    @staticmethod
    def query(statement: str) -> List[OrderedDict]:

        # To be implment Single Tone.
        db_wrapper: Database = Database()
        db = db_wrapper.db
        
        print(f"{statement} execute.")
        resp = db.query(statement)
        
        db_wrapper.close()
        return resp
