from collections import defaultdict
import sys
def swap(x, y):
        temp = heap[x]
        heap[x] = heap[y]
        heap[y] = temp

def minHeapify(posi):
        smallest = posi
        left = 2*posi + 1
        right = 2*posi + 2
 
        if left < len(heap) and heap[left][1] < heap[smallest][1]:
            smallest = left
 
        if right < len(heap) and heap[right][1] < heap[smallest][1]:
            smallest = right
 
       
        if smallest != posi:
        	pos[heap[smallest][0]-1 ] = posi
        	pos[heap[posi][0]-1] = smallest
        	swap(smallest, posi)
        	minHeapify(smallest)

def Min(heap):
 
        
        if len(heap) == 0:
            return
 
        
        root = heap[0]
 
        
        lastNode = heap[len(heap) - 1]
       
        heap[0] = lastNode
        pos[lastNode[0]-1] = 0
        pos[root[0]-1] = len(heap) - 1
 
        
        del heap[-1]
        minHeapify(0)
       
        return root
def decre(v, dist):
 
        
        i = pos[v-1]
 
        
        heap[i][1] = dist
 
       
        while i > 0 and heap[i][1] < heap[(i - 1) / 2][1]:
 
            
            pos[ heap[i][0]-1 ] = (i-1)/2
            pos[ heap[(i-1)/2][0]-1 ] = i
            swap(i, (i - 1)/2 )
 
            
            i = (i - 1) / 2;

f= open('test5','r')
buff=f.readline()
l=map(int,buff.split())
vertex=l[0]
edge=l[1]
d = defaultdict(list)
j=0
l1=[]
for i in range(0,edge):
	l1=[]
	l2=[]
	l=[]
	buff=f.readline()
	l=map(int,buff.split())	
	if(l[0]==j):
		l1.append(l[1])
		l2.append(j)
		l2.append(l[2])
		l1.append(l[2])
		d[j].insert(0, l1)
		d[l[1]].insert(0,l2)


	else:
		j=j+1
		l1.append(l[1])
		l1.append(l[2])
		l2.append(j)
		l2.append(l[2])
		d[j].insert(0, l1)
		d[l[1]].insert(0,l2)
	

f.close()		
heap=[]
heap.append([1,0])
for i in range(2,vertex+1):
	heap.append([i,sys.maxint])

w=[]
pos=[]
p=[]
w1=[]

for i in range(0,vertex):
	w.append(sys.maxint)
	pos.append(i)
	p.append(0)
w[0]=0	 
weight=0
while len(heap) != 0:
 
           
            new = Min(heap)
            u = new[0]
            w1.append(new[1])

           
            weight=weight+new[1]
           
            for i in d[u]:
            	
            	v = i[0]
            	
                if i[1] < w[v-1] and (pos[v-1]<len(heap)):
                    w[v-1] = i[1]
                    
                    decre(v, w[v-1])
                    p[v-1] = u                   


f= open('output.txt','w')
f.write(str(weight)+'\n')
j=1

p1=[]
for i in range(1,len(p)):
		p1.append([p[i],i+1,w[i]])
		
p2=sorted(p1)

for i in range(0,len(p2)):
	
	f.write('{} {} {}\n'.format(str(p2[i][0]),str(p2[i][1]),str(p2[i][2])))
	
f.close()


