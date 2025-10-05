from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1️⃣ Database setup
# Format: 'mysql+pymysql://username:password@localhost/databasename'
DATABASE_URL = 'mysql+pymysql://root:@localhost/set'

engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL statements in console
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# 2️⃣ Define the User model
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, autoincrement=True)  # or use Integer with auto-increment
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False,primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username}, email={self.email})>"

# 3️⃣ Create table if it doesn't exist
Base.metadata.create_all(engine)

# 4️⃣ Insert a new user
try:
    new_user = User(
        # user_id=101.0,  # provide unique ID if not auto-increment
        name='Keshav3',
        username='test_user3',
        email='test3@example.com',
        password='secret3'
    )
    session.add(new_user)
    session.commit()
    print(" Record inserted successfully!")

except Exception as e:
    session.rollback()
    print(" Error:", e)

# 5️⃣ Fetch all users
try:
    users = session.query(User).all()
    print("\n✅ Users in database:")
    for user in users:
        print(user)

except Exception as e:
    print(" Error fetching data:", e)

finally:
    session.close()
