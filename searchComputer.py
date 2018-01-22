from __future__ import print_function
import os
root_directory=''
x=[]
z=[]
q='1'
k=1
f=input("which directory you want to search for:\n1)c\t2)h\n3)i\t4)j\n")
t=input("Enter the file type(0 if none):")
root_directory=f.upper() + ":/"
search=input("what you want to search:")
if os.stat("SearchComputer.txt").st_size != 0:
    with open("SearchComputer.txt","r") as f:
        for line in f:
            (key,value,t1)=line.split("\t")
            if(search.lower() in key.lower() and key.endswith(t)):
                x.append(value)
    print ( )
    if(len(x)==0):
        print("No file found in cache.Press 1 for deep search:")
        q=input()
    else:
        for i in range(0,len(x)):
            u=i+1
            print (str(u)+')'+x[i])
        q=input("If you didnt find your book press 1 to deep search: ")
        if(q!='1'):
            y=int(input("select which file to open:"))
            y=y-1
            os.startfile(x[y])
if(q=='1'):
    x=[]
    for cur_path,directory,files in os.walk(root_directory):
        for file in files:
            if(t!='0'):
             #   print(t)
                if((search.lower() in file.lower()) and file.endswith(t)):
                    x.append(os.path.join(cur_path,file))
                    z.append(file)
                    k=k+1
            else:
                if(search.lower() in file.lower()):
                    x.append(os.path.join(cur_path,file))
                    z.append(file)
                    k=k+1
    print ( )
    if(len(x)==0):
        print("No such file found")
    else:
        for i in range(0,len(x)):
            u=i+1
            print (str(u)+')'+x[i])
        y=int(input("select which file to open:"))
        y=y-1
        os.startfile(x[y])
    if(len(x)!=0):
        with open("SearchComputer.txt","r+") as f:
            for i in range(0,len(x)):
                t2=1
                lines=0
                for line in f:
                    (key,value,t1)=line.split("\t")
                    if(search.lower() in key and x[i] in value):
                        t2=0
                        break
                    lines+=1
                if(lines==1000):
                    f.seek(0,0)
                if(t2==1):
                    f.write(z[i] + "\t" + x[i] + "\t" + "\n")
                #f.seek(0,0)

    p=input("Press enter to quit")
else:
    p=input("Press enter to quit")
