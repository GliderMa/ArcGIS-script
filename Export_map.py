#script function: after load backgroundmap, export each estate with a symbol with rhw background map for current med file


import pandas as pd
import arcpy

filepath='D:/HK B/All_estate_info.csv'
df=pd.read_csv(filepath)





for i in range(0,len(df),1):
    #collect necessary info
    estate=df.at[i,'Estate_name']
    region=df.at[i,'District']
    type=df.at[i,'TYPE_']
    intake_year=df.at[i,'Year_of_Intake']
    completion_year=df.at[i,'Year_of_Completion']
    block_num=df.at[i,'No__of_Blocks']

    #necessary convert
    SQL='Estate_name='+"'"+estate+"'"

    #firstline info works for all estate
    firstline = estate + ', ' + region

    #secondline info check
    #test building number info
    try:
        int_block_num=int(block_num)
        str_block_num=str(int_block_num)
        if int_block_num>1:
            secondline=str_block_num+' Blocks, '+type
        else:
            secondline = str_block_num + ' Block, ' + type

    except:
        ValueError
        secondline=type
    #thirdline info check
    if pd.isnull(df.at[i,'Year_of_Intake'])==True:
        if  pd.isnull(df.at[i,'Year_of_Completion'])==True:
            thirdline=''
        else:
            int_completion_year=int(completion_year)
            str_comp_year=str(int_completion_year)
            thirdline='Completion Year: '+str_comp_year
    else:
        str_year = str(intake_year)
        thirdline = 'Intake year: ' + str_year

    newtext=firstline+'\n'+secondline+'\n'+thirdline
    #print(newtext)

    #the filename of point shapefile
    a=estate.split()
    b='_'.join(a)
    c=b.split('(')
    d='_'.join(c)
    e=d.split(')')
    filename='_'.join(e)




    try:
        # load the point into map
        mxd = arcpy.mapping.MapDocument('CURRENT')
        Address_base ='D:/HK B/Estate_points.gdb/'+filename

        dataframe=arcpy.mapping.ListDataFrames(mxd)[0]

        newlayer = arcpy.mapping.Layer(Address_base)

        arcpy.mapping.AddLayer(dataframe, newlayer, "TOP")

        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

        # set point as green square point
        EstatePoint = filename
        EstatePoint_lyr = "D:/HK B/LayerTemplate/EstatePoint.lyr"
        arcpy.ApplySymbologyFromLayer_management(EstatePoint, EstatePoint_lyr)

        # HOW TO SELECT A POINT, ZOOM TO AS A FIX SCALE

        arcpy.SelectLayerByAttribute_management(EstatePoint, "NEW_SELECTION", SQL)

        dataframe.zoomToSelectedFeatures()
        dataframe.scale=5000
        arcpy.SelectLayerByAttribute_management(EstatePoint, "CLEAR_SELECTION", SQL)



        #how to change text
        elm=arcpy.mapping.ListLayoutElements(mxd,'TEXT_ELEMENT')
        oldtext='aaaaaaaaaaaaaaaaaaaaa'

        for object in elm:
            #print(object.name)
            if oldtext not in object.text:

                object.text=newtext
        arcpy.RefreshActiveView()


        #Export map as vector PDF
        outputname='D:/HK B/MapsforPDF/'+estate+'_'+region+'.pdf'
        arcpy.mapping.ExportToPDF(mxd,outputname,picture_symbol='VECTORIZE_BITMAP')

        #remove the point
        for lyr in arcpy.mapping.ListLayers(mxd, "*", dataframe):
            if lyr.name == filename:
                arcpy.mapping.RemoveLayer(dataframe, lyr)
            else:
                pass
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

        del mxd, dataframe, newlayer
        print(estate + 'done')
    except:
        ValueError
        print(estate+ 'error')



