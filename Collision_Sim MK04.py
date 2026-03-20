#
# Created by lftgr on 19/03/2026
#

import sys
import pygame


width, height = 800, 400
background_Color = (30, 30, 30)
obj1_Color = (255, 100, 100) # Vermelho
obj2_Color = (100, 100, 255) # Azul


class Ball: #Defining what a ball is and what it does
    def __init__(self, x, y, vel_x, color, radius=20, mass=1.0):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.color = color
        self.radius = radius
        self.mass = mass

    def move(self):
        self.x += self.vel_x

        #"If" to check if it hits the border
        if self.x-self.radius < 0 or self.x+self.radius > width:
            self.vel_x *= -1 #Changes direction

    def draw(self, screen): #Instructions on how the ball should be displayed
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def collision(self, other_Ball): #Collision logic
        distance = abs(self.x - other_Ball.x)
        sum_Radius = self.radius + other_Ball.radius

        if distance <= sum_Radius:

            m1 = self.mass #Transforming data for better understanding
            m2 = other_Ball.mass
            v1 = self.vel_x
            v2 = other_Ball.vel_x

            new_v1 = ((m1-m2)*v1 + 2*m2*v2) / (m1+m2) #Elastic collision formula
            new_v2 = ((m2-m1)*v2 + 2*m1*v1) / (m2+m1)

            self.vel_x = new_v1
            other_Ball.vel_x = new_v2


def req_value(message, default_Value): #Requests a value. If user doesn't provide a value: value = default_Value
    try:
        entry = input(f"{message} [Default: {default_Value}]: ")
        if entry.strip() == "":
            return float(default_Value)
        return float(entry)
    except ValueError:
        print(f"Wrong entry format. Using default value: {default_Value}")
        return float(default_Value)



def game(m1, v1, m2, v2, radius1, radius2):
    pygame.init() #Sart pygame
    font = pygame.font.SysFont(None, 30) #Regular font, sized 30
    screen = pygame.display.set_mode((width, height)) #Set screen size
    pygame.display.set_caption("Collision Simulation")
    clock = pygame.time.Clock() #FPS must be set so the game doesn't run on thr processor's full capacity

    ball1 = Ball(100, height // 2, v1, obj1_Color, radius1, mass=m1)
    ball2 = Ball(700, height // 2, -v2, obj2_Color, radius2, mass=m2)

    on = True
    while on: #Defining when window should close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

        ball1.move()
        ball2.move()

        ball1.collision(ball2)

        screen.fill(background_Color)
        ball1.draw(screen)
        ball2.draw(screen)

        text_v1 = font.render(f"Red Ball Velocity: {ball1.vel_x:.2f}m/s", True, obj1_Color) #Defining what should be printed
        text_v2 = font.render(f"Blue ball Velocity: {ball2.vel_x:.2f}m/s", True, obj2_Color)

        text_m1 = font.render(f"Red Ball Mass: {ball1.mass:.2f}kg", True, obj1_Color)
        text_m2 = font.render(f"Blue ball Mass: {ball2.mass:.2f}kg", True, obj2_Color)

        screen.blit(text_v1, (20, 20))
        screen.blit(text_v2, (width - 275, 20))

        screen.blit(text_m1, (20, 40))
        screen.blit(text_m2, (width - 275, 40))

        pygame.display.flip()
        clock.tick(60) #Set FPS to 60

    pygame.quit()
    print("Simulation Closed")
    sys.exit()


def main():

    print("\n\n============================= Sim. Settings =============================") #Settings must first be set by user
    print("              Press Enter if you wish to use default values. \n")

    m1 = req_value("Red ball mass(kg)", 1.0) #Request the mass of ball1
    v1 = req_value("Red ball speed(m/s)", 5.0) #Request the velocity of ball1

    print(f"\n", "-"*30, "\n")

    m2 = req_value("Blue ball mass(kg)", 1.0)  # Request the mass of ball2
    v2 = req_value("Blue ball speed(m/s)", 5.0)  # Request the velocity of ball2

    print("\nStarting Simulation...\n")

    radius1_Calc = int(20 * (m1 ** 0.5))
    radius2_Calc = int(20 * (m2 ** 0.5))

    radius1 = min(100, max(10, radius1_Calc))
    radius2 = min(100, max(10, radius2_Calc))

    game(m1, v1, m2, v2, radius1, radius2)



main()