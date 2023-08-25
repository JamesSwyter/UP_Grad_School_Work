import re
import numpy as np
import pandas as pd

words = ['apple', 'bear', 'cat', 'fivez', 'aa', 'aaaaaaa']

option1 = [w for w in words if len(w) == 5]


option2 = [w for w in words if re.match('[a-z]{5}', w)]
option2_works = [w for w in words if re.match('[a-z]{5}$', w)]


option3 = [w for w in words if re.search('^[a-z]{5}$', w)]


option4 = [w for w in words if re.search('[a-z]{5}$', w)]


option5 = [w for w in words if re.search('^[a-z]{5}', w)]

#print(option1)
#print(option2)
#print(option2_works)
#print(option3)
#print(option4)
#print(option5)

Q = np.linspace(1000, 2000, 21)
#print(Q)
