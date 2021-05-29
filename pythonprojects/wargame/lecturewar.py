import pygame
import random
pygame.init()

screen=pygame.display.set_mode((800,600))

done=False


player_x=200
player_y=500

backgroundImage=pygame.image.load("cosmos.jpg")
playerImage = pygame.image.load("корабль.jpg")
enemyImage=pygame.image.load("enemy.png")
bulletImage= pygame.image.load("bullet.jpg")

enemy_x= random.randint(0,750)
enemy_y=random.randint(20,50)

enemy_dx=8
enemy_dy=20


bullet_x = -100
bullet_y = -100
bullet_shot = False

def player(x,y):
    screen.blit(playerImage,(x,y))

def enemy(x,y):
    screen.blit(enemyImage,(x,y))

def bullet(x,y):
    screen.blit(bulletImage, (x,y))

while not done:
    for event in pygame.event.get():
        #event to quit
        if event.type==pygame.QUIT:
            done=True
      
    enemy_x+=enemy_dx
    
    if enemy_x<0 or enemy_x>736:
        enemy_dx=-enemy_dx
        enemy_y+=enemy_dy
    
    screen.blit(backgroundImage,(0,0))
    k = pygame.key.get_pressed()
    #Moving player
    if k[pygame.K_RIGHT]:
        player_x+=1
    elif k[pygame.K_LEFT]:
        player_x-=1
    #Shooting
    if k[pygame.K_SPACE] and not(bullet_shot):
        bullet_shot = True
        bullet_x = player_x+25-11
        bullet_y = player_y
    
    #MoveBullet
    if bullet_shot:
        bullet_y -=8
    #Aboard
    if bullet_y <=0:
        bullet_shot = False
        bullet_x = -5
        bullet_y = -5
    #Collision with enemy
    if (bullet_x >= enemy_x and bullet_x<= enemy_x + 50) and (bullet_y >= enemy_y-50 and bullet_y <= enemy_y):
        bullet_shot = False
        bullet_x = -100
        bullet_y = -100
        pygame.quit()
    #Collison with player
    if (player_x >= enemy_x and player_x<= enemy_x + 50) and (player_y >= enemy_y and player_y <= enemy_y+86):
        pygame.quit()
    bullet(bullet_x,bullet_y)
    enemy(enemy_x,enemy_y)
    player(player_x,player_y)   

    pygame.display.flip()
