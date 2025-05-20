from globals import *
import pygame

class Button:
    def __init__(self, floor_num: int, x_offset: int = 0):
        self.floor_num = floor_num
        self.pos = (x_offset + BASE_BUTTON_POS_X, BASE_BUTTON_POS_Y - (FLOOR_HEIGHT * self.floor_num))
        self.mouse_over = None

    def draw(self, surface, color: tuple[int, int, int]) -> None:
        pygame.draw.circle(surface, color, self.pos, BUTTON_SIZE)
        pygame.draw.circle(surface, GRAY_FOR_BUTTON_BORDER, self.pos, BUTTON_SIZE, width=2)
        font = pygame.font.SysFont("floor number", FONT_SIZE, True, False)
        text = font.render(str(self.floor_num), False, WHITE)
        rect = text.get_rect(center=self.pos)
        surface.blit(text, rect)

    def onclick(self, click_pos: tuple[int, int]) -> bool:
        x, y = click_pos
        bx, by = self.pos
        return ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 <= BUTTON_SIZE

    def is_mouse_over(self, pos: tuple[int, int]) -> bool:
        x, y = pos
        bx, by = self.pos
        self.mouse_over = ((x - bx) ** 2 + (y - by) ** 2) ** 0.5 <= BUTTON_SIZE
        return self.mouse_over
