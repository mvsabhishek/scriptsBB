import bpy 



import json



#deleting the default cube

# deselect all

bpy.ops.object.select_all(action='DESELECT')

# selection

bpy.data.objects['Cube'].select = True

bpy.data.objects['Lamp'].select = True

bpy.data.objects['Camera'].select = True

# remove it

bpy.ops.object.delete()



#Make sure that both data.json and schwarzP are in the same directory



#run the script to generate the isosurfaces

data = json.load(open('/home/blender/scripts/data.json')) #please make the directory changes accordingly

filename = "/home/blender/scripts/schwarzD.py"

exec(compile(open(filename).read(), filename, 'exec'))



#import the collada file exported by mcubes.export.mesh

fileCollada = "/home/blender/output/"

fileCollada += str(data["collada"])

bpy.ops.wm.collada_import(filepath=fileCollada)



#make transformation (translate, scale, rotate)

bpy.ops.object.select_all(action='DESELECT')

# select object

obj = str(data["objectName"])

bpy.data.objects[obj].select = True





#set origin

bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

#set location

bpy.context.scene.objects.active.location = (0, 0, 0)

#smoothen the surface

bpy.ops.object.shade_smooth()

#set scale

bpy.context.scene.objects.active.scale = (-0.3, -0.3, -0.3)



#set thickness

bpy.ops.object.modifier_add(type='SOLIDIFY')

bpy.context.object.modifiers["Solidify"].use_even_offset = True

bpy.context.object.modifiers["Solidify"].offset = float(data["offset"])

bpy.context.object.modifiers["Solidify"].thickness = float(data["thickness"])

bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify")





#export the object as .stl

stlfile = str(data["stlFile"])

stlfile += ".stl"

bpy.ops.export_mesh.stl(filepath=stlfile, check_existing=True, axis_forward='Y', axis_up='Z', filter_glob="*.stl", use_selection=False, global_scale=1.0, use_scene_unit=False, ascii=False, use_mesh_modifiers=True)
