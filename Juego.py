import pygame
import math
import time
import random

Ancho=598
Alto= 700

Blanco=[255,255,255]
Negro=[0,0,0]
Amarillo=[255,255,0]
Azul=[0,102,255]
Naranja=[255,160,16]
##---------------------------botones--------------------------------------
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)
 ##---------------------------Platafoma--------------------------------------
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, an , al, pos):
    
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([an,al])
        self.image.fill(Azul)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
 ##---------------------------Jugadores--------------------------------------
class Jugador(pygame.sprite.Sprite):

    def __init__(self,m,lim,accion):

        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=accion
        self.con=0
        self.lim=lim

        self.image =m[self.accion][self.con]
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.salto=False
        self.salud=350
    
    def gravedad(self,val):
        if self.vel_y == 0:
            self.vel_y=4
        else:
            self.vel_y += val

    def update(self,plataforma_lista):
        self.gravedad(0.4)

         # Mover arriba/abajo
        self.rect.y += self.vel_y
        
        # Revisamos si chocamos
        bloque_col_list = pygame.sprite.spritecollide(self,plataforma_lista, False)
        for bloque in bloque_col_list:
            
            # Reiniciamos posicion basado en el arriba/bajo del objeto
            if self.vel_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.vel_y < 0:
                self.rect.top = bloque.rect.bottom
            
            # Detener movimiento vertical
            self.vel_y = 0
        
         # Mover izq/der
        self.rect.x += self.vel_x
        
        # Revisar si golpeamos con algo (bloques con colision)
        bloque_col_list = pygame.sprite.spritecollide(self , plataforma_lista, False)
        for bloque in bloque_col_list:
            # Si nos movemos a la derecha,
            # ubicar jugador a la izquierda del objeto golpeado
            if self.vel_x > 0:
                self.rect.right = bloque.rect.left
            elif self.vel_x < 0:
                # De otra forma nos movemos a la izquierda
                self.rect.left = bloque.rect.right

        self.image =m[self.accion][self.con]
        if self.con<self.lim[self.accion]:
            self.con+=1
        else:
            self.con=0
class Jugador2(pygame.sprite.Sprite):
    def __init__(self,m1,lim,accion):

        pygame.sprite.Sprite.__init__(self)
        self.m1=m1
        self.accion=accion
        self.con=0
        self.lim=lim

        self.image =m1[self.accion][self.con]
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.salto=False
        self.salud=350
    
    def gravedad(self,val):
        if self.vel_y == 0:
            self.vel_y=4
        else:
            self.vel_y += val
    
    def update(self,plataforma_lista):

        self.gravedad(0.4)

         # Mover arriba/abajo
        self.rect.y += self.vel_y
        
        # Revisamos si chocamos
        bloque_col_list = pygame.sprite.spritecollide(self,plataforma_lista, False)
        for bloque in bloque_col_list:
            
            # Reiniciamos posicion basado en el arriba/bajo del objeto
            if self.vel_y > 0:
                self.rect.bottom = bloque.rect.top
            elif self.vel_y < 0:
                self.rect.top = bloque.rect.bottom
            
            # Detener movimiento vertical
            self.vel_y = 0
        
         # Mover izq/der
        self.rect.x += self.vel_x
        
        # Revisar si golpeamos con algo (bloques con colision)
        bloque_col_list = pygame.sprite.spritecollide(self,plataforma_lista, False)
        for bloque in bloque_col_list:
            # Si nos movemos a la derecha,
            # ubicar jugador a la izquierda del objeto golpeado
            if self.vel_x > 0:
                self.rect.right = bloque.rect.left
            elif self.vel_x < 0:
                # De otra forma nos movemos a la izquierda
                self.rect.left = bloque.rect.right

        self.image =m1[self.accion][self.con]
        if self.con<self.lim[self.accion]:
            self.con+=1
        else:
            self.con=0
    
