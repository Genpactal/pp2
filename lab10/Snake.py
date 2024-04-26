import pygame
import random
import psycopg2
pygame.init()

#color
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW =(255, 191, 0)

#clock
clock = pygame.time.Clock()
FPS = 10
time_for_big_food = 10*FPS+1  # my time it is just cnt by FPS  10*FPS=10s

#screen
l, w = 1001, 601
screen = pygame.display.set_mode((l,w))
running = True
dx, dy = 0, 0
radius = 10
body = [[10, 10]]
snake_len=1
wall = []
wall_len = 0
condition_kill = False
last_key = str("")

#value
level_value = 1
score_value = 0
record = 0
#text
font = pygame.font.SysFont("comicsansms", 24)
font_Gameover = pygame.font.SysFont("comicsansms", 72)
text4 = font.render("GAME OVER", True, BLACK)


#random cordinate  
def rondom_c():
    value_x = random.randrange(10, l-10)
    value_y = random.randrange(10, w-10)
    x1, y1 = 10 * round(value_x / 10), 10 * round(value_y /10)
    condition = True
    for i in range(len(body)):
        if body[i][0]==x1 and body[i][1] == y1:
            condition = False
            break
    if level_value == 1:
        for i in range(100,400):
            if x1 == 300 and y1 == i:
                condition = False
                break
    if condition == True:
        return x1, y1
    else:
        x1, y1 = rondom_c()
        return x1, y1

food_x, food_y = rondom_c()
BIG_FOOD_X, BIG_FOOD_Y = rondom_c()

def kill_yourself():
    global condition_kill
    for i in range(1,len(body)):
        if body[0][0] == body[i][0] and body[0][1] == body[i][1]:
            condition_kill = True
            break
    return condition_kill
    

def kill_wall_line():
    global condition_kill
    for i in range(100,400):
        if body[0][0] == 300 and body[0][1] == i:
            condition_kill = True
            break
    return condition_kill

def kill_wall():  
    global condition_kill
    for i in range(len(wall)):
        if body[0][0] == wall[i][0] and body[0][1] == wall[i][1]:
            condition_kill = True
            break

    return condition_kill
   


