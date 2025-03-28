import os
import sys
import json
import certifi
import pymongo
import pandas as pd

from dotenv import load_dotenv
from networksecurity.constant import CONFIG_FILE_PATH
from networksecurity.utils.common import read_yaml
from networksecurity.exception.exception import NetworkSecurityException

load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")

ca = certifi.where()

data_push_config = read_yaml(CONFIG_FILE_PATH).data_push

class NetworkDataExtract:
    """
    class with functions to convert the csv data to json and push it to the mongodb.
    """

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        """
        convert csv to json
        """
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        """
        upload data to mongodb
        """
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


def main():
    FILE_PATH = data_push_config.local_data_file
    DATABASE = data_push_config.database_name
    Collection = data_push_config.collection
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)


if __name__ == "__main__":
    main()
