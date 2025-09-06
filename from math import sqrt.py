foo = 3
bar = 3.1
myname = "Rylan Hendricks"

foo_type = type(foo)
bar_type = type(bar)
myname_type = type(myname)

if foo < bar:
    print("foo", foo, "<", "bar", bar)
else:
    print("bar", bar, "<", "foo", foo)
print(foo_type, bar_type, myname_type)

i = 1
for i in range(1, 11):
    print(i**2)
    i += 1

j = 1
for j in range(1, 11):
    if j == 7:
        pass
    else:
        print(j**2)
j += 1

numb = input("Please pick a number: ")
numb = int(numb)
def isPrime(num : int) -> bool:
    for m in range(1, num - 1):
        if num // m == 0 :
            print("True")
            return True
        else:
            print("False")
            return False
    
isPrime(numb)