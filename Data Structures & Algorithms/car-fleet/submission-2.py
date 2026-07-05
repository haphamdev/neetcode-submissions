import math 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        turns = {}
        length = len(position)
        posToSpeed = {}
        for i in range(length):
            posToSpeed[position[i]] = speed[i]
        
        position = sorted(position)


        maxTurn = 0
        turns = []
        for i in range(length):
            turn = (target - position[i]) / posToSpeed[position[i]]
            turns.append(turn)
        maxTurn = 0
        result = set()

        for i in range(length -1, -1, -1):
            if turns[i] < maxTurn:
                turns[i] = maxTurn
                result.add(maxTurn)
            else:
                result.add(turns[i])
                maxTurn = turns[i]

        return len(result)
        