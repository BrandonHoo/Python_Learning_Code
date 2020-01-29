from PIL import Image
from PIL import ImageFilter

image=Image.open('picture.jpg')
image.format,image.size,image.mode
('JPEG',(500,750),'RGB')
image.show()
 
 
 



'''
image = Image.open('picture.jpg')
image.format, image.size, image.mode
('JPEG', (500, 750), 'RGB')
image.show()
'''