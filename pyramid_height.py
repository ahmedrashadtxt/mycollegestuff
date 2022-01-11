blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
layer = 0
blocks_remaining = blocks

for i in range(blocks):
    if blocks_remaining > layer:
        layer += 1
        blocks_remaining = blocks_remaining - layer
        height += 1
    else:
        break

print("The height of the pyramid:", height)
