import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({'Name': name, 'Phone': phone, 'Email': email, 'Address': address})
        messagebox.showinfo("Success", "Contact added successfully")
        clear_fields()
    else:
        messagebox.showerror("Error", "Name and Phone number are required")

def view_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def search_contact():
    search_term = search_entry.get().lower()
    results = [contact for contact in contacts if search_term in contact['Name'].lower() or search_term in contact['Phone']]
    contact_list.delete(0, tk.END)
    for result in results:
        contact_list.insert(tk.END, f"{result['Name']} - {result['Phone']}")

def update_contact():
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        selected_contact = contacts[selected_contact_index[0]]
        selected_contact['Name'] = name_entry.get()
        selected_contact['Phone'] = phone_entry.get()
        selected_contact['Email'] = email_entry.get()
        selected_contact['Address'] = address_entry.get()
        messagebox.showinfo("Success", "Contact updated successfully")
        view_contacts()
    else:
        messagebox.showerror("Error", "No contact selected")

def delete_contact():
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        contacts.pop(selected_contact_index[0])
        messagebox.showinfo("Success", "Contact deleted successfully")
        view_contacts()
    else:
        messagebox.showerror("Error", "No contact selected")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Manager")

tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Phone:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Email:").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Address:").grid(row=3, column=0, sticky="w")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, pady=5)
view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.grid(row=5, column=0, columnspan=2, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=0, padx=5, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=6, column=1, padx=5, pady=5)
update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=7, column=0, columnspan=2, pady=5)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=8, column=0, columnspan=2, pady=5)

contact_list = tk.Listbox(root)
contact_list.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()