import string
import random

def pw_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))


print(pw_gen(int(input("Length of the password: "))))
