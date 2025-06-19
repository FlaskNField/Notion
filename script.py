from notion_client import Client

# Replace 'YOUR_NOTION_INTEGRATION_TOKEN' with your actual Notion integration token
notion = Client(auth='YOUR_NOTION_INTEGRATION_TOKEN')  # <-- Insert your token here

# Function to retrieve all members (users) from the Notion workspace
# Returns a list of dictionaries with each member's name and ID
def get_all_members():
    members_info = []  # List to store member information
    start_cursor = None  # Used for pagination

    while True:
        try:
            # Retrieve a page of members using the Notion API
            response = notion.users.list(start_cursor=start_cursor)
            members = response.get("results", [])

            # Extract and store member information from the response
            for member in members:
                name = member.get("name", "No Name")
                user_id = member.get("id", "No ID")
                members_info.append({"name": name, "id": user_id})

            # Check if there are more pages of results
            if not response.get("has_more", False):
                break  # Exit loop if no more pages

            # Update the start_cursor for the next iteration (pagination)
            start_cursor = response.get("next_cursor")

        except Exception as e:
            # Print any errors that occur and exit the loop
            print(f"An error occurred: {e}")
            break

    return members_info  # Return the list of member info

# Run the function and print the member information
if __name__ == "__main__":
    for member in get_all_members():
        print(f"{member['name']} - Notion ID: {member['id']}")
