#File objects you working with bytes to avoid errors add b

with open('PythonImage.png','rb')as rf:
	with open('PythonImageCopy.png','wb')as wf:
		for line in rf:
			wf.write(line)