from typing import List, Tuple
from process import Process

GanttSegment = Tuple[int,int,str]  # (start, end, pid_or_idle)

def compute_metrics_and_print(algorithm_name: str, gantt: List[GanttSegment], procs: List[Process]):
    busy = sum((end-start) for (start,end,pid) in gantt if pid != 'idle')
    total_time = max((end for (start,end,_) in gantt), default=0)
    cpu_util = (busy / total_time * 100) if total_time > 0 else 0.0

    print(f"\n--- Scheduling Algorithm: {algorithm_name} ---")
    
    #  Numeric timeline
    print("\nGantt Chart (numeric timeline):")
    gantt_str = ""
    last_end = 0
    for s, e, p in gantt:
        
        if s == 0:
            gantt_str += f"[{s}]--{p}--[{e}]"
        
        elif s > last_end: 
            gantt_str += f"--idle--[{s}]--{p}--[{e}]"
        else: 
            gantt_str += f"--{p}--[{e}]"
        last_end = e
    

    print(gantt_str)


    print("\nGantt Chart (ASCII Bar):")
    bar = ""
    label_line = ""
    for s,e,p in gantt:
        length = max(1, e-s)
        segment_char = '░' if p == 'idle' else '█'
        bar += segment_char * length
        label_pos = len(bar) - length//2 - len(p)//2
        if len(label_line) < label_pos:
            label_line += ' '*(label_pos - len(label_line))
        label_line += p
    print(bar)
    print(label_line)

    print("\nTimeline:")
    timeline_str = ""
    for s, e, p in gantt:
        timeline_str += f"{s:<8}"
    timeline_str += f"{gantt[-1][1]}"  # Son zaman
    print(timeline_str)

    print("\nProcess   | Finish Time | Turnaround Time | Waiting Time")
    print("-----------------------------------------------------")
    total_tat = 0
    total_wt = 0
    n = len(procs)
    for p in sorted(procs, key=lambda x: x.original_index):
        if p.finish_time is None:
            ft = "-"
            tat = "-"
            wt = "-"
        else:
            ft = p.finish_time
            tat = p.finish_time - p.arrival
            wt = tat - p.burst
            total_tat += tat
            total_wt += wt
        print(f"{p.pid:<9}| {str(ft):<11}| {str(tat):<15}| {str(wt):<12}")
    avg_tat = total_tat / n
    avg_wt = total_wt / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")
    print(f"CPU Utilization: {cpu_util:.1f}%\n")
