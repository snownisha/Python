#Matrix Addition
X = [[4,1,3],[5 ,7,2],[7 ,8,9]]

Y = [[9,8,7],[6,5,4],[3,2,1]]


result = [[0,0,0],[0,0,0],[0,0,0]]


for i in range(len(X)):
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]

for r in result:
	print(r)
