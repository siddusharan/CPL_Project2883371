# Binary Serach in Python 
# Taking a real-time scenario to find the Contact in a Contact List

import csv #importing csv library to read .csv file

# Creating a binary_search function to on contacts by name
def binary_search(contacts, target_name):
    low, high = 0, len(contacts) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = contacts[mid]["name"]

        if mid_name == target_name:
            return mid  # Contact found
        elif mid_name < target_name:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Contact not found

#  Function to search for a contact in the phone book
def phone_book_search(contacts, target_name):
    contacts.sort(key=lambda x: x["name"])  # Sort the contacts by name

    index = binary_search(contacts, target_name)

    if index != -1:
        # Handle the case when there are multiple contacts with the same name
        start_index = index
        end_index = index

        # Check contacts with the same name towards the left
        while start_index > 0 and contacts[start_index - 1]["name"] == target_name:
            start_index -= 1

        # Check contacts with the same name towards the right
        while end_index < len(contacts) - 1 and contacts[end_index + 1]["name"] == target_name:
            end_index += 1

        # Print all contacts with the same name
        print(f"Contacts found with the name '{target_name}':")
        for i in range(start_index, end_index + 1):
            print(f"Contact: {contacts[i]}")

    else:
        print("Contact not found.")

# Function to read contacts from a CSV file
def read_contacts_from_csv(csv_file_path):
    contacts = []
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append({"name": row["First Name"], "surname":row["Last Name"] ,"phone": row["Phone Number"]})
    return contacts

# .csv file path that from where data will be searched
csv_file_path = (r'/Users/siddusharan/Downloads/CPL_PROJECT/users.csv')
contacts_list = read_contacts_from_csv(csv_file_path)

# Get user input for contact name
search_name_py = input("Enter the contact name to search: ")

# Now you can use the phone_book_search function with the user input and imported contacts list
phone_book_search(contacts_list, search_name_py)
