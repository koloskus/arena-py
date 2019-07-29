import channel
import explore
import requests
import user
import block

c = channel.getChannel('computer-graphics-jjpidmjvw40')

print("Blocks in channel " + c.slug + ":")
for blk in c.contents:
    b = block.Block(blk)
    print(b.block_class + ":")
    print(b.title)
    if b.block_class == 'Image':
        print("     " + b.image.filename)
    print(" ")