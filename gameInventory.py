inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
  print('Inventory:')
  for k, v in inventory.items():
    print(str(v) + ' ' + k)
  print('Total number of items: ' + str(sum(inventory.values())))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
  for item in addedItems:
    inventory[item] = inventory.get(item, 0) + 1

addToInventory(inv, dragonLoot)
displayInventory(inv)