#function: export IndexContour

# Import arcpy module
import arcpy

'''
# Local variables:
Contour = "D:\HK B\IB1000_COMPLETE\Extract\iB1_Kow_J1.gdb\Contour"
Contour__2_ = Contour
test = "D:/HK B/contour.gdb/test1"

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(Contour, "NEW_SELECTION", "FEATURETYPE = 'CIS' OR FEATURETYPE = 'CIU'")

# Process: Copy Features
arcpy.CopyFeatures_management(Contour__2_, test, "", "0", "0", "0")

'''
import arcpy
import arcpy.mapping
import os

path='D:/HK B/IB1000_COMPLETE/Extract'
a=os.listdir(path)
folder_list=[]
for i in range(0,139):
    folder_list.append(a[i])

for folder in folder_list:
    Address_base = path + '/' + folder + '/' + folder + '.gdb/Contour'
    Output_Address=path + '/' + folder + '/' + folder + '.gdb/IndexContour'
    try:
        # load contour into map
        mxd = arcpy.mapping.MapDocument('CURRENT')

        df = arcpy.mapping.ListDataFrames(mxd, '*')[0]

        newlayer = arcpy.mapping.Layer(Address_base)

        arcpy.mapping.AddLayer(df, newlayer, "BOTTOM")

        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

        # select features and update

        Contour = 'Contour'
        Contour__2_ = Contour
        arcpy.SelectLayerByAttribute_management(Contour, "NEW_SELECTION", "FEATURETYPE = 'CIS' OR FEATURETYPE = 'CIU'")
        arcpy.CopyFeatures_management(Contour__2_, Output_Address, "", "0", "0", "0")

        # remove "Contour" then working on next
        for lyr in arcpy.mapping.ListLayers(mxd, "*", df):
            if lyr.name == 'Contour':
                arcpy.mapping.RemoveLayer(df, lyr)
            else:
                pass
        for lyr1 in arcpy.mapping.ListLayers(mxd, "*", df):
            if lyr1.name == 'IndexContour':
                arcpy.mapping.RemoveLayer(df, lyr1)
            else:
                pass
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        del mxd, df, newlayer

    except:
        ValueError
    print(folder)

'''
for number in range(1,17):
    number_str=str(number)
    Address_base="D:\HK B\IB1000_COMPLETE\Extract\iB1_Tsuen_J"+number_str+".gdb\Contour"
    Output_Address="D:\HK B\IB1000_COMPLETE\Extract\iB1_Tsuen_J"+number_str+".gdb\IndexContour"
    try:
        #load contour into map
        mxd=arcpy.mapping.MapDocument('CURRENT')

        df=arcpy.mapping.ListDataFrames(mxd,'*')[0]


        newlayer=arcpy.mapping.Layer(Address_base)

        arcpy.mapping.AddLayer(df,newlayer,"BOTTOM")


        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

    # select features and update

        Contour='Contour'
        Contour__2_=Contour
        arcpy.SelectLayerByAttribute_management(Contour, "NEW_SELECTION", "FEATURETYPE = 'CIS' OR FEATURETYPE = 'CIU'")
        arcpy.CopyFeatures_management(Contour__2_, Output_Address, "", "0", "0", "0")

    # remove "Contour" then working on next
        for lyr in arcpy.mapping.ListLayers(mxd,"*",df):
            if lyr.name=='Contour':
                arcpy.mapping.RemoveLayer(df,lyr)
            else:
                pass
        for lyr1 in arcpy.mapping.ListLayers(mxd,"*",df):
            if lyr1.name=='IndexContour':
                arcpy.mapping.RemoveLayer(df,lyr1)
            else:
                pass
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        del mxd, df, newlayer

    except:ValueError
    print(number)

'''

