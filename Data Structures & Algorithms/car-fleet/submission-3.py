class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        fleets = n
        car_to_speed = {}

        for idx in range(n): # O(n)
            car_to_speed[position[idx]] = speed[idx]

        position.sort() # O(nlogn)

        backlog_car = position[n - 1]
        
        for idx in range(n-2, -1, -1):
            if car_to_speed[position[idx]] <= car_to_speed[backlog_car]:
                backlog_car = position[idx] 
                continue 

            distance = position[idx] + (backlog_car - position[idx]) * car_to_speed[position[idx]]/(car_to_speed[position[idx]]-car_to_speed[backlog_car]) 
            
            if distance <= target:
                fleets -= 1
            else:
                backlog_car = position[idx]
            

        return fleets
        