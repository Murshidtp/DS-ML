f1=open("demo1.txt","r")
f2=open("demo2.txt","r")
i=0
for j in f1:
    i += 1;
    for k in f2:
        if j == k:
            print("Both the lines are same")
        else:
            print("Both  the lines are not same")
f1.close()
f2.close()