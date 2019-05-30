# python has several functions for creating reading updating and deleting(CRUD)
# THE KEY FUNCTION FOR WORKING WITH FILES IS open()
# the open function takes two parameters
# 1.file name- file to be opened
# 2. mode to open the file with


# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists
try:
	f = open('text.txt','a')
except:
	print('text.txt file does not exist')
try:
	f = open('index.html','w')
except:
	print('not successful')
try:
	f = open('demo2.py','x')
except:
	print('successful')