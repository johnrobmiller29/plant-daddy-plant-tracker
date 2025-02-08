import tkinter as tk

# Constants for font styles and colors
TITLE_FONT = ('Helvetica', 18, 'bold')
BUTTON_FONT = ('Helvetica', 10, 'bold')
LABEL_FONT = ('Helvetica', 10, 'bold')
BACKGROUND = 'grey'
FOREGROUND = 'dark green'


class AddPlantUI:
    """
       User Interface class for adding a new plant entry from the Plant Daddy application.

       This class provides a window where users can input information about their plants and
       have the data saved locally to a .txt file.
       """
    def __init__(self, main_menu_callback):
        """
                Initialize the add plant interface and create the layout, title, entry form, and
                the button frame.

                Parameters:
                main_menu_callback (function): Callback function to return to the main menu.
                """
        self.main_menu_callback = main_menu_callback
        self.add_menu = tk.Toplevel()
        self.add_menu.title("Add Plant")

        self.title_frame = tk.Frame(self.add_menu)
        self.form_frame = tk.Frame(self.add_menu)
        self.button_frame = tk.Frame(self.add_menu)

        # Create the title frame containing the window title.
        self.title_canvas = tk.Canvas(self.title_frame, width=300, height=60)
        self.title_canvas.create_rectangle(75, 20, 225, 60, outline='dark green', width=2, fill='grey')
        self.title_canvas.create_text(150, 40, text='Add Plant', font=TITLE_FONT, fill='dark green', justify='center')
        self.title_canvas.pack()

        self.title_frame.pack()

        # Create the entry form frame containing all relevant data for Plant Daddy.
        self.name_label = tk.Label(self.form_frame, text='Plant Name:', font=LABEL_FONT, fg=FOREGROUND)
        self.name_entry = tk.Entry(self.form_frame, width=20)
        self.name_label.grid(row=0, column=0, padx=5, pady=2, sticky='e')
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)

        self.sci_name_label = tk.Label(self.form_frame, text='Scientific Name:', font=LABEL_FONT, fg=FOREGROUND)
        self.sci_name_entry = tk.Entry(self.form_frame, width=20)
        self.sci_name_label.grid(row=1, column=0, padx=5, pady=2, sticky='e')
        self.sci_name_entry.grid(row=1, column=1, padx=5, pady=2)

        self.com_name_label = tk.Label(self.form_frame, text='Common Name:', font=LABEL_FONT, fg=FOREGROUND)
        self.com_name_entry = tk.Entry(self.form_frame, width=20)
        self.com_name_label.grid(row=2, column=0, padx=5, pady=2, sticky='e')
        self.com_name_entry.grid(row=2, column=1, padx=5, pady=2)

        self.water_req_label = tk.Label(self.form_frame, text='Water Requirements:', font=LABEL_FONT, fg=FOREGROUND)
        self.water_req_entry = tk.Entry(self.form_frame, width=20)
        self.water_req_label.grid(row=3, column=0, padx=5, pady=2, sticky='e')
        self.water_req_entry.grid(row=3, column=1, padx=5, pady=2)

        self.sun_req_label = tk.Label(self.form_frame, text='Sun Requirements:', font=LABEL_FONT, fg=FOREGROUND)
        self.sun_req_entry = tk.Entry(self.form_frame, width=20)
        self.sun_req_label.grid(row=4, column=0, padx=5, pady=2, sticky='e')
        self.sun_req_entry.grid(row=4, column=1, padx=5, pady=2)

        self.soil_req_label = tk.Label(self.form_frame, text='Soil Requirements:', font=LABEL_FONT, fg=FOREGROUND)
        self.soil_req_entry = tk.Entry(self.form_frame, width=20)
        self.soil_req_label.grid(row=5, column=0, padx=5, pady=2, sticky='e')
        self.soil_req_entry.grid(row=5, column=1, padx=5, pady=2)

        self.fert_pref_label = tk.Label(self.form_frame, text='Fertilizer Preferences:', font=LABEL_FONT, fg=FOREGROUND)
        self.fert_pref_entry = tk.Entry(self.form_frame, width=20)
        self.fert_pref_label.grid(row=6, column=0, padx=5, pady=2, sticky='e')
        self.fert_pref_entry.grid(row=6, column=1, padx=5, pady=2)

        self.notes_label = tk.Label(self.form_frame, text='Notes:', font=LABEL_FONT, fg=FOREGROUND)
        self.notes_entry = tk.Entry(self.form_frame, width=20)
        self.notes_label.grid(row=7, column=0, padx=5, pady=2, sticky='e')
        self.notes_entry.grid(row=7, column=1, padx=5, pady=2)

        self.form_frame.pack()

        # Create a label to display messages to the user.
        self.message_label = tk.Label(self.add_menu, text='', font=LABEL_FONT, fg='dark green')
        self.message_label.pack()

        # Create the button frame containing the add and return buttons.
        self.add_plant = tk.Button(self.button_frame, text='Add Plant', font=BUTTON_FONT,
                                   bg=BACKGROUND, fg=FOREGROUND, command=self.save_plant)
        self.return_button = tk.Button(self.button_frame, text='Return to Main Menu', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.return_to_main)
        self.add_plant.pack(pady=2)
        self.return_button.pack()

        self.button_frame.pack(pady=5)

    def save_plant(self):
        """
                Save the plant details to the file if all required fields are filled.
                """
        plant_name = self.name_entry.get()
        sci_name = self.sci_name_entry.get()
        com_name = self.com_name_entry.get()
        water_req = self.water_req_entry.get()
        sun_req = self.sun_req_entry.get()
        soil_req = self.soil_req_entry.get()
        fert_pref = self.fert_pref_entry.get()
        notes = self.notes_entry.get()

        if (not plant_name or not sci_name or not com_name or not water_req
                or not sun_req or not soil_req or not fert_pref):
            self.message_label.config(text="All fields except notes are required.")
            return

        try:
            with open('plants.txt', 'a') as file:
                file.write(f'Plant Name: {plant_name}\n')
                file.write(f'Scientific Name: {sci_name}\n')
                file.write(f'Common Name: {com_name}\n')
                file.write(f'Water Requirements: {water_req}\n')
                file.write(f'Sun Requirements: {sun_req}\n')
                file.write(f'Soil Requirements: {soil_req}\n')
                file.write(f'Fertilizer Preferences: {fert_pref}\n')
                file.write(f'Notes: {notes}\n')
                file.write('--------------------\n')
                self.message_label.config(text="Plant added successfully!")
        except Exception as e:
            self.message_label.config(text=f"An error occurred: {e}")

        self.name_entry.delete(0, tk.END)
        self.sci_name_entry.delete(0, tk.END)
        self.com_name_entry.delete(0, tk.END)
        self.water_req_entry.delete(0, tk.END)
        self.sun_req_entry.delete(0, tk.END)
        self.soil_req_entry.delete(0, tk.END)
        self.fert_pref_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)

    def return_to_main(self):
        """
                Close the AddPlantUI window and return to the main menu.
                """
        self.add_menu.destroy()
        if self.main_menu_callback:
            self.main_menu_callback()
