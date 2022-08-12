import os

# Getting Job ID as input from user and storing it in a variable
job_id = input("Enter the Job ID: ")
stream_job_id = job_id

# Split RTMP URL into variables to parse later
rtmp_variable = ("rtmp://")
variable1 = (".sep.bcovlive.io:1935/")

# Parse into a complete stream URL 
rtmp_parse = [rtmp_variable,stream_job_id,variable1,stream_job_id]
rtmp_url = ''.join(rtmp_parse)
print("\nRTMP URL for the Stream: ", rtmp_url, '\n')

# Perofrm RTMPDUMP as output
rtmp_output = "rtmpdump -r {0} -y alive -o /dev/null -B 0.001".format(rtmp_url)
output = os.system(rtmp_output)