# print 1 to n using tail recursion (LEFT)
def func(i,n):
    if i>n:
        return
    func(i-1,n)
    print(i)
func(4,1)