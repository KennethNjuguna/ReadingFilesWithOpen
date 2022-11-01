#File objects

with open('Open.txt','r') as f:
	size_to_read=10

	f_contents=f.read(size_to_read)
	print(f_contents, end='')

	f.seek(0)

	f.cotents=f.read(size_to_read)
	print(f_contents)

	
	

		