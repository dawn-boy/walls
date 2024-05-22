import os,time

for i in range(25):
    time.sleep(2)
    os.system(f"~/.config/ags/scripts/color_generation/colorgen.sh {i}.jpg --apply --smart")
