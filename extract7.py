import os
import tarfile
import zipfile

all_files = [f for f in os.listdir('.') if os.path.isfile(f)] #all_files holds all the files in current directory
for current_file in all_files: 
	print("Reading " + current_file)
#---------------To extract .tgz or tar.gz files ----------------------------
	if (current_file.endswith(".tgz")) or (current_file.endswith("tar.gz")):
		tar = tarfile.open(current_file, "r:gz")
		file_name=os.path.splitext(current_file)[0] #file_name contains only name by removing the extension
		os.makedirs(file_name) #make directory with the file name
		output_file_path=file_name  #Path to store the files after extraction
		print("Trying to Extract " + current_file)
		try:
			tar.extractall(output_file_path) #extract the current file
			print("Extracted to " + output_file_path)
		except:
			print("Failed to extract " + current_file)
		tar.close()
#---------------To extract tar files ----------------------------
	elif (current_file.endswith("tar")):
		tar = tarfile.open(current_file, "r:")
		file_name=os.path.splitext(current_file)[0] #file_name contains only name by removing the extension
		os.makedirs(file_name) #make directory with the file name
		output_file_path=file_name  #Path to store the files after extraction
		print("Trying to Extract " + current_file)
		try:
			tar.extractall(output_file_path) #extract the current file
			print("Extracted to " + output_file_path)
		except:
			print("Failed to extract " + current_file)
		tar.close()
#---------------To extract .tbz or .tar.bz2 files ----------------------------
	elif (current_file.endswith(".tbz")) or (current_file.endswith(".tar.bz2")):
		tar = tarfile.open(current_file, "r:")
		file_name=os.path.splitext(current_file)[0] #file_name contains only name by removing the extension
		os.makedirs(file_name) #make directory with the file name
		output_file_path=file_name  #Path to store the files after extraction
		print("Trying to Extract " + current_file)
		try:
			tar.extractall(output_file_path) #extract the current file
			print("Extracted to " + output_file_path)
		except:
			print("Failed to extract " + current_file)
		tar.close()
#---------------To extract zip files ----------------------------
	elif (current_file.endswith(".zip")):
		zip = zipfile.ZipFile(current_file, "r")
		file_name=os.path.splitext(current_file)[0] #file_name contains only name by removing the extension
		os.makedirs(file_name) #make directory with the file name
		output_file_path=file_name  #Path to store the files after extraction
		print("Trying to Extract " + current_file)
		try:
			zip.extractall(output_file_path) #extract the current file
			print("Extracted to " + output_file_path)
		except:
			print("Failed to extract " + current_file)
		zip.close()
	
		