#!/usr/bin/env python
#-- coding:utf-8 --

import sys

retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

while retry_count < retry_limit:
	username = raw_input('\033[32;1mUsername:\033[0m')
	lock_check = file(lock_file)
	
	for line in lock_check.readlines():
		line = line.split()
		if username == line[0]:
			print 'User is locked!'
			sys.exit('\033[31;1mUser %s is locked!\033[0m' % username)

	password = raw_input('\033[32;1mPassword:\033[0m')
	
	f = file(account_file, 'rb')
	match_flag = False
	for line in f.readlines():
		user, passwd = line.strip('\n').split()
		if username == user and passwd == password:
			print 'Match !', username
			match_flag = True
			break
	f.close()
	if match_flag == False:
		print 'User unmatched!'
		retry_count += 1
	else:
		print 'Welcome login OldBoy Learning system!'
else:
	print 'Your account is locked!'	
