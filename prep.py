def binarySearch (alist, item):
    start=0
    last =len(alist)-1
    found=False

    while first <= last and not found:
        mid_index = (start + last) //2
        if alist[mid_index] == item:
            found=True
        else:
            if item < alist[mid_index]:
                last = mid_index-1
            elif item > alist[mid_index]:
                start = mid_index-1
    if found:
        return mid_index # returning the position that it is found
    elif not found:
        return found # return false if item not found

def sorting_list(a):
    num_round=0
    done=False
    if a:
        while not done:
            done=True
            for i in range(1,len(a)):
                if a[i-1] > a[i]:
                    temp= a[i]
                    a[i]=a[i-1]
                    a[i-1]=temp
                    done=False
                    num_round+=1
                    break

    return (num_round, a)


# =========================== an applied DFS ========================
def findadjecent(grid, coor):
    horizontal=[]
    if coor[0] == len(grid) - 1:
        horizontal=[coor[0] - 1, coor[0]]
    elif coor[0] == 0:
        horizontal = [0,1]
    else:
        horizontal=[coor[0] + 1, coor[0], coor[0] - 1]

    vertical=[]
    if coor[1] == len(grid[coor[0]]) - 1:
        vertical=[coor[1] - 1, coor[1]]
    elif coor[1] == 0:
        vertical = [0,1]
    else:
        vertical=[coor[1] + 1, coor[1], coor[1] - 1]

    adjacent = []
    for i in horizontal:
        for j in vertical:
            if i == coor[0] and j == coor[1]:
                continue
            else:
                adjacent.append((i, j))
    return adjacent

def printgrid(grid):
    for line in grid:
        print line
def DFS(grid, coor):
    print('new DFS search')
    printgrid(grid)
    area_count = 0
    stack = []
    stack.append(coor)
    while stack:
        area_count += 1
        current_coor = stack.pop()
        grid[current_coor[0]][current_coor[1]] = 'X'
        for child_coor in findadjecent(grid, current_coor):
            if grid[child_coor[0]][child_coor[1]] == 1:
                grid[child_coor[0]][child_coor[1]]='X'
                stack.append(child_coor)
    print('finished')
    printgrid(grid)
    return (area_count,grid)


def getBiggestRegion(grid):
    biggest = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:
                temp,grid = DFS(grid, (i, j))

                biggest = temp if temp > biggest else biggest
    return biggest




if __name__  == '__main__':
    grid=[[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]
    result=findadjecent(grid, (0,2) )
    print(result)
    print(getBiggestRegion(grid))

# ==========================================================
# MATRIX EXPONENTIATION
# note: matrix_exponentiation is good for soling linear recurrence in log(n)
# where n is (for example): f(n+1)=f(n)+f(n-1)


def extract_column(matrix, col_num):
    result=[matrix[i][col_num] for i in range(len(matrix))]
	return result

def matrix_multiply(m,n): # m: a * b         n: b*c
	if len(n) == 0 or len(m) == 0:
		raise ValueError('empty matrix')
	elif len(m[0]) != len(n) :
		raise ValueError('dimension error!')
	else:
		result_matrix=[]
		for i in range(len(m)):
			temp=[]
			for j in range(len(n[0])):
				column=extract_column(n,j)
				#print ('column is: ', column)
				cell=sum([m[i][index]*column[index] for index in range(len(column))])
				temp.append(cell)
			result_matrix.append(temp)
			#print ('This line is: ', temp)
		return result_matrix


def finding_steps(n):
	if n == 0 or n ==1:
		return 0
	elif n ==2 :
		return 2
	elif n == 3:
		return 4
	else:
		base=[[4],[2],[1]]
		base_transformation=[[1,1,1],[1,0,0],[0,1,0]]
		transformation=base_transformation
		count=1
		while count*2 < (n-3):
			transformation= matrix_multiply(transformation, transformation)
			count=count*2
		while count<n-3:
			transformation = matrix_multiply( base_transformation, transformation)
			count+=1
		final=matrix_multiply(transformation,base)
		# print(transformation)
		# print(count)
		# print (final)
		return final[0][0]

if __name__ =='__main__':
	a=[[1,1,1],[1,0,0],[0,1,0]]
	b=[[4],[2],[1]]

# =================================================
def merge_sort (alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]

        lefthalf = merge_sort(lefthalf)
        righthalf = merge_sort(righthalf)

        i, j, k =0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i+=1
            else:
                alist[k] = righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf): # incase left half has left over
            alist[k] = lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1

    return alist
# ========================= Tree Traversal ========================
def preOrder(root): # self comes first
    if root == None:
        return ''
    path = ''j

    def helper(path, current):
        path += str(current.data) + ' '
        if current.left != None:
            path = helper(path, current.left)
        if current.right != None:
            path = helper(path, current.right)

        return path

    path = helper(path, root)
    print(path)

# HUFFMAN TREE ENCODING
# encoding for individual letter base on user frequency, greater frequency, shorter encoding

# ============================== QUICK SORT =========================
def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition (alist, first , last)

        quickSortHelper(alist, first. splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition (alist, first, last):
    pivot_value= alist[first]

    left_index= first+1
    right_index= last

    done = False
    while not done:
        while left_index <= right_index  and alist[left_index] <= pivot_value:
            left_index+=1
        while right_index >= left_index and alist[right_index] >= pivot_value:
            right_index-=1
        if right_index < left_index:
            done=True
        else: # swapping element
            temp = alist[left_index]
            alist[left_index]=alist[right_index]
            alist[right_index]=temp
    # after everythign but the first pivot has been organized
    temp = alist[first]    # now the first pivot is in the middle
    alist[first] = alist[left_index]
    alist[left_index] = temp

    return alist

