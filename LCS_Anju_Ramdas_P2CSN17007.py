f= open('input.txt','r')
buff=f.readline()
word1=buff.rstrip()
buff=f.readline()
word2=buff.rstrip()
f.close()
m=len(word1)
n=len(word2)
mat=[]
l=[0]*(m+1)
input1=list(word1)
input2=list(word2)
mat.append(l)
k=[]
for i in range(1,n+1):
	k=[]
	k.append(0)
	for j in range(1,m+1):
		if(input2[i-1]==input1[j-1]):
			k.append(mat[i-1][j-1]+1)
		else:
			k.append(max(mat[i-1][j],k[j-1]))
	mat.append(k)
lenth=mat[n][m]

ans=[]			
i=n
j=m

while(j>0 and i>0):		
	if(input2[i-1]==input1[j-1]):
		ans.insert(0,input2[i-1])
		i=i-1
		j=j-1
	else:
		if(mat[i][j]==mat[i-1][j]):
			i=i-1
		else:
			j=j-1
ans1=''.join(map(str, ans))
f= open('output.txt','w')
f.write(str(lenth)+'\n')	
f.write(ans1+'\n')				
f.close()