# -*- coding: utf-8 -*-

'''
	
	Arrumar a parte da pontuação
		- Clicar para escolher qual dos campos quer pontuar
		- Ajustar isso colocando os resultados em um vetor e então iterando sobre ele
		- Ajusta a fixação da pontuação para cada jogador e então finalizar a primeira parte

'''

import pygame
from Headers.Dice import Dice
from Headers.Button import Button
from random import randint
from copy import deepcopy
import time

pygame.init()

#Cores
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#Tamanho da tela
(width, height) = (500, 600)

#Variaveis
num_dices = 5
num_players = 2
jogador_da_vez = 1
reroll = 3

pontuacao = [[-1]*13 for _ in range(num_players)]

players = ["Felipe", "Ivan"]

def jogada_de_x(array, x):
	return (array.count(x) * x)

def trinca(array):
	for i in range(6):
		if(array.count(i + 1) >= 3):
			return 20
	return 0
def quadra(array):
	for i in range(6):
		if(array.count(i + 1) >= 4):
			return 30
	return 0
def full_house(array):
	for i in range(5):
		for j in range(i + 1, 6):
			if((array.count(i + 1) == 3 and array.count(j + 1) == 2) or (array.count(i + 1) == 2 and array.count(j + 1) == 3)):
				return 25
	return 0
def sequencia_baixa(array):
	for i in range(5):
		if(array.count(i + 1) == 0):
			return 0
	return 30
def sequencia_alta(array):
	for i in range(1, 6):
		if(array.count(i + 1) == 0):
			return 0
	return 40
def general(array):
	for i in range(6):
		if(array.count(i + 1) == num_dices):
			return 50
	return 0

def print_table_score(screen, dices = []):
	start_y = 225
	start_x = 30

	nomes = [" ", "1", "2", "3", "4", "5", "6", "T", "Q", "F", "S+", "S-", "G", "Total"]
	font = pygame.font.SysFont('Comic Sans MS', 12)
	font_selected = pygame.font.SysFont('Comic Sans MS', 14)
	font_selected.set_bold(True)
	tam_first_cell = 40
	for i in range(len(nomes)):
		text_surface = font.render(nomes[i], False, (0, 0, 0))	
		
		pygame.draw.rect(screen, BLACK, (start_x, start_y + i * 25, 460, 25), 1)
		screen.blit(text_surface, (start_x + 4, start_y + i * 25 + 4))
		font.set_bold(False)

	salto = 420 // num_players

	score_atual = []

	for j in range(12):
		if j >= 0 and j <= 5:
			score_atual.append(jogada_de_x(dices, j + 1))
		elif j == 6:
			score_atual.append(trinca(dices))
		elif j == 7:
			score_atual.append(quadra(dices))
		elif j == 8:
			score_atual.append(full_house(dices))
		elif j == 9:
			score_atual.append(sequencia_alta(dices))
		elif j == 10:
			score_atual.append(sequencia_baixa(dices))
		else:
			score_atual.append(general(dices))

	for i in range(num_players):
		for j in range(len(nomes)):
			pygame.draw.rect(screen, BLACK, (start_x + tam_first_cell + salto * i, start_y + j * 25, salto, 25), 1)
			if(j == 0):
				if(i + 1 == jogador_da_vez):
					font.set_bold(True)
					text_surface = font.render(players[i], False, (0, 0, 255))
				else:
					text_surface = font.render(players[i], False, (0, 0, 0))
				screen.blit(text_surface, (start_x + tam_first_cell + 5 + salto * i, start_y + j * 25 + 5))
				font.set_bold(False)
			elif(j == len(nomes) - 1):
					text_surface = font.render(str(pontuacao[i][j - 1]) if pontuacao[i][j - 1] > -1 else "", False, (0, 0, 0))
					screen.blit(text_surface, (start_x + tam_first_cell + 5 + salto * i, start_y + j * 25 + 5))
			else:			
				if(pontuacao[i][j - 1] > -1):
					text_surface = font_selected.render(str(pontuacao[i][j - 1]), False, (255, 0, 0))
					screen.blit(text_surface, (start_x + tam_first_cell + 5 + salto * i, start_y + j * 25 + 2))
				else:
					if(i + 1 == jogador_da_vez and len(dices) > 0):
						text_surface = font.render(str(score_atual[j - 1]) if score_atual[j - 1] > 0 else "", False, (0, 0, 0))
						screen.blit(text_surface, (start_x + tam_first_cell + 5 + salto * i, start_y + j * 25 + 5))
						if(reroll == 0 and score_atual[j - 1] > 0 and pontuacao):
							pygame.draw.rect(screen, RED, (start_x + tam_first_cell + salto * i, start_y + j * 25, salto, 25), 3)

	return score_atual

