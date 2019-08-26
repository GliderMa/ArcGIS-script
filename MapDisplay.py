#function: load backgrondlayers orderlly as a stereotype

import arcpy
import arcpy.mapping

#dataset="Kow_J9"
Dataset_Address="D:/HK B/MapElements.gdb/merged_full_"
#Estate_Folder='D:/HK B/Estates.gdb/'
#Estate_name='Sun_Chui_Shatin'
layer_list=['Building','CartoTransLine','CartoPedLine','BuiltStructureLine','Fence','CartoBuildingLine_modify','BuiltStructurePolygon',
            'Site','IndexContour','Contour','Shoreline','HydroPolygon','BMSslope']
try:

    #load estate layers into map
    mxd = arcpy.mapping.MapDocument('CURRENT')
    df = arcpy.mapping.ListDataFrames(mxd, '*')[0]
    '''
    Estate_Address=Estate_Folder+Estate_name
    newlayer = arcpy.mapping.Layer(Estate_Address)
    arcpy.mapping.AddLayer(df, newlayer, "BOTTOM")
    '''
    # other layers
    for lyr in layer_list:
        Full_Address=Dataset_Address+lyr
        newlayer=arcpy.mapping.Layer(Full_Address)
        arcpy.mapping.AddLayer(df,newlayer,"BOTTOM")
        print(lyr+' done')
    print('load done')
except:
    ValueError
    print('load error')


try:
    #adjust layer format
    #Estate=Estate_name
    Building='merged_full_Building'
    CartoTransLine='merged_full_CartoTransLine'
    CartoPedLine='merged_full_CartoPedLine'
    BuiltStructureLine='merged_full_BuiltStructureLine'
    Fence='merged_full_Fence'
    CartoBuildingLine_modify='merged_full_CartoBuildingLine_modify'
    BuiltStructurePolygon='merged_full_BuiltStructurePolygon'
    Site='merged_full_Site'
    IndexContour='merged_full_IndexContour'
    Contour='merged_full_Contour'
    Shoreline='merged_full_Shoreline'
    HydroPolygon='merged_full_HydroPolygon'
    BMSslope='merged_full_BMSslope'


    #EstateBuilding_lyr = "D:/HK B/LayerTemplate/EstateBuilding.lyr"
    OtherBuilding_lyr = "D:/HK B/LayerTemplate/OtherBuilding.lyr"
    CartoTransLine_lyr="D:/HK B/LayerTemplate/CartoTransLine.lyr"
    CartoPedLine_lyr = "D:/HK B/LayerTemplate/CartoPedLine.lyr"
    BuiltStructureLine_lyr = "D:/HK B/LayerTemplate/BuiltStructureLine.lyr"
    Fence_lyr = "D:/HK B/LayerTemplate/Fence.lyr"
    CartoBuildingLine_modify_lyr = "D:/HK B/LayerTemplate/CartoBuildingLine_modify.lyr"
    BuiltStructurePolygon_lyr = "D:/HK B/LayerTemplate/BuiltStructurePolygon.lyr"
    Site_lyr = "D:/HK B/LayerTemplate/Site.lyr"
    IndexContour_lyr = "D:/HK B/LayerTemplate/IndexContour.lyr"
    Contour_lyr = "D:/HK B/LayerTemplate/Contour.lyr"
    Shoreline_lyr="D:/HK B/LayerTemplate/Shoreline.lyr"
    HydroPolygon_lyr = "D:/HK B/LayerTemplate/HydroPolygon.lyr"
    BMSslope_lyr = "D:/HK B/LayerTemplate/BMSslope.lyr"


    #arcpy.ApplySymbologyFromLayer_management(Estate, EstateBuilding_lyr)
    arcpy.ApplySymbologyFromLayer_management(Building, OtherBuilding_lyr)
    arcpy.ApplySymbologyFromLayer_management(CartoTransLine, CartoTransLine_lyr)
    arcpy.ApplySymbologyFromLayer_management(CartoPedLine, CartoPedLine_lyr)
    arcpy.ApplySymbologyFromLayer_management(BuiltStructureLine, BuiltStructureLine_lyr)
    arcpy.ApplySymbologyFromLayer_management(Fence, Fence_lyr)
    arcpy.ApplySymbologyFromLayer_management(CartoBuildingLine_modify, CartoBuildingLine_modify_lyr)
    arcpy.ApplySymbologyFromLayer_management(BuiltStructurePolygon, BuiltStructurePolygon_lyr)
    arcpy.ApplySymbologyFromLayer_management(Site, Site_lyr)
    arcpy.ApplySymbologyFromLayer_management(IndexContour, IndexContour_lyr)
    arcpy.ApplySymbologyFromLayer_management(Contour, Contour_lyr)
    arcpy.ApplySymbologyFromLayer_management(Shoreline, Shoreline_lyr)
    arcpy.ApplySymbologyFromLayer_management(HydroPolygon, HydroPolygon_lyr)
    arcpy.ApplySymbologyFromLayer_management(BMSslope, BMSslope_lyr)


    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

    del mxd, df, newlayer


except:ValueError
