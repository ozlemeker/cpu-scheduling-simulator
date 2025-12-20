from copy import deepcopy
from collections import deque
from typing import List, Tuple
from process import Process

GanttSegment = Tuple[int,int,str]

def simulate_fcfs(processes: List[Process]) -> Tuple[List[GanttSegment], List[Process]]:
    procs = deepcopy(processes)
    procs.sort(key=lambda p: (p.arrival, p.original_index))
    clock = 0
    gantt = []
    for p in procs:
        if clock < p.arrival:
            gantt.append((clock, p.arrival, 'idle'))
            clock = p.arrival
        p.start_time = clock
        clock += p.burst
        p.finish_time = clock
        p.remaining = 0
        gantt.append((p.start_time, p.finish_time, p.pid))
    return gantt, procs

def simulate_sjf(processes: List[Process]) -> Tuple[List[GanttSegment], List[Process]]:
    procs_all = deepcopy(processes)
    procs_all.sort(key=lambda p: (p.arrival, p.original_index))
    ready = []
    clock = 0
    idx = 0
    n = len(procs_all)
    gantt = []
    while True:
        while idx < n and procs_all[idx].arrival <= clock:
            ready.append(procs_all[idx])
            idx += 1
        if not ready:
            if idx < n:
                next_arr = procs_all[idx].arrival
                if clock < next_arr:
                    gantt.append((clock, next_arr, 'idle'))
                clock = next_arr
                continue
            else:
                break
        ready.sort(key=lambda p: (p.burst, p.arrival, p.original_index))
        p = ready.pop(0)
        p.start_time = clock
        clock += p.burst
        p.finish_time = clock
        p.remaining = 0
        gantt.append((p.start_time, p.finish_time, p.pid))
    return gantt, procs_all

def simulate_priority(processes: List[Process]) -> Tuple[List[GanttSegment], List[Process]]:
    procs_all = deepcopy(processes)
    procs_all.sort(key=lambda p: (p.arrival, p.original_index))
    ready = []
    clock = 0
    idx = 0
    n = len(procs_all)
    gantt = []
    while True:
        while idx < n and procs_all[idx].arrival <= clock:
            ready.append(procs_all[idx])
            idx += 1
        if not ready:
            if idx < n:
                next_arr = procs_all[idx].arrival
                if clock < next_arr:
                    gantt.append((clock, next_arr, 'idle'))
                clock = next_arr
                continue
            else:
                break
        ready.sort(key=lambda p: (p.priority, p.arrival, p.original_index))
        p = ready.pop(0)
        p.start_time = clock
        clock += p.burst
        p.finish_time = clock
        p.remaining = 0
        gantt.append((p.start_time, p.finish_time, p.pid))
    return gantt, procs_all

def simulate_rr(processes: List[Process], quantum: int) -> Tuple[List[GanttSegment], List[Process]]:
    procs_all = deepcopy(processes)
    procs_all.sort(key=lambda p: (p.arrival, p.original_index))
    ready = deque()
    clock = 0
    idx = 0
    n = len(procs_all)
    gantt = []
    # if nothing at t=0 jump to first arrival
    if idx < n and procs_all[idx].arrival > 0:
        gantt.append((0, procs_all[idx].arrival, 'idle'))
        clock = procs_all[idx].arrival
    while True:
        while idx < n and procs_all[idx].arrival <= clock:
            ready.append(procs_all[idx])
            idx += 1
        if not ready:
            if idx < n:
                next_arr = procs_all[idx].arrival
                if clock < next_arr:
                    gantt.append((clock, next_arr, 'idle'))
                clock = next_arr
                continue
            else:
                break
        p = ready.popleft()
        if p.start_time is None:
            p.start_time = clock
        run_for = min(quantum, p.remaining)
        start = clock
        clock += run_for
        p.remaining -= run_for
        end = clock
        gantt.append((start, end, p.pid))
        # adding newly arrived during execution
        while idx < n and procs_all[idx].arrival <= clock:
            ready.append(procs_all[idx])
            idx += 1
        if p.remaining > 0:
            ready.append(p)
        else:
            p.finish_time = clock
    return gantt, procs_all
