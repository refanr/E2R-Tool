import re

with open("./test.txt") as file:
    file_content = file.read()
    lst = re.findall(r'(https:\/\/nyr\.ruv\.is\/audskilid\/[^, ]+?)"', file_content)

with open("urls.txt", "a") as out_file:
    for url in lst:
        out_file.write(url+"\n")
