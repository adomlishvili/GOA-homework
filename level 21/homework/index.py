import queue


pq = queue.PriorityQueue()
pq.put((2, 'low priority task'))
pq.put((1, 'high priority task'))
pq.put((3, 'lowest priority task'))


while not pq.empty():
    priority, task = pq.get()
    print(f'Executing {task} with priority {priority}')
