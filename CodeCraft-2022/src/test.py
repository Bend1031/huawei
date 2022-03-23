tol=10
need=[tol/8 for i in range(8)]
need_int=list(map(int,need))
need_int[-1]=need_int[-1]+tol-sum(need_int)
print()