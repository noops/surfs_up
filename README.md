# surfs_up

## resources:
data: hawaii.sqlite

software: visual studio code, python, sqlalchemy, sqlite, flask

## overview:
For this project temperature and precipitation data from hawaii.sqlite was analyzed in order to decide if opening a surf and icecream shop in Ohau, Hawaii. Within climate_analysis.ipynb tables from hawaii.sqlite are reflected into sqlalchemy. This climate data is explored, using data from several different weather stations on Ohau. The results can be viewed via flask from app.py. Flask is a great tool for this analysis because it allows for data to be shown and shared via a webpage. This is ideal for people who just want to access the results without seeing what is going on under the hood. The data shown via flask is from 2016-2017, it only uses data gained from the weather station with the most reports. Further analysis is completed for temperature and precipitation data from June 2010-2017 and December 2010-2017 incorporating all data from the 9 weather stations on Ohau.

## takeaways:
After breaking the data down into June and December we can see that the temperature on Ohau remains relatively consistent through out the year. The average temperature in June is 75 degrees farenheight versus 71 degrees in December. The maximum temperature in December across 8 years was 83 degrees versus 85 degrees in June. The temperature ranges for June are most likely going to be between 73 and 77 degrees versus between 69 and 74 degrees for December. Precipitation averages across both months are very low. Average precipitation in June is 0.14 inches versus 0.22 inches in December. Although December is slightly colder it is still surfing weather. A surf shop in Ohau is likely to be successful. 

## extra steps:
Further analysis could be done by creating graphs of weather data from individual stations on the island. The summary statistics gathered from June and December could be shown on a webpage via flask. A complete weather analysis from 2010-2017 may also be useful in addition to specific months. It may also be useful to gather data from when Hawaii is affected by a hurricane or tropical storm. This could help with making insurance decisions, and the location for the surf shop. It may not be prudent to build the surf shop if it is likely to be destroyed by a hurricane or tropical storm after a couple of years. 
