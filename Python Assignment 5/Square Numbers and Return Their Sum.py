class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self,sum=None):
         self.x=self.x**2
         self.y=self.y**2
         self.z=self.z**2
         sum=self.x+self.y+self.z
         return sum
a=Point(1,3,5)
print(a.sqSum())