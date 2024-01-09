import re
import logging

def read_from_datatxt(datatxt_file_path):
    
    retrieved_txt = ""

    with open(datatxt_file_path, "r") as txt:
        logging.info(f"{datatxt_file_path} is opened.")
        retrieved_txt += txt.read()
        logging.info(f"Info is read from {datatxt_file_path}.")

    return retrieved_txt

def parse_messedup_jsonbody(retrieved_txt):

    comments_excluded = re.sub(r'#.*', '', retrieved_txt)
    logging.info(f'Comments are excluded from "data.txt"')

        
    pattern = re.compile(r'\s(?=Known)')

    # Split the text at the space before "Known" and insert a colon
    split_text = pattern.split(comments_excluded)
    
    # Join the split parts with a colon
    result = ' : '.join(split_text)

     
    match = re.search(r'(\d+) : (.+?) : (.+)', result)

    if match:
        user_id = int(match.group(1))
        title = match.group(2).strip()
        body = match.group(3).strip()

        result_dict = {
                        "userId": user_id,
                        "title": title,
                        "body": body
                      }

        logging.info(f'Response body is parsed from "data.txt":{result_dict}')
        
        return result_dict
        
    else:
        print("No match found.")
        logging.info("No match found.")
        return None 

    
    
