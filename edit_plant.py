import tkinter as tk
import utilities

# Constants for font styles and colors
TITLE_FONT = ('Helvetica', 18, 'bold')
BUTTON_FONT = ('Helvetica', 10, 'bold')
LABEL_FONT = ('Helvetica', 10, 'bold')
BACKGROUND = 'grey'
FOREGROUND = 'dark green'


class EditPlantUI:
    """
           User Interface class for editing an existing plant entry from the Plant Daddy application.

           This class provides a window where users can search for a plant, have the information
           displayed, and edit/save the entries from the same menu
           """
    def __init__(self, main_menu_callback):
        """
                Initialize the edit plant interface and create the layout, title, search bar, edit form, and
                the button frame.

                Parameters:
                main_menu_callback (function): Callback function to return to the main menu.
                """
        self.main_menu_callback = main_menu_callback
        self.edit_menu = tk.Toplevel()
        self.edit_menu.title("Edit Plant")

        self.title_frame = tk.Frame(self.edit_menu)
        self.search_frame = tk.Frame(self.edit_menu)
        self.edit_frame = tk.Frame(self.edit_menu)
        self.button_frame = tk.Frame(self.edit_menu)

        # Create the title frame containing the window title.
        self.title_canvas = tk.Canvas(self.title_frame, width=300, height=60)
        self.title_canvas.create_rectangle(75, 20, 225, 60, outline='dark green', width=2, fill='grey')
        self.title_canvas.create_text(150, 40, text='Edit Plant', font=TITLE_FONT, fill='dark green',
                                      justify='center')
        self.title_canvas.pack()

        self.title_frame.pack()

        # Create the search frame containing the search entry and button.
        self.search_label = tk.Label(self.search_frame, text='Enter Plant Name To Edit',
                                     font=LABEL_FONT, fg=FOREGROUND)
        self.search_label.pack(pady=5)

        self.search_entry = tk.Entry(self.search_frame, width=20)
        self.search_button = tk.Button(self.search_frame, text='Search', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.search_plant)
        self.search_entry.pack(side='left', padx=5)
        self.search_button.pack(side='left')

        self.search_frame.pack(pady=5)

        # Create the edit frame for the search_plant method to populate.
        self.edit_frame.pack()

        # Create a label to display messages to the user.
        self.message_label = tk.Label(self.edit_menu, text='', font=LABEL_FONT, fg='dark green')
        self.message_label.pack()

        # Create the button frame containing the save and return buttons.
        self.save_button = tk.Button(self.button_frame, text='Save Changes', font=BUTTON_FONT,
                                     bg=BACKGROUND, fg=FOREGROUND, command=self.save_changes)
        self.return_button = tk.Button(self.button_frame, text='Return to Main Menu', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.return_to_main)
        self.save_button.pack(pady=2)
        self.return_button.pack()

        self.button_frame.pack(pady=5)

        # Used to initialize widget dictionary to be created in the search_plant function
        self.entry_widgets = {}

        self.selected_plant = None

    def search_plant(self):
        """
                Search for a plant by name and display its details for editing.
                """
        search_term = self.search_entry.get()
        results = utilities.search_in_file(search_term)
        self.message_label.config(text='')

        self.entry_widgets = {}
        for widget in self.edit_frame.winfo_children():
            widget.destroy()

        if search_term == '':
            self.message_label.config(text="Must enter a keyword to search.")
            self.edit_frame.pack_forget()
        elif results and isinstance(results[0], dict):
            self.message_label.pack_forget()
            self.button_frame.pack_forget()
            self.edit_frame.pack()
            self.message_label.pack()
            self.button_frame.pack()
            self.selected_plant = results[0]
            for key, value in self.selected_plant.items():
                label = tk.Label(self.edit_frame, text=key, font=LABEL_FONT, fg=FOREGROUND)
                label.grid(row=len(self.entry_widgets), column=0, sticky='e')
                entry = tk.Entry(self.edit_frame, width=50)
                entry.insert(0, value)
                entry.grid(row=len(self.entry_widgets), column=1)
                self.entry_widgets[key] = entry
        else:
            self.message_label.config(text="No results found.")
            self.edit_frame.pack_forget()

    def save_changes(self):
        """
                Save the updated plant details to the file.
                """
        if self.selected_plant:
            updated_plant = {key: entry.get() for key, entry in self.entry_widgets.items()}
            utilities.update_plant_in_file(self.selected_plant, updated_plant)
            self.message_label.config(text="Plant updated successfully!")
            self.edit_frame.pack_forget()

        for widget in self.edit_frame.winfo_children():
            widget.destroy()

    def return_to_main(self):
        """
                Close the EditPlantUI window and return to the main menu.
                """
        self.edit_menu.destroy()
        if self.main_menu_callback:
            self.main_menu_callback()
