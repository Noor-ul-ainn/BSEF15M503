#!usr/bin/env python

wait_time = 0
turn_time = 0
total_Wtime = 0
processes = {}
arrival_time = []
burst_time = []
priority_No = []
numOfproc = input("Enter the number of processes:  ")

for i in range(0, numOfproc):
	priority = input("Enter priority No.  ")
	priority_No.append(priority)
	arrival = input("Enter arrival time:  ")
	arrival_time.append(arrival)
	burst = input("Enter burst time:  ")
	burst_time.append(burst)
	processes[i] = [priority_No[i], burst_time[i], arrival_time[i]]

print ("process No.\tPriority No.\tBurst Time\tArrival Time")

for i in range(0, numOfproc):
	
	print i, "               ", processes.get(i)[0], "               ", processes.get(i)[1], "               ", processes.get(i)[2]
for i in range(0, numOfproc-1):
	for j in range(0, numOfproc-i-1):
		if processes.get(j+1)[0] < processes.get(j)[0]:
			temp = processes[j]
			processes[j] = processes[j+1]
			processes[j+1] = temp

total_Ttime = processes.get(0)[1]

for i in range(0, numOfproc):
	total_Wtime = total_Wtime + processes.get(i)[1]
	wait_time = total_Wtime - processes.get(i)[2]
	turn_time = turn_time +(total_Ttime - processes.get(i)[2])
	total_Ttime = total_Ttime + processes.get(i)[1]
	
print "Total wait Time:    ", wait_time
print "Average wait time:  ", float(wait_time)/numOfproc

print "Total TurnAround Time:    ", turn_time
print "Average TurnAround time:  ", float(turn_time)/numOfproc

