import tkinter as tk
from add_plant import AddPlantUI
from view_plant import ViewPlantUI
from edit_plant import EditPlantUI
from delete_plant import DeletePlantUI
from export import ExportUI

# Constants for font styles and colors
TITLE_FONT = ('Helvetica', 18, 'bold')
BUTTON_FONT = ('Helvetica', 10, 'bold')
LABEL_FONT = ('Helvetica', 10, 'bold')
BACKGROUND = 'grey'
FOREGROUND = 'dark green'


class MainMenuUI:
    """
        Main menu interface for the Plant Daddy application.

        This class sets up the main menu with navigation buttons to add, view, edit, delete,
        and export plant data. Each button opens a respective Toplevel window for the
        corresponding operation. The main menu can be hidden and shown as needed.
        """
    def __init__(self):
        """
                Initialize the main menu interface and create the layout, application title, and
                navigation menu.
                """
        self.main_menu = tk.Tk()
        self.main_menu.title("Main Menu")

        self.title_frame = tk.Frame(self.main_menu)
        self.nav_frame = tk.Frame(self.main_menu)

        # Create the title frame containing the application title.
        self.title_canvas = tk.Canvas(self.title_frame, width=300, height=60)
        self.title_canvas.create_rectangle(75, 20, 225, 60, outline='dark green', width=2, fill='grey')
        self.title_canvas.create_text(150, 40, text='Plant Daddy', font=TITLE_FONT, fill='dark green', justify='center')
        self.title_canvas.pack()

        self.title_frame.pack()

        # Create the navigation frame containing the menu buttons.
        self.add_button = tk.Button(self.nav_frame, text='Add a Plant', font=BUTTON_FONT,
                                    bg=BACKGROUND, fg=FOREGROUND, command=self.open_add_menu)
        self.view_button = tk.Button(self.nav_frame, text='View a Plant', font=BUTTON_FONT,
                                     bg=BACKGROUND, fg=FOREGROUND, command=self.open_view_menu)
        self.edit_button = tk.Button(self.nav_frame, text='Edit a Plant', font=BUTTON_FONT,
                                     bg=BACKGROUND, fg=FOREGROUND, command=self.open_edit_menu)
        self.delete_button = tk.Button(self.nav_frame, text='Delete a Plant (RIP)', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.open_delete_menu)
        self.export_button = tk.Button(self.nav_frame, text='Export Plant Data', font=BUTTON_FONT,
                                       bg=BACKGROUND, fg=FOREGROUND, command=self.open_export_menu)
        self.quit_button = tk.Button(self.nav_frame, text='Quit', font=BUTTON_FONT,
                                     bg=BACKGROUND, fg=FOREGROUND, command=self.main_menu.destroy)
        self.add_button.pack(pady=2)
        self.view_button.pack(pady=2)
        self.edit_button.pack(pady=2)
        self.delete_button.pack(pady=2)
        self.export_button.pack(pady=2)
        self.quit_button.pack()

        self.nav_frame.pack(pady=5)

        tk.mainloop()

    def open_add_menu(self):
        """
        Open the AddPlantUI window and hide the main menu.
        """
        self.main_menu.withdraw()
        AddPlantUI(self.return_to_main)

    def open_view_menu(self):
        """
        Open the ViewPlantUI window and hide the main menu.
        """
        self.main_menu.withdraw()
        ViewPlantUI(self.return_to_main)

    def open_edit_menu(self):
        """
        Open the EditPlantUI window and hide the main menu.
        """
        self.main_menu.withdraw()
        EditPlantUI(self.return_to_main)

    def open_delete_menu(self):
        """
        Open the DeletePlantUI window and hide the main menu.
        """
        self.main_menu.withdraw()
        DeletePlantUI(self.return_to_main)

    def open_export_menu(self):
        """
        Open the ExportUI window and hide the main menu.
        """
        self.main_menu.withdraw()
        ExportUI(self.return_to_main)

    def return_to_main(self):
        """
        Show the main menu window.
        """
        self.main_menu.deiconify()


run = MainMenuUI()
