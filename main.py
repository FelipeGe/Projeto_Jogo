import pygame as pg

print("setup start")
pg.init()
window = pg.display.set_mode(size=(600, 480))
print("setup end")

print("Loop start")
while True:
    # Check for events  
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("Quit event detected")
            pg.quit()
            quit()

