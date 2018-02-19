class Dice:
	def __init__(self, num, width = 50, height = 50, thickness_rect = 3, circle_radius = 4, seq = -1):
		self.num = num
		self.width = width
		self.height = height
		self.thickness_rect = thickness_rect
		self.space = 12
		self.circle_radius = circle_radius
		self.selected = False
		self.seq = seq
		self.x = 0
		self.y = 0

		self.BLACK = (0,0,0)

	def left(self, x, y):
		return x

	def right(self, x, y):
		return (x + self.width)

	def bottom(self, x, y):
		return (y + self.height)

	def top(self, x, y):
		return y

	def center(self, x, y):
		return (x + self.width // 2, y + self.height // 2)

	def draw(self, screen, x, y):
		import pygame
		self.x = x
		self.y = y
		if self.num == 0:
			pygame.draw.rect(screen, self.BLACK, (x, y, self.width, self.height), self.thickness_rect)
			font = pygame.font.SysFont('Comic Sans MS', 20)
			font.set_bold(True)
			if(self.seq == 0):
				textsurface = font.render('W', False, (0, 0, 0))
			elif(self.seq == 1):
				textsurface = font.render('E', False, (0, 0, 0))
			elif(self.seq == 2):
				textsurface = font.render('I', False, (0, 0, 0))
			elif(self.seq == 3):
				textsurface = font.render('S', False, (0, 0, 0))
			else:
				textsurface = font.render('S', False, (0, 0, 0))
			screen.blit(textsurface, (self.x + 15, self.y + 7))

		elif self.num == 1:
			pygame.draw.rect(screen, self.BLACK, (x, y, self.width, self.height), self.thickness_rect)
			pygame.draw.circle(screen, self.BLACK, self.center(x, y), self.circle_radius)
		elif self.num == 2:
			pygame.draw.rect(screen, self.BLACK, (x, y, self.width, self.height), self.thickness_rect)
			pygame.draw.circle(screen, self.BLACK, (self.left(x, y) + self.space, self.bottom(x, y) - self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.right(x, y) - self.space, self.top(x, y) + self.space), self.circle_radius)
		elif self.num == 3:
			pygame.draw.rect(screen, self.BLACK, (x, y, self.width, self.height), self.thickness_rect)
			pygame.draw.circle(screen, self.BLACK, (self.left(x, y) + self.space, self.bottom(x, y) - self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, self.center(x, y), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.right(x, y) - self.space, self.top(x, y) + self.space), self.circle_radius)
		elif self.num == 4:
			pygame.draw.rect(screen, self.BLACK, (x, y, self.width, self.height), self.thickness_rect)
			pygame.draw.circle(screen, self.BLACK, (self.left(x, y) + self.space, self.bottom(x, y) - self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.left(x, y) + self.space, self.top(x, y) + self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.right(x, y) - self.space, self.bottom(x, y) - self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.right(x, y) - self.space, self.top(x, y) + self.space), self.circle_radius)
		elif self.num == 5:
			pygame.draw.rect(screen, self.BLACK, (x, y, self.width, self.height), self.thickness_rect)
			pygame.draw.circle(screen, self.BLACK, (self.left(x, y) + self.space, self.bottom(x, y) - self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.left(x, y) + self.space, self.top(x, y) + self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, self.center(x, y), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.right(x, y) - self.space, self.bottom(x, y) - self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.right(x, y) - self.space, self.top(x, y) + self.space), self.circle_radius)
		elif self.num == 6:
			pygame.draw.rect(screen, self.BLACK, (x, y, self.width, self.height), self.thickness_rect)
			pygame.draw.circle(screen, self.BLACK, (self.left(x, y) + self.space, self.bottom(x, y) - self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.left(x, y) + self.space, self.top(x, y) + self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.right(x, y) - self.space, self.bottom(x, y) - self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.right(x, y) - self.space, self.top(x, y) + self.space), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.center(x, y)[0] - 13, self.center(x, y)[1]), self.circle_radius)
			pygame.draw.circle(screen, self.BLACK, (self.center(x, y)[0] + 13, self.center(x, y)[1]), self.circle_radius)

	def is_pressed(self, x, y):
		#print(str(self.num) + " => self.x: " + str(self.x) + " self.y: " + str(self.y) + " x: " + str(x) + " y: " + str(y))
		if(x >= self.x and x <= (self.x + self.width) and y >= self.y and y <= (self.y + self.height)):
			#self.selected = not self.selected
			return True
		return False