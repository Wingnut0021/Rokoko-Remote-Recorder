from ahk import AHK

ahk = AHK()

def click_Brekel():
    win = ahk.active_window
    mousepos = ahk.get_mouse_position()
    ahk.mouse_position = (1641, 1010)
    ahk.click(1641, 1010, coord_mode='Screen')
    win.activate()
    ahk.mouse_position = (mousepos)