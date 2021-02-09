import pygame

pygame.init()
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Platformer")

x = 50
y = 50
width = 40
height = 60
run = True
while run:
	pygame.time.delay(50)
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			run = False
	pygame.draw.rect(window, (255, 255, 0), (x,y,width,height))
	pygame.display.update()
pygame.quit()
