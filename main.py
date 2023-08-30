import time
import concurrent.futures
import random

start=time.perf_counter()


def do_something(seconds):

    print(f'sleepiing {seconds} second.......')
    time.sleep(1)
    print('done sleepng....')

for v in  range(10):
  secs=[ 5,4,3,2,1]
  #x = random.randint(0,100)
  with concurrent.futures.ThreadPoolExecutor() as executor:
    #results= [executor.submit(do_something, x) for _ in range(10) ]
    results = executor.map(do_something , secs)
    for result in results:
    #for f in concurrent.futures.as_completed(results):
       print(results)
       #print(f.result())




#t1=threading.Thread(target=do_something)
#t2 =threading.Thread(Target = dosomething)

#for n in range(9)
#for b in range(10)
# t1=threading.Thread(target=do_something , args=[n])
#t1.start()
#threads.append(t1)

#for thread in threads:
  # threads.join()

#



finish=time.perf_counter()


print(f' finished in {round ( finish-start, 2)} second(s)')
