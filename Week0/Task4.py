

time_data = [
(3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0),
(4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5),
(5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0),
(3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0),
(4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0)
]


#Task4: Analyze Average Time Use

study_hrs = []
entertainment_hrs = []
sleep_hrs = []

for study,entertainment,sleep in time_data:
    study_hrs.append(study)
    entertainment_hrs.append(entertainment)
    sleep_hrs.append(sleep)

study_hrs_average = sum(study_hrs)/len(study_hrs)
entertainment_hrs_average = sum(entertainment_hrs)/len(entertainment_hrs)
sleep_hrs_average = sum(sleep_hrs)/len(sleep_hrs)

print(f"\nAverage hour spend studying: {study_hrs_average} ")
print(f"Average hour spend on entertainment: {entertainment_hrs_average} ")
print(f"Average hour spend on sleep: {sleep_hrs_average:.2f} ")
