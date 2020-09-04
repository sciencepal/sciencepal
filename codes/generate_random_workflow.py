import os
import random

cron_line = '"0 */{prevNo} * * *"'

with open(".github/workflows/rating-chart.yml", "r") as f:
  wf = f.read()
  
randNo = random.randint(1, 8)
newCron = cron_line.format(prevNo=randNo)

for prevNum in range (1, 9):
  prevCron = cron_line.format(prevNo=prevNum)
  if wf.find(prevCron) != -1:
    wf = wf.replace(prevCron, newCron)
    break
print (wf)
