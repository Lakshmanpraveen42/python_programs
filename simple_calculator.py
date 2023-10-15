import tkinter as tk

def on_click(button_text):
    current_text = display.get()
    
    if button_text == "=":
        try:
            result = eval(current_text)
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif button_text == "C":
        display.set("")
    else:
        cursor_position = entry.index(tk.INSERT)
        updated_text = current_text[:cursor_position] + button_text + current_text[cursor_position:]
        display.set(updated_text)
        entry.icursor(cursor_position + 1)  # Move the cursor one position to the right

# Create a basic calculator window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget for the display
display = tk.StringVar()
entry = tk.Entry(window, textvariable=display, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Define the button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# Increase button border width
button_padx = 15
button_pady = 15

# Create and place the buttons in the grid
row, col = 1, 0
for button_text in buttons:
    button = tk.Button(window, text=button_text, padx=button_padx, pady=button_pady, font=("Arial", 20),
                      command=lambda text=button_text: on_click(text))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
