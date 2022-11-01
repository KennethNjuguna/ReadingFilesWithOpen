#File objects you working with bytes to avoid errors add b

with open('PythonImage.png','rb')as rf:
	with open('PythonImageCopy2.png','wb')as wf:
		chunk_size=4096
		rf_chunk=rf.read(chunk_size)
		while len(rf_chunk)>0:
			wf.write(rf_chunk)
			rf_chunk=rf.read(chunk_size)