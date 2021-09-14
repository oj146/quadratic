class Quadr:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def turn(self):
        x_point = (0-self.b)/(2*self.a)
        y_point = (self.a)*pow(x_point,2)+(self.b*x_point)+self.c
        return (x_point,y_point)
        

    def root(self):
        from math import sqrt
        try:
            equ1 = (-self.b+sqrt(self.b**2-(4*self.a*self.c)))/2*self.a
            equ2 = (-self.b-sqrt(self.b**2-(4*self.a*self.c)))/2*self.a
            if equ1 == equ2:
                return (equ1)
            return (equ1,equ2)
        except ValueError:
            return None



