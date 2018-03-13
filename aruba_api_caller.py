import json,requests

class api_session:
	def __init__(self, api_url, username, password, check_ssl):
		self.session = None
		self.api_token = None
		self.api_url = "https://"+ api_url +":4343/v1/"
		self.username = username
		self.password = password
		self.check_ssl = check_ssl
	
	def login(self):
		self.session = requests.Session()
		response = self.session.get(self.api_url + "api/login?" + "username=" + self.username + "&password=" + self.password, verify=self.check_ssl)
		login_data = json.loads(response.text)
		print (login_data["_global_result"]["status_str"])
		self.api_token = login_data["_global_result"]["UIDARUBA"]

	def logout(self):
		response = self.session.get(self.api_url + "api/logout")
		logout_data = json.loads(response.text)
		self.api_token = None
		print (logout_data["_global_result"]["status_str"])

	def get(self, api_path, config_path=None):
		if self.api_token == None:
			login()
		node_path = None
		if config_path is not None:
			node_path = "&config_path=" + config_path
		response = self.session.get(self.api_url + api_path + "?UIDARUBA=" + self.api_token + (node_path if node_path is not None else ''))
		data = json.loads(response.text)
		return data

	def post(self, api_path, config_path, data):
		if self.api_token == None:
			login()
		node_path = "?config_path=" + config_path
		response = self.session.post(self.api_url + api_path + node_path + "&UIDARUBA=" + self.api_token, json=data)
		data = json.loads(response.text)
		return data

	def write_memory(self, config_path):
		node_path = "?config_path=" + config_path
		nothing = json.loads('{}')
		response = self.session.post(self.api_url + "configuration/object/write_memory" + node_path + "&UIDARUBA=" + self.api_token, json=nothing)
		data = json.loads(response.text)
		return data

	def cli_command(self, command):
		mod_command = command.replace(" ", "+")
		response = self.session.get(self.api_url + "configuration/showcommand?command=" + mod_command + "&UIDARUBA=" + self.api_token)
		data = json.loads(response.text)
		return data
