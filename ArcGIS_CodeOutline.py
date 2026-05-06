#ArcGIS Pro python code for processing WorldCover rasters
import arcpy

arcpy.env.workspace = "D:\StateName\DataFolder"

from arcpy.ia import *
from arcpy.sa import *

# Download the landcover rasters from WorldCover for each state
# Download blocks for each state
# Get names of all rasters to merge into one file
# Set input rasters
in_raster1 = arcpy.Raster("ESA_WorldCover_10m_2021_v200_N42W072_Map.tif")
in_raster2 = arcpy.Raster(...)
#...
#Import blocks shapefile
blocks = "tl_2021_44_tabblock20.shp" 

#Mosaic to New Raster
mosaic_to_new = arcpy.management.MosaicToNewRaster([in_raster1,in_raster2, ...], "D:/StateName/DataFolder", "mosaic_landcover.tif", "", "8_BIT_UNSIGNED", "0.000083", "1", "LAST", "FIRST")
full_landcover = "mosaic_landcover.tif"

#Extract by mask to extent of blocks of state
state_LC_extent = ExtractByMask(full_landcover, blocks, "INSIDE")
state_LC_extent.save("state_landcover_clipped.tif")

#Reclassify to green and not green
# 10 = 1, 20 = 1, 30 = 1, 90 = 1, 95 = 1, 100 = 1; other = 0  
outReclass = Reclassify(state_LC_extent, "Value", RemapValue([[10,1],[20,1],[30,1],[40,0],[50,0],[60,0],[80,0],[90,1],[95,1],[100,1]]))
outReclass.save("StateName_reclass.tif")

#Add empty fields w_geocode and h_geocode
arcpy.management.AddField(blocks, "w_geocode", "DOUBLE")
arcpy.management.AddField(blocks, "h_geocode", "DOUBLE")

#Run Zonal Statitsics as Table manually to get percentages

#Join Zonal table to Blocks manually

#Export table manually for processing in R.
#Make sure to project the file when exporting to USA Albers Equal Area Conic.
#Name final output StateInitial_Green_Blocks.shp


