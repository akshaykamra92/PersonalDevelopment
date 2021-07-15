processes = {}
times = {}


def proctimes(ma, pr, ev, tm):
    if ev == 'start':
        processes.setdefault((ma, pr), []).append(float(tm))
    else:
        vals = processes[(ma, pr)]
        diff = float(tm) - float(vals[0])
        vals.pop(0)
        processes[(ma, pr)] = vals
        times.setdefault((ma,pr), []).append(diff)


with open('log', 'r') as file:
    for line in file:
        mach, proc, event, time = line.split()
        proctimes(mach, proc, event, time)

for sessions in times:
    print('Average for ', sessions, ' is', float(sum(times[sessions])/len(times[sessions])))

