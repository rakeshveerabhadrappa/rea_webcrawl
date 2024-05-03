# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 19:24:28 2024

@author: Backpack1
"""

import json

folder_path = "../../net_info"
file_path = folder_path+"/response_header.json"

try:
    with open(file_path, 'r') as json_file:
        header = json.load(json_file)
        print("Data read from JSON file:")
except FileNotFoundError:
    print(f"File {file_path} not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")