#function: export fence and cartobuildingline without OS

import arcpy
import os
import arcpy.mapping

path='D:/HK B/IB1000_COMPLETE/Extract'
a=os.listdir(path)
folder_list=[]
for i in range(0,139):
    folder_list.append(a[i])

for folder in folder_list:
    Address_base = path + '/' + folder + '/' + folder + '.gdb/CartoBuildingLine'
    Output_Address=path + '/' + folder + '/' + folder + '.gdb/CartoBuildingLine_modify'
    Fence_Address = path + '/' + folder + '/' + folder + '.gdb/Fence'

    try:
        # load cartobuildingline into map
        mxd = arcpy.mapping.MapDocument('CURRENT')

        df = arcpy.mapping.ListDataFrames(mxd, '*')[0]

        newlayer = arcpy.mapping.Layer(Address_base)

        arcpy.mapping.AddLayer(df, newlayer, "BOTTOM")

        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        # select features and update

        CartoBuildingLine = "CartoBuildingLine"
        CartoBuildingLine__3_ = CartoBuildingLine
        CartoBuildingLine__2_ = CartoBuildingLine
        test_F = Fence_Address
        CartoBuildingLine__5_ = CartoBuildingLine__2_
        CartoBuildingLine__6_ = CartoBuildingLine__5_
        test_modify = Output_Address

        # Process: Select Layer By Attribute
        arcpy.SelectLayerByAttribute_management(CartoBuildingLine, "NEW_SELECTION", "BUILDINGLINETYPE = 'F'")

        # Process: Copy Features
        arcpy.CopyFeatures_management(CartoBuildingLine__3_, test_F, "", "0", "0", "0")

        # Process: Select Layer By Attribute (2)
        arcpy.SelectLayerByAttribute_management(CartoBuildingLine, "CLEAR_SELECTION", "")

        # Process: Select Layer By Attribute (3)
        arcpy.SelectLayerByAttribute_management(CartoBuildingLine__2_, "NEW_SELECTION",
                                                "BUILDINGLINETYPE = 'F' OR BUILDINGLINETYPE = 'OS'")

        # Process: Select Layer By Attribute (4)
        arcpy.SelectLayerByAttribute_management(CartoBuildingLine__5_, "SWITCH_SELECTION", "")

        # Process: Copy Features (2)
        arcpy.CopyFeatures_management(CartoBuildingLine__6_, test_modify, "", "0", "0", "0")

        # remove "Cartobuildingline" then working on next
        for lyr in arcpy.mapping.ListLayers(mxd, "*", df):
            if lyr.name == 'CartoBuildingLine':
                arcpy.mapping.RemoveLayer(df, lyr)
            else:
                pass
        for lyr1 in arcpy.mapping.ListLayers(mxd, "*", df):
            if lyr1.name == 'CartoBuildingLine_modify':
                arcpy.mapping.RemoveLayer(df, lyr1)
            else:
                pass
        for lyr1 in arcpy.mapping.ListLayers(mxd, "*", df):
            if lyr1.name == 'Fence':
                arcpy.mapping.RemoveLayer(df, lyr1)
            else:
                pass
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        del mxd, df, newlayer
        print(folder)
    except:
        ValueError
        print(folder+' failed')




'''
for number in range(1,26):
    number_str=str(number)
    Address_base="D:\HK B\IB1000_COMPLETE\Extract\iB1_Shatin_J"+number_str+".gdb\CartoBuildingLine"
    Output_Address="D:\HK B\IB1000_COMPLETE\Extract\iB1_Shatin_J"+number_str+".gdb\CartoBuildingLine_modify"
    Fence_Address="D:\HK B\IB1000_COMPLETE\Extract\iB1_Shatin_J"+number_str+".gdb\Fence"
    try:
        #load cartobuildingline into map
        mxd=arcpy.mapping.MapDocument('CURRENT')

        df=arcpy.mapping.ListDataFrames(mxd,'*')[0]


        newlayer=arcpy.mapping.Layer(Address_base)

        arcpy.mapping.AddLayer(df,newlayer,"BOTTOM")


        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
    # select features and update

        CartoBuildingLine = "CartoBuildingLine"
        CartoBuildingLine__3_ = CartoBuildingLine
        CartoBuildingLine__2_ = CartoBuildingLine
        test_F = Fence_Address
        CartoBuildingLine__5_ = CartoBuildingLine__2_
        CartoBuildingLine__6_ = CartoBuildingLine__5_
        test_modify = Output_Address

        # Process: Select Layer By Attribute
        arcpy.SelectLayerByAttribute_management(CartoBuildingLine, "NEW_SELECTION", "BUILDINGLINETYPE = 'F'")

        # Process: Copy Features
        arcpy.CopyFeatures_management(CartoBuildingLine__3_, test_F, "", "0", "0", "0")

        # Process: Select Layer By Attribute (2)
        arcpy.SelectLayerByAttribute_management(CartoBuildingLine, "CLEAR_SELECTION", "")

        # Process: Select Layer By Attribute (3)
        arcpy.SelectLayerByAttribute_management(CartoBuildingLine__2_, "NEW_SELECTION",
                                                "BUILDINGLINETYPE = 'F' OR BUILDINGLINETYPE = 'OS'")

        # Process: Select Layer By Attribute (4)
        arcpy.SelectLayerByAttribute_management(CartoBuildingLine__5_, "SWITCH_SELECTION", "")

        # Process: Copy Features (2)
        arcpy.CopyFeatures_management(CartoBuildingLine__6_, test_modify, "", "0", "0", "0")

    # remove "Cartobuildingline" then working on next
        for lyr in arcpy.mapping.ListLayers(mxd,"*",df):
            if lyr.name=='CartoBuildingLine':
                arcpy.mapping.RemoveLayer(df,lyr)
            else:
                pass
        for lyr1 in arcpy.mapping.ListLayers(mxd,"*",df):
            if lyr1.name=='CartoBuildingLine_modify':
                arcpy.mapping.RemoveLayer(df,lyr1)
            else:
                pass
        for lyr1 in arcpy.mapping.ListLayers(mxd,"*",df):
            if lyr1.name=='Fence':
                arcpy.mapping.RemoveLayer(df,lyr1)
            else:
                pass
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        del mxd, df, newlayer

    except:ValueError
    print(number)
'''