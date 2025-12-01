import tkinter as tk
from tkinter import messagebox
from activate_motions import ORCAKinematic

NUM_MOTIONS = 2
STANDARD_PADX = 10
INNER_PADY = 10
COM_PADX = 5
COM_PADY = 8

LIGHTER_BLUE = "#015A85"
DARK_BLUE = "#002C42"
VIVID_ORANGE = "#F4911E"
IRIS_ORANGE = "#F15E24"
ASH = "#F6F5F5"
STOP_RED = "#BE0020"


class ORCAGui:
    def __init__(self, console, orca_operation):
        self.console = console
        self.orca_operation = orca_operation
        self.console.title("Activate ORCA Kinematic Motions")
        self.console.geometry("475x480")
        self.console.configure(bg=DARK_BLUE)

        # dictionaries for component access
        self.buttons = {}
        self.labels = {}
        self.com_port_entry = {}
        self.com_port_labels = {}
        self.kinematic_labels = {}
        self.kinematic_entry = {}
        self.connect_button = None
        self.active_motion_id = 0

        # main frame
        frame = tk.Frame(self.console, bg=DARK_BLUE)
        frame.grid(row=0, column=0, padx=10, pady=40)

        # heading
        heading = tk.Label(
            frame,
            text="Simultaneous Kinematic Motion Triggering",
            font=("Calibre", 14, "bold"),
            bg=DARK_BLUE,
            fg=ASH,
            pady=2,
        )
        heading.grid(row=0, column=0, columnspan=2, sticky="n", pady=(0, 25))

        self.com_entry_frame = tk.Frame(frame, bg=DARK_BLUE)
        self.com_entry_frame.grid(row=1, column=0, columnspan=3)

        self.com_entry_frame.grid_columnconfigure(0, weight=1)
        self.com_entry_frame.grid_columnconfigure(1, weight=1)
        self.com_entry_frame.grid_columnconfigure(2, weight=1)

        # content frame for labels and buttons
        self.content = tk.Frame(frame, bg=DARK_BLUE)
        self.content.grid(row=3, column=0, columnspan=3, pady=(10, 20))

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_columnconfigure(1, weight=1)
        self.content.grid_columnconfigure(2, weight=1)

        # some centering for the inner grid
        self.console.grid_rowconfigure(0, weight=0)
        self.console.grid_columnconfigure(0, weight=1)

        self.stop_button = tk.Button(
            self.content,
            text="STOP",
            bg=STOP_RED,
            fg=ASH,
            font=("Calibre", 10, "bold"),
            activebackground=STOP_RED,
            activeforeground=ASH,
            command=self.stop_motions,
            width=5,
            relief="raised",
            cursor="X_cursor",
        )

        # creates labels and buttons
        for i in range(NUM_MOTIONS):
            motion_index = i + 1
            lbl_key = f"lbl_{motion_index}"
            btn_key = f"btn_{motion_index}"
            txt_key = f"txt_{motion_index}"

            self.com_port_labels[txt_key] = tk.Label(
                self.com_entry_frame,
                text=f"ORCA {i + 1} COM",
                width=12,
                font=("Calibre", 10),
                bg=LIGHTER_BLUE,
                fg=ASH,
                relief="ridge",
                bd=1,
            )

            self.com_port_entry[txt_key] = tk.Entry(
                self.com_entry_frame,
                width=8,
                font=("Calibre", 10),
                relief="sunken",
                bd=1,
                justify=tk.CENTER,
            )

            self.kinematic_labels[motion_index] = tk.Label(
                self.content,
                text=f"Motion ID",
                width=8,
                font=("Calibre", 10),
                bg=LIGHTER_BLUE,
                fg=ASH,
                justify="right",
                relief="ridge",
                bd=1,
            )

            self.kinematic_entry[txt_key] = tk.Entry(
                self.content,
                width=8,
                font=("Calibre", 10),
                relief="sunken",
                bd=1,
                justify=tk.CENTER,
            )

            self.labels[lbl_key] = tk.Label(
                self.content,
                text="Not Activated",
                width=12,
                font=("Calibre", 11),
                bg=VIVID_ORANGE,
                fg=LIGHTER_BLUE,
                relief="ridge",
                bd=1,
            )

            self.buttons[btn_key] = tk.Button(
                self.content,
                text=f"Trigger",
                bg=IRIS_ORANGE,
                fg=ASH,
                font=("Calibre", 10, "bold"),
                activebackground=IRIS_ORANGE,
                activeforeground=LIGHTER_BLUE,
                width=8,
                cursor="right_ptr",
                command=lambda l=motion_index: self.on_trigger_click(l),
            )

        self.connect_button = tk.Button(
            self.com_entry_frame,
            text="Connect",
            bg=IRIS_ORANGE,
            fg=ASH,
            font=("Calibre", 10, "bold"),
            activebackground=IRIS_ORANGE,
            activeforeground=LIGHTER_BLUE,
            width=8,
            cursor="right_ptr",
            command=lambda: self.connect_orcas(),
        )

        # display labels and buttons in a grid
        self.display_components()

    def stop_motions(self):
        """
        Sleep ORCAs when this button is pressed.
        """
        self.orca_operation.sleep_motor()

    def connect_orcas(self):
        """
        Connects to provided COM ports.
        Outputs a error dialog box if invalid input is supplied.
        """
        orca_coms = []
        for com_key, entry_widget in self.com_port_entry.items():
            com_port = entry_widget.get().strip()
            if len(com_port) > 1:
                messagebox.showwarning(
                    title="Error",
                    message="Please enter a valid COM port number for the motor's RS422 connection.",
                )
            if com_port:
                orca_coms.append(f"COM{entry_widget.get()}")

        self.orca_operation.connect_motors(orca_coms)

    def on_trigger_click(self, clicked_motion_id):
        """
        Triggers the provided motion ID once the button is clicked.
        Toggles the "Running" and "Not Activated" text if two motions are provided.

        Args:
            clicked_motion_id (int): the id of the text-field or trigger button that is clicked.
        """

        if clicked_motion_id == 1:
            other_motion_id = 2
        else:
            other_motion_id = 1

        clicked_label_key = f"lbl_{clicked_motion_id}"
        other_label_key = f"lbl_{other_motion_id}"

        clicked_label = self.labels[clicked_label_key]
        other_label = self.labels[other_label_key]
        other_is_running = other_label.cget("text") == "Running!"

        updated_entry = f"txt_{clicked_motion_id}"
        self.active_motion_id = self.kinematic_entry[updated_entry].get()

        # if the current motion ID is triggered and other motion is running
        if self.active_motion_id != "":
            if other_is_running:
                other_label.config(text="Not Activated")
                clicked_label.config(text="Running!")
            else:
                clicked_label.config(text="Running!")

            self.orca_operation.trigger_motions(self.active_motion_id)

    def display_components(self):
        """
        Displays the labels, text entry fields, and buttons based on a grid within their frames.
        """
        for i in range(NUM_MOTIONS):
            txt_key = f"txt_{i + 1}"
            self.com_port_labels[txt_key].grid(
                row=0, column=i, padx=COM_PADX, pady=(COM_PADY, 15), sticky="ew"
            )
            self.com_port_entry[txt_key].grid(
                row=1, column=i, padx=COM_PADX, pady=(0, COM_PADY), sticky="ew"
            )
            self.connect_button.grid(
                row=1,
                column=NUM_MOTIONS * 2,
                padx=COM_PADX,
                pady=(0, COM_PADY),
                sticky="ew",
            )

        for i in range(NUM_MOTIONS):
            lbl_key = f"lbl_{i + 1}"
            btn_key = f"btn_{i + 1}"
            txt_key = f"txt_{i + 1}"
            key = i + 1

            row_start = i * 2
            next_row = row_start + 1

            self.kinematic_labels[key].grid(
                row=row_start,
                column=0,
                padx=STANDARD_PADX,
                pady=(INNER_PADY, 8),
                sticky="ew",
            )
            self.kinematic_entry[txt_key].grid(
                row=next_row,
                column=0,
                padx=STANDARD_PADX,
                pady=(0, INNER_PADY),
                sticky="ew",
            )
            self.buttons[btn_key].grid(
                row=next_row,
                column=1,
                padx=STANDARD_PADX,
                pady=(0, INNER_PADY),
                sticky="ew",
            )
            self.labels[lbl_key].grid(
                row=next_row,
                column=2,
                padx=STANDARD_PADX,
                pady=(0, INNER_PADY),
                sticky="ew",
            )

            self.stop_button.grid(
                row=next_row + 2,
                column=0,
                columnspan=3,
                padx=STANDARD_PADX,
                pady=INNER_PADY * 2,
                sticky="nsew",
            )


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    orca_operation = ORCAKinematic()
    orca_console = ORCAGui(root, orca_operation)
    root.mainloop()
