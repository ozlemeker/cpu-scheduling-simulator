# CPU Scheduling Simulator

This project is a **CPU scheduling simulator** developed as part of the **CS 305: Operating Systems** course.  
The simulator models and compares four fundamental CPU scheduling algorithms:

- **First-Come First-Served (FCFS)**
- **Shortest Job First (SJF)** (non-preemptive)
- **Priority Scheduling** (non-preemptive)
- **Round Robin (RR)** (preemptive, configurable time quantum)

The simulator reads process definitions from an input file, executes scheduling simulations using a discrete-time
clock model, and produces detailed performance metrics for analysis.

---

## Features

- Modular Python architecture
- File-based process input (arrival time, burst time, priority)
- Gantt chart generation
- Calculation of:
  - Turnaround time
  - Waiting time
  - Average metrics
  - CPU utilization
- Tie-breaking using FCFS order
- Starvation demonstration and analysis
- Configurable Round Robin time quantum

---

## Project Structure

```
scheduler.py   # Main entry point and orchestration
process.py     # Process data structure (dataclass)
algorithms.py  # Scheduling algorithm implementations
utils.py       # Metric calculations and formatted output
```
## Educational Purpose

This project is designed to provide practical insight into CPU scheduling policies and their trade-offs in terms of:
 - Performance vs fairness
 - Starvation risk
 - Responsiveness
 - Suitability for different workload types (CPU-bound vs I/O-bound)
It serves as a foundation for understanding real-world schedulers used in modern operating systems.

## Technologies

 - Language: Python
 - Paradigm: Discrete-event simulation
 - Interface: Command-line (CLI)

## Author

Özlem Eker
CS 305 – Operating Systems
December 2025
