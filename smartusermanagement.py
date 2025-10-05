from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate  # For nicely formatted table

# 1️⃣ Database setup
DATABASE_URL = 'mysql+pymysql://root:@localhost/set'
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# 2️⃣ Define the User model
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, email={self.email})>"

# 3️⃣ Create table if not exists
Base.metadata.create_all(engine)

# 4️⃣ Function to insert a single user
def insert_user(name, username, email, password):
    try:
        new_user = User(name=name, username=username, email=email, password=password)
        session.add(new_user)
        session.commit()
        print(f"✅ User '{username}' inserted successfully!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error inserting '{username}':", e)

# 5️⃣ Function to fetch and display all users
def fetch_users():
    try:
        users = session.query(User).all()
        if users:
            # Format data into a list of lists for tabulate
            table_data = [[u.user_id, u.name, u.username, u.email] for u in users]
            print("\n📋 Users in Database:")
            print(tabulate(table_data, headers=["ID", "Name", "Username", "Email"], tablefmt="fancy_grid"))
        else:
            print("No users found in database.")
    except Exception as e:
        print("❌ Error fetching data:", e)

# 6️⃣ Interactive menu
while True:
    print("\n===== SMART USER MANAGEMENT =====")
    print("1. Insert new user")
    print("2. View all users")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        insert_user(name, username, email, password)
    elif choice == "2":
        fetch_users()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice. Try again.")

# 7️⃣ Close session
session.close()
