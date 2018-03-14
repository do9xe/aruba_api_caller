#!/usr/bin/python3

import json,requests,pprint
from aruba_api_caller import *

session = api_session("10.0.0.1", "admin", "password", False)

session.login()

VLANS = session.get("configuration/container/Interfaces/_data", "/md")

for VLAN in VLANS["_data"]["vlan_id"]:
	print ("VLAN-ID: " + str(VLAN["id"]))
	if "vlan_id__descr" in VLAN:
		print ("Description: " + VLAN["vlan_id__descr"]["descr"])

session.logout()
