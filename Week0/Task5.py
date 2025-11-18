import matplotlib.pyplot as plt

time_data = [
(3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0),
(4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5),
(5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0),
(3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0),
(4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0)
]


#Task5: Visualization - Study vs Sleep Pattern

study_hrs = []
sleep_hrs = []

for study,entertainment,sleep in time_data:
    study_hrs.append(study)
    sleep_hrs.append(sleep)

plt.figure(figsize=(10, 6))

plt.scatter(study_hrs, sleep_hrs,
            color='deepskyblue',   
            s=100,                 
            alpha=0.8,             
            edgecolors='black',  
            linewidth=1)

plt.title("Study hrs vs Sleep hrs", fontsize=16, fontweight="bold")
plt.xlabel("Study hrs per day", fontsize=12)
plt.ylabel("Sleep hrs per day", fontsize=12)


plt.show()