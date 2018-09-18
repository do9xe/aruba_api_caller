from aruba_api_caller import *

#WrapperTest = api_session("127.0.0.1","testuser","password123",port="5000",SSL=False)

#WrapperTest.login()

#response = WrapperTest.write_memory("/md")
#if response["write_memory"]["_result"]["status"] != 0:
#  print("write_memory failed")
#  exit(1)

#WrapperTest.logout()

if convertUptime("Up 19d:17h:40m:51s") != 1705251:
  print("Uptime-conversion for >Up 19d:17h:40m:51s< failed")
  exit(1)

if convertUptime("Down") != 0:
  print("Uptime-conversion for >Down< failed")
  exit(1)
