import pygame
from pygame.display import flip
pygame.init()
rockthrow = pygame.mixer.Sound("swoosh.wav")
enemyhit = pygame.mixer.Sound("hit2.wav")
backmusic = pygame.mixer.music.load("JTS.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()
class game(object):
	def __init__(self, x, y, width, height):
		self.x = 40
		self.y = 400
		self.width = 80
		self.height = 50
		self.speed = 5
		self.jump = False
		self.jump_height = 10
		self.walkcount = 0
		self.left = False
		self.right = False
		self.face = True
		self.hitbox = (self.x + 20, self.y,28,60)

	def hit(self):
		self.x = 60
		self.y = 400
		self.walkcount = 0
		self.jump = False
		self.jump_height = 10
		fontp = pygame.font.SysFont('Helvetica', 80)
		textp = fontp.render('-5',1,(255,0,0))
		window.blit(textp,(250-(textp.get_width()/2),200))
		pygame.display.update()
		i = 0
		while i < 300:
			pygame.time.delay(10)
			i = i + 1
			for a in pygame.event.get():
				if a.type == pygame.QUIT:
					a = 301
					pygame.quit()
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
		self.hitbox = (self.x + 10 , self.y + 20, 29, 65)
		#pygame.draw.rect(window,(255,0,0), self.hitbox, 2)
obj = game(40, 400, 80, 50)

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
		self.hitbox = (self.x + 20, self.y,28,60) 
		self.end = end
		self.path = [self.x,self.end]
		self.walkcount = 0
		self.speed = 3
		self.health = 10
		self.visible = True
		for i in range(8):
			self.walkright[i] = pygame.transform.scale(self.walkright[i],(self.width, self.height))
			self.walkleft[i] = pygame.transform.scale(self.walkleft[i],(self.width, self.height))
	def hit(self):
		print(score)
		if self.health > 0:
		    self.health = self.health - 1
		else:
		    self.visible = False	
	def draw(self,window):
		self.move()
		if self.visible == True:
                        if self.walkcount + 1 >= 24:
                                self.walkcount = 0
                        if self.speed > 0:
                                window.blit(self.walkright[self.walkcount//3],(self.x,self.y))
                                self.walkcount += 1
                        else:
                                window.blit(self.walkleft[self.walkcount//3],(self.x,self.y))
                                self.walkcount += 1
                        self.hitbox = (self.x + 25, self.y + 25,30,70)
                        pygame.draw.rect(window,(255,0,0),(self.hitbox[0], self.hitbox[1]-20,50,10))
                        pygame.draw.rect(window,(0,255,0),(self.hitbox[0], self.hitbox[1]-20,50-(5*(10 - self.health)),10))
		                #pygame.draw.rect(window, (255,0,0),self.hitbox, 2)
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
	runright[i] = pygame.transform.scale(runright[i],(obj.height, obj.width))
	runleft[i] = pygame.transform.scale(runleft[i],(obj.height, obj.width))

def animation():
	window.blit(bg,(0,0))
	text = Font.render("score:"+" "+ str(score),1,(255,255,255))
	window.blit(text,(25,0))
	obj.draw(window)
	enemyobject.draw(window)
	
	#for enemy in range ():

	for throw in rocks:
		throw.shootdraw(window)
	pygame.display.update()

run = True
rocks = []
shootdelay = 0
enemyobject = enemy(100,400,100,100,450)
score = 0
Font = pygame.font.SysFont("Helvetica",25,True) 
while run:
	clock.tick(36)
	if enemyobject.visible == True:
		if obj.hitbox[1] < enemyobject.hitbox[1] + enemyobject.hitbox[3] and  obj.hitbox[1] + obj.hitbox[3] > enemyobject.hitbox[1]:
				if obj.hitbox[0] + obj.hitbox[2] > enemyobject.hitbox[0] and obj.hitbox[0] < enemyobject.hitbox[0] + enemyobject.hitbox[2]:
					obj.hit()
					score = score - 5
	else:
		pass
	if shootdelay > 0:
		shootdelay+= 1
	if shootdelay > 20:
		shootdelay = 0
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			run = False
	for throw in rocks:
		if enemyobject.visible == True:
			if throw.y - throw.radius < enemyobject.hitbox[1] + enemyobject.hitbox[3] and throw.y + throw.radius > enemyobject.hitbox[1]:
				if throw.x + throw.radius > enemyobject.hitbox[0] and throw.x - throw.radius < enemyobject.hitbox[0] + enemyobject.hitbox[2]:
					enemyhit.play()
					enemyobject.hit()
					score = score + 1
					rocks.pop(rocks.index(throw))
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

	
	if keys[pygame.K_w] and shootdelay == 0:
		if obj.face == False:
			facing = -1
		elif obj.face == True:
			facing = 1
		if len(rocks) < 5:
			rocks.append(projectile(round(obj.x + obj.width//2),round(obj.y + obj.height//2 ), 6,(255, 0, 0), facing))
		shootdelay = 1
		rockthrow.play()
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

