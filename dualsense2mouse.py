from pydualsense import *
import mouse
import keyboard


def cross_down(state):
    if (state):
        mouse.click()

def circle_down(state):
    if (state):
        mouse.right_click()    

def left_joystick(stateX, stateY):
    mouse.move(stateX / 30, stateY / 30, False)

def right_joystick(stateX, stateY):
    if abs(stateX) <= 3 and abs(stateY <= 3):
        return
    mouse.wheel(stateY * 0.001)

def L1_down(state):
    if (state):
        keyboard.press('alt')
    else:
        keyboard.release('alt')
        
def R1_down(state):
    if (state):
        keyboard.send('tab')

ds = pydualsense()
ds.init()


ds.cross_pressed += cross_down
ds.circle_pressed += circle_down
ds.left_joystick_changed += left_joystick
ds.right_joystick_changed += right_joystick
ds.l1_changed += L1_down
ds.r1_changed += R1_down


ds.audio.setMicrophoneState(False)
#pointless but why not
ds.triggerL.setMode(TriggerModes.Rigid)
ds.triggerL.setForce(1, 255)
ds.triggerR.setMode(TriggerModes.Rigid)
ds.triggerR.setForce(1, 255)

#ds.close()
