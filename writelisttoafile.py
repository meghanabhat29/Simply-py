list1=["Songs","Music","Notes","Tunes"]
with open("example.txt","w") as myfile:
    for c in list1:
        myfile.write("%s " %c)
file_content=open("example.txt")
print(file_content.read())