#Criando a janela e setando o titulo
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('General Game')

x_inicial = (width - (num_dices * 50 + 100)) // 2
y_inicial = 30

score_atual = []
selected_dices = []
not_selected_dices = [None for _ in range(num_dices)]

roll_btn = Button(width / 2 - 75, 175, 150, 40, "Roll")

#Loop principal onde ocorre os eventos
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if pygame.mouse.get_pressed()[0]:
			selected_to_not_selected = []
			not_selected_to_selected = []

			x, y = pygame.mouse.get_pos()

			for idx, dice in enumerate(selected_dices):
				if(dice.is_pressed(x, y)):
					for i, temp in enumerate(not_selected_dices):
						if(temp is None):
							selected_to_not_selected.append(idx)
							break

			for idx, dice in enumerate(not_selected_dices):
				if(dice is not None):
					if(dice.is_pressed(x, y)):
						not_selected_to_selected.append(idx)

			for i in not_selected_to_selected:
				selected_dices.append(not_selected_dices[i])
				not_selected_dices[i] = None

			for i in selected_to_not_selected:
				for idx, temp in enumerate(not_selected_dices):
					if temp is None:
						not_selected_dices[idx] = selected_dices[i]
						del selected_dices[i]
						break

			if(reroll == 0):
				start_y = 225
				start_x = 30
				salto = 420 // num_players
				for j in range(1, 13):
					if(x >= start_x + 20 + salto * (jogador_da_vez - 1) and x <= start_x + 20 + salto * (jogador_da_vez - 1) + salto and y >= start_y + j * 25 and y <= start_y + j * 25 + 25):
						reroll = 3
						pontuacao[jogador_da_vez - 1][j - 1] = score_atual[j - 1]
						if(pontuacao[jogador_da_vez - 1][-1] == -1):
							pontuacao[jogador_da_vez - 1][-1] = 0
						pontuacao[jogador_da_vez - 1][-1] += score_atual[j - 1]
						not_selected_dices = [None for _ in range(num_dices)]
						selected_dices = []
						jogador_da_vez += 1
						if(jogador_da_vez > num_players):
							jogador_da_vez = 1

			#Clicando no botão
			if(roll_btn.is_pressed(x, y)):
				if((not_selected_dices.count(None) == num_dices and len(selected_dices) > 0) or reroll == 0):
					reroll = 0
				else:
					reroll -= 1
					if(not_selected_dices.count(None) == num_dices):
						for i in range(len(not_selected_dices)):
							not_selected_dices[i] = Dice(randint(1, 6))
					else:
						for i in range(len(not_selected_dices)):
							if not_selected_dices[i] is not None:
								not_selected_dices[i] = Dice(randint(1, 6))
			time.sleep(0.2)

	#Preenchendo a cor de fundo da tela
	screen.fill(WHITE)
	if(not_selected_dices.count(None) == num_dices and len(selected_dices) == 0):
		for idx in range(num_dices):
			temp = Dice(0, seq = idx)
			temp.draw(screen, x_inicial + idx * 75, y_inicial)
	else:
		for idx, dice in enumerate(not_selected_dices):
			if(dice is not None):
				dice.draw(screen, x_inicial + idx * 75, y_inicial)

		for idx in range(len(selected_dices)):
			selected_dices[idx].draw(screen, x_inicial + idx * 75, y_inicial + 75)

	roll_btn.draw(screen, reroll, not_selected_dices, selected_dices)
	finished_array = []
	for i in not_selected_dices:
		if i is not None:
			finished_array.append(i.num)
	for i in selected_dices:
		finished_array.append(i.num)
	score_atual = print_table_score(screen, finished_array)
	#Atualizando a tela
	pygame.display.flip()