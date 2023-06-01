#File objects work with content and read objects

with open('Open.txt','r') as f:
	f_contents=f.read(100)
	print(f_contents, end='')

	f_contents=f.read(100)
	print(f_contents, end='')

	f_contents=f.read(100)
	print(f_contents, end='')

	 