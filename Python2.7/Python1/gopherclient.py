import socket, sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((host, port))
except:
	print "Error connecting to server. "
	sys.exit(1)

fd = s.makefile('rw', 0)
fd.write(filename + "\r\n")

for line in fd.readlines():
	sys.stdout.write(line)
	