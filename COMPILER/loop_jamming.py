import time
from datetime import datetime

def func1(arr1,arr2,arr3):
    t1=datetime.now()
    print(t1.minute,":",t1.second,":",t1.microsecond)
    start=time.time()
    print("Start time:",start)
    for i in range(0,10000000):
        sum=0
        for j in range(0,len(arr1)):
            sum=sum+arr1[j]
        for k in range(0,len(arr2)):
            sum=sum+arr2[k]
        for l in range(0,len(arr3)):
            sum=sum+arr3[l]
        if(sum!=210):
            print(false)
    tm=datetime.now()
    print(tm.minute,":",tm.second,":",tm.microsecond)
    end=time.time()
    print("End time:",end)
    print("Time difference of loop 1 is:",end-start)
    start=time.time()

    for i in range(0,10000000):
        sum=0
        for j in range(0,len(arr1)):
            sum=sum+arr1[j]
            sum=sum+arr2[j]
            sum=sum+arr3[j]
        if(sum!=210):
            print(false)
    tn=datetime.now()
    print(tn.minute,":",tn.second,":",tn.microsecond)
    end=time.time()
    print("End time:",end)
    print("Time difference of loop 2 is:",end-start)
    
arr1=[10,20,30]
arr2=[20,10,30]
arr3=[40,40,10]
func1(arr1,arr2,arr3)


