import tkinter as tk
from tkinter import scrolledtext, messagebox
from bs4 import BeautifulSoup


def extract_ids(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all input, select, and date elements
    input_fields = soup.find_all("input")
    select_fields = soup.find_all("select")
    date_fields = soup.find_all("input", {"type": "date"})

    # Extract the IDs of the fields
    input_ids = [f'#pre{field.get("id")}' for field in input_fields]
    select_ids = [f'#pre{field.get("id")}' for field in select_fields]
    date_ids = [f'#pre{field.get("id")}' for field in date_fields]

    # Combine the IDs in order of occurrence
    all_ids = input_ids + select_ids + date_ids

    return all_ids


def analyze_html():
    html_content = html_input.get("1.0", "end-1c")

    if not html_content.strip():
        messagebox.showerror("Error", "Please enter valid HTML content.")
        return

    field_ids = extract_ids(html_content)

    # Display the result in the result_text widget
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    for field_id in field_ids:
        result_text.insert(tk.END, field_id + "\n")
    result_text.config(state=tk.DISABLED)


# Create the main window
window = tk.Tk()
window.title("HTML Field ID Extractor")

# Create and place widgets
tk.Label(window, text="Paste HTML content:").pack(pady=5)
html_input = scrolledtext.ScrolledText(window, width=50, height=10)
html_input.pack(pady=5)

analyze_button = tk.Button(window, text="Analyze HTML", command=analyze_html)
analyze_button.pack(pady=5)

tk.Label(window, text="Field IDs:").pack(pady=5)
result_text = scrolledtext.ScrolledText(window, width=50, height=10, state=tk.DISABLED)
result_text.pack(pady=5)

# Run the main loop
window.mainloop()
