# TO ME TO UTILS

# FORMATTING
# One blank line at a time within each section
# Two blank lines seperate unrelated sections (eg: each function)
# No blank line after comments

# IMPORTS
import csv
import pygame
import math

# PYGAME INIT
pygame.init()


# VARIABLES
#done = False
# RGB flatuicolors.com
RED   = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE     = (  0,  0,255)
WHITE   = (255,255,255)
BLACK   = (  0,  0,  0)

L_TURQ   = (26, 188, 156)
D_TURQ   = (22, 160, 133)

L_GREEN  = ( 46, 204,113)
D_GREEN  = ( 39, 174, 96)

L_BLUE   = (52, 152, 219)
D_BLUE   = (41, 128, 185)

L_PURPLE = (155, 89, 182)
D_PURPLE = (142, 68, 173)

YELLOW   = (241, 196, 15)
O_YELLOW = (243, 156, 18)

ORANGE   = (230, 126, 34)
D_ORANGE = (211, 84,  0)

RED   = (231, 76, 60)
D_RED   = (192, 57, 43)

GREY_1   = (236, 240, 241)
GREY_2   = (189, 195, 199)
GREY_3   = (149, 165, 166)
GREY_4   = (127, 140, 141)

D_B_GREY = (52, 73, 94)
L_B_GREY = (44, 62, 80)

SKIN     = (255,223,196)

screenx, screeny, size, done = 700, 500, (700, 500), False
font = pygame.font.SysFont("roboto",25,True,False)

# FUNCTIONS
def factorial(i):
    total = i
    while i > 1:
        i -= 1
        total *= i
    return total
    

def setup_pygame(screensize=size,givencaption="Caption required."):
    lsize = screensize
    caption = givencaption
    screen = pygame.display.set_mode(lsize)
    pygame.display.set_caption(caption)
    clock = pygame.time.Clock()
    return [screen,clock]
    

def draw_gnome(x,y,screen,hatcol):
    #BODY
    pygame.draw.polygon(screen, hatcol, [(x+25,y),(x,y+33),(x+50,y+33)])
    pygame.draw.rect(screen, L_BLUE, (x,y+34,50,66))
    pygame.draw.rect(screen, SKIN, (x,y+34,50,25))
    #BEARD
    pygame.draw.rect(screen, WHITE, (x,y+41,10,20))
    pygame.draw.rect(screen, WHITE, (x+40,y+41,10,20))
    pygame.draw.rect(screen, WHITE, (x+5,y+59,40,10))
    pygame.draw.rect(screen,WHITE, (x+15,y+49,20,15),5)
    #EYES
    pygame.draw.rect(screen,BLACK, (x+15,y+39,5,5))
    pygame.draw.rect(screen,BLACK, (x+30,y+39,5,5))
    

def flip():
    pygame.display.flip()


def draw_tick(x,y,width,tickcol):
    pygame.draw.rect(screen, BLACK, (x,y,width,width),5)
    start_x = x+(width/2)
    start_y = y+((width/2)*1.25)
    unit = round(width/25)
    if unit == 0:
        unit = 1
    pygame.draw.polygon(screen, GREEN, ((start_x,start_y),(start_x+ unit*19,start_y+unit*-21),(start_x,start_y+unit*-5),(start_x+unit*-5,start_y+unit*-10)))


# Bailey's text input
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
length_limit = 20

def get_text(my_string,event):
    if len(my_string) <= length_limit:
        # Letters
        if 97 <= event.key <= 122:
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                my_string += alphabet[event.key - 97].upper()
            else:
                my_string += alphabet[event.key - 97]
        # Space
        elif event.key == 32:
            my_string += " "
        # Backspace
        elif event.key == 8:
            my_string = my_string[:-1]
    return my_string


