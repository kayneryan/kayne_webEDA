#Kayne Ryan
#EDA for Maine Internet data

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

url_0 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-0-no-address-range-layer-jLQPM-g3RfNthOkroK_Mf.zip"
url_1 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-1-0-10-1-layer-2Vbn3XwU7ghduyFrvsX3i.zip"
url_2 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-2-10-1-25-3-layer-8lhS3piFE8p5Sof4IZ4C0.zip"
url_3 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-3-25-3-50-10-layer-axu8CkkozyfVxf5kjgcSY.zip"
url_4 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-4-50-10-100-100-layer--pCgIFfvOkurYcKDZ1Db7.zip"
url_5 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-5-100-m-layer-zo2lbPrGRte_B5Ug-kEqS.zip"

df_0 = gpd.read_file(url_0)
df_1 = gpd.read_file(url_1)
df_2 = gpd.read_file(url_2)
df_3 = gpd.read_file(url_3)
df_4 = gpd.read_file(url_4)
df_5 = gpd.read_file(url_5)

#In colab, I ran the .info() method for each dataframe to see number/names of columns
#to confirm the datasets could be merged
#df_0.info()
#df_1.info()
#df_2.info()
#df_3.info()
#df_4.info() I found two column names that needed to be changed
df_4 = df_4.rename(columns={'Street_Nam':'Street Name', 'Global_ID':'Global ID'})
#df_5.info()

all = [df_1, df_2, df_3, df_4, df_5]
combined = df_0
for i in range (len(all)):
  combined = combined.append(all[i])

#these columns all had 0 non-null entries and are thus erroneous to our analysis
droplist = ['mat_total_cost', 'lab_total_cost', 'mat_label', 'mat_description', 'mat_link', 'mat_part_number', 'mat_cost', 'mat_cost_metric', 'mat_manufacturer', 'mat_vendor', 'lab_label', 'lab_description', 'lab_cost', 'lab_fixed_cost', 'lab_cost_metric']
combined.drop(droplist, axis = 1, inplace = True)

#quality check on the resulting dataset
#we end up with a geoDataFrame object with 144253 rows and 9 columns
#combined.info()

#this gets us our plot. Adjusted the size to create more
combined.plot(column='v_layer', legend=True, figsize = (20, 30))

#save the figure
plt.savefig("ConnectivityLayers.jpg")

