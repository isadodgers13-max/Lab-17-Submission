import math

class RightTriangle:
    def __init__(self, side1, side2, hyp=None):
        try:
            # Try to cast all values to float
            self.side1 = float(side1)
            self.side2 = float(side2)
            self.hyp = float(hyp) if hyp is not None else math.sqrt(math.pow(self.side1, 2) + math.pow(self.side2, 2))
        except ValueError:
            raise ValueError("Error: all sides must be numeric values.")

        # Check for negative values
        if self.side1 < 0 or self.side2 < 0 or self.hyp < 0:
            raise ValueError("Error: both sides and the hypotenuse must be nonnegative.")

        # If hyp was provided, verify Pythagorean theorem
        if hyp is not None:
            if abs(math.pow(self.side1, 2) + math.pow(self.side2, 2) - math.pow(self.hyp, 2)) > 0.0001:
                raise ValueError("Error: sides do not form a valid right triangle.")

    def __str__(self):
        return f"Right Triangle with side a = {self.side1:.1f}, side b = {self.side2:.1f}, and hypotenuse = {self.hyp:.1f}"
