# NuneM_project

Main test scenario is the following:
1. Get the "out.log" name of the log file from "config.json"
2. Setup logging
2. Parse json_body from data.txt
3. Get endpoint from "config.json"
4. Send a request with the POST method using endpoint, json_body, header
5. Validate if json response matches validation schema
6. Compare that sent and received data are the same


endpoint = "https://jsonplaceholder.typicode.com/posts"

pip install -r path\requirements.txt

config.json - Contains "endpoint" and "log file name" in json format

data.txt - Contains information from which json body should be parsed
requirements.txt - Contains the list of installed Python packages

project_data.py - Contains necessary data
read_json_file.py - Reads content from "config.json" 
log_config.py - Sets up logging
json_body_parser.py - Reads info from "data.txt" and parses pure json body
json_validation_schema - Displays required json schema
post_method.py - Sends a json request using the POST method
               - Validates that json response matches json validation schema
               - Verifies that sent and received info are the same
project_runner.py- contains all the necessary calls for running the project



