import pandas as pd
import feather

# Create a data frame with the schedule data
df = pd.DataFrame({
		'task': ['Wake up', 'Go surfing', 'Shower', 'Leave for school', 'Return home', 'Finish homework', 'Have a snack', 'Go to the gym', 'Prepare for bed', 'Go to sleep'],
		'start': ['6:00 AM', '6:30 AM', '7:30 AM', '8:00 AM', '3:00 PM', '5:00 PM', '7:30 PM', '8:30 PM', '10:15 PM', '10:45 PM'],
		'end': ['6:30 AM', '7:30 AM', '8:00 AM', '3:00 PM', '5:00 PM', '7:30 PM', '8:30 PM', '10:15 PM', '10:45 PM', '11:00 PM']
})

# Save the data frame to a .feather file
feather.write_dataframe(df, 'schedule.feather')