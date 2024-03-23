class vec2:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<vec2 ({self.x}, {self.y})>"

    def len(self):
        return pow(pow(self.x, 2) + pow(self.y, 2), 0.5)

    def norm(self):
        ln = self.len()
        return vec2(self.x / ln, self.y / ln)

    def __mul__(self, other: int):
        x = self.x * other
        y = self.y * other
        return vec2(x, y)

