#!/usr/bin/python3

class UFO:
	def __init__(self, name, shape, speed):
		self.name = name
		self.shape = shape
		self.speed = speed
	
	def info(self):
		print(f"{self.name} is prepare for advanture!!!")
	
	def form(self):
		print(f"{self.name} has {self.shape} shape")

	def fast(self):
		print(f"{self.name} has maximum speed of {self.speed} KM/Hr.")

class SpaceTraveller(UFO):
	def __init__(self, name, shape, speed, equipments):
		super().__init__(name, shape, speed)
		self.equipment = equipments

	def wormhole(self):
		print("We are going to the wormhole")

	def warpdrive(self):
		print("Initializing warpdrive!!")
	
	def cryocapsule(self):
		print("Prepare for hibernation")

class Research(UFO):
	def __init__(self, name, shape, speed, weapons):
		super().__init__(name, shape, speed)
		self.weapons = weapons

	def abduction(self):
		print("We captured 2 humans")

	def experiment(self):
		print(f"{self.name} is scanning...")

	def fight(self):
		print(f"{self.name} is using {self.weapons}")


if __name__ == "__main__":
	ufo1 = UFO("Optimus", "Oval", 3_000_000)
	ufo2 = UFO("Maximus", "Cube", 2000_000) 
	s1 = SpaceTraveller("Endurance", "Pyramid", 5_000_000, "Cryo capsule")
	r1 = Research("Interceptor", "Pentagon", 4_000_000, "Laser beam pew pew!!")

	ufo1.info()
	ufo2.info()
	s1.info()
	s1.form()
	s1.fast()
	s1.wormhole()
	s1.warpdrive()
	s1.cryocapsule()
	r1.info()
	r1.form()
	r1.fast()
	r1.abduction()
	r1.experiment()
	r1.fight()

	