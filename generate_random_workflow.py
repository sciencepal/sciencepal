import os
import random

class SafeDict(dict):
  def __missing__(self, key):
    if key.strip() != key:
      return '{{' + key + '}}'
    return '{' + key + '}'

with open("workflow.txt", "r") as f:
  wf = f.read()
print (wf.format_map(SafeDict(random_number=random.randint(1,8))))
