#WRITE TO AN EXISTING FILE


f=open("file name","a")
f.write("Now the file has more content")
f.close()

#open and read the file after the appending:
f = open("file name", "r")
print(f.read())


#CREATE NEW FILE


f=open("myfile,txt","x")
print(f.read())