fileOpen = open("TEST1.TXT", "r")
fileWrite = open("createNewText.txt", "w")
lens = 0
min = 21
hr = 13
date = "23/03/2019"
for i in fileOpen :
    strWrite = str(lens) +" " + date + " "+ str(hr)+":"+str(min)+"\n"
    print(strWrite)
    fileWrite.write(strWrite)
    min += 5
    if(min >= 60):
        hr += 1
        min %= 60    
    lens += 1
