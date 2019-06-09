line=input("pls enter a string")
b=0
for i in range(0,len(line)):
    if line[i].isdigit==True:
        b=b+1
if b==len(line):
    print("the string is numeric")
