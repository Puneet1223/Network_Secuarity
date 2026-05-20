from networksecuarity.components.data_ingestion import DataIngestion
from networksecuarity.exception.exception import NetworkSecuarityException
from networksecuarity.logging.logger import logging
from networksecuarity.entity.config_entity import DataIngestionConfig
from networksecuarity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info('initiate the data ingestion')
        
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecuarityException(e,sys)  