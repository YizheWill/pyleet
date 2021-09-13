
def getNthFib(n):
    # Write your code here.
    last = 1
    before_last = 0

    if n == 1:
        return before_last
    if n == 2:
        return last

    for i in range(3, n):
        last, before_last = last + before_last, last
    return last + before_last
