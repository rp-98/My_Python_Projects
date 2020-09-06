#Random paswsword generator of length 8 with having from digits,characters and special character
import random
element=char=[chr(i)  for i in range(33,127)]
element=''.join(element)
#give all the keyword character (digit,character,special character)
#  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
password=random.sample(element,8) #random sampling
password=''.join(password)
print('Your Random Generated Password is:')
print(password)
