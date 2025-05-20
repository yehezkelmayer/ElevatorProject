import pygame
from globals import *
from factory import NeighborhoodFactory
from management import is_global_reset_clicked, reset_all_buildings

neighborhood = NeighborhoodFactory.create_neighborhood(BUILDING_CONFIGS)

pygame.init()
pygame.mixer.music.load(DING_FILE_PATH)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("elevators system")
surface = pygame.Surface((ENVIRONMENT_WIDTH, ENVIRONMENT_HEIGHT))

scroll_speed = 30
scroll_y = ENVIRONMENT_HEIGHT - SCREEN_HEIGHT

run = True
for idx, building in enumerate(neighborhood.buildings):
    if len(building.elevators) <= 0:
        print(f"Building {idx + 1}: No elevators, use the stairs.")
        run = False
    elif len(building.floors) <= len(building.elevators):
        print(f"Building {idx + 1}: Number of floors must be greater than elevators.")
        run = False

previous_time = pygame.time.get_ticks()

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                environment_y = y + scroll_y
                neighborhood.handle_click((x, environment_y))
                if is_global_reset_clicked(event.pos, SCREEN_WIDTH):
                    reset_all_buildings(neighborhood)
            elif event.button == 4:
                scroll_y = max(0, scroll_y - scroll_speed)
            elif event.button == 5:
                scroll_y = min(scroll_y + scroll_speed, ENVIRONMENT_HEIGHT - SCREEN_HEIGHT)

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - previous_time) / 1000
    previous_time = current_time

    surface.fill(GREEN)
    neighborhood.draw(surface, delta_time)
    screen.blit(surface, (0, 0), (0, scroll_y, SCREEN_WIDTH, SCREEN_HEIGHT))

    neighborhood.draw_reset_button(screen, surface)

    x, y = pygame.mouse.get_pos()
    y += scroll_y
    neighborhood.handle_mouse_over((x, y))

    pygame.display.flip()

pygame.quit()
