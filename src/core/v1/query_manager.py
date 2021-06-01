
from collections import OrderedDict
from typing import Any, List

from core.interfaces.abstract_query_manager import AbstractQueryManager as AQM
from server.common.database import Database
from server.util.logger import RecommendLogger as Logger


class QueryManager(AQM):
    logger = Logger(__name__)
    
    @staticmethod
    def query(statement: str) -> List[OrderedDict]:

        db_wrapper: Database = Database()
        try:
            # To be implment Single Tone.
            db = db_wrapper.db
            
            QueryManager.logger.info(f"{statement} execute successfully.")
            resp = db.query(statement)
        except Exception as e:
            QueryManager.logger.info(f"{statement} failed.")
            resp = []
        finally:
            db_wrapper.close()
        return resp
