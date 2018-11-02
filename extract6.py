import os
import tarfile

files = [f for f in os.listdir('.') if os.path.isfile(f)] 
for fname in files: 
	if (fname.endswith(".tgz")) or (fname.endswith("tar.gz")):
		tar = tarfile.open(fname, "r:gz")
		tar.extractall()
		tar.close()
	elif (fname.endswith("tar")):
		tar = tarfile.open(fname, "r:")
		tar.extractall()
		tar.close()