import pygame
from pygame.display import flip

pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()
class game(object):
	def __init__(self, x, y, width, height):
		self.x = 40
		self.y = 400
		self.width = 100
		self.height = 100
		self.speed = 5
		self.jump = False
		self.jump_height = 10
		self.walkcount = 0
		self.left = False
		self.right = False
		self.face = True
	def draw(self,window):
		if self.walkcount + 1 >= 36:
			self.walkcount = 0
		if obj.left == True:
			window.blit(runleft[self.walkcount//3] , (self.x,self.y))
			self.walkcount = self.walkcount + 1
		elif obj.right == True:
			window.blit(runright[self.walkcount//3], (self.x,self.y))
			self.walkcount =self.walkcount + 1
		else:
			if self.face == True:
				window.blit(idleright, (self.x,self.y))
			elif self.face == False:
				window.blit(idleleft, (self.x,self.y))
obj = game(40, 400, 100, 100)

class projectile(object):
	def __init__(self,x,y,radius,color,facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.speed = 8*facing
	def shootdraw(self,window):
		pygame.draw.circle(window,self.color, (self.x,self.y), self.radius)


class enemy(object):
	walkleft = [pygame.image.load("Walk (1) flip.png"),pygame.image.load("Walk (2) flip.png"),pygame.image.load("Attack (3) flip.png"),pygame.image.load("Walk (4) flip.png"), pygame.image.load("Walk (5) flip.png"), pygame.image.load("Walk (6) flip.png"),pygame.image.load("walk (7) flip.png"), pygame.image.load("walk (8) flip.png")]
	walkright = [pygame.image.load("Walk (1).png"),pygame.image.load("Walk (2).png"),pygame.image.load("Walk (3).png"),pygame.image.load("Walk (4).png"), pygame.image.load("Walk (5).png"), pygame.image.load("Walk (6).png"),pygame.image.load("Walk (7).png"), pygame.image.load("Walk (8).png")]
	def __init__(self,x,y,width,height,end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x,self.end]
		self.walkcount = 0
		self.speed = 3
		for i in range(8):
			self.walkright[i] = pygame.transform.scale(self.walkright[i],(self.width, self.height))
			self.walkleft[i] = pygame.transform.scale(self.walkleft[i],(self.width, self.height))
	def draw(self,window):
		self.move()
		if self.walkcount + 1 >= 24:
			self.walkcount = 0
		if self.speed > 0:
			window.blit(self.walkright[self.walkcount//3],(self.x,self.y))
			self.walkcount += 1
		else:
			window.blit(self.walkleft[self.walkcount//3],(self.x,self.y))
			self.walkcount += 1
	def move(self):
                if self.speed > 0:
                	if self.x + self.speed < self.path[1]:
                		self.x += self.speed
                	else:
                		self.speed = self.speed*-1
                		self.walkcount = 0
                else:
                	if self.x-self.speed > self.path[0]:
                		self.x += self.speed
                	else:
                		self.speed = self.speed*-1
                		self.walkcount = 0



bg = pygame.image.load("backgound.png")
bg = pygame.transform.scale(bg, (500,500))
runright = [pygame.image.load("Run (1).png"),pygame.image.load("Run (2).png"),pygame.image.load("Run (3).png"),pygame.image.load("Run (4).png"),
pygame.image.load("Run (5).png"), pygame.image.load("Run (6).png"), pygame.image.load("Run (7).png"), pygame.image.load("Run (8).png"), pygame.image.load("Run (9).png"),
pygame.image.load("Run (10).png"), pygame.image.load("Run (11).png"), pygame.image.load("Run (12).png")]

runleft = [pygame.image.load("Run (1)flip.png"),pygame.image.load("Run (2)flip.png"),pygame.image.load("Run (3)flip.png"),pygame.image.load("Run (4)flip.png"),
pygame.image.load("Run (5)flip.png"), pygame.image.load("Run (6)flip.png"), pygame.image.load("Run (7)flip.png"), pygame.image.load("Run (8)flip.png"), pygame.image.load("Run (9)flip.png"),
pygame.image.load("Run (10)flip.png"), pygame.image.load("Run (11)flip.png"), pygame.image.load("Run (12)flip.png")]

idleright = pygame.image.load("idle right.png")
idleright = pygame.transform.scale(idleright, (obj.height, obj.width))
idleleft = pygame.image.load("idle left.png")
idleleft = pygame.transform.scale(idleleft, (obj.height, obj.width))
for i in range(12):
	runright[i] = pygame.transform.scale(runright[i],(obj.width, obj.height))
	runleft[i] = pygame.transform.scale(runleft[i],(obj.width, obj.height))

def animation():
	window.blit(bg,(0,0))
	obj.draw(window)
	enemyobject.draw(window)
	for throw in rocks:
		throw.shootdraw(window)
	pygame.display.update()

run = True
rocks = []
enemyobject = enemy(40,400,100,100,450)
while run:
	clock.tick(36)
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			run = False
	for throw in rocks:
		if throw.x < 500 and throw.x > 0:
			throw.x += throw.speed
		else:
			rocks.pop(rocks.index(throw))
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT] and obj.x<=450:
		obj.x = obj.x + obj.speed
		obj.left = False
		obj.right = True
		obj.face = True
	elif keys[pygame.K_LEFT] and obj.x>= 5:
		obj.x = obj.x - obj.speed
		obj.left = True
		obj.right = False
		obj.face = False
	else:
		obj.right = False
		obj.left = False
		obj.walkcount = 0

	
	if keys[pygame.K_w]:
		if obj.face == False:
			facing = -1
		elif obj.face == True:
			facing = 1
		if len(rocks) < 5:
			rocks.append(projectile(round(obj.x + obj.width//2),round(obj.y + obj.height//2 ), 6,(255, 0, 0), facing))
	if obj.jump == False:
		if keys[pygame.K_SPACE]:
			obj.jump = True		
	else:
		if obj.jump_height>= -10:
			cond = 1
			if obj.jump_height<0:
				cond = -1
			obj.y = obj.y - (obj.jump_height**2)*0.5*cond
			obj.jump_height = obj.jump_height - 1
		else:
			obj.jump = False
			obj.jump_height = 10
	animation()
pygame.quit()
