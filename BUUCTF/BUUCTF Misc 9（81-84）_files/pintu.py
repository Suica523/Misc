import os
from PIL import Image

width_i = 134
height_i = 130

line_max = 6
row_max = 6

all_path = []
num = 0
pic_max=line_max*row_max

dirName = os.getcwd()

for root, dirs, files in os.walk(dirName):
        for file in files:
            if ".zip" not in file and ".py" not in file and ".png" not in file:
                all_path.append(os.path.join(root, file))

toImage = Image.new('RGBA',(width_i*line_max,height_i*row_max))


for i in range(0,row_max): 

    for j in range(0,line_max):

        pic_fole_head =  Image.open(all_path[num])
        width,height =  pic_fole_head.size
    
        tmppic = pic_fole_head.resize((width_i,height_i))

        f = open(all_path[num],'rb')
        h = '';
        s = f.read(1)
        while s:
            byte = ord(s)
            h += hex(byte)
            s = f.read(1)
        h = int(str.replace(str.replace(h[-8:],'0xd9',''),'0x3',''))
        print(h)
        f.close()
        a = (h-1) // row_max

        b = (h-1) % line_max

        print(a,'---',b)
    
        loc = (int(b%line_max*width_i),int(a%line_max*height_i))
    
        toImage.paste(tmppic,loc)
        num= num+1

        if num >= len(all_path):
                print("breadk")
                break

    if num >= pic_max:
        break

toImage.save('result.png')