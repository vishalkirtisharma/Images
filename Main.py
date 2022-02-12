# pip install pillow
from PIL import Image

# Assign Varriable to that Images
demo=Image.open("demo.jpg")
mask= Image.open("Mask.jpg")
Stroke= Image.open("Stroke.png")

# chagne Demo size 330 Widhth x 381 Height (Width,Height)
demo= demo.resize((330,381))

# Add Demo to their first position with gap of Height 66 Wight 63 loop up to 5 for gap of width 27 

Width =27
for i in range(10):
    mask.paste(im=demo,box=(Width,63))
    # mask.paste(im=Stroke,box=(gap,63))
    Width += 27 + 330 #330
    
#copy data first row and paste 7 time that row with height of 32 
Height = 408
Crop= mask.crop((0,0,2480,480))

for i in range(7):
    mask.paste(im=Crop,box=(0,Height))
    # mask.paste(im=Stroke,box=(gap,63))
    Height += 408



# save that file with folder
mask.save("F.jpg")


# Open Prepare file for user
mask.show()