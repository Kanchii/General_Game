class Button:
	def __init__(self, x, y, width, height, text, num_dices = 5):
		import pygame

		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.num_dices = num_dices
		self.font = pygame.font.SysFont('Comic Sans MS', 20)

	def draw(self, screen, num_reroll, not_selected_dices, selected_dices):
		import pygame
		all_selected = (not_selected_dices.count(None) == self.num_dices and len(selected_dices) == self.num_dices)
		textsurface = self.font.render(('Roll (' + str(num_reroll) + ')') if not all_selected and num_reroll > 0 else 'Finish', False, (0, 0, 0))

		pygame.draw.rect(screen, (125, 125, 125), (self.x, self.y, self.width, self.height))
		pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)

		screen.blit(textsurface, (self.x + self.width // 2 - 25, self.y + 5))

	def is_pressed(self, x, y):
		if(x >= self.x and x <= (self.x + self.width) and y >= self.y and y <= (self.y + self.height)):
			return True
		return False