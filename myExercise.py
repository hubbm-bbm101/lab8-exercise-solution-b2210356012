import sys
mdict={}
with open(sys.argv[1],"r",encoding="utf-8") as f:
    list1 = (f.read().splitlines())
    for i in list1:
        mdict[i.split(":")[0]]=i.split(":")[1]
    for j in sys.argv[2].split(","):
        try:
            print(j,":",mdict[j])
        except KeyError:
            print("Can not find the record of",j)


