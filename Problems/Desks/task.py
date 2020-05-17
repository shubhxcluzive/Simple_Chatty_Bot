# put your python code here
no_of_desk = 0
n1 = int(input())
n2 = int(input())
n3 = int(input())
if (n1 + n2 + n3)%2 == 0:
    no_of_desk = (n1 + n2 + n3)/2
else:
    no_of_desk = int((n1 + n2 + n3)/2) + 1
print(int(no_of_desk))
