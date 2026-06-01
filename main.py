from networksecuarity.components.data_ingestion import DataIngestion 
from networksecuarity.components.data_validation import DataValidation
from networksecuarity.components.data_transformation import DataTransformation
from networksecuarity.entity.config_entity import DataIngestionConfig,DataTransformationConfig,DataValidationConfig
from networksecuarity.entity.config_entity import TrainingPipelineConfig
import sys
from networksecuarity.exception.exception import NetworkSecuarityException
from networksecuarity.logging.logger import logging

if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info('initiate the data ingestion')
        
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate Data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        print(dataingestionartifact)
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("Data Transformation Started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Completed")


    except Exception as e:
        raise NetworkSecuarityException(e,sys)  