BandPantalla=0
BandNivel=0
Nivel=1
ContSaltos= 0
ContSaltosFuera= 0
ContSaltos2= 0
ContSaltosFuera2=0

selectJugador1=0
selectJugador2=0

ContVictoria1=0
ContVictoria2=0

contInst=0
contHis=0

minutes = 0
seconds = 0
milliseconds = 0

if __name__ == '__main__':
    pygame.init()
    
    iniciar=pygame.image.load('iniciar.png')
    iniciar2=pygame.image.load('iniciar2.png')
    historia=pygame.image.load('historia.png')
    historia2=pygame.image.load('historia2.png')
    instrucciones=pygame.image.load('instrucciones.png')
    instrucciones2=pygame.image.load('instrucciones2.png')
    salir=pygame.image.load('salir.png')
    salir2=pygame.image.load('salir2.png')
    jugar= pygame.image.load('jugar.png')
    jugar2=pygame.image.load('jugar2.png')
    next1= pygame.image.load('ok.png')
    next2= pygame.image.load('ok2.png')
    
    boton1=Boton(iniciar2,iniciar,100,400)
    boton2=Boton(historia2,historia,100,470)
    boton3=Boton(instrucciones2,instrucciones,105,540)
    boton4=Boton(salir2,salir,100,610)
    boton5=Boton(jugar,jugar2,485,620)
    boton6=Boton(next1,next2,1000,600)

    cursor=Cursor()
    ##Imagenes Barra de salud
    salud1= pygame.image.load('salud.png')
    salud2= pygame.image.load('salud2.png')

    ##Metodo RESIZABLE redimenciona la pantalla
    Pantalla= pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
    Reloj=pygame.time.Clock()
    ##reloj cronometro
    fin= False

    ##pos plataformas
    plataforma_lista =pygame.sprite.Group()
    if BandNivel==0:  
        p=Plataforma(782,10,[200,405])
        plataforma_lista.add(p)
 
    ##Fuente cronometro
    fuente=pygame.font.SysFont('Arial',34,True,False)
    fuente1=pygame.font.SysFont('Arial',100,True,False)
    texto1 = fuente.render("PLAYER 1", 100, (255, 255, 255))
    texto2 = fuente.render("PLAYER 2", 100, (255, 255, 255))
    texto3 = fuente.render("VENOM", 100, (255, 255, 255))
    texto4 = fuente.render("FLASH", 100, (255, 255, 255))
    texto5 = fuente.render("HULK", 100, (255, 255, 255))
    texto6 = fuente.render("WOLVERINE", 100, (255, 255, 255))
    texto7 = fuente.render("<", 100, (255, 255, 255))
    texto8 = fuente.render(">", 100, (255, 255, 255))
    texto9 = fuente1.render("YOU WIN!!!",100, (255,255,255))
    texto11 = fuente1.render("EMPATE!!!",100, (255,255,255))
        
##Iconos iniciales--------------------------------------------------------------------------
    imagen=pygame.image.load('hulkICON.png')
    imagen1=pygame.image.load('VenomICON.png')

    puno=pygame.mixer.Sound('puno.wav')
    BandSonido=0

