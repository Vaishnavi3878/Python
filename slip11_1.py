x=(1,2,3,4)
y=(3,5,2,1)
z=(2,2,3,1)
print("Original Data are:")
print(x)
print(y)
print(z)
print("After adding tuple elements is:",end=" ")
ans=tuple(map(sum,zip(x,y,z)))
print(ans)
