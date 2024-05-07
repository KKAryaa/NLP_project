
import os
from text_summarizer.logging import logger
from text_summarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config

    def Validate_all_files_exist(self)-> bool:
        try:
            valiation_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.STATUS_FILE:
                    valiation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Status: {valiation_status}")

                else:
                    valiation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {valiation_status}")

            return valiation_status
        
        except Exception as e:
            raise e