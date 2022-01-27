import time

# Define the Class

print("Hello! I am Vendorr the pricey and I am here to sell you healthy and affordable snacks.")

class VendingMachine:
  def __init__(self, product, price):
    self.product = product
    self.price = price
    self.inventory = 0
    self.dollabills = 0

  def restock(self, amount):
    self.inventory += amount
    return print("Current inventory is " +str(self.inventory)+ " of our " +str(self.product))

  def addfunds(self,money):
    self.dollabills += money
    if self.inventory <= 0:
      return print("Are you actually putting money into an empty vending machine? This is honestly embarrassing.\nI, Vendorr the pricey, will now take your money and leave you with nothing.")
    elif self.inventory > 0:
      return print("So close! Now you can use the vend.vend method to get your very own " + str(self.product) + ".")

  def vend(self):

    if self.inventory > 0:

      if self.dollabills == self.price:
        return print("Here is your x-tra exclusive " + str(self.product) + ". Goodbye!")
      elif self.dollabills > self.price:
        extra = self.dollabills - self.price
        self.dollabills = 0
        self.inventory = self.inventory - 1
        return print("Here is your x-tra exclusive " + str(self.product) + ". However, I Vendorr the great will take your " + str(extra) + " and\n leave you here to get scammed again!")
      elif self.dollabills < self.price:
        print("You are so close to a " + str(self.product) + ". Just a few more dollars!\nMake sure to use the vend.addfunds method to get your very own " + str(self.product) + "!")

    else:
      self.dollabills = 0
      print("No.")

vend = VendingMachine('vegan kit-kat', 1000000)

vend.restock(100)
