#!/var/ossec/framework/python/bin/python3

import sys
import json
import requests

# Read configuration parameters
alert_file = open(sys.argv[1])
api_key = sys.argv[2]
hook_url = sys.argv[3]

# Read the alert file
alert_json = json.loads(alert_file.read())
alert_file.close()

#msg_data
alert_level = alert_json['rule']['level']
description = alert_json['rule']['description']
agent_name = alert_json['agent']['name']
full_log = alert_json['full_log']

#headers
headers = {'Content-Type': 'application/json', "Authorization": f"Bearer {api_key}"}

#data
data = {"Input": f"alert level: {alert_level}\n description: {description}\n Agent name: {agent_name}\n Full log: {full_log}"}

# Send the request
response = requests.post(hook_url, data=json.dumps(data), headers=headers)

sys.exit(0)
