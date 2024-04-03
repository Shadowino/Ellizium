import time

timer1 = 0
timer2 = 0

while 1:
    print(time.time() - timer1)
    if (time.time() - timer1) > 1:
        timer1 = time.time()
|       print("timer1")
        pass
    if (time.time() - timer2) > 2.0:
        timer2 = time.time()
        print("timer2")
        pass
    
    
    
    pass


