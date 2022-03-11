import re

x = "$00.12"

out = re.search('^([$]|-[$])?[0]|[1-9]', x)

print(out)
