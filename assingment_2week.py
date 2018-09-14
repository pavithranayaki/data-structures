def transpose(m):
    p=[[row[i] for row in m] for i in range(len(m)+1)]
    return p
print(transpose([[1,1,1],[2,2,2],[3,3,3]]))
