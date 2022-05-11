from hi_numba import TicToc,FindE
import os
from threading import Thread

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 10000000
    
    find_es = []
    threads = []
    
    for i in range(os.cpu_count()):
        find_es.append(FindE())
        threads.append(Thread(target = find_es[i].generating_numbers, args=(n,)))
        print("started the thread number #%d"%i)
              
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
     
    i2=0
    n2=0
    
    for find_e in find_es:
        i2 += find_e.i
        n2 += find_e.n
        
    print("E = %12.8f "%(n2/i2))
    print("TIME = %.6f seconds"%(tt.toc()))
    
##  HÜSNA İBİŞ 180315033

