# Import tkinter and feather at the top of the module
import tkinter as tk
import feather

# Define a function to create the GUI
def create_gui():
		# Read the schedule data from the .feather file
		df = feather.read_dataframe('schedule.feather')

		# Create a GUI window
		root = tk.Tk()

		# Add a label and a table to the GUI window
		label = tk.Label(root, text='My Schedule')
		table = tk.Frame(root)

		# Add a header row to the table
		header = tk.Frame(table)
		header.pack(side=tk.TOP)

		# Add a column for each field in the data frame
		for i, col in enumerate(df.columns):
				label = tk.Label(header, text=col)
				label.grid(row=0, column=i)

		# Add a row for each row in the data frame
		entries = []
		for i, row in df.iterrows():
				frame = tk.Frame(table)
				frame.pack(side=tk.TOP)
				
				# Add a cell for each field in the row
				entry_row = []
				for j, val in row.iteritems():
						entry = tk.Entry(frame)
						entry.pack(side=tk.LEFT)
						entry.insert(0, str(val))
						entry_row.append(entry)
				entries.append(entry_row)

		# Add a 'Save' button to the GUI
		def save_data():
				# Update the data frame with the data from the entries
				for i, row in enumerate(entries):
						for j, entry in enumerate(row):
								df.iloc[i, j] = entry.get()
				
				# Write the updated data frame to the .feather file
				feather.write_dataframe(df, 'schedule.feather')
				
		save_button = tk.Button(root, text='Save', command=save_data)
		save_button.pack()
		
		# Pack the label and table
#		label.pack()
		table.pack()
		
		# Run the GUI event loop
		root.mainloop()

# Call the create_gui function to create and display the GUI
create_gui()