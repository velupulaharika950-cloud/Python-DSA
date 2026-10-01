def binarysearch(ar,target):
    l=0
    r=len(ar)-1
    m=(1+r)//2
    while l<r:
        if ar[m]==target:
            print(f'{target} is found at index {m}')
            return
        elif ar[m]<target:
            l=m+1
            m=(1+r)//2
        else:
            r=m-1
            m=(1+r)//2
    print("element not found")
        
b=[10,20,30,40,50,60]
binarysearch(b,22)