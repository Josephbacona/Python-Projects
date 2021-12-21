
import webbrowser
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self)

        self.master = master
        self.master.title('Web Generator')
        self.varNewContent = StringVar()

        self.btnSubmit = Button(self.master, text="Submit", command=lambda: webgenerator(self))
        self.btnSubmit.grid(row=2,column=1,padx=(30,0), pady=(30,0), sticky=NE)

        self.lblNewContent = Label(self.master,text='Enter Text: ', font=("Helvetia", 16), fg='black', bg='lightgray' )
        self.lblNewContent.grid(row=0,column=0,padx=(30,0), pady=(30,0))

        self.txtNewContent = Entry(self.master,text=self.varNewContent, font=("Helvetia", 16), fg='black', bg='lightblue')
        self.txtNewContent.grid(row=0,column=1,padx=(30,0), pady=(30,0))

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1,padx=(30,90), pady=(30,0), sticky=NE)

    def submit(self):
        nc = self.varNewContent.get()
        self.lblDisplay.config(text='The new content of the page now says "{}"'.format(nc))

    def cancel(self):
        self.master.destroy()
        

def webgenerator(self):
    #This is creating and HTML file showing the text in the <h1> heading
    message1 = """
    <html>
        <body>
            <h1>
            Stay tuned for our amazing summer sale!
            </h1>
        """
    #This will be the new content showed on the page inputed by the user 
    message2 = self.txtNewContent.get()

    message3 = """
        </body>
    </html>"""

    with open('index.html','w') as f:
        f.write(message1 + message2 + message3)
    #This is opening the html file created earlier in a new tab
    url = 'index.html'
    webbrowser.open_new_tab(url)

txt = "{}".format("")

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
