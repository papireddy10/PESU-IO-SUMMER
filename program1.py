line=input("enter comma separated nos.")
l=[]
for i in range(0,len(line)):
    if line[i]!=',':
            x=int(line[i])
            l.append(x)
tup_req=tuple(l)
print("required list is",l)
print("required tuple is",tup_req)
