import csv
#读csv文件
r=open('cpustatus.csv','r')
reader=csv.reader(r)
for i in reader:
    print(i)
r.close()
#写
rw=open('cpustatus.csv','w',newline='')
writer=csv.writer(rw,dialect='excel')
writer.writerow([1,2])
rw.flush()
rw.close()