class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        ans = [0] * m

        # available_servers: min-heap of (weight, index)
        # Servers are initially available.
        available_servers = []
        for i in range(n):
            heapq.heappush(available_servers, (servers[i], i))

        # busy_servers: min-heap of (finish_time, weight, index)
        # Servers are added here when assigned a task.
        busy_servers = []

        # task_queue: collections.deque of (task_original_index, task_duration)
        # Tasks are added here when they arrive but cannot be assigned immediately.
        task_queue = collections.deque()

        current_time = 0  # Current simulation time
        next_task_arrival_idx = 0 # Index of the next task to arrive

        # Loop until all tasks have been assigned
        # Continue as long as there are tasks to process (either newly arriving or in the queue)
        while next_task_arrival_idx < m or task_queue:
            # 1. Determine the actual `current_time` for this iteration's assignments.
            # If no servers are available, we must wait for one to become free.
            # The earliest a server becomes free is `busy_servers[0][0]`.
            if not available_servers:
                # If available_servers is empty, busy_servers must be non-empty if
                # tasks are pending, due to constraints (n >= 1) and the loop condition.
                current_time = busy_servers[0][0]
            else:
                # If servers are available, we can process tasks at `current_time`.
                # However, `current_time` must be at least `next_task_arrival_idx`
                # because tasks cannot be processed before they arrive.
                current_time = max(current_time, next_task_arrival_idx)
            
            # 2. Free up any servers that have finished their tasks by `current_time`.
            while busy_servers and busy_servers[0][0] <= current_time:
                finish_time, weight, server_idx = heapq.heappop(busy_servers)
                heapq.heappush(available_servers, (weight, server_idx))

            # 3. Add tasks that have arrived by `current_time` to the `task_queue`.
            # Tasks arrive sequentially, `task_j` at second `j`.
            while next_task_arrival_idx < m and next_task_arrival_idx <= current_time:
                task_queue.append((next_task_arrival_idx, tasks[next_task_arrival_idx]))
                next_task_arrival_idx += 1

            # 4. Assign tasks from the `task_queue` to `available_servers`.
            # This loop continues as long as there are tasks waiting and servers available.
            while task_queue and available_servers:
                weight, server_idx = heapq.heappop(available_servers)
                current_task_original_idx, task_duration = task_queue.popleft()
                
                ans[current_task_original_idx] = server_idx
                # The server will be busy until `current_time + task_duration`.
                heapq.heappush(busy_servers, (current_time + task_duration, weight, server_idx))
        
        return ans

import heapq
import collections