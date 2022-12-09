from pynput.mouse import Controller, Button
import time
n = 0
mouse = Controller()
while True:
    mouse.click(Button.left, 1)
    n = n+1
    print("clicked", n)

    time.sleep(30)