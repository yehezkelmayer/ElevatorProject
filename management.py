
from typing import Any
import pygame.mouse
import elevator
from globals import *

def get_quickest_elv(building, task_pos: tuple[int, int]) -> tuple[Any | None, float | Any]:
    """
    chooses the quickest elevator
    :param building: the building to be checked
    :param task_pos: y point that the elevator needs go there, int
    :return: the quickest elevator and the time to arrive to the task's y, (elevator, time) tuple
    """
    min_time = float("inf")
    quickest_elevator = None

    for elv in building.elevators:
        if elv.pos[1] == task_pos and elv.suspending_for_floor == 2:
            return elv, 0
        elif elv.pos[1] == task_pos:
            return None, None

        last_task_y = elv.get_last_elevator_y()
        current_task_time = elevator.get_current_task_time(task_pos, last_task_y)
        if elv.tasks_time + current_task_time < min_time:
            min_time = elv.tasks_time + current_task_time
            quickest_elevator = elv
    return quickest_elevator, min_time

def is_button_clicked(building, pos):
    """
    checks if a button was clicked
    :param building: the building to be checked
    :param pos: the mouse click position (x, y) tuple
    :return: None
    """
    is_button_pressed, floor = building.is_floors_button_clicked(pos)
    if is_button_pressed and not floor.is_elv_on_way:
        quickest_elevator, min_time = get_quickest_elv(building, floor.pos[1])
        if quickest_elevator:
            floor.floor_timer = min_time
            task_y = floor.pos[1]
            quickest_elevator.add_new_task(task_y)

def draw_global_reset_button(screen, screen_width: int) -> None:
    """
    draws the reset button
    :param screen: teh pygam surface to draw on it
    :param color: the button's color (int, int, int)
    :return: None
    """
    pos = get_global_reset_button_pos(screen_width)
    pygame.draw.circle(screen, GRAY_FOR_BUTTON_BORDER, pos, RESET_BUTTON_SIZE + 3)
    pygame.draw.circle(screen, LIGHT_BLUE, pos, RESET_BUTTON_SIZE)
    
    font = pygame.font.SysFont("arial", FONT_SIZE)
    text = font.render("reset", True, WHITE)
    screen.blit(text, (pos[0] - 24, pos[1] - 17))

def get_global_reset_button_pos(screen_width: int) -> tuple[int, int]:
    return screen_width - 50, 50  

def is_global_reset_clicked(click_pos: tuple[int, int], screen_width: int) -> bool:
    x, y = click_pos
    bx, by = get_global_reset_button_pos(screen_width)
    return ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 < RESET_BUTTON_SIZE

def reset_building(building) -> None:
    for elv in building.elevators:
        elv.pos = elv.pos[0], BASE_ELEVATOR_POS_Y
        elv.current_floor = 0
        elv.tasks = []
        elv.tasks_time = 0
        elv.suspending_for_floor = 2

    for floor in building.floors:
        floor.is_elv_on_way = False
        floor.floor_timer = 0

def reset_all_buildings(neighborhood) -> None:
    for building in neighborhood.buildings:
        reset_building(building)

def reset_mouse_over(pos: tuple[int, int]) -> bool:
    """
    checks if mouse over the reset button
    :param pos: the mouse over position (x, y) tuple
    :return: True or False
    """
    x, y = pos
    bx, by = RESET_BUTTON_POS
    if ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 <= RESET_BUTTON_SIZE:
        return True

def mouse_over(building, pos: tuple[int, int]) -> None:
    """
    checks if mouse over some floor's button or the reset button
    :param building: the building to be checked
    :param pos: the mouse over position (x, y) tuple
    :return: None
    """
    x, y = pos
    reset_button_y = y - (ENVIRONMENT_HEIGHT - SCREEN_HEIGHT)
    reset = reset_mouse_over((x, reset_button_y))
    button = None
    for floor in building.floors:
        if floor.button.is_mouse_over(pos) and floor.floor_timer == 0:
            button = True
    # change the cursor
    if reset or button:
        pygame.mouse.set_cursor(pygame.cursors.tri_left)
    else:
        pygame.mouse.set_cursor(pygame.cursors.arrow)
