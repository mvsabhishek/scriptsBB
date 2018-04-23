import bpy

bpy.ops.wm.addon_install(filepath="/home/blender/sverchok-master.zip")
bpy.ops.wm.addon_enable(module="sverchok-master")
# deselect all
bpy.ops.object.select_all(action='DESELECT')
# selection
bpy.data.objects['Cube'].select = True
bpy.data.objects['Lamp'].select = True
bpy.data.objects['Camera'].select = True
# remove it
bpy.ops.object.delete() 
bpy.ops.wm.save._userpref()
