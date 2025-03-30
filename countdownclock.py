import time
while True:
    x=input("How long shoud the timer go, in seconds: ")
    if not(x.isdigit() and int(x)>0):
        print("Invalid Input")
    else:
        break
x=int(x)            
while x > 0:
    minutes, seconds=divmod(x, 60)
    timer="{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    x-=1
print("Timer ends")    