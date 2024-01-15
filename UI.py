import tkinter as tk
import main


def convert_text():
    input_text = entry_input.get()
    #checks if the type choosen by the user is the same if not it converts it
    if var_conversion.get() != var_output.get():
        output_text = main.transform(input_text,var_conversion.get(), var_output.get())


    else:
        output_text=input_text

    entry_output.delete(1.0, tk.END)  # Clear the output text box
    entry_output.insert(tk.END, output_text)



# Create the main Tkinter window
root = tk.Tk()
root.title("ATCG Codec")

# Type of Input Menu
label_input = tk.Label(root, text="Type of input : ")
label_input.pack(padx=10, pady=5, anchor=tk.W)

conversion_types = ["String", "Binary", "DNA","String_format"]
var_conversion = tk.StringVar(value=conversion_types[0])
conversion_menu = tk.OptionMenu(root, var_conversion, *conversion_types)
conversion_menu.pack(padx=10, pady=5, anchor=tk.W)

# Type of Output Menu
label_output = tk.Label(root, text="Type of output : ")
label_output.pack(padx=10, pady=5, anchor=tk.W)

output_types = ["String", "Binary", "DNA","String_format" , "String_reverse"]
var_output = tk.StringVar(value=output_types[0])
output_menu = tk.OptionMenu(root, var_output, *output_types)
output_menu.pack(padx=10, pady=5, anchor=tk.W)

# Space between menu and input box
label_space = tk.Label(root, text="")
label_space.pack(padx=5, pady=2, anchor=tk.W)

# Input Text Box
label_input = tk.Label(root, text="Input Text :")
label_input.pack(padx=10, pady=5, anchor=tk.W)

entry_font = ("Helvetica", 14)
entry_input_var = tk.StringVar()
entry_input = tk.Entry(root, textvariable=entry_input_var, font=entry_font, width=40)
entry_input.pack(fill=tk.X, padx=10, pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_text)
convert_button.pack(padx=10, pady=10)

# Output Text Box
label_output = tk.Label(root, text="Output Text :")
label_output.pack(padx=10, pady=5, anchor=tk.W)

entry_output = tk.Text(root, height=5, width=40)
entry_output.pack(fill=tk.X, padx=10, pady=5)

# Set minimum size for the window
root.minsize(width=400, height=400)
root.maxsize(width=700, height=500)

# Run the Tkinter event loop
root.mainloop()



###""
#######erroor AttributeError: 'Conversion' object has no attribute 'String_to_String_format'
####
###
##
#