import main
import tkinter as tk

conn = main.create_connection()

def enterCommand(event=None):
    command = entry1.get().split()
    #command = [i.lower() for i in command]
    print(f"command entered, {command=}")

    if command[0] == "insert":
        data = tuple(command[1:])
        main.new_country(conn, data)
        print("country created")

    elif command[0] == "delete":
        if command[1] == "name":
            main.deleteCountry(conn, name=command[2])
        elif command[1] == "id":
            main.deleteCountry(conn, id=command[2])
        elif command[1] == "all":
            main.deleteAllCountry(conn)
            print("deleted all")
        else:
            labelwarning["text"] = "unknown type, use name or id"
            return
    else:
        labelwarning["text"] = "unknown command, try again"
        return

    labelwarning["text"] = ""
    clearEntry()
    updateFrame()

def clearEntry():
    entry1.delete(0, "end")

def updateFrame():
    # whats in the frame
    for e in frame1.winfo_children():
        e.grid_forget()

    labelf1 = tk.Label(frame1, text="ID", bg="white", font='Helvetica 10 bold')
    labelf1.grid(row=0, column=0, padx=5, pady=5)
    labelf2 = tk.Label(frame1, text="Land Mass", bg="white", font='Helvetica 10 bold')
    labelf2.grid(row=0, column=2, padx=5, pady=5)
    labelf3 = tk.Label(frame1, text="Name", bg="white", font='Helvetica 10 bold')
    labelf3.grid(row=0, column=1, padx=5, pady=5)

    data = main.fetchadd(conn)
    print(data)
    for r, re in enumerate(data):
        for c, ce in enumerate(re):
            nlabel = tk.Label(frame1, text=ce, bg="white")
            nlabel.grid(row=r+1, column=c)


root = tk.Tk()
root.title("DB GUI")
root.geometry("200x350")

label1 = tk.Label(text="Enter Commands Here: ")
label1.grid(row=0, column=0, columnspan=2)
entry1 = tk.Entry(width=30)
entry1.grid(row=1, column=0, columnspan=2)
entry1.bind('<Return>', enterCommand)


but1 = tk.Button(text="Clear", command=clearEntry)
but1.grid(row=2, column=0)
but2 = tk.Button(text="Enter", command=enterCommand)
but2.grid(row=2, column=1)

labelwarning = tk.Label(root, text="")
labelwarning.grid(row=3)


frame1 = tk.Frame(root, bg='white', width=200, height=200, pady=3)
frame1.grid(row=4, columnspan=4, column=0, sticky="EW")

updateFrame()

root.mainloop()
