

def optimize_tasks_procedural(tasks):
    tasks.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    total_wait_time = 0
    current_time = 0
    for task in tasks:
        current_time += task[0]
        total_wait_time += current_time
    return tasks, total_wait_time

def optimize_tasks_functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: (x[1], -x[0]), reverse=True)
    wait_times = list(map(lambda t: t[0], sorted_tasks))
    total_wait_time = reduce(lambda acc, t: acc + t[0], zip(wait_times, range(len(wait_times))), 0)
    return sorted_tasks, total_wait_time

zadania = [
    (3, 10),
    (1, 35),
    (5,10)
]
print(optimize_tasks_procedural(zadania))
print(optimize_tasks_functional(zadania))
