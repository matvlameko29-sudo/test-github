password = input('Введите пороль')

errors = []
allowed_special = ['*', '-', '#']

if len(password) != 8:
    errors.append("Длина пароля не равна 8")

has_upper = False
has_lower = False
has_digit = False
has_special = False
has_invalid = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in allowed_special:
        has_special = True
    else:
        has_invalid = True

if not has_upper:
    errors.append("В пароле отсутствуют заглавные буквы")
if not has_lower:
    errors.append("В пароле отсутствуют строчные буквы")
if not has_digit:
    errors.append("В пароле отсутствуют цифры")
if not has_special:
    errors.append("В пароле отсутствуют специальные символы")
if has_invalid:
    errors.append("В пароле используются непредусмотренные символы")

if len(errors) == 0:
    print("Надежный пароль")
else:
    for error in errors:
        print(error)