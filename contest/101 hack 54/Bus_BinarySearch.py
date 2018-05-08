#!/bin/python3

import os
import sys
from math import ceil

def binary_search(L,x):
    l = -1
    r = len(L)
    if x>L[-1] or x<0:
        print('Error: x out of range')
    if x == 0:
        return 0,0
    while r - l > 1:
        m = l + r >> 1
        if L[m] < x:
            l = m
        else:
            r = m
    return L[l],L[r]

def bus_pick_t(w,v,x,time_arrival):
    return max( 0 , ceil((time_arrival-x/v)/w)*w )
                
def minimumTimeToEnd(stations, w, v, q):
    arrival = stations[-1]
    
    for _ in range(q):
        x, t, u = map(int, input().rstrip().split())
        left, right = binary_search(stations,x)
        
        # prev stop
        prev_stop_x = left
        time_arrival_at_stop = t + (x - prev_stop_x)/u
        bus_pick_time = bus_pick_t(w,v,prev_stop_x,time_arrival_at_stop)
        arrival_time_1 = bus_pick_time + arrival/v
        
        # next stop
        next_stop_x = right
        time_arrival_at_stop = t + (next_stop_x - x)/u
        bus_pick_time = bus_pick_t(w,v,next_stop_x,time_arrival_at_stop)
        arrival_time_2 = bus_pick_time + arrival/v
        
        # by walk
        arrival_by_walking = t + abs(x - arrival)/u
        
        
        print(min(arrival_time_1,arrival_time_2,arrival_by_walking))
        
if __name__ == '__main__':
    n = int(input())
    stations = list(map(int, input().rstrip().split()))
    w, v = map(int, input().rstrip().split())
    q = int(input())
    minimumTimeToEnd(stations, w, v, q)