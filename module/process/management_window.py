""" Outer library """
import sys
from tkinter import *
""" Inner library """
import module.data.gui as GUI
import module.process.management_image as management_image
import module.process.Blender.management_blender as management_blender

""" Processes """
# Generate window
## Create
def makeWindow(textList, main_x, main_y, sub_x, sub_y, learntime):
    mainWindow(textList, main_x, main_y, learntime)
    subWindow(textList, sub_x, sub_y, learntime)

    GUI._root.mainloop()

## Main
def mainWindow(textList, x, y, learntime):
    #region # Window
    GUI._root = Tk()
    GUI._root.title(textList["MainWindowName"])
    GUI._root.geometry(str(x) + "x" + str(y))
    #endregion

    #region # Image Size
    ## Frame
    makeLabel(textList["ImageSizeFrame"], 50, 5)
    frame = Frame(
        GUI._root, # Setting
        width = 550, height = 220, # Scale
        bd = 4, relief = "groove" # Border
    )
    frame.place(x = 25, y = 30) # Position

    ## Image width
    makeLabel(textList["ImageWidth"], 50, 40)
    GUI._root._slider_image_w = makeSlider(
        management_image.resizeImage, event = "<ButtonRelease-1>", # Event
        x = 50, y = 60, # Position
        w = 500,  min = 64, max = 2048, # Scale
        tick = 256
    )
    ## Image height
    makeLabel(textList["ImageHeight"], 50, 115)
    GUI._root._slider_image_h = makeSlider(
        management_image.resizeImage, event = "<ButtonRelease-1>", # Event
        x = 50, y = 135, # Position
        w = 500, min = 64, max = 2048, # Scale
        tick = 256
    )
    
    ## Set image size
    makeLabel(textList["ImageSize"], 50, 190)
    ### 64px
    makeButton(
        textList["64px"], # Text
        lambda:management_image.resizeImage(64, True), # Event
        x = 50, y = 215, # Position
        w = 60, h = 25 # Scale
    )
    ### 128px
    makeButton(
        textList["128px"], # Text
        lambda:management_image.resizeImage(128, True), # Event
        x = 135, y = 215, # Position
        w = 60, h = 25 # Scale
    )
    ### 256px
    makeButton(
        textList["256px"], # Text
        lambda:management_image.resizeImage(256, True), # Event
        x = 220, y = 215, # Position
        w = 60, h = 25 # Scale
    )
    ### 512px
    makeButton(
        textList["512px"], # Text
        lambda:management_image.resizeImage(512, True), # Event
        x = 305, y = 215, # Position
        w = 60, h = 25 # Scale
    )
    ### 1024px
    makeButton(
        textList["1024px"], # Text
        lambda:management_image.resizeImage(1024, True), # Event
        x = 390, y = 215, # Position
        w = 60, h = 25 # Scale
    )
    ### 2048px
    makeButton(
        textList["2048px"], # Text
        lambda:management_image.resizeImage(2048, True), # Event
        x = 475, y = 215, # Position
        w = 60, h = 25 # Scale
    )
    #endregion

    #region # Image edit
    ## Frame
    makeLabel(textList["ImageEditFrame"], 50, 255)
    frame = Frame(
        GUI._root, # Setting
        width = 550, height = 220, # Scale
        bd = 4, relief = "groove" # Border
    )
    frame.place(x = 25, y = 275) # Position

    ## Save
    ### Input
    makeLabel(textList["SaveFileName"], 50, 280)
    makeLabel(textList["SaveFileFrontName"], 50, 300)
    GUI._root._saveName = makeInputText(textList["SaveFileDefaultName"], 100, 300, 35)
    makeLabel(textList["SaveFileBackName"], 430, 300)
    ### Button
    makeButton(
        textList["ButtonSave"], # Text
        management_image.saveImage, # Event
        x = 485, y = 300, # Position
        w = 60, h = 25 # Scale
    )

    ## Image change
    ### Slider
    makeLabel(textList["ImageChange"], 50, 340)
    GUI._root._slider_image_list = makeSlider(
        management_image.changeImage, event = "<ButtonRelease-1>", # Event
        x = 50, y = 360, # Position
        w = 420, min = 0, max = 199, # Scale
        tick = 25
    )

    makeLabel(textList["ImageChangeFPS"], 50, 410)
    GUI._root._slider_image_fps = makeSlider(
        x = 50, y = 430, # Position
        w = 420, min = 1, max = 100, # Scale
        tick = 20
    )
    ### Button
    makeButton(
        textList["ImageAutoChange"], # Text
        management_image.startAutoImage, # Event
        x = 485, y = 375, # Position
        w = 60, h = 25 # Scale
    )
    makeButton(
        textList["ImageStopChange"], # Text
        management_image.stopAutoImage, # Event
        x = 485, y = 445, # Position
        w = 60, h = 25 # Scale
    )
    #endregion

    #region # Resimulation
    ### Slider
    makeLabel(textList["SimulationCount"], 50, 495)
    GUI._root._slider_simulation_count = makeSlider(
        x = 50, y = 515, # Position
        w = 360, min = 1000, max = 50000, # Scale
        tick = 10000
    )
    ### Button
    makeButton(
        textList["ButtonResimulation"], # Text
        management_image.resimulateImage, # Event
        x = 425, y = 530, # Position
        w = 120, h = 25 # Scale
    )
    #endregion

    #region # Blender
    makeButton(
        textList["ButtonBlender"], # Text
        management_blender.runBlender, # Event
        x = 50, y = 565, # Position
        w = 120, h = 25 # Scale
    )
    #endregion

    #region # Exit
    makeButton(
        textList["ButtonExit"], # Text
        sys.exit, # Event
        x = 530, y = 565, # Position
        w = 60, h = 25 # Scale
    )
    #endregion
    