##PRESENTACION-----------------------------------------------------------------------------------------------------                    

    while not fin :
        if selectJugador1==0:
            lim=[5,12,19,5,6,7,6,5,11,9,6,7,7]
             ## imagen jugador venom
            img = pygame.image.load('venom1.png')
            m=[]

            for x in range(30):#filas
                ls=[]
                for i in range(20):#columnas
                    cuadro=img.subsurface(i*130,x*110,130,110)#recortar imagen
                    ls.append(cuadro)
                m.append(ls)
            j=Jugador(m,lim,1)
            jugadores=pygame.sprite.pygame.sprite.Group()
            jugadores.add(j)

            selectJugador1=30
        if selectJugador1==1:
             # imagen jugador flash
            lim=[4,4,6,4,3,6,2,1,1,5,2,6,3]
            img = pygame.image.load('flash.png')
            m=[]

            for x in range(30):#filas
                ls=[]
                for i in range(20):#columnas
                    cuadro=img.subsurface(i*106,x*105,106,105)#recortar imagen
                    ls.append(cuadro)
                m.append(ls)
            j=Jugador(m,lim,4)
            jugadores=pygame.sprite.pygame.sprite.Group()
            jugadores.add(j)

            selectJugador1=31
        if selectJugador2==0:
            lim=[4,4,7,3,6,9,19,4,5,19,5,7]
            ## imagen jugador Jugador2
            img1 = pygame.image.load('hulk.png')
            m1=[]
            for x in range(30):#filas
                ls1=[]
                for i in range(20):#columnas
                    cuadro1=img1.subsurface(i*110,x*106,110,106)#recortar imagen
                    ls1.append(cuadro1)
                m1.append(ls1)
            
            j2=Jugador2(m1,lim,4)
            jugadores2=pygame.sprite.pygame.sprite.Group()
            jugadores2.add(j2)
            selectJugador2=30
        if selectJugador2==1:
            lim=[2,3,6,2,4,5,3,9,9]
            ## imagen jugador Jugador2
            img1 = pygame.image.load('wolverine1.png')
            m1=[]
            for x in range(30):#filas
                ls1=[]
                for i in range(20):#columnas
                    cuadro1=img1.subsurface(i*110,x*106,110,106)#recortar imagen
                    ls1.append(cuadro1)
                m1.append(ls1)
            
            j2=Jugador2(m1,lim,0)
            jugadores2=pygame.sprite.pygame.sprite.Group()
            jugadores2.add(j2)
            selectJugador2=31
        if j.rect.y >= (Alto + j.rect.height):
            j.salud=0
            ContVictoria2+=1
            if Nivel==1:
                Nivel=2
                BandNivel=2   
            elif Nivel==2:
                Nivel=3
                BandNivel=3
            elif Nivel==3:
                BandNivel=100
                Nivel=4
                j.rect.x=200
                j.rect.y=200           
        elif j2.rect.y >= (Alto + j2.rect.height):
            j2.salud=0
            ContVictoria1+=1
            if Nivel==1:
                Nivel=2
                BandNivel=2
            elif Nivel==2:
                Nivel=3
                BandNivel=3
            elif Nivel==3:
                BandNivel=100
                Nivel=4 
                j2.rect.x=200
                j2.rect.y=200          
        if BandSonido==0:
            pygame.mixer.music.load('intro2.mp3')
            pygame.mixer.music.play(10)
            BandSonido=30
        if BandNivel==5:
            BandPantalla=5
            fondo= pygame.image.load('anuncio.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            posIndicador1=(220,450)
            posIndicador2=(900,450)
            BandNivel=55
            sonido1=pygame.mixer.Sound('round1.wav')
        if BandNivel==6:
            texto10 = fuente.render("CONTROLES VENOM", 100, (255, 255, 255))
            fondo=pygame.image.load('ControlesVenom.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            boton6.update(Pantalla,cursor)
            BandPantalla=2
            BandNivel=60
            contInst=1
        if BandNivel==7:
            texto10 = fuente.render("CONTROLES FLASH", 100, (255, 255, 255))
            fondo=pygame.image.load('ControlesFlash.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            boton6.update(Pantalla,cursor)
            BandPantalla=2
            BandNivel=60
            contInst=2
        if BandNivel==8:
            texto10 = fuente.render("CONTROLES HULK", 100, (255, 255, 255))
            fondo=pygame.image.load('ControlesHulk.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            boton6.update(Pantalla,cursor)
            BandPantalla=2
            BandNivel=60
            contInst=3
        if BandNivel==9:
            texto10 = fuente.render("CONTROLES WOLVERINE", 100, (255, 255, 255))
            fondo=pygame.image.load('ControlesWolverine.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            boton6.update(Pantalla,cursor)
            BandPantalla=2
            BandNivel=60
            contInst=4
        if BandNivel==100:
            BandNivel=101
            BandPantalla=5
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            pygame.mixer.music.stop()
            sound4=pygame.mixer.Sound('win.wav')
            jugadores.remove(j)
            jugadores2.remove(j2)    
        if BandNivel==0:
            fondo=pygame.image.load('logo.png')
            Ancho = 598
            Alto =700
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            Pantalla.blit(fondo,[0,0])
            boton1.update(Pantalla,cursor)
            boton2.update(Pantalla,cursor)
            boton3.update(Pantalla,cursor)
            boton4.update(Pantalla,cursor)
            BandPantalla=0
            contHis=0
            contInst=0
        if BandNivel==1:
            minutes = 0
            seconds = 0
            milliseconds = 0
            pygame.mixer.music.load('kombat.mp3')
            pygame.mixer.music.play(10)
            Round=pygame.image.load('round1.png')
            fondo= pygame.image.load('escenario.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            j.rect.x=180
            j2.rect.x=900
            BandPantalla=1
            BandNivel=50
            sonido2=pygame.mixer.Sound('round2.wav')
        if BandNivel==2:
            minutes = 0
            seconds = 0
            milliseconds = 0
            j.salud=350
            j2.salud=350
            j.rect.x=180
            j.rect.y=0
            j2.rect.x=900
            j2.rect.y=0
            sonido2.play()
            Round=pygame.image.load('round2.png')
            pygame.mixer.music.play(5)
            plataforma_lista.remove(p)
            p=Plataforma(800,10,[200,380])
            plataforma_lista.add(p)
            fondo= pygame.image.load('escenario1.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            BandPantalla=1
            BandNivel=50
            sonido3=pygame.mixer.Sound('finalRound.wav')
        if BandNivel==3:
            j.gravedad(0.0001)
            j2.gravedad(0.001)
            j.salud=350
            j2.salud=350
            j.rect.x=180
            j.rect.y=0
            j2.rect.x=1200
            j2.rect.y=0
            minutes = 0
            seconds = 0
            milliseconds = 0
            sonido3.play()
            pygame.mixer.music.play(10)
            Round=pygame.image.load('finalRound.png')
            plataforma_lista.remove(p)
            p=Plataforma(225,1,[175,425])
            plataforma_lista.add(p)
            p=Plataforma(225,1,[760,425])
            plataforma_lista.add(p)
            p=Plataforma(240,1,[460,288])
            plataforma_lista.add(p)
            p=Plataforma(950,10,[100,600])
            plataforma_lista.add(p)
            fondo= pygame.image.load('escenarioFinal.jpg')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            j.rect.x=180
            j2.rect.x=740
            BandPantalla=1
            BandNivel=50
        if BandNivel==4:
            fondo=pygame.image.load('his1.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            BandPantalla=2
            BandNivel=59
            boton6.update(Pantalla,cursor)
            contHis=1
        if BandNivel==10:
            fondo=pygame.image.load('his2.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            BandPantalla=2
            BandNivel=59
            boton6.update(Pantalla,cursor)
            contHis=2
        if BandNivel==11:
            fondo=pygame.image.load('his3.png')
            Ancho = 1200
            Alto =675
            Pantalla=pygame.display.set_mode([Ancho,Alto], pygame.RESIZABLE)
            BandPantalla=2
            BandNivel=59
            boton6.update(Pantalla,cursor)
            contHis=3
        if BandNivel==50:
            if minutes <= 1:
                ##Colisiones Jugadores Nivel 1----------------------------------------------------------
                if j.salud>=0 and j2.salud>=0:
                    lista_colisiones=pygame.sprite.spritecollide(j,jugadores2,False)
                    for j1 in lista_colisiones:
                        if selectJugador1==30:
                            if j.rect.right>=j2.rect.left-50 and j.accion==0:
                                if j2.salud>=0:
                                    j2.salud+=-0.5
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==3:
                                if j2.salud>=0:
                                    j2.salud+=-0.4
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==6:
                                if j2.salud>=0:
                                    j2.salud+=-1
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==8:
                                if j2.salud>=0:
                                    j2.salud+=-0.2
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==7:
                                if j2.salud>=0:
                                    j2.salud+=-0.4
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==5:
                                if j2.salud>=0:
                                    j2.salud+=-0.3
                                    print(j2.salud)
                        else:
                            if j.rect.right>=j2.rect.left-50 and j.accion==0:
                                if j2.salud>=0:
                                    j2.salud+=-0.5
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==1:
                                if j2.salud>=0:
                                    j2.salud+=-0.4
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==2:
                                if j2.salud>=0:
                                    j2.salud+=-0.2
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==3:
                                if j2.salud>=0:
                                    j2.salud+=-0.3
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==9:
                                if j2.salud>=0:
                                    j2.salud+=-0.3
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==10:
                                if j2.salud>=0:
                                    j2.salud+=-1
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==11:
                                if j2.salud>=0:
                                    j2.salud+=-0.3
                                    print(j2.salud)
                            if j.rect.right>=j2.rect.left-50 and j.accion==12:
                                if j2.salud>=0:
                                    j2.salud+=-0.6
                                    print(j2.salud)
                    
                    lista_colisiones=pygame.sprite.spritecollide(j2,jugadores,False)
                    for J2 in lista_colisiones:
                        if selectJugador2==30:
                            if j2.rect.left<=j.rect.right and j2.accion==0:
                                if j.salud>=0:
                                    j.salud+=-0.3
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==8:
                                if j.salud>=0:
                                    j.salud+=-0.5
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==2:
                                if j.salud>=0:
                                    j.salud+=-0.7
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==10:
                                if j.salud>=0:
                                    j.salud+=-0.4
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==3:
                                if j.salud>=0:
                                    j.salud+=-1
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==11:
                                if j.salud>=0:
                                    j.salud+=-0.4
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==7:
                                if j.salud>=0:
                                    j.salud+=-0.8
                                    print(j.salud)
                        else:
                            if j2.rect.left<=j.rect.right and j2.accion==1:
                                if j.salud>=0:
                                    j.salud+=-0.6
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==2:
                                if j.salud>=0:
                                    j.salud+=-0.7
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==4:
                                if j.salud>=0:
                                    j.salud+=-0.6
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==5:
                                if j.salud>=0 and j2.salud<=350:
                                    j2.salud+=0.1
                                    print(j.salud)
                            if j2.rect.left<=j.rect.right and j2.accion==6:
                                if j.salud>=0:
                                    j.salud+=-1
                                    print(j.salud)
                    
                else:
                    if Nivel==1:
                        BandNivel=2
                        Nivel=2
                        if j.salud>j2.salud:
                            ContVictoria1+=1
                        else:
                            ContVictoria2+=1
                    elif Nivel==2:
                        BandNivel=3
                        Nivel=3
                        if j.salud>j2.salud:
                            ContVictoria1+=1
                        else:
                            ContVictoria2+=1
                    elif Nivel==3:
                        BandNivel=100
                        Nivel=4
                        if j.salud>j2.salud:
                            ContVictoria1+=1
                        else:
                            ContVictoria2+=1         
            else:
                if Nivel==1:
                    BandNivel=2
                    Nivel=2
                    if j.salud>j2.salud:
                        ContVictoria1+=1
                    elif j2.salud>j.salud:
                        ContVictoria2+=1
                elif Nivel==2:
                    BandNivel=3
                    Nivel=3
                    if j.salud>j2.salud:
                        ContVictoria1+=1
                    elif j2.salud>j.salud:
                        ContVictoria2+=1
                elif Nivel==3:
                    BandNivel=100
                    Nivel=4
                    if j.salud>j2.salud:
                        ContVictoria1+=1
                    elif j2.salud>j.salud:
                        ContVictoria2+=1
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True           
##NIVEL 1------------------------------------------------------------------------------------------------------                     
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton1.rect):  
                    ##bandera para ir a seleccion de judores
                    BandNivel=5
                if cursor.colliderect(boton2.rect):
                    BandNivel=4
                if cursor.colliderect(boton3.rect):
                    BandNivel=6
                if cursor.colliderect(boton4.rect):
                    fin=True
                if cursor.colliderect(boton5.rect):
                    clock=pygame.time.Clock()
                    BandNivel=1
                    sonido1.play()
                if cursor.colliderect(boton6.rect):
                    if contInst==1:
                        BandNivel=7
                    if contInst==2:
                        BandNivel=8
                    if contInst==3:
                        BandNivel=9
                    if contInst==4:
                        BandNivel=0
                    if contHis==1:
                        BandNivel=10
                    if contHis==2:
                        BandNivel=11
                    if contHis==3:
                        BandNivel=0

            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    if BandNivel==50:
                        if selectJugador1==30:
                            j.accion=12
                            j.vel_x=5
                            j.vel_y=0
                        else:
                            j.accion=7
                            j.vel_x=5
                            j.vel_y=0                        
                if event.key==pygame.K_a:
                    if BandNivel==50:
                        if selectJugador1==30:
                            j.accion=11
                            j.vel_x=-5
                            j.vel_y=0
                        else:
                            j.accion=8
                            j.vel_x=-5
                            j.vel_y=0 
                if event.key==pygame.K_v:
                    if BandNivel==50:
                        puno.play()
                        if selectJugador1==30:
                            j.accion=0
                            j.con=0
                        else:
                            j.accion=2
                            j.con=0
                if event.key== pygame.K_b:
                    if BandNivel==50:
                        puno.play()
                        if selectJugador1==30:
                            j.accion=3
                            j.con=0
                        else:
                            j.accion=1
                            j.con=0
                if event.key==pygame.K_n:
                    if BandNivel==50:
                        if selectJugador1==30:
                            j.accion=6
                            j.con=0
                        else:
                            j.accion=12
                            j.con=0
                if event.key==pygame.K_m:
                    if BandNivel==50: 
                        if selectJugador1==30:
                            j.accion=8
                            j.con=0
                        else:
                            puno.play()
                            j.accion=3
                            j.con=0
                if event.key==pygame.K_g:
                    if BandNivel==50:
                        if selectJugador1==30:
                            j.accion=7
                            j.con=0
                        else:
                            puno.play()
                            j.accion=0
                            j.con=0
                if event.key==pygame.K_h:
                    if BandNivel==50:
                        if selectJugador1==31:
                            j.accion=10
                            j.con=0
                if event.key==pygame.K_j:
                    if BandNivel==50:
                        if selectJugador1==31:
                            j.accion=9
                            j.con=0
                if event.key==pygame.K_s:
                    if BandNivel==50:
                        if selectJugador1==30:
                            j.accion=5
                            j.con=0
                        else:
                            puno.play()
                            j.accion=11
                            j.con=0
                    if BandNivel==55:
                        imagen1=pygame.image.load('flashICON.png')
                        posIndicador1=(220,550)
                        selectJugador1=1
                if event.key == pygame.K_w:
                    if BandNivel==50:

                        if selectJugador1==30:
                            j.accion=2
                            j.con=0
                        if selectJugador1==31:
                            j.accion=6
                            j.con=0
                
                        if j.rect.right>p.rect.left and j.rect.left<p.rect.right:
                            ContSaltos+=1

                            j.rect.y += 10
                            plataforma_col = pygame.sprite.spritecollide(j, plataforma_lista, False)
                            j.rect.y -= 10

                            if len(plataforma_col) > 0:
                                ContSaltosFuera=0
                                ContSaltos=0
                            if ContSaltos<2:
                                puno.play()
                                if Nivel==3:
                                    j.vel_y=-16
                                else:
                                    j.vel_y=-12
                        elif (ContSaltosFuera<3 and j.rect.right<=p.rect.left)or (ContSaltosFuera<3 and j.rect.left > p.rect.right):
                            ContSaltosFuera+=1
                            j.vel_y=-15

                    if BandNivel==55:
                        selectJugador1=0
                        imagen1=pygame.image.load('VenomICON.png')
                        posIndicador1=(220,450)  
                if event.key==pygame.K_RIGHT:
                    if BandNivel==50:
                        if selectJugador2==30:
                            j2.accion=9
                            j2.vel_x=5
                            j2.vel_y=0
                        else:
                            j2.accion=8
                            j2.vel_x=5
                            j2.vel_y=0
                if event.key==pygame.K_LEFT:
                    if BandNivel==50:
                        if selectJugador2==30:
                            j2.accion=6
                            j2.vel_x=-5
                            j2.vel_y=0
                        else:
                            j2.accion=7
                            j2.vel_x=-5
                            j2.vel_y=0
                if event.key==pygame.K_1:
                    if BandNivel==50:
                        if selectJugador2==30:
                            puno.play()
                            j2.accion=11
                            j2.con=0
                        else:
                            j2.accion=6
                            j2.con=0
                if event.key==pygame.K_2:
                    if BandNivel==50:
                        puno.play()
                        if selectJugador2==30:
                            j2.accion=3
                            j2.con=0
                        else:
                            j2.accion=2
                            j2.con=0
                if event.key==pygame.K_3:
                    if BandNivel==50:
                        if selectJugador2==30:
                            puno.play()
                            j2.accion=10
                            j2.con=0
                        else:
                            j2.accion=5
                            j2.con=0
                if event.key==pygame.K_4:
                    if BandNivel==50:
                        if selectJugador2==30:
                            j2.accion=2
                            j2.con=0
                        else:
                            j2.accion=4
                            j2.con=0
                if event.key==pygame.K_5:
                    if BandNivel==50:
                        if selectJugador2==30:
                            puno.play()
                            j2.accion=0
                            j2.con=0
                if event.key==pygame.K_6:
                    if BandNivel==50:
                        if selectJugador2==30:
                            puno.play()
                            j2.accion=8
                            j2.con=0
                        
                if event.key == pygame.K_DOWN:
                    if BandNivel==50:
                        puno.play()
                        if selectJugador2==30:
                            j2.accion=7
                            j2.con=0   
                        else:
                            j2.accion=1
                            j2.con=0
                    if BandNivel==55:
                        selectJugador2=1
                        imagen=pygame.image.load('wolICON.png')
                        posIndicador2=(900,550)
                if event.key == pygame.K_UP:
                    if BandNivel==55:
                        selectJugador2=0
                        imagen=pygame.image.load('hulkICON.png')
                        posIndicador2=(900,450)
                    if BandNivel==50:  
                        if selectJugador2==30:
                            j2.accion=5
                            j2.con=0
                        if selectJugador2==31:
                            j2.accion=3
                            j2.con=0 
                        if j2.rect.right>p.rect.left and j2.rect.left<p.rect.right:
                            ContSaltos2+=1

                            j2.rect.y += 10
                            plataforma_col = pygame.sprite.spritecollide(j2, plataforma_lista, False)
                            j2.rect.y -= 10

                            if len(plataforma_col) > 0:
                                ContSaltosFuera2=0
                                ContSaltos2=0
                            if ContSaltos2<2:
                                puno.play()
                                if Nivel==3:
                                    j2.vel_y=-16
                                else:
                                    j2.vel_y=-12
                        elif (ContSaltosFuera2<3 and j2.rect.right<=p.rect.left)or (ContSaltosFuera2<3 and j2.rect.left > p.rect.right):
                            ContSaltosFuera+=1
                            j2.vel_y=-15 
                    
                    
            if event.type==pygame.KEYUP:
                if selectJugador1==30:
                    j.accion=1
                    j.vel_x=0
                    j.vel_y=0
                    j.con=0
                else:
                    j.accion=4
                    j.vel_x=0
                    j.vel_y=0
                    j.con=0
                if selectJugador2==30:
                    j2.accion=4
                    j2.vel_x=0
                    j2.vel_y=0
                    j2.con=0
                else:
                    j2.accion=0
                    j2.vel_x=0
                    j2.vel_y=0
                    j2.con=0
        
##-------------------------------------------------------------------------------------------------------------------------------
        if BandPantalla==5:        
            if Nivel==4:
                Pantalla.fill(Negro)
                if ContVictoria1>ContVictoria2:
                    if selectJugador1==30:
                        sound4.play()
                        Pantalla.blit(texto9,(370,150))
                        Pantalla.blit(texto3,(570,270))
                        Pantalla.blit(imagen1,[530,330])
                    else:
                        sound4.play()
                        Pantalla.blit(texto9,(370,150))
                        Pantalla.blit(texto4,(570,270))
                        Pantalla.blit(imagen1,[550,300])

                elif ContVictoria2>ContVictoria1 :
                    if selectJugador2==30:
                        sound4.play()
                        Pantalla.blit(texto9,(370,150))
                        Pantalla.blit(texto5,(570,270))
                        Pantalla.blit(imagen,[530,330])
                    else:
                        sound4.play()
                        Pantalla.blit(texto9,(370,150))
                        Pantalla.blit(texto6,(570,270))
                        Pantalla.blit(imagen,[530,330])
                else:
                    Pantalla.blit(texto11,(370,150))
            else:
                Pantalla.fill(Negro)
                Pantalla.blit(fondo,[450,0])
                Pantalla.blit(texto1,(100,100))
                Pantalla.blit(texto3,(70,450))
                Pantalla.blit(texto4,(70,550))
                Pantalla.blit(texto2,(900,100))
                Pantalla.blit(texto5,(950,450))
                Pantalla.blit(texto6,(950,550))
                Pantalla.blit(texto7,posIndicador1)
                Pantalla.blit(texto8,posIndicador2)
                Pantalla.blit(imagen1,[300,350])
                Pantalla.blit(imagen,[620,350])
                boton5.update(Pantalla,cursor)            
        if BandPantalla==1:
            Pantalla.blit(fondo,[0,0])
            pygame.draw.line(Pantalla,Naranja,[77,55],[77 + j.salud,55],30)
            pygame.draw.line(Pantalla,Naranja,[773,55],[773 + j2.salud,55],30)
            Pantalla.blit(salud1,[0,0])
            Pantalla.blit(salud2,[750,0])
             ##plataforma_lista.draw(Pantalla)
            jugadores.update(plataforma_lista)
            jugadores.draw(Pantalla)
            jugadores2.update(plataforma_lista)
            jugadores2.draw(Pantalla)
            
            if minutes==0 and seconds<= 5:
                Pantalla.blit(Round,[475,200])
            
            if milliseconds > 1000:
                seconds += 1
                milliseconds -= 1000
            if seconds > 60:
                minutes += 1
                seconds -= 60
            
            info= fuente.render("{}:{}".format(minutes, seconds),0,Blanco)
            Pantalla.blit(info,[580,50])
        

            ##print ("{}:{}".format(minutes, seconds))

            milliseconds += clock.tick_busy_loop(60)        
        if BandPantalla==2:
            Pantalla.blit(fondo,[0,0])
            if BandNivel==60:
                Pantalla.blit(texto10,(450,50))
            boton6.update(Pantalla,cursor)
        pygame.display.flip()
        cursor.update()
        Reloj.tick(20)                  