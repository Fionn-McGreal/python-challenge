import csv
totalmonths=0
Totalprofit =0
changelist=[]
Month=[]
with open('budget_data.csv') as data:
    reader=csv.reader(data)
    header=next(reader)
    firstrow=next(reader)
    totalmonths+=1
    Totalprofit+=int(firstrow[1])
    previous=int(firstrow[1])
    for row in reader:
        totalmonths+=1
        Totalprofit+=int(row[1])
        change=int(row[1])-previous
        previous=int(row[1])
        changelist.append(change)
        Month.append(row[0])
averagechange=sum(changelist)/len(changelist)
minchange=min(changelist)
maxchange=max(changelist)
minchangeindex=changelist.index(minchange)
maxchangeindex=changelist.index(maxchange)
minmonth=Month[minchangeindex]
maxmonth=Month[maxchangeindex]
print(f"Average change: ${round(averagechange,2)}, min change {minmonth}: ${minchange}, max change {maxmonth}: ${maxchange}")

with open ('ouput.txt','w') as txt_file : 
    print(f"Average change: ${round(averagechange,2)}, min change {minmonth}: ${minchange}, max change {maxmonth}: ${maxchange}", file = txt_file)
