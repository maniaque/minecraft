from pyncraft.minecraft import Minecraft
import time, math

mc = Minecraft.create(address="127.0.0.1", port=4711)

block_grass = "GRASS_BLOCK"
block_stone = "COBBLESTONE"
block_glass = "GLASS"
block_farmland = "FARMLAND"
block_dirtpath = "DIRT_PATH"
# block_dirtpath = "TNT"
block_air = "AIR"
block_water = "WATER"
block_carrots = "CARROTS"
block_potatoes = "POTATOES"
block_wheat = "WHEAT"
block_beetroots = "BEETROOTS"

block_doorwood = "SPRUCE_DOOR"
block_lantern = "LANTERN"
block_torch = "WALL_TORCH"

def create_box(beginX, beginZ, beginY, length, width, heigth):
  # setBlocks adds one!
  for y in range(0, heigth):
    newY = beginY + y;
    mc.setBlocks(beginX, newY, beginZ,              beginX + length - 1, newY, beginZ,             block_stone)  # 1,1 to x,1
    mc.setBlocks(beginX, newY, beginZ,              beginX,              newY, beginZ + width - 1, block_stone)  # 1,1 to 1,x
    mc.setBlocks(beginX, newY, beginZ + width - 1,  beginX + length - 1, newY, beginZ + width - 1, block_stone)  # 1,x to x,x
    mc.setBlocks(beginX + length - 1, newY, beginZ, beginX + length - 1, newY, beginZ + width - 1, block_stone)  # x,1 to x,x

  # roof (will be on last layer)
  mc.setBlocks(beginX, beginY + heigth - 1, beginZ, beginX + length - 1, beginY + heigth - 1, beginZ + width - 1, block_stone)  # 5,1 to 5,5

# directionX = -1
# directionZ = -1

# use 5, 30; 30, 5; 30, 30 then
startX = 5
startZ = 5

sizeX = 10
sizeZ = 10

posY = -60

endX = startX + sizeX
endZ = startZ + sizeZ

r = 10

# clear
for y in range(0, 100):
  mc.setBlocks(startX - 10, posY, startZ - 10, endX + 10, posY + y, endZ + 10, block_air)

# # super clear
# for y in range(0, 100):
#   mc.setBlocks(0, posY, 0, 100, posY + y, 100, block_air)

box_heigth = 5

create_box(startX, startZ, posY, sizeX, sizeZ, box_heigth)

# two sides of glass
mc.setBlocks(startX + 1, posY + 1, startZ, startX + sizeX - 2, posY + box_heigth - 2, startZ, block_glass)
mc.setBlocks(startX, posY + 1, startZ + 1, startX, posY + box_heigth - 2, startZ + sizeZ - 2, block_glass)

# holes for doors
mc.setBlocks(14, posY, 10, 14, posY + 1, 9, block_air)
mc.setBlocks(10, posY, 14, 9, posY + 1, 14, block_air)

# lanterns (inside)
mc.setBlock(startX + 3, posY + box_heigth - 2, startZ + 3, block_lantern)
mc.setBlock(startX + 3, posY + box_heigth - 2, startZ + sizeZ - 4, block_lantern)
mc.setBlock(startX + sizeX - 4, posY + box_heigth - 2, startZ + 3, block_lantern)
mc.setBlock(startX + sizeX - 4, posY + box_heigth - 2, startZ + sizeZ - 4, block_lantern)

# lanterns (outside)
mc.setBlock(startX - 1, posY + box_heigth - 1, startZ, block_stone)
mc.setBlock(startX,     posY + box_heigth - 1, startZ - 1, block_stone)
mc.setBlock(startX - 1, posY + box_heigth - 2, startZ, block_lantern)
mc.setBlock(startX,     posY + box_heigth - 2, startZ - 1, block_lantern)

mc.setBlock(startX + sizeX,     posY + box_heigth - 1, startZ, block_stone)
mc.setBlock(startX + sizeX - 1, posY + box_heigth - 1, startZ - 1, block_stone)
mc.setBlock(startX + sizeX,     posY + box_heigth - 2, startZ, block_lantern)
mc.setBlock(startX + sizeX - 1, posY + box_heigth - 2, startZ - 1, block_lantern)

mc.setBlock(startX,     posY + box_heigth - 1, startZ + sizeZ, block_stone)
mc.setBlock(startX - 1, posY + box_heigth - 1, startZ + sizeZ - 1, block_stone)
mc.setBlock(startX,     posY + box_heigth - 2, startZ + sizeZ, block_lantern)
mc.setBlock(startX - 1, posY + box_heigth - 2, startZ + sizeZ - 1, block_lantern)

mc.setBlock(startX + sizeX,     posY + box_heigth - 1, startZ + sizeZ - 1, block_stone)
mc.setBlock(startX + sizeX - 1,     posY + box_heigth - 1, startZ + sizeZ, block_stone)
mc.setBlock(startX + sizeX,     posY + box_heigth - 2, startZ + sizeZ - 1, block_lantern)
mc.setBlock(startX + sizeX - 1,     posY + box_heigth - 2, startZ + sizeZ, block_lantern)
