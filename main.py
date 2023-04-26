from pathlib import Path
from PIL import Image
from datetime import datetime
import os

def walker(path):

    rotation_angles = [10,20,30,40,50,60,70,80,90,100]
    os.mkdir(path=str(path) + "/GEN")

    save_path = str(path) + "/GEN/"

    for angle in rotation_angles:
        path = Path(path)
        for item in path.iterdir():
            if item.is_file():
                if str(item).split(".")[1] == "DS_Store":
                    pass
                else:
                    with Image.open(item) as im:
                        name = str(datetime.now())+ ".png"
                        im2 = im.convert('RGBA')
                        rot = im2.rotate(angle, expand=1)
                        fff = Image.new('RGBA', rot.size, (255,)*4)
                        out = Image.composite(rot, fff, rot)
                        out.convert(im.mode).save(str(save_path) + name)

    


walker("/Users/bathiyaseneviratne/Desktop/ACA013")