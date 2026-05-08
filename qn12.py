nums = list(map(int, input("Enter 10 integers separated by spaces: ").split()))
MyList1 = [x for x in nums if x % 2 != 0 and x % 3 != 0]
MyList2 = [x for x in nums if x % 9 == 0]
print(*(MyList1))
print(*(MyList2))
