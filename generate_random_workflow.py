import os
import random

with open("workflow.txt", "r) as f:
  wf = f.read()
print (wf.format(random_number=random.randint(1,8)))
