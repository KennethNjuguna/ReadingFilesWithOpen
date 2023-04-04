#File objects you working with bytes to avoid errors add b
#B ensures the image doesnt loose pixualization

with open('PythonImage.png','rb')as rf:
	with open('PythonImageCopy.png','wb')as wf:
		for line in rf:
			wf.write(line)