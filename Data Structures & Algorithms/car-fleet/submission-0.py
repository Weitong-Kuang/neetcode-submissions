class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed),reverse=True)
        fleets = 0
        lead_time = 0.0
        
        for pos,spd in cars:
            time = (target - pos) / spd
            if time > lead_time:
                fleets += 1
                lead_time = time
        return fleets