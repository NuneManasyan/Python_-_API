import logging
import os
import project_data
   
def setup_logging(json_content):
        
    logging.basicConfig(
                            level=logging.INFO,
                            format="[%(levelname)s] - %(message)s ",
                            filename=os.path.join(project_data.folder_name, json_content["log file name"]),
                            filemode="w+",
                            encoding="utf-8"
                        )



  
    