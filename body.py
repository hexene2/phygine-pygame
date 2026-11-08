class RigidBody:
    def __init__(self, x, y, sizeX, sizeY, mass, velocityX, velocityY, forceX,forceY):
        self.x = x
        self.y = y
        

        self.sizeX = sizeX
        self.sizeY = sizeY
        

        self.mass = mass
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.accelerationX = 0
        self.accelerationY = 0
        
        self.forceX= forceX
        self.forceY= forceY

    def update(self,dt):
        self.accelerationX = self.forceX/self.mass
        self.accelerationY = self.forceY/self.mass

        self.velocityX += dt*self.accelerationX
        self.velocityY += dt*self.accelerationY

        self.x += dt*self.velocityX
        self.y += dt*self.velocityY