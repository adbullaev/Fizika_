import math

# Constants
SPEED_OF_LIGHT = 299792458  # meters per second (m/s)
SECONDS_IN_YEAR = 365 * 24 * 60 * 60  # number of seconds in a year

# Ship characteristics


class Spaceship:
    def __init__(self, name, mass, speed):
        self.name = name
        self.mass = mass
        self.speed = speed
        self.time_shift = 0

    def calculate_time_shift(self):
        if self.speed > SPEED_OF_LIGHT:
            # Calculate time dilation using special relativity formula
            time_dilation_factor = 1 / \
                math.sqrt(1 - (SPEED_OF_LIGHT**2 / self.speed**2))
            self.time_shift = (self.speed / SPEED_OF_LIGHT) * \
                SECONDS_IN_YEAR * time_dilation_factor
        else:
            self.time_shift = 0

    def display_info(self):
        if self.time_shift > 0:
            print(f"Космический корабль {self.name} превысил скорость света!")
            print(
                f"Время на борту переместилось на {self.time_shift} секунд в будущее.")
        else:
            print(
                f"Космический корабль {self.name} движется со скоростью {self.speed} м/с.")


# Create a spaceship instance
ship = Spaceship("Квазар", 2000000, SPEED_OF_LIGHT * 2)  # 1.2x speed of light

# Calculate time shift
ship.calculate_time_shift()

# Display the results
ship.display_info()
