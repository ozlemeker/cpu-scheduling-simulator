import sys
import os
from process import Process
from utils import compute_metrics_and_print
from algorithms import simulate_fcfs, simulate_sjf, simulate_priority, simulate_rr

def parse_input(filename: str):
    procs = []
    idx = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith('#'):
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) != 4:
                raise ValueError(
                    f"Invalid line: '{line}'\n"
                    f"Expected format: 'PID, Arrival, Burst, Priority'"
                )
            pid, a, b, pr = parts
            procs.append(Process(pid=pid, arrival=int(a), burst=int(b), priority=int(pr), original_index=idx))
            idx += 1
    return procs

def main():
    if len(sys.argv) < 2:
        print(f"========================================\nCPU SCHEDULING SIMULATOR\nOzlem Eker - 220444078\n========================================")
        print("(processes.txt, quantum=3)\n")
        
        # EXE ile birlikte gelen dosyayı bul
        if getattr(sys, 'frozen', False):
            # PyInstaller ile paketlenmişse
            base_path = sys._MEIPASS
        else:
            # Normal Python çalıştırılıyorsa
            base_path = os.path.dirname(__file__)
        
        infile = os.path.join(base_path, "processes.txt")
        q = 3
    else:
        infile = sys.argv[1]
        q = None
        if len(sys.argv) >= 3:
            try:
                q = int(sys.argv[2])
                if q <= 0:
                    raise ValueError()
            except ValueError:
                print("Quantum must be a positive integer.")
                input("...")
                sys.exit(1)

    try:
        procs = parse_input(infile)
    except FileNotFoundError:
        print(f"HATA: '{infile}' dosyasi bulunamadi!")
        input("...")
        sys.exit(1)
    
    if not procs:
        print("No processes found in input.")
        input("..")
        sys.exit(1)

    gantt, out_fcfs = simulate_fcfs(procs)
    compute_metrics_and_print("FCFS", gantt, out_fcfs)

    gantt, out_sjf = simulate_sjf(procs)
    compute_metrics_and_print("SJF (non-preemptive)", gantt, out_sjf)

    gantt, out_pri = simulate_priority(procs)
    compute_metrics_and_print("Priority (non-preemptive)", gantt, out_pri)

    if q is None:
        print("Round Robin skipped (provide <quantum> as 2nd argument).")
    else:
        gantt, out_rr = simulate_rr(procs, q)
        compute_metrics_and_print(f"Round Robin (quantum={q})", gantt, out_rr)
    
    input("\n...")

if __name__ == "__main__":
    main()