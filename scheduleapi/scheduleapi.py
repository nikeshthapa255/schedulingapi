import math
def gcd(a,b) :
    if (a < b) :
        return gcd(b, a)

    # base case
    if (abs(b) < 0.001) :
        return a
    else :
        return (gcd(b, a - math.floor(a / b) * b))
def lcm(a,b):
    return (a*b)/gcd(a,b)


def priority(ch, x, order, pos):
    if ch==1:#for rm and dm
        return -order[x[4]]
    elif ch==2:#for lst
        return -(x[2]-pos-x[1])
    elif ch==3:#for edf
        return -x[2]
    else:
        raise ValueError("Wrong input for choosen fields")




#task, priority
#task - arrival time, execution time, time period, deadline
#1- rm and dm ; 2- lst; 3- edf
def schedule(tasks, order, which_schedule):
    H=1
    for val in tasks:
        H=lcm(H, val[2])
    H=round(H)
    todo=make_task(tasks, H)
    s1,m1=scheduling(todo, order, which_schedule, H)
    print_schedule(s1, m1)





#do scheduling 
def scheduling(todo, order, which_schedule, H):
    schedule_with_preemption=['' for i in range(H)]
    previous=[]
    missed=[]
    pos=0
    while pos<H:
        if todo[pos] or previous:
            previous.extend(todo[pos])
            previous.sort( key= lambda x: priority(which_schedule, x, order, pos))
            while previous and previous[-1][2]<pos:
                missed.append(previous.pop()[3])
            if previous:
                mn=previous.pop()
                schedule_with_preemption[pos]=mn[3]
                mn[1]-=1
                if mn[1]:
                    previous.append(mn)
        pos+=1
    return schedule_with_preemption, missed



#print output
def print_schedule(schedule, missed):
    H=len(schedule)
    print("Time", "Job", sep='\t')
    for i in range(H):
        print(i+1,schedule[i], sep='\t')
    print('Missed', *missed)




#make tasks
def make_task(tasks, H):
    todo=[[] for i in range(H)]
    for task in tasks:
        #print(task)
        arrival_time=int(task[0])
        deadline=task[3]
        period=int(task[2])
        execution_time=task[1]
        num=task[4]
        ch=0
        for arr in range(arrival_time, H, period):
            ch+=1
            todo[arr].append([arr, execution_time, deadline + (ch-1)*period, str(num)+str(ch), num])
    return todo
