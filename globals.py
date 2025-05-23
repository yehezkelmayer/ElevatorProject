
import pygame


BUILDING_CONFIGS = [
    (14, 1),
    (7, 2),
    (8, 3)      
]

MAX_FLOORS = max(BUILDING_CONFIGS)[0]

MAX_ELEVATOR = max(BUILDING_CONFIGS, key=lambda x: x[1])[1]

# general
ELEVATOR_VELOCITY = 160 

ELV_ING_PATH = "pic/elv.png"  
ACTIVE_ELV_ING_PATH = "pic/active_elv.png"  
FLOOR_IMG_PATH = "pic/floor.jpg"  
DING_FILE_PATH = "sound/ding.mp3"

# sizes
ELEVATOR_WIDTH, ELEVATOR_HEIGHT = 65, 70
FLOOR_WIDTH, FLOOR_HEIGHT = 150, 80
FLOOR_SPACER_HEIGHT = 7
TIMER_WIDTH, TIMER_HEIGHT = 90, 40
BUTTON_SIZE = 20
RESET_BUTTON_SIZE = 30
FONT_SIZE = 22
MARGIN = 8
SCREEN_HEIGHT = (650)
ENVIRONMENT_HEIGHT = max(800, MAX_FLOORS  * (FLOOR_HEIGHT +  MARGIN))

NUMBER_OF_BUILDINGS = len(BUILDING_CONFIGS)
# spacing between buildings
BUILDING_SPACING = 50  
# width of one building area: floors + elevator shaft
BUILDING_AREA_WIDTH = FLOOR_WIDTH + (ELEVATOR_WIDTH * MAX_ELEVATOR) 
# override environment width to fit all buildings
ENVIRONMENT_WIDTH = (
    NUMBER_OF_BUILDINGS * BUILDING_AREA_WIDTH
    + (NUMBER_OF_BUILDINGS  + 1) * BUILDING_SPACING
)
SCREEN_WIDTH = max(500, ENVIRONMENT_WIDTH)  # if you scroll horizontally

# positions
GROUND_FLOOR_POS_X, GROUND_FLOOR_POS_Y = (MARGIN, ENVIRONMENT_HEIGHT - FLOOR_HEIGHT - MARGIN)
BASE_BUTTON_POS_X, BASE_BUTTON_POS_Y = (MARGIN + FLOOR_WIDTH // 2, ENVIRONMENT_HEIGHT - FLOOR_HEIGHT // 2 - MARGIN)
TIMER_POS_ON_FLOOR_X, TIMER_POS_ON_FLOOR_Y = 15, 32
BASE_ELEVATOR_POS_X, BASE_ELEVATOR_POS_Y = (MARGIN + FLOOR_WIDTH, GROUND_FLOOR_POS_Y)
RESET_BUTTON_POS = (SCREEN_WIDTH - 40, 40)

# colors
WHITE = 230, 230, 230
GRAY = 100, 100, 100
GRAY_FOR_OVER = 120, 120, 120
GRAY_FOR_BUTTON_BORDER = 180, 180, 180
BLACK = 0, 0, 0
RED = 255, 20, 20
GREEN = (100, 200, 200)
LIGHT_BLUE = (100, 170, 255)
LIGHT_BLUE = (100, 170, 255)




