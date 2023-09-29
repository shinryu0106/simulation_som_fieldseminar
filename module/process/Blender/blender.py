""" Outer library """
import os
import glob
import bpy

""" Processes """
# Delete all objects
def deleteAllObjects():
    #region
    # Delete object in all scene(Error)
    # for item in bpy.context.scene.objects:
        # bpy.context.scene.objects.unlink(item)
    #endregion
    # Delete all data object
    for item in bpy.data.objects:
        bpy.data.objects.remove(item)
    # Delete all mesh data
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)
    # Delete all materials
    for item in bpy.data.materials:
        bpy.data.materials.remove(item)

# Operation image object
## Create image
def createImage():
    #Debug# print(list(bpy.data.textures.keys())[0])
    bpy.ops.texture.new()
    bpy.data.textures[list(bpy.data.textures.keys())[0]].name = "NewTexture"
    list_of_files = glob.glob(os.getcwd() + "/store/*")
    latest_file = max(list_of_files, key=os.path.getmtime)
    bpy.data.textures["NewTexture"].image = bpy.data.images.load(filepath = latest_file)

## Create object
def createObject():
    # Add main object
    bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.ops.object.shade_smooth()
    plane = bpy.context.active_object

    # Add Multires
    plane.modifiers.new(name = "Multires", type='MULTIRES')
    for i in range(6):
        bpy.ops.object.multires_subdivide(modifier="Multires", mode='SIMPLE')

    # Add displace
    new_displace = plane.modifiers.new(name = "Displace", type='DISPLACE')
    new_displace.texture = bpy.data.textures['NewTexture']

# Save(Not duplicate)
def saveBlendFile():
    num = 0
    while True:
        if os.path.isfile(os.getcwd() + "/store/save_" + str(num) + ".blend"):
            num += 1
        else:
            bpy.ops.wm.save_as_mainfile(filepath = os.getcwd() + "/store/save_" + str(num) + ".blend")
            return

""" Main(__main__ cannot use) """
#region
# Delete
deleteAllObjects()
# Operation image object
## Create image
createImage()
## Create object
createObject()
# Save
saveBlendFile()
#endregion