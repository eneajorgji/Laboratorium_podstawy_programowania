from math import inf


def most_tasks(tasks):
    t = -inf
    tasks_taken = []
    for i, task in enumerate(tasks):
        start, end = task
        if start >= t:
            tasks_taken.append(i)
            t = end
    return tasks_taken


task_list = [(0, 2), (3, 4), (4, 6), (1, 5), (2, 5), (1, 2), (6, 8), (7, 9), (6, 10), (8, 11)]

print(most_tasks(task_list))
