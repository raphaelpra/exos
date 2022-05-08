class Plus:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"Plus [{self.left} + {self.right}]"
    def eval(self):
        return self.right.eval() + self.left.eval()

class Mult:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return f"Mult [{self.left} * {self.right}]"
    def eval(self):
        return self.right.eval() * self.left.eval()

class Power:
    def __init__(self, what, power):
        self.what = what
        self.power = power
    def __str__(self):
        return f"Power [{self.what} ** {self.power}]"
    def eval(self):
        return self.what.eval() ** self.power.eval()

class Number:
    def __init__(self, atom):
        self.atom = atom
    def __str__(self):
        return f"[N {self.atom}]"
    def eval(self):
        return self.atom

if __name__ == '__main__':
    exps = [
        Mult(Number(27), Plus(Number(43), Number(12))),
        Power(Mult(Number(1), Number(3)),
              Plus(Number(1), Number(2)))
        ]
    for exp in exps:
        print(f"exp = {exp} -> eval = {exp.eval()}")
