#Assignments For Lessons 19 To 20
# Task [1]
print(type(1))
print(type(1.5))
print(type(1+2j))

# Task [2]



f=1+2j

# Print Imaginary Part Here
print(f.imag)
# Print Real Part Here
print(f.real)

# Task [3]

num = 10

# Needed Ouput
# 10.0000000000
print(float(num))



# Task [4]
num = 159.650

# Needed Output
# 159
d=int(num)
print(d)
# <class 'int'>
print(type(d))

# Task [5]

print(100 - 115 ) #-15
print(50 * 30) # 1500
print(21 % 4) # 1
print(110 // 11) # 10
print(97 // 20) # 4

# Assignments For Lessons 21 To 23
# Task [1]
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
print(friends[0])
# "Osama" => Method Two
print(friends[-5])
# "Mahmoud" => Method One
print(friends[-1])
# "Mahmoud" => Method Two
print(friends[4])


# Task [2]

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama", "Sayed", "Mahmoud"
print(friends[0],friends[2],friends[4])
# "Ahmed", "Ali"
print(friends[1],friends[3])



# Task [3]

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
print(friends)
# "Ali", "Mahmoud"



# Task [4]
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
friends[-1],friends[-2]="Elzero","Elzro"
print(friends)


# Task [5]
friends_2 = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
x = friends_2.insert(0,5)
print(x)
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Task [6]
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
k=friends.pop(0)
g= friends.pop(0)

print(friends)
# ["Ahmed", "Sayed"]
l= friends.pop(-1)
print(friends)


# Task [7]

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
k = friends +employees +school
print(k)

# Task [8]
friends123 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
k= sorted(friends123)
print(k)
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
m= sorted(friends123)
l= m.reverse()
print(l)

# Task [9]
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# 6
print(len(friends))
