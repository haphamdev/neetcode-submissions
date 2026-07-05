class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        currentMin = min(self.data[-1][1],val) if self.data else val
        self.data.append((val, currentMin))

    def pop(self) -> None:
        val, _ = self.data.pop()
        return val

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
