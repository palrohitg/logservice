import os 
import datetime
from datetime import timedelta

def list_directory_file(directory_path):
    return os.listdir(directory_path)

def file_size(file_path):
    return os.path.getsize(file_path)

def delete_current_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted successfully")
    else:
        print(f"File {file_path} doesn't exists")
        
def get_current_timestamp():
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_timestamp

def convert_str_to_date_time(str_time_stamp):
    return datetime.strptime(str_time_stamp, "%Y-%m-%d %H:%M:%S")
    