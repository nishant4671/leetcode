class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        logs.sort(key=lambda log: log[1])
        
        indexed_queries = []
        for i, q_time in enumerate(queries):
            indexed_queries.append((q_time, i))
        indexed_queries.sort(key=lambda item: item[0])
        
        ans = [0] * len(queries)
        
        server_activity_counts = collections.Counter()
        
        log_ptr_left = 0
        log_ptr_right = 0
        
        for q_time, original_index in indexed_queries:
            window_start = q_time - x
            window_end = q_time
            
            while log_ptr_right < len(logs) and logs[log_ptr_right][1] <= window_end:
                server_id = logs[log_ptr_right][0]
                server_activity_counts[server_id] += 1
                log_ptr_right += 1
            
            while log_ptr_left < len(logs) and logs[log_ptr_left][1] < window_start:
                server_id = logs[log_ptr_left][0]
                server_activity_counts[server_id] -= 1
                if server_activity_counts[server_id] == 0:
                    del server_activity_counts[server_id]
                log_ptr_left += 1
            
            active_servers_count = len(server_activity_counts)
            
            ans[original_index] = n - active_servers_count
            
        return ans