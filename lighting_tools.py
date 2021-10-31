# -*- coding: utf-8 -*-

import re
from Katana import Nodes3DAPI
from Katana import NodegraphAPI
from Nodes3DAPI.Manifest import FnAttribute, FnGeolib

 
def get_light_material(selected_name):
#example:
#selected_scene_graph_names = ScenegraphManager.getActiveScenegraph()
#selected_scene_graph_locations = selected_scene_graph_names.getSelectedLocations()
#get_light_material(selected_scene_graph_locations)
    # why?? need?...
    node = NodegraphAPI.GetViewNodes()[0]
    runtime = FnGeolib.GetRegisteredRuntimeInstance()
    txn = runtime.createTransaction()
    op = Nodes3DAPI.GetOp(txn, node)
    client = txn.createClient()
    txn.setClientOp(client, op)
    runtime.commit(txn)

 
    material_attrs = []
    lightcrate_attrs = []

    for sn in selected_name:
        lo = client.cookLocation(sn)
        attr_exclusiveTo = lo.getAttrs().getChildByName("attributeEditor.exclusiveTo")
        attr_material = lo.getAttrs().getChildByName("attributeEditor.material.exclusiveTo")


        if attr_material == None:
            #print ("checked!! Do select light ")
            pass
        else:
            re_attr_exclusiveTo = re.sub(r'[0-9]+','', attr_exclusiveTo.getValue())

            if re_attr_exclusiveTo != "LightCreate":
                #print ("checked!! Slected Lightfiter")
                pass
            else:
                material_attrs.append(attr_material.getValue())

                lightcrate_attr = attr_exclusiveTo.getValue()
                lightcrate_attrs.append(re.findall("\d+", lightcrate_attr))

    light_attrs = list(zip(material_attrs, lightcrate_attrs))
    return light_attrs

 

def set_material_values(light_attrs, param_name, param_value):
#example: 
#light_attrs = get_light_material(selected_scene_graph_locations)
#param_name = 'exposure'
#param_value = 10
#set_material_values(light_attrs, param_name, param_value)
    if param_value == 'on':
        param_value = '1'
    if param_value == 'off':
        param_value = '0'

    unlimit_int_param = ["exposure", "intensity"]
    limit_int_param = ["diffuse", "specular"]
    bool_param = ["enableShadows", "areaNormalize", "visibleInRefractionPath", "camera"]     
    str_param = ["lightGroup", "LightLinkSetup_illumination", "LightLinkSetup_shadow"]
  
  
    if param_name in str_param:
        i = 0
        while i < len(light_attrs):
            #print ("Done : "+ light_attrs[i][0])
            mat = light_attrs[i][0]
            NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.enable').setValue(1, 0)
            NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.value').setValue(str(param_value), 0)
            i += 1
    
    elif param_name in unlimit_int_param:
        i = 0
        while i < len(light_attrs):
            #print ("Done : "+ light_attrs[i][0])
            mat = light_attrs[i][0]
            NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.enable').setValue(1, 0)
            NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.value').setValue(float(param_value), 0)
            i += 1

    elif param_name in bool_param:
        if param_value == "0" or param_value == "1":

            if param_value == 'yes':
                param_value = 1
            elif param_value == 'no':
                param_value = 0        

            i = 0
            while i < len(light_attrs):
                #print ("Done : "+ light_attrs[i][0])
                mat = light_attrs[i][0]
                NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.enable').setValue(1, 0)
                NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.value').setValue(int(param_value), 0)
                i += 1
        else:
            NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.value').setValue(int(param_value), 0)

    elif param_name in limit_int_param:
        if float(param_value) <= 1:
            i = 0
            while i < len(light_attrs):
                #print ("Done : "+ light_attrs[i][0])
                mat = light_attrs[i][0]
                NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.enable').setValue(1, 0)
                NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.value').setValue(float(param_value), 0)
                i += 1            
        else:
            NodegraphAPI.GetNode(mat).getParameter('shaders.prmanLightParams.' + param_name + '.value').setValue(int(param_value), 0)

def set_camera_viz(light_attrs, param_value):
#example:
#light_attrs = get_light_material(selected_scene_graph_locations)
#param_value = 0
#set_camera_viz(light_attrs, param_value)
    if param_value == 'yes':
        param_value = 1
    elif param_value == 'no':
        param_value = 0        

    i = 0
    while i < len(light_attrs):
        #print ("Done : "+ str(light_attrs[i][1]))
        light_state_num = "".join(light_attrs[i][1])
    
        cam_param = NodegraphAPI.GetNode('PrmanLightStatements' + light_state_num).getParameter('prmanStatements.attributes.visibility.camera.value')
        cam_param.setValue(1, 0)
        cam_param.setValue(param_value, 0)
        i += 1



def set_multi_linking(light_attrs, path_list, onoff, linking):
#example:
#light_attrs = get_light_material(selected_scene_graph_locations)
#path_list= ['/root/world/geo/char', '/root/world/cam', '/root/world/geo/dummy']
#linking = 'light_linking'
#onoff = 'off'
    if linking == 'LightLinking':
        linking = 'LightLinkSetup_illumination'
    elif linking == 'ShadowLinking':
        linking = 'LightLinkSetup_shadow'



    i = 0
    while i < len(light_attrs):
        str_path_list = " ".join(path_list)
        light_state_num = "".join(light_attrs[i][1])

        linking_param = NodegraphAPI.GetNode(linking + light_state_num).getParameter(onoff)
        linking_param.setValue(str(str_path_list), 1)
        i += 1
   
    

