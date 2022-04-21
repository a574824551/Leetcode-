M = 4

#编号，cpu核数，内存，架构，NP加速
serves = [[0,2,200,0,1],
         [1,3,400,0,1],
         [2,3,400,1,0],
         [3,3,300,0,1]]

#最大数量，策略，cpu核数，内存，架构，NP加速
need = [3,1,3,200,0,1]

strategy = need[1]
tmp_ser = []
for ser in serves:
    cpuCount, memSize ,cpuArch, supportNP = ser[1],ser[2],ser[3], ser[4]
    if cpuArch == need[-2] and supportNP == need[-1] and ser[1]>= need[2] and ser[2]>= need[3]:
        tmp_ser.append({'num':ser[0], "cpuCount":ser[1], "memSize":ser[2]})

if strategy == 1:
    tmp_ser = sorted(tmp_ser, key = lambda i:(i['cpuCount'], i['memSize'], i['num']))
elif strategy == 2:
    tmp_ser = sorted(tmp_ser, key= lambda i: (i['memSize'], i['cpuCount'], i['num']))

if len(tmp_ser) == 0:
    res = '0'
if len(tmp_ser)>= need[0]:
    res = str(need[0])+' '+' '.join(str(x['num']) for x in tmp_ser[:need[0]])
else:
    res = str(need[0])+' ' + ' '.join(str(x['num']) for x in tmp_ser)
