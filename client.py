from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey=b'secret password')

while True:
	msg = input("Enter target city no--> ")
	conn.send(msg)

conn.close()
