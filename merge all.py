#function: merge all discreate tiles to a seamless tile
import arcpy
import arcpy.mapping
import os


'''
working_pipeline=[['Building','BUILDINGID'],['CartoTransLine','CARTOTRANSPORTATIONLINEID'],['CartoPedLine','CARTOPEDESTRIANLINEID'],['BuiltStructureLine','BUILTSTRUCTURELINEID'],['Fence','CARTOBUILDINGLINEID'],
['CartoBuildingLine_modify','CARTOBUILDINGLINEID'],['BuiltStructurePolygon','BUILTSTRUCTUREPOLYGONID'],['Shoreline','SHORELINEID'],
['Site','SITEID;SITESTYPE'],['IndexContour','CONTOURID'],['Contour','CONTOURID'],['HydroPolygon','HYDROPOLYGONID'],['BMSslope','BMSSLOPEID']]
'''
# Site need to identify sitetype as well
working_pipeline=[['BuildingAnno','FeatureID;AnnotationClassID;TextString']]
# get folder name

path='D:/HK B/IB1000_COMPLETE/Extract'
a=os.listdir(path)
folder_list=[]
for i in range(1,140):
    folder_list.append(a[i])

for element in working_pipeline:

    layer=element[0]
    UniqueID=element[1]




    raw_address="D:/HK B/IB1000_COMPLETE/Extract/11-NW-1D/11-NW-1D.gdb/"+layer
    append_address='D:/HK B/MapElements.gdb/append_'+layer
    output_address ='D:/HK B/MapElements.gdb/merged_'+layer
    arcpy.CopyFeatures_management(raw_address, append_address, "", "0", "0", "0")
    #append the first part
    for folder in folder_list:
        Address_base = path + '/' + folder + '/' + folder + '.gdb/'+layer
        try:

            arcpy.Append_management(Address_base,
                                    append_address, "TEST", "", "")
            print(folder+'append '+layer+' done')
        except:
            ValueError
            print(folder + 'error on' +layer)

    #Kowlong part
    for number in range(1, 29):
        number_str = str(number)
        Address_base=path+'/iB1_Kow_J'+number_str+'.gdb/'+layer
        try:

            arcpy.Append_management(Address_base,
                                    append_address, "TEST", "", "")
            print('Kow'+number_str+'append '+layer+' done')
        except:
            ValueError
            print('Kow'+number_str + 'error on' +layer)
    #Shatin part
    for number in range(1, 27):
        number_str = str(number)
        Address_base=path+'/iB1_Shatin_J'+number_str+'.gdb/'+layer
        try:

            arcpy.Append_management(Address_base,
                                    append_address, "TEST", "", "")
            print('Shatin'+number_str+'append '+layer+' done')
        except:
            ValueError
            print('Shatin'+number_str + 'error on' +layer)
    for number in range(1, 17):
        number_str = str(number)
        Address_base=path+'/iB1_Tsuen_J'+number_str+'.gdb/'+layer
        try:

            arcpy.Append_management(Address_base,
                                    append_address, "TEST", "", "")
            print('Tsuen'+number_str+'append '+layer+' done')
        except:
            ValueError
            print('Tsuen'+number_str + 'error on' +layer)
    print('append '+layer+' work done')

    try:
        arcpy.Dissolve_management(append_address, output_address, UniqueID, "", "MULTI_PART",
                                  "DISSOLVE_LINES")
        print(layer+' successed')
    except:
        ValueError
        print('dissolve '+layer+ ' error')