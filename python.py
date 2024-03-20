from PIL import Image
obrazek = Image.open("pitbull.jpg")

#blackandwhite filter
def BlackAndWhiteFilter():
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer < 51:
                obrazek.putpixel((x,y), (192, 192, 192))
            if prumer >= 51 and prumer < 102:
                obrazek.putpixel((x,y), (128, 128, 128))
            if prumer >= 102 and prumer < 153:
                obrazek.putpixel((x,y), (255, 255, 255))
            if prumer >= 153 and prumer < 204:
                obrazek.putpixel((x,y), (79, 79, 79))
            if prumer >= 204:
                obrazek.putpixel((x,y), (0, 0, 0))
            y += 1
        x += 1
    obrazek.show()
    
#darkblue filter
def DarkBlueFilter():
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer < 51:
                obrazek.putpixel((x,y), (0, 0, 238))
            if prumer >= 51 and prumer < 102:
                obrazek.putpixel((x,y), (0, 0, 139))
            if prumer >= 102 and prumer < 153:
                obrazek.putpixel((x,y), (0, 154, 205))
            if prumer >= 153 and prumer < 204:
                obrazek.putpixel((x,y), (16, 78, 139))
            if prumer >= 204:
                obrazek.putpixel((x,y), (0, 0, 0))
            y += 1
        x += 1
    obrazek.show()

#LightGreen Filter
def lightgreen_filter():
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
            obrazek.putpixel((x,y), (r , b, r))
            if prumer < 51:
                obrazek.putpixel((x,y), (144, 238, 144))
            if prumer >= 51 and prumer < 102:
                obrazek.putpixel((x,y), (180, 238, 180))
            if prumer >= 102 and prumer < 153:
                obrazek.putpixel((x,y), (118, 238, 0))
            if prumer >= 153 and prumer < 204:
                obrazek.putpixel((x,y), (84, 255, 159))
            if prumer >= 204:
                obrazek.putpixel((x,y), (0, 255, 0))
            y += 1
        x += 1
    obrazek.show()