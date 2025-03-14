# Login page client side
import tkinter
from tkinter import DISABLED

# Define constants
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
project_icon = "./images/DME.ico"

class Server_login:

    def connect_server(self):
        '''Start the server on a given port number'''
        self.root.withdraw()
        import server

    def start_ldap(self):
        pass


    def main(self):
        # Define window
        self.root = tkinter.Tk()
        self.root.title("DME (Admin login)")
        #self.root.iconbitmap(project_icon)    #It doesn't worked in Linux, but it worked for Windows
        self.root.geometry("600x600")
        self.root.resizable(0, 0)
        self.root.config(bg=black)

        # Define GUI Layout
        # Create Frames
        title_frame = tkinter.Frame(self.root, bg=black)
        info_frame = tkinter.Frame(self.root, bg=black)
        buttons_frame = tkinter.Frame(self.root, bg=black)
        errors_frame = tkinter.Frame(self.root, bg=black)
        title_frame.pack()
        info_frame.pack()
        buttons_frame.pack()
        errors_frame.pack()

        # Title Frame Layout
        self.title_label = tkinter.Label(title_frame, text="Administrator Login", font=my_font, fg=light_green, bg=black)
        self.title_label.pack(padx=10, pady=20)

        # Info Frame layout
        self.chatroom_ip_label = tkinter.Label(info_frame, text="Chatroom Server IP * : ", font=my_font, fg=light_green, bg=black)
        self.chatroom_ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
        self.chatroom_port_label = tkinter.Label(info_frame, text="Chatroom Server port * : ", font=my_font, fg=light_green, bg=black)
        self.chatroom_port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)
        self.ldap_ip_label = tkinter.Label(info_frame, text="LDAP Server IP : ", font=my_font, fg=light_green, bg=black)
        self.ldap_ip_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
        self.ldap_port_label = tkinter.Label(info_frame, text="LDAP Server Port : ", font=my_font, fg=light_green, bg=black)
        self.ldap_port_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10)
        self.ldap_name_label = tkinter.Label(info_frame, text="LDAP Server administrator name : ", font=my_font, fg=light_green, bg=black)
        self.ldap_name_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font)
        self.ldap_password_label = tkinter.Label(info_frame, text="LDAP Server administrator password : ", font=my_font, fg=light_green, bg=black)
        self.ldap_password_entry = tkinter.Entry(info_frame, borderwidth=3, font=my_font, width=10,show="*")

        self.chatroom_ip_label.grid(row=0, column=0, padx=8, pady=16)
        self.chatroom_ip_entry.grid(row=0, column=1, padx=8, pady=16)
        self.chatroom_port_label.grid(row=1, column=0, padx=8, pady=16)
        self.chatroom_port_entry.grid(row=1, column=1, padx=8, pady=16)
        self.ldap_ip_label.grid(row=2, column=0, padx=8, pady=16)
        self.ldap_ip_entry.grid(row=2, column=1, padx=8, pady=16)
        self.ldap_port_label.grid(row=3, column=0, padx=8, pady=11)
        self.ldap_port_entry.grid(row=3, column=1, padx=8, pady=11)
        self.ldap_name_label.grid(row=4, column=0, padx=8, pady=16)
        self.ldap_name_entry.grid(row=4, column=1, padx=8, pady=16)
        self.ldap_password_label.grid(row=5, column=0, padx=8, pady=16)
        self.ldap_password_entry.grid(row=5, column=1, padx=8, pady=16)

        # Buttons Frame Layout
        self.connect_button = tkinter.Button(buttons_frame, text="Start", font=my_font, bg=light_green, borderwidth=5, width=10, command= self.connect_server)  # , command=lambda: connect(my_connection))
        self.signup_button = tkinter.Button(buttons_frame, text="End", font=my_font, bg=light_green, borderwidth=5, width=10, state=DISABLED)  # ,command=lambda: disconnect(my_connection))
        self.connect_button.grid(row=4, column=0, padx=10, pady=16)
        self.signup_button.grid(row=4, column=1, padx=10, pady=16)

        # Errors Frame Layout ... Incase an error occurs this label will show up
        self.error_output = tkinter.Label (errors_frame, width=60, font=my_font, bg=black, fg=light_green)
        self.error_output.pack(padx=10, pady=10)

        # Run the root window's mainloop()
        self.root.mainloop()

# Create a clientlogin object and run the main() method
server_login = Server_login()
server_login.main()
