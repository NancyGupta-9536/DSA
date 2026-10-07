# print 1 to n using recursion (head recursion)
def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1,n)
func(1,4)