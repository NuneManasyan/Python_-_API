import logging
import project_data
import requests
from jsonschema import validate, ValidationError
import json_validation_schema as J_V



class JsonQuery:
        
    def post_api(self, str_endpoint, result_dict, headers):        
        self.str_endpoint = str_endpoint
        self.result_dict = result_dict
             
        for attempt in range(2):
            try:
                post_request_response = requests.post(self.str_endpoint, json=self.result_dict, headers=project_data.headers)
            
                if post_request_response:
                    
                    logging.info(f"POST method: Successful response!")
                    assert 200 <= post_request_response.status_code <= 299, "Failed: post_request_response.status_code"                    
                    
                    response = post_request_response.json()
                    logging.info(f"The following response is received: {response}")
                   
                    return response
                    
            except requests.RequestException:
                print(f"Attempt {attempt+1}: Failed. Retrying ...")
                logging.error(f"Attempt {attempt+1}: Failed. Retrying ..")
                
    def json_validator(self,post_request_response): 
        try:
            validate(post_request_response, schema = J_V.json_schema)
            logging.info("JSON content is validated.")
        except ValidationError as x:
            logging.error(f"Validation Error: {x}")
       
            
    
    def match_sent_received_data(self, json_body, modif_response):        
        if modif_response == json_body:
            logging.info("Sent and received data are the same.")            
        else:
            logging.error("Sent and received data mismatch error")
            
            

