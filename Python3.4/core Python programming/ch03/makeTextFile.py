'makeTextFile.py -- create text file'
import os
ls = os.linesep

# get filename
while True:
    fname = input('Enter file name: ')
    if os.path.exists(fname):
        print("ERROR: '%s' already exists" % fname)
    else:
        break
# get file content (text) lines
all1 = []
print("\nEnter lines ('.' by itself to quit).\n")

# loop until user terminates input
while True:
    entry = input('>')
    if entry == '.':
        break
    else:
        all1.append(entry)
# write lines to file with NEWLINE line terminator
fobj = open(fname, '+w')
fobj.write('\n'.join(all1))
fobj.close()
              
