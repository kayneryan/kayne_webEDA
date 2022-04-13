#Kayne Ryan
#EDA for Maine Internet data

from click import style
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import webbrowser as wb


url_den_uns = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/density-of-unserved-may-be-layer-UKtUhvoEC95KBH6HsnWIU.zip"
url_el_ar = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/eligible-areas-2-22-layer-G8qemhB46k7dh-m1XZ2JM.zip"
url_gr_app = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/grant-applications-layer-o-xxbSzyTNCM52P_VsBxG.zip"
url_mb_uns = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/may-be-unserved-layer-gpC0SCaV9wS6W-zZCePjz.zip"
url_serv = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/served-subscirber-locations-2-22-layer-9a3JpnMadKDLj_zPqDCkv.zip"
url_0 = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/tier-0-no-address-range-layer-jLQPM-g3RfNthOkroK_Mf.zip"
url_1 = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/tier-1-0-10-1-layer-2Vbn3XwU7ghduyFrvsX3i.zip"
url_2 = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/tier-2-10-1-25-3-layer-8lhS3piFE8p5Sof4IZ4C0.zip"
url_3 = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/tier-3-25-3-50-10-layer-axu8CkkozyfVxf5kjgcSY.zip"
url_4 = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/tier-4-50-10-100-100-layer--pCgIFfvOkurYcKDZ1Db7.zip"
url_5 = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/tier-5-100-m-layer-zo2lbPrGRte_B5Ug-kEqS.zip"
url_und = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/underserved-subscriber-locations-2-22-layer-hB7nPTjNUkTq5GppZ-zz0.zip"
url_uns_lay = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/unserved-layer-R8i8goNVLFFHfh1Xun4rj.zip"
url_uns_sub = "/Users/kayneryan/Roux/DS5010/GitHub/kayne_webEDA/data/unserved-subscriber-loactions-2-22-layer-fHdE-gCVA5OAEm5DCUt2P.zip"

#df_den_uns = gpd.read_file(url_den_uns)
#df_el_ar = gpd.read_file(url_el_ar)
#df_gr_app = gpd.read_file(url_gr_app)
#df_mb_uns = gpd.read_file(url_mb_uns)
##df_serv = gpd.read_file(url_serv) 
df_0 = gpd.read_file(url_0)
df_1 = gpd.read_file(url_1)
df_2 = gpd.read_file(url_2)
df_3 = gpd.read_file(url_3)
df_4 = gpd.read_file(url_4)
df_5 = gpd.read_file(url_5)
#df_und = gpd.read_file(url_und)
#df_uns_lay = gpd.read_file(url_uns_lay)
#df_uns_sub = gpd.read_file(url_uns_sub) 

#df_den_uns_sm = df_den_uns[["v_layer", "geometry"]]
#df_el_ar_sm = df_el_ar[["v_layer", "geometry"]]
##df_gr_app_sm = df_gr_app[["v_layer", "geometry"]]
#df_mb_uns_sm = df_mb_uns[["v_layer", "geometry"]]
#df_serv_sm = df_serv[["v_layer", "geometry"]]
df_0_sm = df_0[["v_layer", "geometry"]]
df_1_sm = df_1[["v_layer", "geometry"]]
df_2_sm = df_2[["v_layer", "geometry"]]
df_3_sm = df_3[["v_layer", "geometry"]]
df_4_sm = df_4[["v_layer", "geometry"]]
df_5_sm = df_5[["v_layer", "geometry"]]
#df_und_sm = df_und[["v_layer", "geometry"]]
#df_uns_lay_sm = df_uns_lay[["v_layer", "geometry"]]
#df_uns_sub_sm = df_uns_sub [["v_layer", "geometry"]]
print("check 1")

m = folium.Map(location=[43.66, -70.26],
    zoom_start=12, control_scale=True, min_lat = -72, 
    max_lat = -66, min_lon = 42, max_long = 48)

# Convert points to GeoJSON
df_0_gjson = folium.features.GeoJson(df_0_sm, name="Tier 0 (No Address Range)")
#df_0_gjson.setStyle(color = "#e01709")
df_0_gjson.add_to(m)

df_1_gjson = folium.features.GeoJson(df_1_sm, name="Tier 1 (0 - 10/1)")
df_1_gjson.add_to(m)

df_2_gjson = folium.features.GeoJson(df_2_sm, name="Tier 2 (10/1 - 25/3")
df_2_gjson.add_to(m)

df_3_gjson = folium.features.GeoJson(df_3_sm, name="Tier 3 (25/3 - 50/10)")
df_3_gjson.add_to(m)

df_4_gjson = folium.features.GeoJson(df_4_sm, name="Tier 4 (50/10 - 100/100)")
df_4_gjson.add_to(m)

df_5_gjson = folium.features.GeoJson(df_5_sm, name="Tier 5 (> 100M)")
df_5_gjson.add_to(m)

m.fit_bounds([(-72,42), (-66, 48) ])

folium.LayerControl().add_to(m)

m.save("Internet_in_ME.html")
wb.open("src/Internet_in_ME.html", new=1)

print("done!")