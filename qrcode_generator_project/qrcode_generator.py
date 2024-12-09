import tkinter as tk
import qrcode
import os


qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size= 10,
    border= 4
)

def makeQRcode():
    qr.clear()
    url = get.get()
    if url == "":
        WaringLabel1 = tk.Label(root, text="Please type in the url to create a QRcode", fg="red")
        WaringLabel1.place(x=250, y=100, anchor=tk.CENTER)
    else:
        CoverLabel1 = tk.Label(root, text="                                                                    ")
        CoverLabel1.place(x=250, y=100, anchor=tk.CENTER)
        flag1 = 0
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.show()

def download():
    
    os.chdir('downloads')
    url = get.get()
    name = downloadEntry.get()
    if url == "":
        WaringLabel2 = tk.Label(root, text="Please type in the url to download a QRcode", fg="red")
        WaringLabel2.place(x=250, y=245, anchor=tk.CENTER)
    else:
        CoverLabel2 = tk.Label(root, text="                                                                                     ")
        CoverLabel2.place(x=250, y=245, anchor=tk.CENTER)
        if name == "":
            WaringLabel3 = tk.Label(root, text="Please type in the png name to download a QRcode", fg="red")
            WaringLabel3.place(x=250, y=270, anchor=tk.CENTER)
        else:
            CoverLabel3 = tk.Label(root, text="                                                                                           ")
            CoverLabel3.place(x=250, y=270, anchor=tk.CENTER)
            qr.clear()
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(name)
            downloadedLabel = tk.Label(root, text="Downloaded!!!")
            downloadedLabel.place(x=250, y=245, anchor=tk.CENTER)
    os.chdir('../')
        
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x350")

label = tk.Label(root, text="Type your url!!")
get = tk.Entry(root, width=50)
button = tk.Button(root, text="Go!", command= makeQRcode)
downloadLabel = tk.Label(root, text="Type in a name to save your QRcode (Please add .png at the end)")
downloadEntry = tk.Entry(root, width=25)
downloadButton = tk.Button(root, text="Download", command= download)
button_quit = tk.Button(root, text="Quit", command= root.destroy)

label.place(x=250, y=10, anchor=tk.CENTER)
get.place(x=250,y=35, anchor=tk.CENTER)
button.place(x=250, y=70, anchor=tk.CENTER)
downloadLabel.place(x=250, y=150, anchor=tk.CENTER)
downloadEntry.place(x=250, y=175, anchor=tk.CENTER)
downloadButton.place(x=250, y=210, anchor= tk.CENTER)
button_quit.place(x=250, y=330, anchor=tk.CENTER)

root.mainloop()
