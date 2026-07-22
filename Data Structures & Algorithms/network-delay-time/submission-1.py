class Solution:
    from collections import heapq
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """EDGES -> adjacency list  O(M) 
           Run Dijkstras(O(N + M))
           Find max in dsitance (O(N))"""
        adj_hash = {}
        for edge in times: 
            if not adj_hash.get(edge[1]):
                adj_hash[edge[1]] = []
            if adj_hash.get(edge[0]):
                adj_hash[edge[0]].append((edge[1], edge[2]))
            else:
                adj_hash[edge[0]] = [(edge[1], edge[2])]

        
        # Run Dijkstras From here 
        visited = set()
        min_heap = [(0, k)]
        distance = [float("inf") for i in range(n + 1)]
        distance[0] = -1 # Arbitrary
        distance[k] = 0
        while min_heap:
            _,curr = heapq.heappop(min_heap)
            if curr in visited:
                continue 
            visited.add(curr)
            # check children and update distance
            for edge in adj_hash[curr]:
                distance[edge[0]] = min(distance[edge[0]], distance[curr] + edge[1])
                # add child 
                heapq.heappush(min_heap, (distance[edge[0]], edge[0]))

        print(distance)               
     
        if max(distance) == float("inf"):
            return -1
        else:
            return max(distance)


                      
                    
                    



