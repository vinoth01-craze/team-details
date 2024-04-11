import streamlit as st
import pandas as pd
import sqlite3

# Function to display the form and team details table
def display_team_details(conn):
    st.write("""
    # Team Details
    """)
    st.markdown(
        """
        <style>
        .stTextInput>div>div>input[type="number"] {
            width: 1000px !important; /* Adjust width of number input box */
            background-color: white !important; /* Set background color to white */
        }
        h1 {
            width: 400px;
            padding: 0%;
            top: 5%;
            left: 40%;
            font-size: 60px;
            color: lightwhite;
            font-family: Garamond, serif;
            white-space: nowrap; /* Ensures text stays on a single line */
            -webkit-animation: glow 1s ease-in-out infinite alternate;
            -moz-animation: glow 1s ease-in-out infinite alternate;
            animation: glow 1s ease-in-out infinite alternate;
            margin-bottom: 100px;
            background-clip: padding-box;
            box-shadow: 0 0 50px white;
        }
        h2{
            color:lightblue;
            font-family: Copperplate, Papyrus, fantasy;
        }
        h3{
            color:yellow;
          font-family: Copperplate, Papyrus, fantasy;
        }
        P {
            color: white;
            font-family: Copperplate, Papyrus, fantasy;
        }
        .stButton>button {
            background-color: black; /* Background color of the button */
        }
        .stButton>button:hover {
            cursor: pointer;
        }
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1598690042638-1b9844b7ef83?q=80&w=2065&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
            object-fit:center;
        }
        @-webkit-keyframes glow {
            from {
                text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #e60073, 0 0 40px #e60073, 0 0 50px #e60073, 0 0 60px #e60073, 0 0 70px #e60073;
            }
            to {
                text-shadow: 0 0 20px #fff, 0 0 30px #ff4da6, 0 0 40px #ff4da6, 0 0 50px #ff4da6, 0 0 60px #ff4da6, 0 0 70px #ff4da6, 0 0 80px #ff4da6;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create form inputs
    team_name = st.text_input("Team Name")
    member1_name = st.text_input("Team Member 1 Name")
    member1_reg_num = st.text_input("Team Member 1 Register Number")
    member2_name = st.text_input("Team Member 2 Name")
    member2_reg_num = st.text_input("Team Member 2 Register Number")
    topic = st.text_input("Topic")

    if st.button("Submit"):
        # Append the new entry to the database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teams (team_name, member1_name, member1_reg_num, member2_name, member2_reg_num, topic) VALUES (?, ?, ?, ?, ?, ?)",
                       (team_name, member1_name, member1_reg_num, member2_name, member2_reg_num, topic))
        conn.commit()

    st.write("""
    ## Team Details
    """)
    # Retrieve data from the database
    df = pd.read_sql("SELECT * FROM teams", conn)
    st.write(df)

# Create or connect to the SQLite database
conn = sqlite3.connect("team_details.db")

# Create a table if it doesn't exist
conn.execute('''CREATE TABLE IF NOT EXISTS teams
             (id INTEGER PRIMARY KEY,
             team_name TEXT,
             member1_name TEXT,
             member1_reg_num TEXT,
             member2_name TEXT,
             member2_reg_num TEXT,
             topic TEXT)''')

# Display the team details
display_team_details(conn)
