s = "aB3c!a2#"
sp = sum(1 for c in s if not c.isalpha() and not c.isdigit())
print(sp)

from collections import Counter 
freq = {k:v for k,v in Counter(s.lower()).items() if s.lower().count(k)>1 and k.isalpha()}
print(freq)

digit_sum = sum(int(c) for c in s if c.isdigit())
print(digit_sum)