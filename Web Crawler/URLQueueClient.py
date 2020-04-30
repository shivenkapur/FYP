import socket
import requests

def URLQueueClient():

	sock = socket.socket()
	sock.connect(('127.0.0.1', 8000))
	response = requests.get('http://localhost:8000/getAllUrls')
	print(response.text)
	sock.close() 