#SCL
conn = psycopg2.connect(
	database="snake",
	user='snake_user',
	password='Esko28:)',
	host='localhost',
	port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True

login_name = str(input('Pls enter your login: '))
sql = f"select * from snakedata where user_login =\'{login_name}\'"
cursor.execute(sql)
info = cursor.fetchall()

if len(info) > 0:
    print("You already have account, looading your data")
    score_value = info[0][1]
    level_value = info[0][2]
    FPS = info[0][3]
    snake_len = int(info[0][4])
    wall_len = int(info[0][5])
    body[0][0] = int(info[0][6])
    body[0][1] = int(info[0][7])
    dx = -10
    record = info[0][8]
    for i in range(1,snake_len):
        body.append([-i*200,-i*200])
    for j in range(wall_len):
        food_x2, food_y2 = rondom_c()
        wall.append([food_x2, food_y2])
    print(body)

        

        


else:
    print("this login didnt regestrated, So now you have new acount")
    sql_insert = f"INSERT INTO snakedata(user_login, last_score, last_level, last_FPS, snake_len, wall_len, snake_x, snake_y, record) VALUES( \'{login_name}\',\'{score_value}\',\'{level_value}\',\'{FPS}\', \'{snake_len}\', \'{wall_len}\',\'{body[0][0]}\', \'{body[0][1]}\', \'{record}\' )"
    cursor.execute(sql_insert)


def GAME_OVER():
    global running
    global sql_insert1
    global score_value
    global record
    screen.fill(RED)
    screen.blit(text1, (850,5))
    screen.blit(text2, (850,35))
    screen.blit(text3, (850,65))
    screen.blit(text4, (425,225))
    sql_insert1 = f"UPDATE snakedata set  last_score = 0, last_level = 1, last_FPS = 10, snake_len = 1, wall_len = 0, snake_x=10, snake_y=10  where user_login = \'{login_name}\' "
    cursor.execute(sql_insert1)
    if score_value > record:
        sql_insert1 = f"UPDATE snakedata set record = \'{score_value}\'  where user_login = \'{login_name}\' "
        record = score_value
        cursor.execute(sql_insert1)
  


    
 



#main
while running:
    wall_len = len(wall)
    snake_len=len(body)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and last_key!="K_LEFT":
                dx = 10
                dy = 0
                last_key = "K_RIGHT"

            if event.key == pygame.K_LEFT and last_key!="K_RIGHT":
                dx = -10
                dy = 0
                last_key = "K_LEFT"

            if event.key == pygame.K_UP and last_key!="K_DOWN":
                dx = 0
                dy = -10
                last_key = "K_UP"

            if event.key == pygame.K_DOWN and last_key!="K_UP":
                dx = 0
                dy = 10
                last_key = "K_DOWN"

            if event.key == pygame.K_p:
                print("PAUSE")
                sql_insert = f"UPDATE snakedata set last_score =\'{score_value}\',last_level =\'{level_value}\',last_FPS =\'{FPS}\',snake_len=\'{snake_len}\',wall_len=\'{wall_len}\', snake_x=\'{body[0][0]}\', snake_y=\'{body[0][1]}\', record = \'{record}\' where user_login = \'{login_name}\'; "
                cursor.execute(sql_insert)
                running = False
                
                

                
    #value 
    text1 = font.render("Score: "+str(score_value), True, WHITE)
    text2 = font.render("Level: "+str(level_value), True, WHITE)
    text3 = font.render("FPS: "+str(FPS), True, WHITE)
    text5 = font.render("Record: "+str(record), True, WHITE)


    #eating
    if body[0][0]==food_x and body[0][1]==food_y:
        food_x, food_y = rondom_c()
        body.append([0, 0])
        score_value += 10
        time_for_big_food = 10*FPS +1

    
    #eating BIF FOOD
    elif body[0][0]==BIG_FOOD_X and body[0][1]== BIG_FOOD_Y:
        body.append([0, 0])
        score_value += 30
        time_for_big_food = 10*FPS+1


    #level
    last_level = level_value
    level_value = 1 + score_value //50
    
    #body change
    for i in range(len(body) - 1, 0, -1):
        body[i][0] = body[i - 1][0]
        body[i][1] = body[i - 1][1]

    #return to screen
    if body[0][0] > l-11:
        body[0][0] = 10
    if body[0][1] > w-11:
        body[0][1] = 10
    if body[0][1] < 10:
        body[0][1] = w-11
    if body[0][0] < 10:
        body[0][0] = l-11
    
    #body coordination
    body[0][0] += dx
    body[0][1] += dy

    # main screen     
    screen.fill(BLACK)

  
    # Draw score level FPS
    screen.blit(text1, (850,5))
    screen.blit(text2, (850,35))
    screen.blit(text3, (850,65))
    screen.blit(text5, (850,95))

    # Draw food
    pygame.draw.circle(screen, WHITE, (food_x, food_y), radius-5)

    if time_for_big_food == 0:
        BIG_FOOD_X, BIG_FOOD_Y = rondom_c()

    if time_for_big_food <= 10*FPS:
        pygame.draw.circle(screen, YELLOW, (BIG_FOOD_X, BIG_FOOD_Y), radius)
        time_for_big_food += 1

    if time_for_big_food > 10*FPS:
        BIG_FOOD_X, BIG_FOOD_Y = -100, -100

    # Draw snake body
    for i, (x, y) in enumerate(body):
        if i!=0:
            pygame.draw.circle(screen, GREEN, (x, y), radius)

    # Draw snake head
    pygame.draw.circle(screen, RED, (body[0][0], body[0][1]), radius)
    
    #level 1
    if level_value == 1:
        pygame.draw.line(screen, BLUE, (300,100),(300, 400), 10)
        if kill_wall_line() == True:
            print("BLUE WALL")
            GAME_OVER()


    # add wall circle & add FPS next level
    if last_level != level_value:
        FPS += 3
        food_x2, food_y2 = rondom_c()
        wall.append([food_x2, food_y2])
        time_for_big_food = 0

    if level_value > 1:
        for i in range(len(wall)):
            pygame.draw.circle(screen, BLUE, (wall[i][0], wall[i][1]), radius-5)
        if kill_wall()== True:
            print("SMALL WALL")
            GAME_OVER()
    
    # Kill yourself
    if kill_yourself()==True:
        print("killed yourself")
        GAME_OVER
        


    pygame.display.flip()

    clock.tick(FPS)


conn.commit()

pygame.quit()