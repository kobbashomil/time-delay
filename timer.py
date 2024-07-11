import time
my_time=int(input('enter time'))
while True:
 #my_time= 24*60*60+1

 for x in reversed(range (0,my_time)):
  seconds= x% 60
  minutes=int(x/60)%60
  hours=int(x/3600)
  time.sleep(1)
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  if (seconds ==10 ):
       print("work machine")
