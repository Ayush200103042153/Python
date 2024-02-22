#DELETE A FILE


import os
os.remove("demofile.txt")


#CHECK IF A FILE EXISTS


import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exists")    


#DELETE FOLDER    
import os
os.rmdir("my folder")