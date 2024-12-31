from functools import reduce
def schedule_tasks_procedural(tasks):
    tasks.sort(key=lambda x: x[1])
    selected_tasks = []
    current_end_time = 0
    total_reward = 0

    for task in tasks:
        if task[0] >= current_end_time:
            selected_tasks.append(task)
            current_end_time = task[1]
            total_reward += task[2]

    return total_reward, selected_tasks

def schedule_tasks_functional(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    def select_task(selected, task):
        if not selected or task[0] >= selected[-1][1]:
            return selected + [task]
        return selected
    selected_tasks = reduce(select_task, sorted_tasks, [])
    total_reward = sum(map(lambda x: x[2], selected_tasks))
    return total_reward, selected_tasks

tasks = [
    (1, 3, 50),
    (2, 5, 20),
    (3, 9, 100),
    (6, 8, 70),
    (5, 7, 60)
]

print("Proceduralne podejście:")
reward_proc, schedule_proc = schedule_tasks_procedural(tasks)
print("Maksymalna nagroda:", reward_proc)
print("Harmonogram:", schedule_proc)

print("\nFunkcyjne podejście:")
reward_func, schedule_func = schedule_tasks_functional(tasks)
print("Maksymalna nagroda:", reward_func)
print("Harmonogram:", schedule_func)
