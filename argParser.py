import os
import json
import argparse

def argParser():
    description = ("YouData: retrieve metadata/data (views, likes, tags) associated with Youtube channels.\n\n"\
    "1. Create / Update API key - python3 <key> --api   (obtained from Youtube's Data v3 API, for more information refer to https://developers.google.com/youtube/v3/getting-started)\n"\
    "2. Retrieve data associated with youtube channel - python3 <channel keyword/url>")
    parser = argparse.ArgumentParser()
    parser.add_argument("x")
    parser.add_argument("-api", help = "Create/ update API key.", action="store_true")
    parser.add_argument("-id", help = "Get youtube data using channel ID format.", action="store_true")
    parser.add_argument("-csv", help = "Write to csv file.", action="store_true")
    args = parser.parse_args()
    if args.api: #Initialise or update API key.
        auth_key = args.x
        auth_dict = { "auth_key": auth_key}
        json_object = json.dumps(auth_dict) 
        with open("auth_key.json", "w") as outfile:
            outfile.write(json_object)
    
    return args
    

def ready_to_write(args):
    # Ready to write to file.
    if os.stat("auth_key.json").st_size == 0:
        print("API key is missing / not initialised!")

    # Check if optional arguments are selected.
    if args.api:
        return False
    
    return True
        