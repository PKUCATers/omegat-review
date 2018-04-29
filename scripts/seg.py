#coding=utf-8

f=open("segs.txt","r",encoding="utf-8")
f2=open("tmx.txt","r",encoding="utf-8")
num=0
for line in f.readlines():
    num=num+1
    line=line.split("\t")
    name=line[0]
    start=int(line[1])
    end=int(line[2])
    #print(start)
    #print(end)
    segment=""
    if num>1:
        segment=str(start)+"\n"
    for i in range(start,end+1):
        segline=f2.readline()
        segment=segment+segline
        while segline.replace("\n","")!=str(i+1): #片段会跨行，所以用片段号进行划分
            segline=f2.readline()
            if segline.replace("\n","")==str(end+1): #去除读到最后一个片段多读一行的情况
                break
            segment=segment+segline

        #print(segment)
    fw=open(str(num)+".txt","w",encoding="utf-8")
    fw.write(segment)
    fw.close()