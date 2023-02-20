

ben = 21
john = 30
billy = 19
ollie = 45
rinty = 0

people = [ben, john, billy, ollie, rinty]
p1 = people[0]

print(people)
while True:
    p1 -= 1
    print(p1)
    if p1 == 0:
        people.pop(p1)
        print(people)
        break

for person in people:
    if person == 0:
        print("0 left")
