import pandas as pd
taxi = pd.read_csv("https://stepik.org/media/attachments/lesson/360340/2_taxi_nyc.csv")
taxi = taxi.rename(columns={"pcp 01": "pcp_01",
                     "pcp 06": "pcp_06",
                     "pcp 24": "pcp_24"})

grouped = taxi.groupby(["borough", "hday"])["pickups"].sum()
min_pickups = grouped.idxmin()
print(min_pickups)