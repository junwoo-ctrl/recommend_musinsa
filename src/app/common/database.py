from typing import List, Dict

import dataset
from dataset import Database

from app.util.tools import Config
from app.util.logger import RecommendLogger as Logger


class Database:
    
    def __init__(self):
        self.db = None
        self.config: Config = Config.get_config()
        self.url: str = self._get_endpoint()
        self.logger = Logger(__name__)
        self._connect_db()

    def _connect_db(self) -> Database:
        db: Database = self._connect()
        self.db = db
        self.logger.info('database connect.!')

    def get_db(self) -> Database:
        if self.db is None:
            self._connect_db()
        return self.db

    def _get_endpoint(self) -> str:
        database_endpoint = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4".format(
            user=self.config.user,
            password=self.config.password,
            host=self.config.host,
            database=self.config.database,
        )
        return database_endpoint
    
    def _connect(self) -> Database:
        return dataset.connect(self.url)

    def connect(self) -> None:
        if self.db is None:
            self._connect_db()

    def _ping(self) -> bool:
        statement = """SELECT 1"""
        try:
            resp = [r for r in self.db.query(statement)]
        except Exception as e:
            self.logger.error(str(e))
        return resp

    def _close(self) -> bool:
        self.db.close()

    def close(self) -> None:
        self._close()

    def query(self, statement: str) -> List[Dict]:
        try:
            resp = [r for r in self.db.query(statement)]
            return resp
        except Exception as e:
            self.logger.error(str(e))
            return []
