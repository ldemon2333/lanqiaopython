M=int(2e5)+5
N=2*M
class node:
    def __init__(self,prev:int,to:int,next:int):
        self.prev=prev
        self.to=to
        self.next=next

broke_pos=[-1]*N ; broken=[False]*N
father=[0]*N
edge=[node(-1,-1,-1)]           #保存结点之间连边的列表
first=[0]*N
edge_idx=1
def init(n:int):                #并查集的模板
    for i in range(n+1):
        father[i]=i
def find_father(x:int):
    if father[x]==x:return x
    f=find_father(father[x])
    father[x]=f
    return f
def unite(x:int,y:int):
    x=find_father(x) ; y=find_father(y)
    if x==y:return 
    else:father[x]=y

def add_edge(e1:int,e2:int):    #添加边的函数
    global edge_idx
    cu_node=node(e1,e2,first[e1])
    edge.append(cu_node)
    first[e1]=edge_idx
    edge_idx+=1

res=[0]*N
if __name__=="__main__":
    n,m=map(int,input().split())
    init(n)
    for i in range(m):
        x,y=map(int,input().split())
        add_edge(x,y) ; add_edge(y,x)   #由于是无向边，所以需要双向连边
    k=int(input())
    for i in range(1,k+1):
        broke_pos[i]=int(input())
        broken[broke_pos[i]]=True
    block_num=n-k
    for i in range(1,2*m+1):            #先连接所有的安全星球
        pos1=edge[i].prev ; pos2=edge[i].to
        if (not broken[pos1]) and (not broken[pos2]) and (find_father(pos1)!=find_father(pos2)):
            unite(pos1,pos2)
            block_num-=1
    res[k+1]=block_num
    for i in range(k,0,-1):             #逆向修复被破坏的星球
        block_num+=1
        broken[broke_pos[i]]=False
        j=first[broke_pos[i]]
        while j:
            if (not broken[edge[j].to]) and (find_father(broke_pos[i])!=find_father(edge[j].to)):
                block_num-=1
                unite(broke_pos[i],edge[j].to)
            j=edge[j].next
        res[i]=block_num
    for i in range(1,k+2):print(res[i])