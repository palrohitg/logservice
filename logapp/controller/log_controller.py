import json 
import os 
from datetime import datetime, timedelta
from logapp.utils import utils
from logapp.utils.constants import Constants 

class LogController:

    def process_log(self, **kwargs):
        try:
            log_data = self.log_data(kwargs)
            self.save_logs(log_data)
            return log_data.get("id"), True 
        except Exception as e:
            print(f"error occured {e}")
            return None, False 
        
    
    def log_data(self, kwargs):
        log_data = {}
        log_data["id"] = kwargs.get("id")
        log_data["user_id"] = kwargs.get("user_id")
        log_data["event_name"] = kwargs.get("event_name")
        log_data["unix_ts"] = kwargs.get("unix_ts")
        return log_data
        
    def get_current_directory(self):
        return os.getcwd()
    
    def save_logs(self, log_data=None):
        return self.save_logs_in_file(log_data)

    def save_logs_in_file(self, log_data=None):
        relative_path = self.get_file_name()
        self.append_dict_to_json_file(log_data,  self.get_current_directory() + "/logs/{}.log".format(relative_path))
    
    def check_time_difference(self, file_time_stamp_str):
        current_timestamp = utils.get_current_timestamp()
        try:
            timestamp = utils.convert_str_to_date_time(file_time_stamp_str)
            time_diff = datetime.strptime(current_timestamp, Constants.TIME.DATE_TIME_SECOND) - timestamp
            if time_diff <= timedelta(minutes=5):
                return True 
            return False
        except Exception as e:
            print(f"### Error Occurred {e} ####")
        return False
    
    def check_if_file_exits_for_current_data(self, file_names):
        current_timestamp = utils.get_current_timestamp()  
        for file_name in file_names: 
            file_time_stamp = file_name.replace(".log", "")
            is_within_5_minutes = self.check_time_difference(file_time_stamp)
            if is_within_5_minutes:
                return file_time_stamp 
        return str(current_timestamp)
    
    def get_file_name(self):
        directory_path = self.get_current_directory() + "/logs/"
        file_names = utils.list_directory_file(directory_path)
        file_name  = self.check_if_file_exits_for_current_data(file_names)
        return file_name
        
    def append_dict_to_json_file(self, data, file_path): 
        try:
            with open(file_path, 'a') as file:
                json.dump(data, file)
                file.write('\n')  # Add a newline after each dictionary
            print("Data appended successfully to the JSON file.")
        except IOError as e:
            print(f"Error: {e}")
    