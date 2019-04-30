import requests

class Server:
	info = {}
	players = {}
	name = ""

def getAllServers():
	r = requests.get('http://servers-live.fivem.net/api/servers/')
	data = r.json()

	return data

def getServer(ip):
	server = Server()
	try:
		r = requests.get("http://"+ip+"/info.json")
		server.info = r.json()
		r = requests.get("http://"+ip+"/players.json")
		server.players = r.json()
		all_servers = getAllServers()
	except Exception:
		raise Exception("Incorrect IP or server is not responding.")

	for s in all_servers:
		if s['EndPoint'] == ip:
			server.info['vars']['sv_hostname'] = s['Data']['hostname']
			server.name = s['Data']['hostname']
	
	return server
