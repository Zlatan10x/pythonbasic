roll_no = [143,162,128,282,186]
friends = ["Adnan","Siam","Adnan","Arafat","Hasan","Raju"]

print(friends)
print(roll_no)

friends.extend(roll_no)
print(friends)

for num in roll_no :
    friends.remove(num)
friends.append("Mehedi")
print(friends)

friends.sort()
print(friends)

roll_no.sort()
print(roll_no)

#friends.clear()
print(friends)


roll_no.insert(3,43)
print(roll_no)

friends.pop()
print(friends)


print(friends.index("Raju"))

print(friends.count("Adnan"))

roll_no.reverse()
print(roll_no)

friends2 = friends.copy()
print(friends2)