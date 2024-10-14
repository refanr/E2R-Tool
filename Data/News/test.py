import re

with open("Data/News/test.txt") as file:
    file_content = file.read()
    lst = re.findall(r'(https:\/\/nyr\.ruv\.is\/audskilid\/[^, ]+?)"', file_content)
print(len(lst))
old_lst = []
with open("Data/News/urls.txt", "r") as in_file:
    old_lst = in_file.readlines()
print(len(old_lst))
with open("Data/News/urls.txt", "a") as out_file:
    i = 0
    for url in lst:
        if url not in old_lst:
            i += 1
            out_file.write(url+"\n")
    print(i)