import statistics

def median(approaches, days):
    flag = 0
    for i in range (len(approaches)):
        m = statistics.median(approaches[0:days])
        if approaches[i] <= (m / 2):
            flag += 1
    print(flag)
        
median([90, 80, 100, 30, 110, 70, 130, 35], 3)