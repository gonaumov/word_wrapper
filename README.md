# Word wrapper in Python

I wrote this Python script in order to automate something which often is missing 
in text editors or even IDE's. Text editors have word wrap however they don't have
an option to have line break after a specified number of symbols or characters. People
do it with regular expression when there is need. First you need to replace all whitespaces
with one single space and after that to add a new line on the first opportunity 
after the characters count you want. The first opportunity means the first space
available. This script will iterate all .txt files in current directory
and will wrap the text to a new line at the earliest opportunity
after the 84th character then the original file will be kept untouched and will be created a result file with name original_file_result.txt. 
I don't pretend the solution is ideal and this little script have been written just for fun. You can check example_input.txt and
example_input_result.txt If you have better suggestion let me know. 