import pygame
           

pygame.init()
pygame.mixer.init()

jump_sound = pygame.mixer.Sound('jump.wav')
levelup_sound = pygame.mixer.Sound('levelup.wav')
gameover_sound = pygame.mixer.Sound('gameover.wav')

pygame.mixer.music.load('roblox-music-badli.mp3')
pygame.mixer.music.play(-1)

wight,height = 800,400
win = pygame.display.set_mode((wight,height))
pygame.display.set_caption('dino game')

ground_img = pygame.image.load('ground.png')
cactus_img = pygame.image.load('cactus.png')
dino_img = pygame.image.load('dino.png')
pterodactyl_img = pygame.image.load('pterodactyl.png')

jump = 0


dino_wight, dino_height = 60,60
dino_x,dino_y = 50, height-dino_height-20
dino_vel_y = 0
gravity = 1
jump_height = -15
is_jumping = False

obstacle_wight, obstacle_height = 20, 50
obstacle_x, obstacle_y = wight, height-obstacle_height-20
obstacle_vel = 10
speed = 1

obstacle1_wight, obstacle1_height = 30, 30
obstacle1_x, obstacle1_y = wight-300, height-obstacle1_height-100


obstacle1_vel = 10
speed1 = 3

dino_img = pygame.transform.scale(dino_img, (dino_wight, dino_height))
cactus_img = pygame.transform.scale(cactus_img, (obstacle_wight, obstacle_height))
pterodactyl_img = pygame.transform.scale(pterodactyl_img, (obstacle1_wight, obstacle1_height))

score = 0
high_score = 0
font = pygame.font.SysFont('PressStart2P-Regular.ttf', 20)

clock = pygame.time.Clock()
run = True
game_active = False
initial_start = True 

while run:
    clock.tick(60)
    


    if score >= 100:
        win.fill((0,255,0))
    else:
        win.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                if not game_active:
                    game_active = True
                    initial_start = False

                    score = 0
                    dino_x = 50
                    dino_y = height - dino_height - 20
                    dino_vel_y = 0
                    is_jumping = False

                    obstacle_x = wight
                    obstacle1_x = wight - 300

                elif not is_jumping:
                    is_jumping = True
                    jump += 1
                    dino_vel_y = jump_height
                    jump_sound.play()

   
    if game_active:
        keys = pygame.key.get_pressed()

        if not is_jumping and keys[pygame.K_SPACE]:
            is_jumping = True
            jump += 1
            
            dino_vel_y = jump_height

        if is_jumping:
            dino_vel_y += gravity
            dino_y += dino_vel_y

        if dino_y > height - dino_height - 20:
            dino_y = height - dino_height - 20
            is_jumping = False

        obstacle_x -= obstacle_vel
        obstacle1_x -= obstacle1_vel

        if obstacle_x < -obstacle_wight:
            obstacle_x = wight
            score += 1

        if obstacle1_x < -obstacle1_wight:
            obstacle1_x = wight
            score += 1
        if score % 100 == 0:
            levelup_sound.play()
        if score> high_score:
            high_score = score

        
        win.blit(dino_img, (dino_x, dino_y))
        win.blit(cactus_img, (obstacle_x, obstacle_y))
        win.blit(pterodactyl_img, (obstacle1_x, obstacle1_y))
        score_text = font.render(f'Score: {score}', True, (0,0,0))
        win.blit(score_text, (10,10))

        high_score_text = font.render(f'High Score: {high_score}', True, (0,0,0))
        win.blit(high_score_text, (10,40))



        if (dino_x < obstacle_x+obstacle_wight and dino_x+dino_wight>obstacle_x and dino_y < obstacle_y+obstacle_height
        and dino_y + dino_height > obstacle_y) or ((dino_x < obstacle1_x + obstacle1_wight and
        dino_x + dino_wight > obstacle1_x and dino_y < obstacle1_y + obstacle1_height and dino_y + dino_height > obstacle1_y)):
        
            score = 0
            obstacle_x = wight
            obstacle1_x = wight-300
            dino_x = 50
            dino_y = height-dino_height-20  
            speed = 1
            speed1 = 1
            gameover_sound.play()

            #GAME OVER
            game_active = False

            
   
            

 
    else:
        if initial_start:
            start_text = font.render('Press SPACE to Start', True, (0,0,0))
            win.blit(start_text, (wight//2 - start_text.get_width()//2, height//2 - start_text.get_height()//2))
        else:
            game_over_text = font.render('Game Over! Press SPACE to Restart', True, (0,0,0))
            win.blit(game_over_text, (wight//2 - game_over_text.get_width()//2, height//2 - game_over_text.get_height()//2))
            high_score_text = font.render(f'High Score: {high_score}', True, (0,0,0))
            win.blit(high_score_text, (wight//2 - high_score_text.get_width()//2, height//2 + 30))
            
    pygame.display.update()
    
pygame.quit()