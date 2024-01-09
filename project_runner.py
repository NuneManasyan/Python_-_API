import os
import datetime
import logging
import log_config
import project_data
import json_body_parser
import post_method
import read_json_file


json_file_path = os.path.join(project_data.folder_name, project_data.j_file_name)
j_content = read_json_file.read_json_file_content(json_file_path)    
log_config.setup_logging(j_content)

start = datetime.datetime.now() 
logging.info(f"Program has started at: {start}")


datatxt_file_path = os.path.join(project_data.folder_name, project_data.datatxt_file_name)
retrieved_txt = json_body_parser.read_from_datatxt(datatxt_file_path)
final_json_body = json_body_parser.parse_messedup_jsonbody(retrieved_txt)


str_endpoint = j_content["endpoint"]
headers = project_data.headers
jq_obj = post_method.JsonQuery()
j_response = jq_obj.post_api(str_endpoint, final_json_body, headers)
jq_obj.json_validator(j_response)
j_response.pop('id')
jq_obj.match_sent_received_data( final_json_body, j_response )

finish = datetime.datetime.now()
duration = finish - start
logging.info(f"Program has ended at: {finish}")
logging.info(f"Program run lasted: {duration}")