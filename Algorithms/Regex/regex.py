import re
text_to_search = '''This is something I can do in python . regex / yes okay 93 9324857 0- ajay.com'''
phone_number = '''
cat
bat
lat
rat

my phone number list
CAPITAL LETTERS
408-306-9382
408.306.1234
900.306.1234
800-123-7565
408*306*7565
123456789

Mr. Ajay 
Mrs. Pattu
Ms Lalita
Mr. Bijay
Mr Suraj
Mr. T

'''

emails = '''
GcAjay80@gmail.com
DavidRooney710@gmail.com
DeadGod555@gmail.com
bijay.gc@unersity.edu
suraj-gurung@unersity.net

'''

urls = '''
https://www.google.com  
http://boozercart.com
https://youtube.com
https://www.nasa.com
'''

# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[^b]at') --> exclude b # [^]
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}') --> phone number

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') --> |(pipe) is or ? is optional and * for 0 or any + 1 or more
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z]+\.(com|edu|net)') --> matching emails

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(2))
