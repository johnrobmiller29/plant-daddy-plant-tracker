import tkinter as tk
import utilities
from edit_plant import EditPlantUI
from delete_plant import DeletePlantUI

# Constants for font styles and colors
TITLE_FONT = ('Helvetica', 18, 'bold')
BUTTON_FONT = ('Helvetica', 10, 'bold')
LABEL_FONT = ('Helvetica', 10, 'bold')
BACKGROUND = 'grey'
FOREGROUND = 'dark green'


class ViewPlantUI:
    """
               User Interface class for searching and viewing an existing plant entry from the
               Plant Daddy application.

               This class provides a window where users can search for a plant and have the information
               displayed for them, as well as links to the edit and delete menus.
               """
    def __init__(self, main_menu_callback):
        """
                Initialize the view plant interface and create the layout, title, search bar, results
                frame, and the button frame.

                Parameters:
                main_menu_callback (function): Callback function to return to the main menu.
                """
        self.main_menu_callback = main_menu_callback
        self.view_menu = tk.Toplevel()
        self.view_menu.title("View Plant")

        self.title_frame = tk.Frame(self.view_menu)
        self.search_frame = tk.Frame(self.view_menu)
        self.results_frame = tk.Frame(self.view_menu)
        self.button_frame = tk.Frame(self.view_menu)

        # Create the title frame containing the window title.
        self.title_canvas = tk.Canvas(self.title_frame, width=300, height=60)
        self.title_canvas.create_rectangle(75, 20, 225, 60, outline='dark green', width=2, fill='grey')
        self.title_canvas.create_text(150, 40, text='View Plant', font=TITLE_FONT, fill='dark green', justify='center')
        self.title_canvas.pack()

        self.title_frame.pack()

        # Create the search frame containing the search entry and button.
        self.search_label = tk.Label(self.search_frame, text='Enter Plant Name To View',
                                     font=LABEL_FONT, fg=FOREGROUND)
        self.search_label.pack(pady=5)

        self.search_entry = tk.Entry(self.search_frame, width=20)
        self.search_button = tk.Button(self.search_frame, text='Search', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.search_plant)
        self.search_entry.pack(side='left', padx=5)
        self.search_button.pack(side='left')

        self.search_frame.pack(pady=5)

        # Create the results frame to display search results to user
        self.results_label = tk.Label(self.results_frame, text='', font=LABEL_FONT, fg=FOREGROUND)
        self.results_label.pack()

        self.results_frame.pack()

        # Create a label to display messages to the user.
        self.message_label = tk.Label(self.view_menu, text='', font=LABEL_FONT, fg='dark green')
        self.message_label.pack()

        # Create the button frame containing the save and return buttons.
        self.edit_button = tk.Button(self.button_frame, text='Open Edit Menu', font=BUTTON_FONT,
                                     bg=BACKGROUND, fg=FOREGROUND, command=self.open_edit_screen)
        self.delete_button = tk.Button(self.button_frame, text='Open Delete Menu', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.open_delete_screen)
        self.return_button = tk.Button(self.button_frame, text='Return to Main Menu', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.return_to_main)
        self.edit_button.pack(pady=2)
        self.delete_button.pack(pady=2)
        self.return_button.pack()

        self.button_frame.pack(pady=5)

    def search_plant(self):
        """
                Search for plants by name and display their details.
                """
        search_term = self.search_entry.get()
        results = utilities.search_in_file(search_term)

        # Prevents blank search input and displays message
        if search_term == '':
            self.message_label.config(text="Must enter a keyword to search.")
            formatted_results = ''
        # Displays results as long as they exist
        elif results and isinstance(results[0], dict):
            self.message_label.config(text='')
            formatted_results = "\n\n".join(
                "\n".join(f"{key}: {value}" for key, value in result.items()) for result in results
            )
        # Displays message when no results are found
        else:
            self.message_label.config(text="No results found.")
            formatted_results = ''

        self.results_label.config(text=formatted_results)

    def open_edit_screen(self):
        """
                Close the current window and open the EditPlantUI window.
                """
        self.view_menu.destroy()
        EditPlantUI(self.return_to_main)

    def open_delete_screen(self):
        """
                Close the current window and open the DeletePlantUI window.
                """
        self.view_menu.destroy()
        DeletePlantUI(self.return_to_main)

    def return_to_main(self):
        """
                Close the current window and return to the main menu.
                """
        self.view_menu.destroy()
        if self.main_menu_callback:
            self.main_menu_callback()
