import re


def valid_password(password):
	reg = r"^[A-Za-z0-9@-]{6,18}"
	return re.findall(reg, password)

	
print(valid_password("my-p@ssw0rd"))


	