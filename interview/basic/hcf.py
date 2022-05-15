def compute_hcf(x,y):
    if(x>y):
        j=y
    else:
        j=x
    for i in range(1,j+1):
        if(x%i==0 and y%i==0):
            hcf=i
    return hcf

# Function to find HCF the Using Euclidian algorithm
def compute_euclidian_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

x1=110
x2=22
print(compute_hcf(x1,x2))
print(compute_euclidian_hcf(x1,x2))