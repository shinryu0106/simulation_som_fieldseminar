""" Outer library """
from PIL import Image, ImageTk
""" Inner library """
import module.data.gui as GUI
import module.process.simulation as simulation
import module.process.error as error

""" Global """
# Image
global _resultImg_PIL
global _resultImg_Tkinter
# Timer
global _image_num
global _changing_img

""" Processes """
# Save image
def saveImage():
    try:
        num = GUI._root._slider_image_list.get()
        print("Save:" + str(num))
        _resultImg_PIL[num].save("store/" + GUI._root._saveName.get() + ".png")
    except:
        error.messageEnd("Error:Cannot save")

# Simulate image
def simulateImage(learntime, x, y):
    global _resultImg_PIL
    global _resultImg_Tkinter
    _resultImg_PIL = simulation.simulation(learntime, x, y)
    _resultImg_Tkinter = ImageTk.PhotoImage(_resultImg_PIL[0])

# Resimulate image
def resimulateImage():
    global _resultImg_PIL
    _resultImg_PIL = simulation.simulation(GUI._root._slider_simulation_count.get(), GUI._root._slider_image_w.get(), GUI._root._slider_image_h.get())
    showImage(
        _resultImg_PIL[GUI._root._slider_image_list.get()], # Image
        GUI._root._slider_image_w.get(), GUI._root._slider_image_h.get() # Scale
    )

# Show image
def showImage(
    image, # Image
    w, h # Scale
):
    global _resultImg_Tkinter
    _resultImg_PIL_temp = image
    _resultImg_PIL_temp = _resultImg_PIL_temp.resize((w, h))
    _resultImg_Tkinter = ImageTk.PhotoImage(_resultImg_PIL_temp)
    GUI._sub._canvas.itemconfig(GUI._sub._img, image = _resultImg_Tkinter)

# Change image
## Manual
def changeImage(self):
    stopAutoImage()
    if len(_resultImg_PIL) >= 200:
        showImage(
            _resultImg_PIL[GUI._root._slider_image_list.get()], # Image
            GUI._root._slider_image_w.get(), GUI._root._slider_image_h.get() # Scale
        )
    else:
        print("Error:Simulation count is less than 200")

## Auto
### Start
def startAutoImage():
    global _changing_num
    global _changing_img
    _changing_num = GUI._root._slider_image_list.get()
    _changing_img = True
    changeAutoImage()

### Update
def changeAutoImage():
    global _changing_num
    global _changing_img
    _changing_num = _changing_num + 1 if _changing_num < 199 else 0

    showImage(
        _resultImg_PIL[_changing_num], # Image
        GUI._root._slider_image_w.get(), GUI._root._slider_image_h.get() # Scale
    )

    if _changing_img == True:
        GUI._sub.after(101 - GUI._root._slider_image_fps.get(), changeAutoImage)

### Stop
def stopAutoImage():
    global _changing_img
    _changing_img = False

# Repaint image size
def resizeImage(px, fromSlider = False):
    if fromSlider: # Set slider value
        GUI._root._slider_image_w.set(px)
        GUI._root._slider_image_h.set(px)

    #Debug# print("Image width:" + str(GUI._root._slider_image_w.get()))
    #Debug# print("Image height:" + str(GUI._root._slider_image_h.get()))

    showImage(
        _resultImg_PIL[GUI._root._slider_image_list.get()], # Image
        GUI._root._slider_image_w.get(), GUI._root._slider_image_h.get() # Scale
    )