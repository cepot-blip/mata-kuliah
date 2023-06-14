

#   MENENTUKAN BILANGAN PRIMA DENGAN FUNGSI 1 - 200

def prima(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, 201):
    if prima(i):
        print(i, end=" ")



