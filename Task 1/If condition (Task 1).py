#inheritence

class MobilePhone:
    def __init__(self, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = "Touch Screen"
        self.network_type = "4G/5G"
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
    
    def display_specs(self):
        return f"Screen: {self.screen_type}, Network: {self.network_type}, Dual SIM: {self.dual_sim}, " \
               f"Front Camera: {self.front_camera}MP, Rear Camera: {self.rear_camera}MP, RAM: {self.ram}GB, Storage: {self.storage}GB"
    
    def make_call(self, number):
        return f"Calling {number}..."
    
    def receive_call(self, caller):
        return f"Incoming call from {caller}..."
    
    def take_a_picture(self):
        return f"Picture taken with {self.rear_camera}MP rear camera!"

class Apple(MobilePhone):
    def __init__(self, front_camera, rear_camera, ram, storage):
        super().__init__(dual_sim=False, front_camera=front_camera, rear_camera=rear_camera, ram=ram, storage=storage)
        self.brand = "Apple"
    
    def apple_features(self):
        return "iOS Ecosystem, Face ID, Secure Enclave"
    
class Samsung(MobilePhone):
    def __init__(self, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(dual_sim, front_camera, rear_camera, ram, storage)
        self.brand = "Samsung"
    
    def samsung_features(self):
        return "Android OS, Knox Security, Samsung Pay"

#apple objects
iphone_12 = Apple(front_camera=12, rear_camera=12, ram=4, storage=128)
iphone_13 = Apple(front_camera=12, rear_camera=12, ram=6, storage=256)

#samsung objects
samsung_s21 = Samsung(dual_sim=True, front_camera=16, rear_camera=32, ram=16, storage=256)
samsung_a52 = Samsung(dual_sim=False, front_camera=8, rear_camera=16, ram=8, storage=128)