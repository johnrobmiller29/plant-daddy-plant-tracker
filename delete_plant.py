import tkinter as tk
from tkinter import messagebox
import utilities

# Constants for font styles and colors
TITLE_FONT = ('Helvetica', 18, 'bold')
BUTTON_FONT = ('Helvetica', 10, 'bold')
LABEL_FONT = ('Helvetica', 10, 'bold')
BACKGROUND = 'grey'
FOREGROUND = 'dark green'


class DeletePlantUI:
    """
        User interface for deleting a plant from the Plant Daddy application.

        This class provides a window where users can search for a plant by name,
        view the search results, and delete the selected plant after confirmation.
        """
    def __init__(self, main_menu_callback):
        """
                Initialize the delete plant interface and create the layout, title, search bar, message label,
                and the button frame.

                Parameters:
                main_menu_callback (function): A callback function to return to the main menu.
                """
        self.main_menu_callback = main_menu_callback
        self.delete_menu = tk.Toplevel()
        self.delete_menu.title("Delete Plant")
        self.selected_plant = None

        # Create the title frame containing the window title.
        self.title_frame = tk.Frame(self.delete_menu)
        self.search_frame = tk.Frame(self.delete_menu)
        self.results_frame = tk.Frame(self.delete_menu)
        self.button_frame = tk.Frame(self.delete_menu)

        self.title_canvas = tk.Canvas(self.title_frame, width=300, height=60)
        self.title_canvas.create_rectangle(75, 20, 225, 60, outline='dark green', width=2, fill='grey')
        self.title_canvas.create_text(150, 40, text='Delete Plant', font=TITLE_FONT, fill='dark green',
                                      justify='center')
        self.title_canvas.pack()

        self.title_frame.pack()

        # Create the search frame containing the search entry and button.
        self.search_label = tk.Label(self.search_frame, text='Enter Plant Name To Delete',
                                     font=LABEL_FONT, fg=FOREGROUND)
        self.search_label.pack(pady=5)

        self.search_entry = tk.Entry(self.search_frame, width=20)
        self.search_button = tk.Button(self.search_frame, text='Search', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.search_plant)
        self.search_entry.pack(side='left', padx=5)
        self.search_button.pack(side='left')

        self.search_frame.pack(pady=5)

        # Create the results frame to display search results.
        self.results_label = tk.Label(self.results_frame, text='', font=LABEL_FONT, fg=FOREGROUND)
        self.results_label.pack()

        self.results_frame.pack()

        # Create a label to display messages to the user.
        self.message_label = tk.Label(self.delete_menu, text='', font=LABEL_FONT, fg='dark green')
        self.message_label.pack()

        # Create the button frame containing the delete and return buttons.
        self.delete_button = tk.Button(self.button_frame, text='Delete Plant :(', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.show_confirmation)
        self.return_button = tk.Button(self.button_frame, text='Return to Main Menu', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.return_to_main)
        self.delete_button.pack(pady=2)
        self.return_button.pack()

        self.button_frame.pack(pady=5)

    def search_plant(self):
        """
                Search for a plant in the file based on the entered search term.
                """
        search_term = self.search_entry.get()
        results = utilities.search_in_file(search_term)

        if search_term == '':
            self.message_label.config(text="Must enter a keyword to search.")
            formatted_results = ''
        elif results and isinstance(results[0], dict):
            self.selected_plant = results[0]
            self.message_label.config(text='')
            self.message_label.pack()
            formatted_results = "\n\n".join(
                "\n".join(f"{key}: {value}" for key, value in result.items()) for result in results
            )
        else:
            self.selected_plant = None
            formatted_results = ""
            self.message_label.config(text="No results found.")

        self.results_label.config(text=formatted_results)

    def show_confirmation(self):
        """
                Show a confirmation dialog before deleting the selected plant.
                """
        if self.selected_plant:
            result = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this plant?")
            if result:  # User clicked 'Yes'
                self.delete_plant()
            else:  # User clicked 'No'
                self.message_label.config(text="Deletion canceled.")
        else:
            self.message_label.config(text="No plant selected for deletion.")

    def delete_plant(self):
        """
                Delete the selected plant from the file.
                """
        if self.selected_plant:
            utilities.delete_plant_from_file(self.selected_plant)
            self.message_label.config(text="Plant deleted successfully!")
            self.selected_plant = None
            self.results_label.config(text="")

    def return_to_main(self):
        """
                Close the DeletePlantUI window and return to the main menu.
                """
        self.delete_menu.destroy()
        if self.main_menu_callback:
            self.main_menu_callback()