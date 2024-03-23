class vec2:
    # def __init__(self):
    #     self.x = 0
    #     self.y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # self.__init__()

    def __str__(self):
        return f"<vec2 ({self.x}, {self.y})>"

    def len(self):
        return pow(pow(self.x, 2) + pow(self.y, 2), 0.5)

    def norm(self):
        ln = self.len()
        if ln == 0: return self
        return vec2(self.x / ln, self.y / ln)

    def __mul__(self, other: int):
        x = self.x * other
        y = self.y * other
        return vec2(x, y)

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)
