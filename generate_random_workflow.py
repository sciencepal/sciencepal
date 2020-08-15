import os
import random

with open("workflow.txt", "r") as f:
  wf = f.read()
print (wf.replace("{random_number}", str(random.randint(1, 8))))
