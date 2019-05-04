import os

ok = 201
i = 6
while(i<=25):
    if(i<10):
        stri = "00"+str(i)
    else:
        stri = "0"+str(i)
    oldFile = "20190503_163141_"+stri+".jpg"
    newFile = "ok_"+str(ok)+".jpg"
    os.system("cp "+oldFile+" new_image/"+newFile)
    i = i + 1
    ok = ok + 1
