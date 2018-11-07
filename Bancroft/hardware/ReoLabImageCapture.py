
'''
ReoLabImageCapture.py

This provides a function to interface with the C# program, ReoLabImageCapture.

'''

import socket
import os

def Capture(Filename):
	HOST = 'localhost'
	PORT = 11223
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	b = bytes(Filename, 'ascii')
	b += bytes([10])
	s.sendall(b)
	s.close()
	
if __name__ == "__main__":
	print ("ReoLabImageCapture.py Test:")
	Capture(os.getcwd() + "\\test13jpg")
	