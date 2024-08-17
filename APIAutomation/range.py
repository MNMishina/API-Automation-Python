# range start, stop, step
import random

r = list(range(0, 11, 2))
# print(r)

# for f in range(10):
#     print(f)

r = random.randrange(0, 10000000)
user_random = "User" + str(r)
print(user_random)