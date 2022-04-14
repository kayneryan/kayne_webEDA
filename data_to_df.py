#Kayne Ryan
#Ingest Web Connectivity data, create dataframes

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import os

url_den_uns = "https://github.com/pbogden/broadband/raw/master/zipfiles/density-of-unserved-may-be-layer-UKtUhvoEC95KBH6HsnWIU.zip"
url_el_ar = "https://github.com/pbogden/broadband/raw/master/zipfiles/eligible-areas-2-22-layer-G8qemhB46k7dh-m1XZ2JM.zip"
url_gr_app = "https://github.com/pbogden/broadband/raw/master/zipfiles/grant-applications-layer-o-xxbSzyTNCM52P_VsBxG.zip"
url_mb_uns = "https://github.com/pbogden/broadband/raw/master/zipfiles/may-be-unserved-layer-gpC0SCaV9wS6W-zZCePjz.zip"
url_serv = "https://github.com/pbogden/broadband/raw/master/zipfiles/served-subscirber-locations-2-22-layer-9a3JpnMadKDLj_zPqDCkv.zip"
url_0 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-0-no-address-range-layer-jLQPM-g3RfNthOkroK_Mf.zip"
url_1 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-1-0-10-1-layer-2Vbn3XwU7ghduyFrvsX3i.zip"
url_2 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-2-10-1-25-3-layer-8lhS3piFE8p5Sof4IZ4C0.zip"
url_3 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-3-25-3-50-10-layer-axu8CkkozyfVxf5kjgcSY.zip"
url_4 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-4-50-10-100-100-layer--pCgIFfvOkurYcKDZ1Db7.zip"
url_5 = "https://github.com/pbogden/broadband/raw/master/zipfiles/tier-5-100-m-layer-zo2lbPrGRte_B5Ug-kEqS.zip"
url_und = "https://github.com/pbogden/broadband/raw/master/zipfiles/underserved-subscriber-locations-2-22-layer-hB7nPTjNUkTq5GppZ-zz0.zip"
url_uns_lay = "https://github.com/pbogden/broadband/raw/master/zipfiles/unserved-layer-R8i8goNVLFFHfh1Xun4rj.zip"
url_uns_sub = "https://github.com/pbogden/broadband/raw/master/zipfiles/unserved-subscriber-loactions-2-22-layer-fHdE-gCVA5OAEm5DCUt2P.zip"

print("check 1")

df_den_uns = gpd.read_file(url_den_uns)
print("pt 2")
df_el_ar = gpd.read_file(url_el_ar)
print("pt 3")
df_gr_app = gpd.read_file(url_gr_app)
print("pt 4")
df_mb_uns = gpd.read_file(url_mb_uns)
print("pt 5")
df_serv = gpd.read_file(url_serv) 
print("pt 6")
df_0 = gpd.read_file(url_0)
print("pt 7")
df_1 = gpd.read_file(url_1)
print("pt 8")
df_2 = gpd.read_file(url_2)
print("pt 9")
df_3 = gpd.read_file(url_3)
print("pt 10")
df_4 = gpd.read_file(url_4)
print("pt 11")
df_5 = gpd.read_file(url_5)
print("pt 12")
df_und = gpd.read_file(url_und)
print("pt 13")
df_uns_lay = gpd.read_file(url_uns_lay)
print("pt 14")
df_uns_sub = gpd.read_file(url_uns_sub) 
print("pt 15")


list1 = [df_den_uns, df_el_ar, df_gr_app, df_mb_uns, df_serv, df_0, df_1, df_2,
            df_3, df_4, df_5, df_und, df_uns_lay, df_uns_sub]

list2 = ["df_den_uns", "df_el_ar", "df_gr_app", "df_mb_uns", "df_serv", 
        "df_0", "df_1", "df_2", "df_3", "df_4", "df_5", 
        "df_und", "df_uns_lay", "df_uns_sub"]

for i in range(len(list1)):
    list1[i].to_file(list2[i]+".geojson", driver="geoJSON")

print ("done!")