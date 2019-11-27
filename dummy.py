from scheduleapi import scheduleapi



print("Enter periodic jobs")
num=int(input())
tasks=[list(map(int,input().split()))+[_+1] for _ in range(num)]

# priority according to RM
order={ val[4]:idx for idx,val in enumerate(sorted(tasks, key = lambda x: x[3])) }
print(order)
#1- rm and dm , 2- lst , 3- edf
scheduleapi.schedule(tasks, order, 3)
