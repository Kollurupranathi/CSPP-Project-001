"""The python code helps to read the command line input for curl method."""
#the first line is a comment
import sys
#importing sys library using "import" keyword
from lib.helper import curl
#Importing "curl" functions from helper library using "from" "import" keywords
URL = None
#URL is a variable which is initialized with none
ARG_CNT = len(sys.argv) - 1
#length is a function containing a predefined argument "sys.argv" and it is used to length of the file
#ARG_CNT is a variable assigned with len(sys.argv) minus one

if ARG_CNT != 1:
    print('Usage: curl [URL]...')
#"if" is a conditional statement used to perform multiple outcomes of a previous step
# if the value of ARG_CNT varialble is not equal to one, the condition will be true. This makes to execute the next line
#print is a function used to print the data given in it
#Here, it print a string "Usage: curl [URL]..."
if ARG_CNT == 1:
    URL = sys.argv[1]
    if 'http' not in URL[:5]:
        URL = "http://"+URL
    print(curl(URL))
# if the value of ARG_CNT variable is equal to one, the condition will be true. This makes to execute the next line
#sys.argv[1] is stored in a variable named "URL"
# if an URL does not have 'http' in it 
# then overwrite the URL variable by adding 'http' to the existing URL variable
#print the function curl containing URL as an argument
