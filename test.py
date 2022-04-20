import time
from datetime import datetime

session_file = open("cotps_session.txt", "a")
log_session_to_file='Session Completed! at '+str(datetime.now())+'\r'
session_file.write(log_session_to_file)      
session_file.close()