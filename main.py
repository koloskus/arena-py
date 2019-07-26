from channel import Channel

channel = Channel('computer-graphics-jjpidmjvw40')

print("title:", channel.title)
print("by:", channel.user.username)
for block in channel.contents:
    print(block.base_class, block.title)
