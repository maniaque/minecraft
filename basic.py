from pyncraft.minecraft import Minecraft
import time, math

mc = Minecraft.create(address="127.0.0.1", port=4711)

block_grass = "GRASS_BLOCK"
block_farmland = "FARMLAND"
block_dirtpath = "DIRT_PATH"
# block_dirtpath = "TNT"
block_air = "AIR"
block_water = "WATER"
block_carrots = "CARROTS"
block_potatoes = "POTATOES"
block_wheat = "WHEAT"
block_beetroots = "BEETROOTS"

directionX = -1
directionZ = -1

startX = -5
startZ = -5

sizeX = 11
sizeZ = 11

posY = -61

endX = startX + directionX * sizeX
endZ = startZ + directionZ * sizeZ

# clear up
mc.setBlocks(startX, posY, startZ, endX, posY, endZ, block_grass)
# exit(1)

# water
mc.setBlock(startX + directionX * 5, posY, startZ + directionZ * 5, block_water)

# farmland
mc.setBlocks(startX + directionX * 1, posY, startZ + directionZ * 1, startX + directionX * 4, posY, startZ + directionZ * 4, block_farmland)
mc.setBlocks(startX + directionX * 1, posY, startZ + directionZ * 6, startX + directionX * 4, posY, startZ + directionZ * 9, block_farmland)
mc.setBlocks(startX + directionX * 6, posY, startZ + directionZ * 1, startX + directionX * 9, posY, startZ + directionZ * 4, block_farmland)
mc.setBlocks(startX + directionX * 6, posY, startZ + directionZ * 6, startX + directionX * 9, posY, startZ + directionZ * 9, block_farmland)

# dirt path
mc.setBlocks(startX, posY, startZ, startX, posY, startZ + directionZ * 10, block_dirtpath)
mc.setBlocks(startX, posY, startZ, startX + directionX * 10, posY, startZ, block_dirtpath)
mc.setBlocks(startX + directionX * 10, posY, startZ, startX + directionX * 10, posY, startZ + directionZ * 10, block_dirtpath)
mc.setBlocks(startX, posY, startZ + directionZ * 10, startX + directionX * 10, posY, startZ + directionZ * 10, block_dirtpath)

# first part of cross
mc.setBlocks(startX + directionX * 5, posY, startZ, startX + directionX * 5, posY, startZ + directionZ * 10, block_dirtpath)

# second part
mc.setBlocks(startX, posY, startZ + directionZ * 5, startX + directionX * 10, posY, startZ + directionZ * 5, block_dirtpath)

# water again
mc.setBlock(startX + directionX * 5, posY, startZ + directionZ * 5, block_water)

# carrots
mc.setBlocks(startX + directionX * 1, posY + 1, startZ + directionZ * 1, startX + directionX * 4, posY + 1, startZ + directionZ * 4, block_carrots)

# potatoes
mc.setBlocks(startX + directionX * 1, posY + 1, startZ + directionZ * 6, startX + directionX * 4, posY + 1, startZ + directionZ * 9, block_potatoes)

# wheat
mc.setBlocks(startX + directionX * 6, posY + 1, startZ + directionZ * 1, startX + directionX * 9, posY + 1, startZ + directionZ * 4, block_wheat)

# beetroots
mc.setBlocks(startX + directionX * 6, posY + 1, startZ + directionZ * 6, startX + directionX * 9, posY + 1, startZ + directionZ * 9, block_beetroots)