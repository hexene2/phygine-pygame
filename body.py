g = 9.8
from pygame import draw

class pointMass:
    def __init__(self ,x,y,mass,velocityX, velocityY, forceX,forceY):
        self.x = x
        self.y = y
        self.mass = mass
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.accelerationX = 0
        self.accelerationY = 0
        self.forceX= forceX
        self.forceY= forceY

    def update(self,dt):
        self.accelerationX = self.forceX/self.mass 
        self.accelerationY = self.forceY/self.mass + g

        self.velocityX += dt*self.accelerationX
        self.velocityY += dt*self.accelerationY

        self.x += dt*self.velocityX
        self.y += dt*self.velocityY


class RigidBody:

    def __init__(self, arr, velocityX, velocityY, forceX,forceY):
        self.pointMasses = []
        for i in arr:
            tempPointMass = pointMass(i[0],i[1],i[2],velocityX,velocityY,forceX,forceY)
            self.pointMasses.append(tempPointMass)
        self.pointMassPos = []
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.accelerationX = 0
        self.accelerationY = 0
        
        self.forceX= forceX
        self.forceY= forceY

    def update(self,dt):
        for i in self.pointMasses:
            i.update(dt)
            print(i.x,i.y)


    def draw(self,screen , relativeX ,relativeY):

        for i in self.pointMasses:
            self.pointMassPos.append((i.x+relativeX,i.y+relativeY))
        draw.polygon(screen, (255,255,255), self.pointMassPos)
        self.pointMassPos = []
    