## Sub
def subWindow(textList, x, y, learntime):
    #region # Window
    GUI._sub = Toplevel()
    GUI._sub.title(textList["SubWindowName"])
    GUI._sub.geometry(str(x) + "x" + str(y))
    #endregion

    #region # Image
    ## Canvas
    GUI._sub._canvas = Canvas(
        GUI._sub, # Setting
        bg = "black", # Color
        width = 2046, height = 2046, # Scale
        scrollregion = (0, 0, 2048, 2048) # Scroll
    )
    GUI._sub._canvas.place(x = 0, y = 0) # Position
    
    ## Image
    management_image.simulateImage(learntime, int(x), int(y)) # Simulation
    GUI._sub._img = GUI._sub._canvas.create_image(0, 0, image = management_image._resultImg_Tkinter, anchor = NW) # Show image
    #endregion

# Generate label
def makeLabel(
        t, # Text
        x = 0, y = 0, # Position
):
    label = Label(text = t) # Text
    label.place(x = x, y = y) # Position

# Generate button
def makeButton(
        t, # Text
        func, # Event
        x = 0, y = 0, # Position
        w = 50, h = 50 # Scale
):
    button = Button(
        GUI._root, # Setting
        text = t, # Text
        command = func # Event
    )
    button.place(
        x = x, y = y, # Position
        width = w, height = h # Scale
    )

# Generate slider
def makeSlider(
    func = None, event = "<Button-1>", # Event
    x = 0, y = 0, # Position
    w = 100, h = 10, min = 1, max = 100, # Scale
    tick = 64 # Interval of tick
):
    slider_temp = IntVar()
    slider = Scale(
        variable = slider_temp, orient = HORIZONTAL,
        length = w, width = h, sliderlength = h, to = min, from_ = max, # Scale
        tickinterval = tick # Interval of tick
    )
    slider.place(x = x, y = y) # Position
    if func != None:
        slider.bind(event, func)

    return slider_temp

# Generate input text
def makeInputText(
    t = "", # Text
    x = 0, y = 0, # Position
    w = 100 # Scale
):
    inputText = Entry(width = w)
    inputText.insert(END, t)
    inputText.place(x = x, y = y)
    return inputText