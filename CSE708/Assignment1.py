import sys 
edges =[]
def graphExists(a):
 
    # Keep performing the operations until one
    # of the stopping condition is met
    node = 1
    while True:
 
        # Sort the list in non-decreasing order
        a = sorted(a, reverse = True)
 
        # Check if all the elements are equal to 0
        if a[0]== 0 and a[-1]== 0:
            return True
 
        # Store the first element in a variable
        # and delete it from the list
        v = a[0]
        a = a[1:]
        if v>len(a):
            return False
 
        # Subtract first element from next v elements
        for i in range(v):
            a[i]-= 1
            if a[i]<0:
                return False
        for i in range(v):
            edges.append((node,node+i+1))
        node += 1
    


def main():
    node = int(input())
    seq =list(map(int,sys.stdin.readline().strip().split()))

    degree_sum = sum(seq) 
    if graphExists(seq):
        for x,y in edges:
            print("{} {}".format(x,y))
    else:
        print(-1)

if __name__ == '__main__':
    main()
