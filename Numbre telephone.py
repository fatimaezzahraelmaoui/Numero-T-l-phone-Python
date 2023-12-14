import re

def numero_telephone(numero):
    return bool((re.match(r'^\d{2}-\d{3}-\d{4}$',numero)))

num = numero_telephone(611487594)
print(num)