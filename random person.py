Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
... 
... random_friend = random.randint(0, 4)
... if random_friend == 0:
...     print(friends[0])
... elif random_friend == 1:
...     print(friends[1])
... elif random_friend == 2:
...     print(friends[2])
... elif random_friend == 3:
...     print(friends[3])
... else:
