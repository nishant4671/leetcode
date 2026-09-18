class Fancy:
    MOD = 10**9 + 7
    def __init__(self):
        self.base = []
        self.mul = 1
        self.add = 0
    def append(self, val: int) -> None:
        inv = pow(self.mul, self.MOD - 2, self.MOD)
        stored = (val - self.add) % self.MOD
        stored = stored * inv % self.MOD
        self.base.append(stored)
    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD
    def multAll(self, m: int) -> None:
        self.mul = self.mul * m % self.MOD
        self.add = self.add * m % self.MOD
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.base):
            return -1
        return (self.base[idx] * self.mul + self.add) % self.MOD