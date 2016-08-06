import multiprocessing,time


def cube(x):
    
    proc_name = multiprocessing.current_process().name
    time.sleep(10)
    print " Computation result : " + str(x**3) + " done by :" + proc_name + "\n"
    return x**2


if __name__=="__main__":
    
    pool=multiprocessing.Pool(processes=4)
#     res = pool.map(cube, range(7))
#     print res
    res = pool.map_async(cube, range(7))
    print res.get()