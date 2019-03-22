
from bluedot import BlueDot
from signal import pause


def show_percentage(pos):
    horizontal = ((pos.x + 1) / 2)
    percentage = round(horizontal * 100, 2)
    print("{}%".format(percentage))


bd = BlueDot()
bd.color = "blue"
bd.square = True
bd.border = True
bd.visible = True

bd.when_moved = show_percentage

pause()
