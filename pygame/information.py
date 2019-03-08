import pygame

# Initialization
pygame.init()
pygame.font.init()
window_size = (1000, 700)
screen = pygame.display.set_mode((window_size))

# load images
bubblesortInfomation_image = pygame.image.load('bubblesortInfomation_image.png')
quicksortInfomation_image = pygame.image.load('quicksortInfomation_image.png')
mergesortInfomation_image = pygame.image.load('mergesortInfomation_image.png')
insertionsortInfomation_image = pygame.image.load('insertionsortInfomation_image.png')
bogosortInfomation_image = pygame.image.load('bogosortInfomation_image.png')
radixsortInfomation_image = pygame.image.load('radixsortInfomation_image.png')

backSelected_btn = pygame.image.load('backSelected_btn.png')
backUnselected_btn = pygame.image.load('backUnselected_btn.png')

# UI coordinates
backBtn_x, backBtn_y, backBtn_w, backBtn_h = 48, 28, 42, 42

def update_draw():
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(1000000000)

def information_run(sort_type):
	if sort_type == 'bubblesort': screen.blit(bubblesortInfomation_image, (0,0))
	if sort_type == 'quicksort': screen.blit(quicksortInfomation_image, (0,0))
	if sort_type == 'mergesort': screen.blit(mergesortInfomation_image, (0,0))
	if sort_type == 'insertionsort': screen.blit(insertionsortInfomation_image, (0,0))
	if sort_type == 'bogosort': screen.blit(bogosortInfomation_image, (0,0))
	if sort_type == 'radixsort': screen.blit(radixsortInfomation_image, (0,0))
	update_draw()

	backSelected_drawn = False
	
	while True:
		for event in pygame.event.get():
			mousePos = pygame.mouse.get_pos()

			# If cursor over back_btn
			if backBtn_x+backBtn_w > mousePos[0] > backBtn_x and backBtn_y+backBtn_h > mousePos[1] > backBtn_y:
				if not backSelected_drawn: 
					screen.blit(backSelected_btn, (0, 0))
					update_draw()
					backSelected_drawn = True                    
				if event.type == pygame.MOUSEBUTTONDOWN: 
					if event.button == 1: return True 
			else: 
				if backSelected_drawn: 
					screen.blit(backUnselected_btn, (0, 0))
					update_draw()
					backSelected_drawn = False