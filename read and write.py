#File objects

with open('Open.txt','r') as rf:
	with open('Open_Copy.txt','w')as wf:
		for line in rf:
			wf.write(line)