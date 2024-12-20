import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess

def query_ai(prompt):
    """
    Sends a prompt to the Ollama AI model and retrieves the response.
    """
    try:
        # Run the Ollama 
        result = subprocess.run(
            ["ollama", "run", "qwen2:1.5b"],
            input=prompt, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  
        )
        
        # Check for errors
        if result.returncode != 0:
            return f"Error: {result.stderr.strip()}"
        
        # Return the AI's response
        return result.stdout.strip()
    
    except Exception as e:
        return f"Exception occurred: {str(e)}"

def send_query():
    """
    Gets input from the user and sends it to the AI model.
    """
    user_input = input_text.get("1.0", tk.END).strip()  
    if not user_input:
        messagebox.showerror("Error", "Input cannot be empty!")
        return
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Processing...\n")
    root.update_idletasks()
    
    # Send the query to the AI model
    response = query_ai(user_input)
    
    # Display the  response
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, response)

def clear_text():
    """
    Clears the input and output text areas.
    """
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

def save_output():
    """
    Saves the output text to a .txt file.
    """
    output = output_text.get("1.0", tk.END).strip()
    if not output:
        messagebox.showerror("Error", "No output to save!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Save Output"
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(output)
        messagebox.showinfo("Success", "Output saved successfully!")

# Main window
root = tk.Tk()
root.title("MaxTac")
root.configure(bg="#f5f5f5")

# Configure grid layout for responsiveness
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Main frame
main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.grid(sticky="nsew", padx=10, pady=10)

# Input label and text box
input_label = tk.Label(main_frame, text="Enter your prompt:", bg="#f5f5f5", font=("Arial", 12))
input_label.grid(row=0, column=0, sticky="w", pady=5)

input_text = tk.Text(main_frame, height=5, font=("Arial", 12), wrap="word")
input_text.grid(row=1, column=0, sticky="nsew", pady=5)

# Configure input_text to resize
main_frame.rowconfigure(1, weight=1)
main_frame.columnconfigure(0, weight=1)

# Button frame
button_frame = tk.Frame(main_frame, bg="#f5f5f5")
button_frame.grid(row=2, column=0, pady=10)

# Send button
send_button = tk.Button(button_frame, text="Run", command=send_query, bg="#4CAF50", fg="white", font=("Arial", 12), width=12)
send_button.pack(side="left", padx=5)

# Clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_text, bg="#f44336", fg="white", font=("Arial", 12), width=12)
clear_button.pack(side="left", padx=5)

# Save button
save_button = tk.Button(button_frame, text="Save", command=save_output, bg="#2196F3", fg="white", font=("Arial", 12), width=12)
save_button.pack(side="left", padx=5)

# Output label and text box
output_label = tk.Label(main_frame, text="Response:", bg="#f5f5f5", font=("Arial", 12))
output_label.grid(row=3, column=0, sticky="w", pady=5)

output_text = tk.Text(main_frame, height=10, font=("Arial", 12), wrap="word")
output_text.grid(row=4, column=0, sticky="nsew", pady=5)

# Configure output_text to resize
main_frame.rowconfigure(4, weight=2)

# Run the application
root.mainloop()
