import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = random.randint(0, 4)
if random_friend == 0:
    print(friends[0])
elif random_friend == 1:
    print(friends[1])
elif random_friend == 2:
    print(friends[2])
elif random_friend == 3:
    print(friends[3])
else:
    print(friends[4])