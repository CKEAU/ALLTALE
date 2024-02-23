#浞河智慧仿生系统
'''
The Space's structure
'''

'''植物体仿生(地球)'''
class PlantCell:
    def __init__(self):
        self.core = PlantCore()
        self.energy_level = 0
        self.photosynthesis_rate = 0

    def perform_photosynthesis(self, light_intensity):
        self.photosynthesis_rate = light_intensity * 0.1  # 简化假设光合作用速率与光照强度成正比
        self.energy_level += self.photosynthesis_rate
        print(f"Photosynthesis rate: {self.photosynthesis_rate}, Energy level increased to: {self.energy_level}")

    def consume_energy(self, energy_usage):
        if self.energy_level >= energy_usage:
            self.energy_level -= energy_usage
            print(f"Energy consumed: {energy_usage}, Energy level decreased to: {self.energy_level}")
        else:
            print("Not enough energy for consumption.")

class Plant:
    def __init__(self, leaf_count=5):
        self.cells = [PlantCell() for _ in range(leaf_count)]
        self.environment = {'light_intensity': 0}

    def update_environment(self, new_light_intensity):
        self.environment['light_intensity'] = new_light_intensity
        for cell in self.cells:
            cell.perform_photosynthesis(new_light_intensity)

    def simulate_day_night_cycle(self, day_length=12, night_length=12):
        for _ in range(day_length):
            self.update_environment(100)  # 白天光照强度假设为100
            print("Daytime - Photosynthesis")
        for _ in range(night_length):
            self.update_environment(0)  # 夜晚光照强度为0
            for cell in self.cells:
                cell.consume_energy(1)  # 每个细胞在夜晚消耗一定的能量

class PlantCore:
    def __init__(self):
        self.name = 'The Plant Core'
        self.description = 'The Plant Core is a core of the artificial life, it is a part of the artificial life system.'
        self.cells = ["Nucleus", "Cytoplasm", "Membranes", "Mitochondria", "Chloroplast", "DNA", "Wall"]
        self.cell_components = {
            "Nucleus": "The nucleus is the center of the cell's information processing, storing genetic information.",
            "Cytoplasm": "The cytoplasm is the cell's body where various metabolic processes occur.",
            "Membranes": "Membranes are the cell's boundary, regulating the passage of substances.",
        }
        self.molecule_functions = {
            "DNA": "DNA carries the genetic code essential for cell replication and function.",
            "Chloroplast": "Chloroplasts are responsible for photosynthesis, converting light energy into chemical energy.",
            "Mitochondria": "Mitochondria generate ATP, the main energy source for cellular activities.",
        }
        self.show()

    def show(self):
        print(self.name)
        print(self.description)
        print(self.cells)
        print("\nCell Components:")
        for component, description in self.cell_components.items():
            print(f"{component}: {description}")
        print("\nMolecules and Their Functions:")
        for molecule, function in self.molecule_functions.items():
            print(f"{molecule}: {function}")

if __name__ == "__main__":
    plant_core = PlantCore()
    artificial_plant = Plant()
    print("Starting plant system simulation...")
    artificial_plant.simulate_day_night_cycle()
