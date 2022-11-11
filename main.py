import random
class Human:
  def __init__(self, name = "Міра Косякова", job = None,home = None, car = None):
    self.name = name
    self.job = job
    self.home = home
    self.car = car
    self.money = 5000
    self.gladness = 80
    self.satiety = 94
  def get_home(self):
    pass
  def get_car(self):
    pass
  def get_job(self):
    pass
  def food(self):
    pass
  def work(self):
    pass
  def shopping(self):
    pass
  def clothes(self):
    pass
  def chill(self):
    pass
  def clean_home(self):
    pass

  def day_indexes(self, day):
    pass
  def is_alive(self):
    pass
  def live(self, day):
    pass

class Auto:
  def __init__(self, brand_list):
    self.brand = random.choice(list(brand_list))
    self.strength = brand_list[self.brand]['strength']
    self.fuel = brand_list[self.brand]['fuel']
    self.consumption = brand_list[self.brand]['consumption']
brands_of_car = {"Reno":{'fuel':190, "strength":80, "consumption":9},
                 "Opel":{'fuel':150, "strength":60, "consumption":7},
                 "Scoda":{'fuel':205, "strength":85, "consumption":5},
                 "Rolls-Royce":{'fuel':250, "strength":90, "consumption":10},
                 "BMW":{'fuel':237, "strength":100, "consumption":10},
                 "Lada":{'fuel':80, "strength":60, "consumption":7}}
class Clothes:
  def __init__(self, brand_list):
    self.brand = random.choice(list(brand_list))
    self.modern = brand_list[self.brand]['modern']
    self.style = brand_list[self.brand]['style']
    self.price = brand_list[self.brand]['price']
brands_of_clothes = {"Chanel":{'modern':1000, "style":645, "price":3000},
                     "Prada":{'modern':750, "style":700, "price":3500},
                     "Versace":{'modern':1000, "style":800, "price":2500},
                     "Fendi":{'modern':300, "style":600, "price":2000},
                     "Gucci":{'modern':900, "style":500, "price":5000},
                     "Nice":{'modern':1000, "style":800, "price":900}}