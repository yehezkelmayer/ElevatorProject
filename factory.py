from neighborhood import INeighborhood, Neighborhood
from building import Building

class NeighborhoodFactory:
    """
    Factory class for creating Neighborhood instances.
    """
    @staticmethod
    def create_neighborhood(building_configs: list[tuple[int, int]]) -> INeighborhood:
        """
        Builds a Neighborhood from a list of building configurations.

        :param building_configs: list of tuples -> (floors, elevators) for each building
        :return: Neighborhood object
        """
        buildings = [
            Building(floors, elevators)
            for floors, elevators in building_configs
        ]
        return Neighborhood(buildings)
