import pygame
import sys

clock=pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1920, 960))
pygame.display.set_caption("Game")

background=pygame.image.load('images/background.jpg').convert()
ghost=pygame.image.load("images/ghost.png").convert_alpha()
bg_sound=pygame.mixer.Sound("sounds/8bit_game_track.wav")
ghost_timer=pygame.USEREVENT+1
pygame.time.set_timer(ghost_timer,6000)
ghost_list=[]

walk_right=[pygame.image.load('images/sprite_sheet/walk_right1.png').convert_alpha(),
            pygame.image.load('images/sprite_sheet/walk_right2.png').convert_alpha(),
            pygame.image.load('images/sprite_sheet/walk_right3.png').convert_alpha(),
            pygame.image.load('images/sprite_sheet/walk_right4.png').convert_alpha(),]

walk_left=[pygame.image.load('images/sprite_sheet/walk_left1.png').convert_alpha(),
            pygame.image.load('images/sprite_sheet/walk_left2.png').convert_alpha(),
            pygame.image.load('images/sprite_sheet/walk_left3.png').convert_alpha(),
            pygame.image.load('images/sprite_sheet/walk_left4.png').convert_alpha(),]


i=0
bg_x=0
player_speed=5
player_x=140
player_y=770
is_jump=False
jump_count=7

bg_sound.play()

while True:
    
    screen.blit(background,(bg_x,0))
    screen.blit(background,(bg_x+1920,0))
    

    player_rect=walk_left[0].get_rect(topleft=(player_x,player_y))
    
    if ghost_list:
        for el in ghost_list:
            screen.blit(ghost,el)
            el.x-=10
    
        if player_rect.colliderect(el):
            print("You lose")


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:

        screen.blit(walk_left[i],(player_x,player_y))
    else:
        screen.blit(walk_right[i],(player_x,player_y))

    
    
    

        
    
    if keys[pygame.K_LEFT] and player_x>50:
        
        player_x-=player_speed
        
      
    elif keys[pygame.K_RIGHT] and player_x<1900:
        
        player_x+=player_speed


    #for sprite sheet
    if i==3:
        i=0
    else:
        i+=1
    #for bg
    bg_x-=15
    if bg_x==-1920:
        bg_x=0
  
    
    #for jump
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump=True
    else:
        if jump_count>=-7:
            if jump_count>0:
                player_y-=(jump_count**2)/1.5
            else:
                player_y+=(jump_count**2)/1.5
                
            jump_count-=1
        else:
            is_jump=False
            jump_count=7
    


  
    

    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==ghost_timer:
            ghost_list.append(ghost.get_rect(topleft=(1922,750)))

    clock.tick(10)
        
        
        
  
                
                        
    
            
            