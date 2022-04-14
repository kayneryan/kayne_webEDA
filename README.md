# Initial exploratory data analysis for Maine Web Connectivity project

## Purpose
Our class has been tasked with analyzing data from the Maine DOT related to internet connectivity capabilities 
(or lack thereof) across localities in Maine. Specifically, we are going to:
* analyze current investments
* demonstrate community readiness
* highlight unconnected/unserved areas
* demonstrate connectivity in context of other socioeconomic demographics
* represent wireless offerings in context of unconnected/unserved


## Process
This initial analysis examines six of the datasets made available to our class and plots them on a map.  
The six datasets include 'Tier 0', 'Tier 1', 'Tier 2', 'Tier 3', 'Tier 4', and 'Tier 5' in their filenames, so I wanted to explore if indeed they were related to one another.  
I created geoPandas dataframes for each dataset and identified basic information about them. I then cleaned up two column names so that everything could merge cleanly.  
I then merged the datasets together, and removed erroneous columns that contained no data within them. 

Finally, I plotted the combined dataset and included a legend so the viewer can see what each tier means and how they layer on top of one another. 

## Payoff
The result is a map of Maine, with what appears to be streets highlighted in different colors. There is little information beyond the tier names to suggest what they mean, so further analysis is needed. 

![map of connectivity tiers in Maine](https://github.com/kayneryan/kayne_webEDA/raw/main/src/ConnectivityLayers.jpg)


## Bonus interactive map - view the [GH Pages site](https://kayneryan.github.io/kayne_webEDA/)
  
This file shows an interactive map with Tiers 1-5 of the data, where the user can toggle each layer. I tried to assign different colors to each layer but couldn't figure out how, and I could only do Tiers 1-5 to fit underneath the 100MB hosting limit set by GitHub. 

