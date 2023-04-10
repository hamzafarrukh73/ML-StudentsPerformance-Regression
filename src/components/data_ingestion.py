# Built-in
import os
import sys

# Data handling
import pandas as pd

# Selection
from sklearn.model_selection import train_test_split

# Custom
from src.logger import logging
from src.exception import CustomException
from src.configs import DataIngestionConfig


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            data = pd.read_csv('data/raw/data.csv')
            logging.info('Reading the dataset')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            data.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.raw_data_path,
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e, sys)
