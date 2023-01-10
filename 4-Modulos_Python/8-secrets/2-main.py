import secrets
import string as s
from secrets import SystemRandom as Sr

# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"


print(s.ascii_letters)
print(s.digits)
print(s.punctuation)
print()
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

random = secrets.SystemRandom()
