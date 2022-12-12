import bpy

defaultUVMapName = "UVMap"

if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        if obj.type != "MESH":
            continue
        bpy.context.view_layer.objects.active = obj
        layercount = len(obj.data.uv_layers)
        for uv in reversed(obj.data.uv_layers):
            uv.name = "temp"
        for uv in reversed(obj.data.uv_layers):
            if uv.active_render:
                uv.name = defaultUVMapName
            else:
                uv.active = True
                bpy.ops.mesh.uv_texture_remove()
