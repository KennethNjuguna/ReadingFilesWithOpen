#File objects

with open('Open.txt','r') as f:
	f_contents=f.readline()
	print(f_contents, end='')

	f_contents=f.readline()
	print(f_contents, end='')