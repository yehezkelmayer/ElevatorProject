from building import Building
from management import draw_global_reset_button, is_button_clicked, mouse_over
from globals import BUILDING_SPACING, BUILDING_AREA_WIDTH, ENVIRONMENT_HEIGHT
import pygame

class INeighborhood:
    def draw(self, surface, delta_time: float) -> None:
        raise NotImplementedError("This method should be overridden by subclasses.")

    def handle_click(self, pos: tuple[int, int]) -> None:
        raise NotImplementedError("This method should be overridden by subclasses.")

    def handle_mouse_over(self, pos: tuple[int, int]) -> None:
        raise NotImplementedError("This method should be overridden by subclasses.")

    def switch_building(self, new_index: int) -> None:
        raise NotImplementedError("This method should be overridden by subclasses.")

class Neighborhood:
    def __init__(self, buildings: list[Building]):
        self.buildings = buildings
        print(self.buildings)

    def draw(self, surface, delta_time: float) -> None:
        for idx, building in enumerate(self.buildings):
            sub = pygame.Surface((BUILDING_AREA_WIDTH, ENVIRONMENT_HEIGHT), pygame.SRCALPHA)
            sub.fill((0, 0, 0, 0))
            building.draw(sub, delta_time)
            x_off = BUILDING_SPACING + idx * (BUILDING_AREA_WIDTH + BUILDING_SPACING)
            surface.blit(sub, (x_off, 0))

    def draw_reset_button(self, screen, surface) -> None:
        width, _ = surface.get_size()
        draw_global_reset_button(screen, width)        

    def handle_click(self, pos: tuple[int, int]) -> None:
        x, y = pos
        for idx, building in enumerate(self.buildings):
            x_start = BUILDING_SPACING + idx * (BUILDING_AREA_WIDTH + BUILDING_SPACING)
            x_end = x_start + BUILDING_AREA_WIDTH
            if x_start <= x <= x_end:
                relative_pos = (x - x_start, y)
                is_button_clicked(building, relative_pos)

    def handle_mouse_over(self, pos: tuple[int, int]) -> None:
        x, y = pos
        for idx, building in enumerate(self.buildings):
            x_start = BUILDING_SPACING + idx * (BUILDING_AREA_WIDTH + BUILDING_SPACING)
            x_end = x_start + BUILDING_AREA_WIDTH
            if x_start <= x <= x_end:
                relative_pos = (x - x_start, y)
                mouse_over(building, relative_pos)


