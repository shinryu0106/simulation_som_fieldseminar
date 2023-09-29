""" Outer library """
import subprocess
""" Inner library """
import module.process.error as error
import module.process.management_image as management_image

""" Processes """
# Run Blender
def runBlender():
    try:
        management_image.saveImage() # Save image
        print("Start Blender...")
        subprocess.run(["/Applications/Blender.app/Contents/MacOS/Blender", "--python", "/Users/tanakakeisuke/Documents/3 First Semester/フィールド演習/Summer/Work/module/process/Blender/blender.py"]) # Run Blender
    except:
        error.messageEnd("Error:Blender is not installed or there is another cause")