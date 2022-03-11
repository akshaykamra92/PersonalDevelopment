# processes = {}
# times = {}
#
#
# def proctimes(ma, pr, ev, tm):
#     if ev == 'start':
#         processes.setdefault((ma, pr), []).append(float(tm))
#     else:
#         vals = processes[(ma, pr)]
#         diff = float(tm) - float(vals[0])
#         vals.pop(0)
#         processes[(ma, pr)] = vals
#         times.setdefault((ma,pr), []).append(diff)
#
#
# with open('log', 'r') as file:
#     for line in file:
#         mach, proc, event, time = line.split()
#         proctimes(mach, proc, event, time)
#
# for sessions in times:
#     print('Average for ', sessions, ' is', float(sum(times[sessions])/len(times[sessions])))

########### Alternate

started = {}
completed = {}


def visitations(mach, proc, event, time):
    if event == 'start':
        started.setdefault((mach,proc),[]).append(time)
    if event == 'end':
        val = started[(mach,proc)]
        completed.setdefault(proc,[]).append(float(float(time) - float(val.pop())))
        # if len(val) > 0:
        #     started[(mach,proc)] = val
        # else:
        #     started.pop((mach,proc))
        for key,value in completed.items():
            print('The Average for ' + key + ' is '+ str(float(sum(value)/len(value))))
        print('\n')


with open('log', 'r') as file:
    for inp in file:
        machi,proci,eventi,timei = inp.split()
        visitations(machi,proci,eventi,timei)
        # print(completed)