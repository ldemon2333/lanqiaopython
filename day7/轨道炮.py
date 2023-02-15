N = int(input())
X = [0 for _ in range(1010)]        #记录N个敌人的横坐标
Y = [0 for _ in range(1010)]        #记录N个敌人的纵坐标
vx = [0 for _ in range(1010)]       #记录N个敌人在x方向的速度，没有则为0
vy = [0 for _ in range(1010)]       #记录N个敌人在y方向的速度，没有则为0
for i in range(N):                  #速度以x方向向右，y方向向上为正
    data = input().split()          #输入每组数据
    X[i] = int(data[0])             #记录当前数据的横坐标
    Y[i] = int(data[1])             #记录当前数据的纵坐标
    if data[3] == 'U':              #向上,y方向为正
        vy[i] = int(data[2])
    elif data[3] == 'D':            #向下，y方向为负
        vy[i] = -1*int(data[2])
    elif data[3] == 'R':            #向右，x方向为正
        vx[i] = int(data[2])
    elif data[3] == 'L':            #向左，x方向为负
        vx[i] = -1*int(data[2])
                                    #本题的所有数据，要么只在x方向移动，要么只在y方向移动
def f(p,v):                         #统计当前坐标和对应坐标方向在某时刻能获得的最大消灭敌人数
    mx = 0                          #记录最大值
    for i in range(N):              #取出该方向的每一个敌人作为基准，计算当前最多消灭敌人数
        time = {}                   #新建字典，用于记录t时刻有多少其他敌人与当前目标在同一坐标线上(计算横坐标时为纵坐标，反之为横坐标)
        cnt = 1                     #由于以X[i]为目标，所以我们至少会打中他一个
        for j in range(i+1,N):      #对其他目标进行判定，由于对称性，先前判断过的无需继续判断了
            if v[i] == v[j]:
                if p[i]==p[j]:      #发现与当前目标位置相同，速度也相同，那么他一定也会被打中
                    cnt +=1
                mx = max(mx,cnt)    #更新最大数量，继续下一个目标的判断
                continue
            dx = p[i]-p[j]          #相对位置
            dv = v[j]-v[i]          #相对速度
            t = dx//dv
            if dx%dv or t<0:        #此时这个敌人与我们当前目标是不会在某个时刻有相同纵坐标的
                continue
            time[t] = time.get(t,0)+1   #此时这个敌人与我们当前锁定的目标会在时刻t处于同一纵坐标用字典统计当前时刻，更新数值
            mx = max(mx,time[t]+cnt)    #获取整个字典中最大的值

    return mx                       #返回该方向上的最大值

mx = max(f(X,vx),f(Y,vy))           #对x和y两个方向分别进行判断，最后取最大值
print(mx)