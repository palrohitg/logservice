from django.core.management.base import BaseCommand
from django.utils import timezone
import json 
from django.db import transaction
from logapp.models import UserLog
import datetime
import glob
import os 
from datetime import timedelta
from logapp.utils.constants import Constants 
from logapp.utils import utils


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        """
           It will read all the files which created date is more than 
           five minutes from current timestamp. Read the logs data and insert 
           into SQL in batches.  
        """
        try:
            self.process_old_data()
        except Exception as e:
            print(f"#### Error Occurred While Processing Data {e}")
       
    
    def check_file_time_difference(self, file_time_stamp_str): 
        current_timestamp = utils.get_current_timestamp()
        try:
            timestamp = utils.convert_str_to_date_time()
            time_diff = datetime.strptime(current_timestamp,Constants.TIME.DATE_TIME_SECOND ) - timestamp
            if time_diff > timedelta(minutes=5):
                return True 
            return False
        except Exception as e:
            print(f"Error Occured Due to {e}")
        return False
    
    def get_file_to_process(self, file_names):
        """
            Will read file_name if file_name is created more than 5 mins then
            process that files or file_size below greater than 10MB
        """
        for file_name in file_names:
            file_name_timestamp = file_name.replace(".log", "")
            file_size = utils.file_size(self.get_directory_path_of_logs() + file_name)
            if file_size > Constants.Management.FILE_SIZE or self.check_file_time_difference(file_name_timestamp):
                self.write_data_in_batches(self.get_directory_path_of_logs() + file_name) 
               

    def get_directory_path_of_logs(self):
        return os.getcwd() + "/logs/"
    
    def process_old_data(self):
        directory_path = self.get_directory_path_of_logs()
        file_names = utils.list_directory_file(directory_path)
        self.get_file_to_process(file_names)
    
    def parse_log_line(self, line):
        try:
            dict_data = json.loads(line)  
            return dict_data
        except Exception as e:
            print("parsing files exception occured here")
            return None 
         
    def convert_into_data_set(self, lines):
        data_set= []
        for line in lines:
            log_data = self.parse_log_line(line.strip())
            data_set.append(log_data)
        return data_set
    
    def get_batch_count(self, data_set):
        total_records = len(data_set)
        batches = (total_records // Constants.Management.BATCH_SIZE) + 1 
        return batches
    
    def unix_to_datetime(self, unix_ts):
        try:
            dt = datetime.datetime.fromtimestamp(unix_ts)
            return dt 
        except Exception as e:
            print(f"######### Error occur While Creating User Object {e} #########")
    
    def get_user_log(self, user_logs):
        user_logs_list = []
        for logs in user_logs:
            event_id = logs.get("id", None)
            user_id = logs.get("user_id", None)
            event_name = logs.get("event_name", None) 
            unix_ts = logs.get("unix_ts", None) 
            try: 
                if event_id and user_id and event_name and unix_ts: 
                    unix_ts_date_format = self.unix_to_datetime(int(unix_ts))
                    log = UserLog(
                            event_id=event_id,
                            user_id = user_id, 
                            event_name = event_name,
                            event_time_stamp = unix_ts_date_format, 
                        )
                    user_logs_list.append(log)
            except Exception as e:
                print(f"######### Error occur While Creating User Object {e} #########")
        return user_logs_list
        

        
    def write_data_in_batches(self, file_path):
        
        log_files = glob.glob(file_path)
        transaction_written = False 
        
        for file_path in log_files:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                data_set = self.convert_into_data_set(lines)
                batches = self.get_batch_count(data_set)
                for i in range(batches):
                    start = i * Constants.Management.BATCH_SIZE
                    if start == 0:
                        end = 1 * Constants.Management.BATCH_SIZE
                    else:
                        end = start * Constants.Management.BATCH_SIZE
                    print("start : ", start)
                    print("end : ", end)
                    batch_data = data_set[start:end] 
                    if batch_data:
                        users_logs = self.get_user_log(batch_data)
                        if users_logs: 
                            print("######### Before Inserting #########")
                            try: 
                                with transaction.atomic():
                                    UserLog.objects.bulk_create(users_logs)
                                    transaction_written = True       
                            except Exception as e:
                                print(f"######### Error Occur during Insertion {e} #########")
                                transaction_written = False 
                        else:
                            print("######### Error occur While Creating User Object  #########")
                            
        if transaction_written:
            utils.delete_current_file(file_path)
            print(f"Processed batch {i + 1} of {batches}")           
                        
        