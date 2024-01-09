import os
import json
import project_data

def read_json_file_content(json_file_path):
      
    if os.path.exists (json_file_path):
        with open (json_file_path, "r") as j_file:            
            json_content = json.load(j_file)
            if json_content:                             
                return json_content                                    
            else:
                print(f"The {project_data.j_file_name} file is empty")
    else:
        print(f"The '{project_data.j_file_name}' file does not exist.")
        

