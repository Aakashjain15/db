from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["university_db"]  # Database name
collection = db["faculty_info"]  # Collection name

# Function to get faculty data from user and insert it into the database
def get_and_insert_faculty_info():
    print("Enter Faculty Information:")

    # Get input for each field
    name = input("Name of Faculty: ")
    designation = input("Designation: ")
    emp_id = int(input("EMP ID: "))
    domains = input("Domains (separated by commas): ").split(",")  # Convert to list
    university_email_id = input("University Email ID: ")
    image_link = input("Image Link: ")
    max_teams = int(input("Max Teams: "))
    total_batches = int(input("Total Batches: "))

    # Create a dictionary to store the data
    faculty_data = {
        "Name": name,
        "Designation": designation,
        "EMP_ID": emp_id,
        "Domains": [domain.strip() for domain in domains],  # Clean up whitespace
        "University_Email_ID": university_email_id,
        "Image_Link": image_link,
        "Max_Teams": max_teams,
        "Total_Batches": total_batches
    }

    # Insert the data into the database
    result = collection.insert_one(faculty_data)
    print(f"Faculty information inserted with ID: {result.inserted_id}")

# Call the function to insert data
if __name__ == "__main__":
    get_and_insert_faculty_info()
