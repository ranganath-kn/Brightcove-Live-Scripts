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

# Getting Input from the User to save the captured source and seconds
local_path = input("Enter the Path to Save the Captured Input (add the path with filename eg: /downloads/filename.mp4): ")
seconds = input("Enter the Duration to Capture (in seconds)(usually 20 seconds): ")

# Parsing the Commands
rtmp_segment1 = "rtmpdump -r {0}".format(rtmp_url)
rtmp_segment2 = " -y alive -o {0}".format(local_path)
rtmp_segment3 = " -B {0}".format(seconds)

rtmp_segments_parse = [rtmp_segment1,rtmp_segment2,rtmp_segment3]
rtmp_source_capture = ''.join(rtmp_segments_parse)
print("\nRequested Command to Capture Source: ", rtmp_source_capture, '\n')

# Executing the Capture
output = os.system(rtmp_source_capture)