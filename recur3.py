# print n to 1 using recursion (tail recursion)
def func(i,n):
    if i>n:
        return
    func(i+1,n)
    print(i)
func(1,4)