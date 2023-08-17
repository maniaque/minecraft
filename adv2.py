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
block_tnt = "TNT"

block_doorwood = "SPRUCE_DOOR"
block_lantern = "LANTERN"
block_torch = "WALL_TORCH"

def create_frame(beginX, beginZ, beginY, length, width):
  # setBlocks adds one!
  mc.setBlocks(beginX, beginY, beginZ,              beginX + length - 1, beginY, beginZ,             block_tnt)  # 1,1 to x,1
  mc.setBlocks(beginX, beginY, beginZ,              beginX,              beginY, beginZ + width - 1, block_tnt)  # 1,1 to 1,x
  mc.setBlocks(beginX, beginY, beginZ + width - 1,  beginX + length - 1, beginY, beginZ + width - 1, block_tnt)  # 1,x to x,x
  mc.setBlocks(beginX + length - 1, beginY, beginZ, beginX + length - 1, beginY, beginZ + width - 1, block_tnt)  # x,1 to x,x

# use 5, 30; 30, 5; 30, 30 then
startX = 5
startZ = 5

sizeX = 20
sizeZ = 20

posY = -60

endX = startX + sizeX
endZ = startZ + sizeZ

# clear
for y in range(0, 100):
  mc.setBlocks(startX - 10, posY, startZ - 10, endX + 10, posY + y, endZ + 10, block_air)

create_frame(startX, startZ, posY, sizeX, sizeZ)
create_frame(startX + 1, startZ + 1, posY + 1, sizeX - 2, sizeZ - 2)
create_frame(startX + 2, startZ + 2, posY + 2, sizeX - 4, sizeZ - 4)
create_frame(startX + 3, startZ + 3, posY + 3, sizeX - 6, sizeZ - 6)
create_frame(startX + 4, startZ + 4, posY + 4, sizeX - 8, sizeZ - 8)
create_frame(startX + 5, startZ + 5, posY + 5, sizeX - 10, sizeZ - 10)
create_frame(startX + 6, startZ + 6, posY + 6, sizeX - 12, sizeZ - 12)
create_frame(startX + 7, startZ + 7, posY + 7, sizeX - 14, sizeZ - 14)
create_frame(startX + 8, startZ + 8, posY + 8, sizeX - 16, sizeZ - 16)
create_frame(startX + 9, startZ + 9, posY + 9, sizeX - 18, sizeZ - 18)
