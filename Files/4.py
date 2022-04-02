#Write a program to append a file with the contents of another file.
f1=open("demo1.txt","r")
data=f1.read()
f2=open("demo2.txt","a")
f2.write(data)
f1.close()
f2.close()
