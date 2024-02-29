

import speedtest
import time
s = speedtest.Speedtest()

print("Loading Servers")
s.get_servers()

print("Connecting to the Best Server")
bestServer = s.get_server()
print(f"Connected to {bestServer['host']} located in {bestServer['country']} ")
time.sleep(1)

print("Starting Speed Test...")
time.sleep(2)

print("Pinging The Server...")
ping= s.results.ping
time.sleep(1)

print("Downloading...")
download = s.download()
time.sleep(1)

print("Uploading...")
upload = s.upload()
time.sleep(1)


def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    print(result)

print("*************RESULTS*************")
border_msg(f"Ping: {ping:.2f} ms")
border_msg(f"Download Speed: {download /1024/1024:.2f} Mbit/s")
border_msg(f"Upload Speed: {upload /1024/1024:.2f} Mbit/s")
print("************THANKYOU************")