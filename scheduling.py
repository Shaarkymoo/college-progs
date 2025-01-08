def processor(ammount) -> list:
    licct = []
    for a in range(ammount):
        deets = str(input("Enter details(name,arrival,burst) seperated with commas for process "+str(a)+":>"))
        deets = deets.split(',')
        licct.append([deets[0],eval(deets[1]),eval(deets[2]),0,0])
        print("details for process",deets[0],":\n","\tarrival time =",deets[0][0],",\tburst time =",deets[0][1])
    
    # [processName,arrivalTime,burstTime,turnAroundTime,waitingTime]

    print(licct)
    return licct

def fcfs(book):
    notZero = len(book)
    while notZero:
        for a in range(len(book)):
            if book[a][2] == 0:
                notZero -= 1
                continue

            book[a][3] += book[a][2]

            for b in range(len(book)):
                if b == a:
                    continue
                if book[b][2] != 0:
                    book[b][4] += book[a][2]
                    book[b][3] += book[a][2]
            
            book[a][2] = 0

    for a in range(len(book)):
        book[a][3] -= book[a][1]
        book[a][4] -= book[a][1]
    
    global keepGoing
    keepGoing = False
    return book

def sjf(book):
    secondsPassed = 0
    notZero = len(book)
    while notZero:
        bursts = []
        for a in range(len(book)):
            if book[a][1]<=secondsPassed and book[a][2]!=0:
                bursts.append(book[a])

        print(bursts)
        minimum = bursts[0][2]
        for a in bursts:
            if a[2]<=minimum:
                minimum = a[2]
        
        print(bursts,minimum)

        for b in range(len(bursts)):
            for a in range(len(book)):
                if bursts[b][0]==book[a][0] and book[a][2]==minimum:

                    book[a][3] += book[a][2]
                    secondsPassed += book[a][2]

                    for c in range(len(book)):
                        if c == a:
                            continue
                        if book[c][2] != 0:
                            book[c][4] += book[a][2]
                            book[c][3] += book[a][2]
                    
                    book[a][2] = 0
                    notZero-=1



        print(book)
        print()

    for a in range(len(book)):
        book[a][3] -= book[a][1]
        book[a][4] -= book[a][1]

    global keepGoing
    keepGoing = False
    return book

def srtf(book):
    secondsPassed = 0
    notZero = len(book)
    while notZero:
        bursts = []
        for a in range(len(book)):
            if book[a][1]<=secondsPassed and book[a][2]!=0:
                bursts.append(book[a])

        minimum = bursts[0][2]
        for a in bursts:
            if a[2]<=minimum:
                minimum = a[2]
        
        print(bursts,minimum)
        condition = True
        for b in range(len(bursts)):
            if not condition:
                break
            for a in range(len(book)):
                if bursts[b][0]==book[a][0] and book[a][2]==minimum:
                    print("something happened for")

                    book[a][3] += 1
                    secondsPassed += 1

                    for c in range(len(book)):
                        if c == a:
                            continue
                        if book[c][2] != 0:
                            book[c][4] += 1
                            book[c][3] += 1
                    
                    book[a][2] -= 1
                    if book[a][2]==0:
                        notZero-=1

                    condition = False
                    break

        print(book)
        print()

    for a in range(len(book)):
        book[a][3] -= book[a][1]
        book[a][4] -= book[a][1]

    global keepGoing
    keepGoing = False
    return book
    
def rr(book):
    #quantum = int(input("Enter Time Quantum>>"))
    quantum = 4
    notZero = len(book)
    while notZero:
        for a in range(len(book)):
            if book[a][2] == 0:
                continue

            execution = (quantum if quantum<=book[a][2] else book[a][2])

            book[a][3] += execution

            for b in range(len(book)):
                if b == a:
                    continue
                if book[b][2] != 0:
                    book[b][4] += execution
                    book[b][3] += execution
            
            book[a][2] -= execution
            if book[a][2]==0:
                notZero-=1

            #print(book)


    for a in range(len(book)):
        book[a][3] -= book[a][1]
        book[a][4] -= book[a][1]
    
    global keepGoing
    keepGoing = False
    return book

def avg(book):
    wt = 0
    tat = 0
    count = 0
    for a in book:
        wt += a[4]
        tat += a[3]
        count+=1
    
    awt = wt / count
    atat = tat / count

    return awt,atat


global keepGoing
keepGoing = True

while keepGoing:
    ammount = int(input("Enter number of processes:>"))
    print()
    book = processor(ammount) 
    #book = [['p1', 0, 8, 0, 0],['p2', 1, 4, 0, 0],['p3', 2, 9, 0, 0],['p4', 3, 5, 0, 0]]
    #print(book)
    algorithm = int(input("Choose scheduling algorithm.\n1.FCFS\n2.SJF\n3.SRTF\n4.RR\n5.End\n>>>"))
    #algorithm = 4
    #print(algorithm)
    if algorithm == 1:
        final = fcfs(book)
    elif algorithm == 2:
        final = sjf(book)
    elif algorithm == 3:
        final = srtf(book)
    elif algorithm == 4:
        final = rr(book)
    elif algorithm == 5:
        print()
        final = None
        keepGoing = False
    print(final)
    print(avg(book))
    print()
    
