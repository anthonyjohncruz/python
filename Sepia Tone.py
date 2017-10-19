def sepia (oldPixel):
    red = oldPixel.getRed()
    green = oldPixel.getGreen()
    blue = oldPixel.getBlue()
    
    newred = (red*0.393 + green*0.769 + blue*0.189)
    newgreen = (red*0.349 + green*0.686 + blue*0.168)
    newblue = (red*0.272 + green*0.534 + blue*0.131)
    
    newPixel = Pixel (newred, newgreen, newblue)
    return newPixel
