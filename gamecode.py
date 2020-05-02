
import pygame
import random
import sys

pygame.init()
HEIGHT=850
WIDTH=1300
GREEN=(0,255,0)
BLUE=(0,0,255)
RED=(255,0,0)

YELLOW=(255,255,0)

SPEED=10

x=0
y=0


a=[46,553,50,553,54,553,58,553]#for green token
b=[46,918,157,815,253,918,253]#for yellow token
c=[382,157,482,157,382,255,482,255]#for red token
d=[46,653,50,653,54,653,58,653]#for blue token

ypos=653

x_ch=0
y_ch=0




walk3 = [pygame.image.load('3.jpg')]
walk2 = [pygame.image.load('2.jpg')]
walk1=[pygame.image.load('1.jpg')]
walk4=[pygame.image.load('4.jpg')]
walk5=[pygame.image.load('5.jpg')]
walk6=[pygame.image.load('6.jpg')]
#bg = pygame.image.load('bg.jpg')



clock=pygame.time.Clock()
sky=pygame.image.load('game.jpg')
sky = pygame.transform.scale(sky, (WIDTH-250, HEIGHT))



imageX= 500; # x coordnate of image
imageY= 500; # y coordinate of image





screen = pygame.display.set_mode((WIDTH,HEIGHT))
gameover = False

space=50





def redrawGameWindow(i,x,y):
    global walkCount
   
    walkCount = 0
    if i==1:
        screen.blit(walk1[walkCount],(x,y))

    elif i==2:
        screen.blit(walk2[walkCount], (x,y))
        
    elif i==3:
        screen.blit(walk3[walkCount], (x,y))
        
    elif i==4:
        screen.blit(walk4[walkCount],(x,y))
    elif i==5:
        screen.blit(walk5[walkCount],[x,y])
    elif i==6:
        screen.blit(walk6[walkCount],[x,y])
    pygame.display.update()

z=0
q=0
w=0
v=0
n=0


g=1
h=1
inx=325
iny=782
vid=0

i=0
t=1

k=-1



dice=0
sc=-1
good=0
qk=0
wk=0

p_x=0
p_y=1

gx=0
gy=1


    
        
while not gameover:

        
  
    for event in pygame.event.get():
       
        
        
                        
        if event.type == pygame.QUIT:
        
            gameover=True
            break
        
        if event.type == pygame.KEYDOWN:
         
            if event.key == pygame.K_RIGHT :
                i=random.randint(1,6)
                

                    
                x = 100
                y = 100
                k+=i
                #for ladder
                if k==18:
                    k=65
                elif k==31:
                    k=52
                elif k==72:
                    k=90
                elif k==66:
                    k=99
                    if p_x>5:
                        gameover=True
                        break

                


                #for snake    
                elif k==45:
                    k=11
                elif k==24:
                    k=5
                elif k==73:
                    k=51
                elif k==87:
                    k=75



                #for reaching 100 game wins
                elif k==99:
                    if p_x>5:
                        
                        
                        gameover=True
                        break

                #until reaches 100
                elif k>99:
                    
                    k=n
                    
                n=k
                
                q=n%10
                w=n//10
                d[p_x]=325+q*100
                d[p_y]=789-w*75

                if k==99 and p_x<=6:
                    k=0
                    p_x+=2
                    p_y+=2




                                
                    
                    
         
         
            elif event.key == pygame.K_LEFT :
                i=random.randint(1,6)
                
                #dice=random.randint(1,6)
                

                    
                #sc+=dice
                sc+=i
                #for ladder
                if sc==18:
                    sc=65
                elif sc==31:
                    sc=52
                elif sc==72:
                    sc=90
                elif sc==66:
                    sc=99
                    if gx>5:
                        gameover=True
                        break


                #for snake    
                elif sc==45:
                    sc=11
                elif sc==24:
                    sc=5
                elif sc==73:
                    sc=51
                elif sc==87:
                    sc=75



                #for reaching 100 game wins
                elif sc==99:
                    if gx>5:
                        
                        gameover=True
                        break
                #until reaches 100
                elif sc>99:
                    
                    sc=good
                 
                    
                good=sc
                
                qk=good%10
                wk=good//10
                a[gx]=325+qk*100
                a[gy]=789-wk*75
                if k==99 and p_x<=6:
                    k=0
                    gx+=2
                    gy+=2





                                
                    
                    
    z=0



      
          


        





    screen.fill((204,255,229))
    
    screen.blit(sky,(250,0))
    pygame.draw.rect(screen,(255,255,255),(0,296,250,225))
  



    
    pygame.draw.circle(screen, BLUE,(d[0],d[1]) , 25, 0)
    pygame.draw.circle(screen, BLUE,(d[2],d[3]) , 25, 0)
    pygame.draw.circle(screen, BLUE,(d[4],d[5]) , 25, 0)
    pygame.draw.circle(screen, BLUE,(d[6],d[7]) , 25, 0)




    pygame.draw.circle(screen, GREEN,(a[0],a[1]) , 25, 0)
    pygame.draw.circle(screen, GREEN,(a[2],a[3]) , 25, 0)
    pygame.draw.circle(screen, GREEN,(a[4],a[5]) , 25, 0)
    pygame.draw.circle(screen, GREEN,(a[6],a[7]) , 25, 0)
         
        
    


    g,h = pygame.mouse.get_pos()
    print(g,h)
         
    redrawGameWindow(i,x,y)

    clock.tick(30)
    
pygame.mixer.music.stop()
        
pygame.quit()
