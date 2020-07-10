class Coordinate(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        xDiffSquared = (self.x - other.x)**2
        yDiffSquared = (self.y - other.y)**2
        
        return (xDiffSquared + yDiffSquared)**0.5
    
    def __str__(self):
         return "This is my __str__ method speaking. How can I help you?"
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
c = Coordinate(3,4)
o = Coordinate(0,0)

print(c.distance(o)) # c.distance inherits distance method, & automatically provides c as the first argument to this method

print('Another style of writing the same thing:')
print(Coordinate.distance(c, o))

print(Coordinate(1,2))

print(isinstance(c, Coordinate))

d = Coordinate(1,1)

diff = c-d
print(diff.x, diff.y)