# CLASSES
#"Let's make some sliders bitchezzzzzz"~Kai 2k17
class Slider():
    def __init__(self,x,y,height,slider_type,col,radius,screen):
        self.start_coords = [x,y]
        self.x_pos = x
        self.y_pos = y
        self.height = height
        self.type = slider_type
        self.colour = col
        self.radius = radius
        self.screen = screen
        self.held = False
        if self.type == "rectangle":
            self.x_length = self.radius*2
            self.y_length = int(self.x_length*0.4)
        elif self.type == "square":
            self.x_length = self.radius*2
            self.y_length = self.x_length
        elif self.type == "circle":
            self.x_length = self.radius*2
            self.y_length = self.radius*2
            self.origin = [self.x_pos+self.radius,self.y_pos]
    def detect(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.current_pos = pygame.mouse.get_pos()
            if self.type == "circle" and (self.current_pos[0] - self.origin[0])**2 + (self.current_pos[1] - self.origin[1])**2 < self.radius**2:
                self.held = True
            elif self.type != "circle" and self.current_pos[0] >= self.x_pos and self.current_pos[0] <= self.x_pos+self.x_length and self.current_pos[1] >= self.y_pos and self.current_pos[1] <= self.y_pos + self.y_length:
                self.held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.held = False
    def draw(self, text=False,lfont=font):
        pygame.draw.line(self.screen, (0, 0, 0), (self.start_coords[0]+self.radius,self.start_coords[1]), (self.start_coords[0]+self.radius,self.start_coords[1]+self.height), 5)
        if self.held:
            self.current_pos = pygame.mouse.get_pos()
            self.y_pos = self.current_pos[1]
            if self.y_pos > self.start_coords[1] + self.height:
                self.y_pos = self.start_coords[1] + self.height
            if self.y_pos < self.start_coords[1]:
                self.y_pos = self.start_coords[1]
        if self.type == "circle":
            pygame.draw.circle(self.screen, self.colour, (self.x_pos+self.radius,self.y_pos), self.radius)
            self.origin = [self.x_pos+self.radius,self.y_pos]
        if self.type == "rectangle" or self.type == "square":
            pygame.draw.rect(self.screen, self.colour, (self.x_pos,self.y_pos-(self.y_length//2),self.x_length,self.y_length))
        if text:
            self.number = lfont.render(str(self.return_percent_value()),1,(0,0,0))
            self.screen.blit(self.number,(self.start_coords[0],self.start_coords[1]+self.height))
    def return_absolute_value(self):
        return self.y_pos
    def return_percent_value(self):
        self.value = (self.start_coords[1] + self.height) - self.y_pos
        self.value = int((self.value / self.height) * 100)
        return self.value


class Toggle_button():
    def __init__(self, x, y, radius, button_type, screen, start_position, on, off):
        self.x_pos,self.y_pos, self.radius, self.type, self.on, self.off = x, y, radius, button_type, on ,off
        if start_position == True:
            self.colour = on
            self.boolean = True
        else:
            self.colour = off
            self.boolean = False
        self.screen = screen
        if self.type == "circle":
            self.diameter = self.radius*2
            self.midpoint = [self.x_pos,self.y_pos]
        if self.type == "square":
            self.height = self.radius*2
            self.midpoint = [self.x_pos+self.radius,self.y_pos+self.radius]
        if self.type == "rectangle":
            self.width = self.radius*2
            self.height = self.width*0.4
            self.midpoint = [self.x_pos+self.radius, self.y_pos+int(self.height/2)]
    def draw(self):
        if self.boolean == True:
            self.colour = self.on
        else:
            self.colour = self.off
        if self.type == "circle":
            pygame.draw.circle(self.screen,(0,0,0),(self.x_pos,self.y_pos),self.radius)
            pygame.draw.circle(self.screen,self.colour,(self.x_pos,self.y_pos),self.radius-3)
        if self.type == "square":
            pygame.draw.rect(self.screen,self.colour,(self.x_pos, self.y_pos,self.height,self.height))
            pygame.draw.rect(self.screen,(0,0,0),(self.x_pos, self.y_pos,self.height,self.height),3)
        if self.type == "rectangle":
            pygame.draw.rect(self.screen,self.colour,(self.x_pos,self.y_pos,self.width,self.height))
            pygame.draw.rect(self.screen,(0,0,0),(self.x_pos,self.y_pos,self.width,self.height),3)
    def detect(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                if self.type == "circle":
                    if (self.pos[0] - self.midpoint[0])**2 + (self.pos[1] - self.midpoint[1])**2 < self.radius**2:
                        self.boolean = not self.boolean
                if self.type == "square":
                    if self.pos[0] >= self.x_pos and self.pos[0] <= self.x_pos + self.height and self.pos[1] >= self.y_pos and self.pos[1] <= self.y_pos + self.height:
                        self.boolean = not self.boolean
                if self.type == "rectangle":
                    if self.pos[0] >= self.x_pos and self.pos[0] <= self.x_pos + self.width and self.pos[1] >= self.y_pos and self.pos[1] <= self.y_pos + self.height:
                        self.boolean = not self.boolean


class Tickbox():
    def __init__(self, x, y, width, bgcol, tickcol, start_set, screen):
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.bgcolour = bgcol
        self.tickcol = tickcol
        self.boolean = start_set
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.bgcolour, (self.x_pos,self.y_pos,self.width,self.width))
        pygame.draw.rect(self.screen, (0,0,0), (self.x_pos,self.y_pos,self.width,self.width),3)
        if self.boolean == True:
            self.start_x = self.x_pos+(self.width/2)
            self.start_y = self.y_pos+((self.width/2)*1.25)
            self.unit = round(self.width/25)
            if self.unit == 0:
                self.unit = 1
            pygame.draw.polygon(self.screen, self.tickcol, ((self.start_x,self.start_y),(self.start_x+ self.unit*19,self.start_y+self.unit*-21),(self.start_x,self.start_y+self.unit*-5),(self.start_x+self.unit*-5,self.start_y+self.unit*-10)))
            pygame.draw.polygon(self.screen, (0,0,0), ((self.start_x,self.start_y),(self.start_x+ self.unit*19,self.start_y+self.unit*-21),(self.start_x,self.start_y+self.unit*-5),(self.start_x+self.unit*-5,self.start_y+self.unit*-10)),2)

    def detect(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pos = pygame.mouse.get_pos()
            if self.pos[0] >= self.x_pos and self.pos[0] <= self.x_pos + self.width and self.pos[1] >= self.y_pos and self.pos[1] <= self.y_pos + self.width:
                self.boolean = not self.boolean


class Open_CSV():
    def __init__(self, filename, col=0, row=0):
        self.filename = filename
        self.x_pos = col
        self.y_pos = row
        self.file = open(self.filename,"r+")
        self.reader = csv.reader(self.file)
        self.rows = []
        for row in self.reader:
            self.rows.append(row)
    def read(self, row = -1, col = -1):
        if row < 0 or row >= len(self.rows):
            return self.rows
        elif col >= len(self.rows[row]) or col < 0:
            return self.rows[row]
        else:
            self.temp = self.rows[row]
            return self.temp[col]


class Toggle_button2():
    def __init__(self, x, y, radius, screen, off, correctcol, wrongcol):
        self.x_pos = x
        self.y_pos = y
        self.radius = radius
        self.off = off
        self.correctcol = correctcol
        self.wrongcol = wrongcol
        self.colour = self.off
        self.guess = 0
        self.screen = screen
        self.width = self.radius*2
        self.height = self.width*0.4
        self.midpoint = [self.x_pos+self.radius, self.y_pos+int(self.height/2)]
        self.click = False
    def draw(self, click=False):
        self.click = click
        if self.guess == 0:
            self.colour = self.off
        if self.guess == 1:
            self.colour = self.correctcol
        elif self.guess == 2:
            self.colour = self.wrongcol
        pygame.draw.rect(self.screen,self.colour,(self.x_pos,self.y_pos,self.width,self.height))
        pygame.draw.rect(self.screen,(0,0,0),(self.x_pos,self.y_pos,self.width,self.height),3)
    def detect(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.pos = pygame.mouse.get_pos()
            if self.pos[0] >= self.x_pos and self.pos[0] <= self.x_pos + self.width and self.pos[1] >= self.y_pos and self.pos[1] <= self.y_pos + self.height:
                self.click = True
            return(self.click)


class Key_detect():
    def __init__(self,screen,font=font,col=(0,0,0),text=""):
        self.starttext = text
        self.input_string = ""
        self.screen, self.clock, self.font = screen, pygame.time.Clock(),font
        self.col = col
    def draw(self):
        self.screen.fill(GREY_1)
        self.text = self.font.render(self.starttext+self.input_string,True,self.col)
        self.screen.blit(self.text,[0,0])
    def run(self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if 97 <= event.key <= 122:
                        self.mod = pygame.key.get_mods()
                        if self.mod == 1 or self.mod == 2:
                            self.input_string += alphabet[event.key - 97].upper()
                            self.mod = 0
                        else:
                            self.input_string += alphabet[event.key - 97]
                    elif event.key == 32:
                        self.input_string += " "
                    elif event.key == 8:
                        self.input_string = self.input_string[:-1]
                    elif event.key == 13:
                        self.done = True
                        return self.input_string

            self.draw()
            flip()
            self.clock.tick(60)


#I'm not a gnelf!
class Gnome():
    def __init__(self,x,y,screen,hatcol,scale=1,hasbeard=True,skin=SKIN):
        self.x, self.y, self.screen, self.hatcol, self.scale, self.hasbeard,self.skin = x, y, screen, hatcol, scale, hasbeard, skin
        self.width, self.height, self.body = 50*self.scale, 100*self.scale, L_BLUE
    def draw(self):
        #BODY
        pygame.draw.polygon(self.screen, self.hatcol, [(self.x+(int(25*self.scale)),self.y),(self.x,self.y+(int(self.scale*33))),(self.x+(int(self.scale*50)),self.y+(int(self.scale*33)))])
        pygame.draw.rect(self.screen, self.body, (self.x,self.y+(int(self.scale*33)),int(self.scale*50),int(self.scale*66)))
        pygame.draw.rect(self.screen, self.skin, (self.x,self.y+(int(self.scale*33)),int(self.scale*50),int(self.scale*25)))
        #BEARD
        if self.hasbeard:
            pygame.draw.rect(self.screen, WHITE, (self.x,self.y+(int(self.scale*41)),int(self.scale*10),int(self.scale*20)))
            pygame.draw.rect(self.screen, WHITE, (self.x+(int(self.scale*40)),self.y+(int(self.scale*41)),int(self.scale*10),int(self.scale*20)))
            pygame.draw.rect(self.screen, WHITE, (self.x+(int(self.scale*5)),self.y+(int(self.scale*57)),int(self.scale*40),int(self.scale*10)))
            pygame.draw.rect(self.screen,WHITE, (self.x+(int(self.scale*15)),self.y+(int(self.scale*49)),int(self.scale*20),int(self.scale*15)),int(self.scale*5))
        #EYES
        pygame.draw.rect(self.screen,BLACK, (self.x+(int(self.scale*15)),self.y+(int(self.scale*39)),int(self.scale*5),int(self.scale*5)))
        pygame.draw.rect(self.screen,BLACK, (self.x+(int(self.scale*30)),self.y+(int(self.scale*39)),int(self.scale*5),int(self.scale*5)))

#I'm gonna smurf you right in the smurf! You smurfin' smurf!
class Smurf(Gnome):
    def __init__(self,x,y,screen,scale=1,hasbeard=False):
        super().__init__(x,y,screen,WHITE,scale,hasbeard,L_BLUE)
        self.body, self.hasbeard = WHITE, hasbeard
    def draw(self):
        super().draw()
        if not self.hasbeard:
            pygame.draw.rect(self.screen,BLACK, (self.x+(int(self.scale*15)),self.y+(int(self.scale*49)),int(self.scale*20),int(self.scale*5)))
        else:
            self.hatcol, self.body = RED, RED

class Dragable():
    def __init__(self,x=0,y=0,xlen=10,ylen=10,iscircle=False):
        self.x, self.y, self.width, self.height, self.toggle, self.iscircle = x, y, xlen, ylen, False, iscircle
        self.x_offset, self.y_offset = self.width//2, self.height//2
    def detect(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.check():
            self.toggle = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.toggle = False
    def set_offsets(self,x,y):
        self.x_offset = x
        self.y_offset = y
    def logic(self):
        self.m_pos = pygame.mouse.get_pos()
        if self.toggle:
            self.x = self.m_pos[0] - self.x_offset
            self.y = self.m_pos[1] - self.y_offset
    def check(self):
        if self.iscircle == False:
            if self.m_pos[0] > self.x and self.m_pos[0] < self.x+self.width and self.m_pos[1] > self.y and self.m_pos[1] < self.y+self.height:
                return True
            else:
                return False
        else:
            self.origin = [self.x+self.x_offset,self.y+self.y_offset]
            if (self.m_pos[0]-self.origin[0])**2 + (self.m_pos[1]-self.origin[1])**2 < (self.width//2)**2:
                return True
            else:
                return False


class Toggle_switch():
    def __init__(self, lcl_coords, lcl_dimentions, lcl_colours,lcl_speed=1):
        # Set argument variables
        self.x,       self.y       = lcl_coords[0],     lcl_coords[1]
        self.width,   self.height  = lcl_dimentions[0], lcl_dimentions[1]
        self.colours, self.speed    = lcl_colours,       lcl_speed
        
        # Set hard variables
        self.tab_width             = self.width * 0.5
        self.position              = 0
        self.tab_info              = [self.x, self.y,self.tab_width,self.height]

        self.on_col = self.colours[0]
        self.off_col = self.colours[1]

        self.r, self.b, self.g = 0, 0, 0
        self.i = 0
        
    def draw(self):
        # Fill background
        pygame.draw.rect(screen, GREY_3, (self.x, self.y, self.width, self.height))

        # Animation
        if type(self.speed) == float or type(self.speed) == int:
            for i in range(self.speed):
                self.__tab_x_should = self.x+(self.position*(self.width-self.tab_width))
                if self.tab_info[0] != self.__tab_x_should:
                    self.tab_info[0] += (self.__tab_x_should - self.tab_info[0]) / abs(self.__tab_x_should - self.tab_info[0])
        else:
            self.__tab_x_should = self.x+(self.position*(self.width-self.tab_width))
            if self.tab_info[0] != self.__tab_x_should:
                self.tab_info[0] = self.__tab_x_should
                    
        

        # Draw tab and outline
        self.__draw_tab(self.tab_info,self.colours[self.position])
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height),3)

    def __draw_tab(self, lcl_info, lcl_colour):
        # Set colour
        col = (self.r, self.g, self.b)

        # Difference in on/off colours
        d_r = self.off_col[0] - self.on_col[0]
        d_g = self.off_col[1] - self.on_col[1]
        d_b = self.off_col[2] - self.on_col[2]

        # Slider position -> %
        value = self.width - (self.tab_info[0] - self.x)
        value = value / 100
        value = (value - 0.5) * 4
        value = 1 + value
        percentage = value

        # Change colour components
        self.r = self.on_col[0] + (d_r * percentage)
        self.g = self.on_col[1] + (d_g * percentage)
        self.b = self.on_col[2] + (d_b * percentage)
                
        # Draw background, then outline
        pygame.draw.rect(screen, col, (lcl_info[0],lcl_info[1],lcl_info[2],lcl_info[3]))
        pygame.draw.rect(screen, BLACK, (lcl_info[0],lcl_info[1],lcl_info[2],lcl_info[3]),3)

    def detect(self, lcl_event):
        if lcl_event.type == pygame.MOUSEBUTTONDOWN:
            self.m_pos = pygame.mouse.get_pos()
            if self.x <= self.m_pos[0] <= (self.x+self.width):
                if self.y <= self.m_pos[1] <= (self.y+self.height):
                    # If clicked, switch position
                    if self.position == 1:
                        self.position = 0
                    else:
                        self.position = 1

    def return_value(self):
        # If the tab is on the right, return true
        if self.position == 1:
            return True
        else:
            return False


class Drop_down():
    def __init__(self, lcl_coords, lcl_dimentions,lcl_options):
        # Define argument variables     
        self.x,       self.y        = lcl_coords[0],     lcl_coords[1]
        self.width,   self.height   = lcl_dimentions[0], lcl_dimentions[1]
        self.options, self.selected = lcl_options,       lcl_options[0]

        # Define hard variables
        self.active                 = False

    """ < Detection block > """
    def detect(self, lcl_event):
        # Check if the mouse has been pressed
        if lcl_event.type == pygame.MOUSEBUTTONDOWN:

            # Set m_pos for future use
            self.m_pos = pygame.mouse.get_pos()

            # Run appropriate function
            if self.active:
                self.detect_whenActive()
            else:
                self.detect_whenNotActive()

    def detect_whenActive(self):
        # Check if the mouse is clicked inside one of the boxes
        if self.x <= self.m_pos[0] <= (self.x + self.width):
            if self.y <= self.m_pos[1] <= (self.y + (self.height*len(self.options))):

                # cannot use m_pos as it's a tuple, so need to use new variable
                self.clicked_y = self.m_pos[1]
                self.clicked_y = self.clicked_y - self.y

                # floor divide by height of single box to see which was clicked
                self.clicked_y = self.clicked_y // self.height

                # Set selected value, and set active to False
                self.selected = self.options[self.clicked_y]
        self.active = False

    def detect_whenNotActive(self):
        # Check if the mouse is clicked inside the box
        if self.x <= self.m_pos[0] <= (self.x + self.width):
            if self.y <= self.m_pos[1] <= (self.y + self.height):

                # Set active to True
                self.active = True
    """ </ Detection block > """

    """ < Drawing block > """
    def draw(self):
        # Run appropiate drawing function
        if self.active:
            self.draw_whenActive()
        else:
            self.draw_whenNotActive()

    def draw_whenActive(self):
        # Change how the list is displayed
        self.new_options = self.options
        self.new_options.insert(0, self.new_options.pop(self.new_options.index(self.selected)))

        # Draw each item in the list
        for i in range(len(self.new_options)):
            pygame.draw.rect(screen, BLACK, (self.x,self.y+(self.height*i),self.width, self.height),3)
            self.text = font.render(self.new_options[i], True, BLACK)
            screen.blit(self.text,[self.x + 3, ((self.y + (self.height*i)) + self.height) - (self.text.get_height() + 2)])

    def draw_whenNotActive(self):
        # Draw a box with the selected option displayed
        pygame.draw.rect(screen, BLACK,(self.x, self.y, self.width, self.height),3)
        self.text = font.render(self.selected, True, BLACK)
        screen.blit(self.text,[self.x + 3, (self.y + self.height) - (self.text.get_height() + 2)])
    """ </ Drawing block > """