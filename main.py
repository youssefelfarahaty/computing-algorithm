#this function is to calculate equation of straight line and to determine the third point is on the same line =0 ,inside right (<0) ,outside left (>0)
def slope(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])
    # (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
#function to generate the convex hull points,
def convexhull(p):
    # get size of input points
    n=len(p)
    # any 3 points will form a triangle, so returned as convex without checking
    if n<=3:
        return(p)
    #We store the hull points in form of a set
    hull=set()
    for i in range(n):
        for j in range(i+1,n):
            left=[]
            right=[]
            for k in range(n):
                if k!=i and k!=j:#take 3 different points
                    s=slope(p[i],p[j],p[k])
                    if s>0:#on left of stline
                        left.append(p[k])
                    elif s<0:#on right of stline
                        right.append(p[k])
            if not left and right: #right not empty
                hull.add(tuple(p[i]))
                hull.add(tuple(p[j]))
            elif left and not right: #left not empty
                hull.add(tuple(p[j]))
                hull.add(tuple(p[i]))
    return(hull)

#main function
n=int(input("Enter number of points: "))
points=[]
#takes input as an order pair and store it in a list called points
for i in range(n):
    x,y=map(float,input(f"Enter coordinates of {i+1}: ").split())
    points.append([x,y])
hull=convexhull(points)
print(hull)
"""
test cases:

test case 1:
n=8
points= [[0, 3], [1, 1], [2, 2], [4, 4],[0, 0], [1, 2], [3, 1], [3, 3]]
output=[(0,0),(4,4),(3,1),(0,3)]

test case 2:
n=7
points = [[1, 2], [2, 4], [4, 3], [5, 1], [3, 0], [2, 1], [3, 2]]
output=[(3,0),(5,1),(4,3),(2,4),(1,2),(2,1)]

test case 3:
n=4
points = [[1, 1], [2, 3], [3, 2], [5, 1]]
output={(2, 3), (1, 1), (5, 1)}

test case 4:
n=6
points = [[2, 4], [4, 5], [1, 3], [3, 6], [5, 1],[6, 2]]
output={(6, 2), (5, 1), (4, 5), (3, 6), (1, 3)}

test case 5:
n=5
points=[[1.1,1.2],[-2,4],[-3,12],[4,-16],[12,8]]
output={(-3.0, 12.0), (4.0, -16.0), (12.0, 8.0), (-2.0, 4.0)}

test case 6:
n=9
points=[[2,7],[5,4],[1,2],[8,9],[3,6],[4,1],[7,3],[9,5],[6,8]]
output={(1, 2), (2, 7), (7, 3), (9, 5), (8, 9), (4, 1)}
"""