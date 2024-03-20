from PIL import Image
obrazek = Image.open("pitbull.jpg")

#
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
    

BlackAndWhiteFilter()