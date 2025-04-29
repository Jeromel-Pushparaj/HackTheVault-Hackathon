from pymongo import MongoClient
from bson.objectid import ObjectId

skills_list = [
    "Automation Testing",
    "Blockchain",
    "Data Science",
    "Database",
    "DevOps Engineer",
    ".Net Developer",
    "ETL Developer",
    "Electrical Engineering",
    "HR",
    "Hadoop",
    "Java Developer",
    "Network Security Engineer",
    "Operations Manager",
    "PMO",
    "Python Developer",
    "SAP Developer",
    "Sales",
    "Testing",
    "Web Designing"
]

# 1. Connect to MongoDB
connection_string = "mongodb://localhost:27017/"  # Replace with your connection string!
client = MongoClient(connection_string)

# 2. Get the database
db = client['app']  # Use the 'app' database

# 3. Get the collection
collection = db['roles']  # Use the 'roles' collection

# 4. Iteratively insert data with _id
try:
    for skill in skills_list:
        # Create a document with _id and skill
        data = {
            "_id": ObjectId(),  # Generate a unique ObjectId for each document
            "skill": skill
        }
        result = collection.insert_one(data)
        print(f"Inserted document with ID: {result.inserted_id}, Skill: {skill}")
except Exception as e:
    print(f"An error occurred: {e}")

# 5. Close the connection (optional, but good practice)
client.close()