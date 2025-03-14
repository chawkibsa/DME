# Login page client side
import tkinter
from tkinter import StringVar, END

# Define constants
# Define fonts and colors
my_font = ("SimSun", 14)
black = "#010101"
light_green = "#1fc742"
white = "#ffffff"
red = "#ff3855"
orange = "#ffaa1d"
yellow = "#fff700"
green="#1fc742"
blue = "#5dadec"
purple = "#9c51b6"
project_image = "./images/DME.png"
project_icon = "./images/DME.ico"

class Client_Login:
    # Default constructor ... DOESNT DO ANYTHING

    # Define Methods
    def login(self, event=None):
        # Get required information for input fields
        self.username = self.name_entry.get()
        self.password = self.password_entry.get()

        if not self.username or not self.password:
            self.error_output.config(text="Please Fill in the fields")
        else:
            # Use those credentials to authenticated to the LDAP admin
            self.root.withdraw()
            import client

    def signup(self):
        pass

    def main(self):
        # Define window
        self.root = tkinter.Tk()
        self.root.title("DME (client login)")
        #self.root.iconbitmap(project_icon)    #It doesn't worked in Linux, but it worked for Windows
        self.root.geometry("600x600")
        self.root.resizable(0, 0)
        self.root.config(bg=black)

        # Define GUI Layout
        # Create Frames
        title_frame = tkinter.Frame(self.root, bg=black)
        info_frame = tkinter.Frame(self.root, bg=black)
        #color_frame = tkinter.Frame(self.root, bg=black)
        buttons_frame = tkinter.Frame(self.root, bg=black)
        errors_frame = tkinter.Frame(self.root, bg=black)
        title_frame.pack()
        info_frame.pack()
        #color_frame.pack()
        buttons_frame.pack()
        errors_frame.pack()

        # Title Frame Layout
        self.title_label = tkinter.Label(title_frame, text="Client Login", font=my_font, fg=light_green, bg=black)
        self.title_label.pack(padx=10, pady=20)

        # Info Frame layout
        self.name_label = tkinter.Label(info_frame, text="Client Name : ", font=my_font, fg=light_green, bg=black)
        self.name_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
        self.password_label = tkinter.Label(info_frame, text="Client Password : ", font=my_font, fg=light_green, bg=black)
        self.password_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
        #self.ip_label = tkinter.Label(info_frame, text="HOST IP : ", font=my_font, fg=light_green, bg=black)
        #self.ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
        #self.port_label = tkinter.Label(info_frame, text="Port Num : ", font=my_font, fg=light_green, bg=black)
        #self.port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)

        self.name_label.grid(row=0, column=0, padx=8, pady=16)
        self.name_entry.grid(row=0, column=1, padx=8, pady=16)
        self.password_label.grid(row=1, column=0, padx=8, pady=16)
        self.password_entry.grid(row=1, column=1, padx=8, pady=16)
        #self.ip_label.grid(row=2, column=0, padx=8, pady=11)
        #self.ip_entry.grid(row=2, column=1, padx=8, pady=11)
        #self.port_label.grid(row=3, column=0, padx=8, pady=16)
        #self.port_entry.grid(row=3, column=1, padx=8, pady=16)

        # Color Frame Layout
        #self.color = StringVar()
        #self.color.set(white)
        #self.white_button = tkinter.Radiobutton(color_frame, width=5, text="White", variable=self.color, value=white, bg=black, fg=light_green, font=my_font)
        #self.red_button = tkinter.Radiobutton(color_frame, width=5, text="Red", variable=self.color, value=red, bg=black, fg=light_green, font=my_font)
        #self.orange_button = tkinter.Radiobutton(color_frame, width=5, text="Orange", variable=self.color, value=orange, bg=black, fg=light_green, font=my_font)
        #self.yellow_button = tkinter.Radiobutton(color_frame, width=5, text="Yellow", variable=self.color, value=yellow, bg=black, fg=light_green, font=my_font)
        #self.green_button = tkinter.Radiobutton(color_frame, width=5, text="Green", variable=self.color, value=green, bg=black, fg=light_green, font=my_font)
        #self.blue_button = tkinter.Radiobutton(color_frame, width=5, text="Blue", variable=self.color, value=blue, bg=black, fg=light_green, font=my_font)
        #self.purple_button = tkinter.Radiobutton(color_frame, width=5, text="Purple", variable=self.color, value=purple, bg=black, fg=light_green, font=my_font)
        #self.color_buttons = [self.white_button, self.red_button, self.orange_button, self.yellow_button, self.green_button, self.blue_button, self.purple_button]

        #self.white_button.grid(row=1, column=0, padx=2, pady=11)
        #self.red_button.grid(row=1, column=1, padx=2, pady=11)
        #self.orange_button.grid(row=1, column=2, padx=2, pady=11)
        #self.yellow_button.grid(row=1, column=3, padx=2, pady=11)
        #self.green_button.grid(row=1, column=4, padx=2, pady=11)
        #self.blue_button.grid(row=1, column=5, padx=2, pady=11)
        #self.purple_button.grid(row=1, column=6, padx=2, pady=11)


        # Buttons Frame Layout
        self.connect_button = tkinter.Button(buttons_frame, text="Connect", font=my_font, bg=light_green, borderwidth=5, width=10, command=self.login)  # , command=lambda: connect(my_connection))
        self.signup_button = tkinter.Button(buttons_frame, text="Signup", font=my_font, bg=light_green, borderwidth=5, width=10)  # ,command=lambda: disconnect(my_connection))
        self.connect_button.grid(row=4, column=0, padx=10, pady=16)
        self.signup_button.grid(row=4, column=1, padx=10, pady=16)

        # Errors Frame Layout ... Incase an error occurs this label will show up
        self.error_output = tkinter.Label (errors_frame, width=60, font=my_font, bg=black, fg=light_green)
        self.error_output.pack(padx=10, pady=10)

        # Run the root window's mainloop()
        self.root.mainloop()

# Create a clientlogin object and run the main() method
clientlogin = Client_Login()
clientlogin.main()



