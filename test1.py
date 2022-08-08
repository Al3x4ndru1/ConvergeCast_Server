from drawnow import *
import matplotlib.pyplot as plt
import numpy as np
import time 

arr_full = None
arr = []


fig, ax = plt.subplots(nrows=2, ncols=2)

def test_draw_1():
    plt.subplots(221)
    plt.plot(arr,'ro-', label='test1')
    plt.subplots(222)
    plt.plot(arr,'go-', label='test2')
    plt.subplots(223)
    plt.plot(arr,'bo-', label='test3')


def window():
    global arr_full
    global arr

    win_size = 10

    arr.append(arr_full.pop(0))
    if len(arr) > win_size:
        arr.pop(0)

def loop_1():
    while True:
        window()
        drawnow(test_draw_1)
        time.sleep(0.1)


# def loop():
#     while True:
#         loop_1()
#         loop_2()
#         loop_3()

def main():
    global arr_full 
    arr_full = np.random.randint(1,10,100).tolist()
    loop_1()

main()
