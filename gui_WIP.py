import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk

window_height = 550
window_width = 800

conversations = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10', 'item11']
num_of_conversation = len(conversations)
messages_from_server = ["message1", "message2", "message3", "message4", "message5", "message6", "message7", "message8"]
number_of_messages = len(messages_from_server)

messages_directory = {
    "conversation": {
        "date": {
            "user":
                "message"
        }
    }
}


# Frame in which is the chat
class ChatFrame(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(fg_color="#28192e",
                       border_color="#3e325d",
                       border_width=1,
                       corner_radius=0,
                       width=800 - 260)

    def create_widgets(self):
        MessageFrame(self, conversations[0])
        pass


class MessageFrame:
    def __init__(self, parent, conversation):
        self.conversation_title = ctk.CTkLabel(parent, text="Chat with: " + conversation,
                                               text_font=("Arial", 18, "bold"), width=260)
        self.conversation_title.pack(side="top", fill="x", pady=6, padx=10, anchor="n")
        pass


class MessageLabel(MessageFrame):
    # display chat messages
    def __init__(self, parent, chat_partner, conversation, color="#1f192e"):
        super().__init__(parent)
        self.parent = parent
        self.color = color
        self.chat_partner = chat_partner
        self.conversation = conversation

        self.canv = ctk.CTkCanvas(self.parent, bg=self.color)
        self.canv.config(width=300, height=200)

        # scrollregion has to be larger than canvas size
        # otherwise it just stays in the visible canvas
        self.canv.config(scrollregion=(0, 0, 300, number_of_messages * 62))  # TODO: Muss noch geändert werden zu ...
        # TODO: ... number of messages * height of message

        self.canv.config(highlightthickness=0)

        self.ybar = ttk.Scrollbar(self.parent)
        self.ybar.config(command=self.canv.yview)
        # connect the two widgets together
        self.canv.config(yscrollcommand=self.ybar.set)
        self.ybar.pack(side=RIGHT, fill=Y)
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH)

        for msg in messages_from_server:
            self.msg = msg
            message_ready = self.chat_partner + ": " + self.msg
            self.message_frame = ctk.CTkFrame(self.canv, width=960, height=100, fg_color="#1f192e")

            self.message_user = ctk.CTkLabel(self.message_frame, text=message_ready, text_font=("Arial", 12, "bold"),
                                             fg_color=self.color, width=800 - 260, anchor="e")
            self.message_user.grid(column=1, pady=6, padx=10, anchor="e")


# Frame in which is the conversation list
class Conversation_List(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(fg_color="#1f192e",
                       border_color="#3e325d",
                       border_width=2,
                       corner_radius=0,
                       width=260)

    def create_widgets(self):
        self.conversation_list_header = ctk.CTkLabel(self, text="Conversations", text_font=("Arial", 18, "bold"),
                                                     width=260)
        self.conversation_list_header.pack(side="top", fill="x", pady=6, padx=10, anchor="n")
        Conversation_Buttons(self)


class Conversation_Buttons:
    def __init__(self, parent, color="#1f192e"):
        self.parent = parent
        self.color = color

        self.canv = ctk.CTkCanvas(self.parent, bg=self.color)
        self.canv.config(width=300, height=200)

        # scrollregion has to be larger than canvas size
        # otherwise it just stays in the visible canvas
        self.canv.config(scrollregion=(0, 0, 300, num_of_conversation * 62))
        self.canv.config(highlightthickness=0)

        self.ybar = ttk.Scrollbar(self.parent)
        self.ybar.config(command=self.canv.yview)
        # connect the two widgets together
        self.canv.config(yscrollcommand=self.ybar.set)
        self.ybar.pack(side=RIGHT, fill=Y)
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH)

        for ctr in range(num_of_conversation):
            self.conversations_frame = ctk.CTkFrame(self.canv, width=960, height=100, fg_color="#1f192e")
            self.chats = ctk.CTkButton(self.conversations_frame, text="Chat #" + str(ctr + 1), width=230, height=50,
                                       corner_radius=5, border_width=2, fg_color="#453847",
                                       text_font=("Arial", 16, "bold")).grid()
            self.canv.create_window(10, 3 + (62 * ctr), anchor=NW, window=self.conversations_frame)


# Class for main Window
class Main_Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Messenger")
        self.geometry("800x550+310+100")
        self.resizable(False, False)
        self.configure(bg="#28192e")
        self.create_widgets()

    def create_widgets(self):
        chat_window = ChatFrame(self)
        chat_window.pack(side="right", fill=tk.BOTH, expand=False)

        conversation_list = Conversation_List(self)
        conversation_list.pack(side="left", fill=tk.BOTH, expand=False)


if __name__ == "__main__":
    app = Main_Window()
    app.mainloop()
