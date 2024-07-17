from datetime import datetime
from os import getenv

from dotenv import load_dotenv

from pixela_client import PixelaClient

load_dotenv()

TOKEN = getenv("TOKEN")
USERNAME = getenv("USERNAME")
GRAPH_ID = getenv("GRAPH_ID")

client = PixelaClient(token=TOKEN, username=USERNAME)

print("""
             _     _ _     _____                _             
  /\  /\__ _| |__ (_) |_  /__   \_ __ __ _  ___| | _____ _ __ 
 / /_/ / _` | '_ \| | __|   / /\/ '__/ _` |/ __| |/ / _ \ '__|
/ __  / (_| | |_) | | |_   / /  | | | (_| | (__|   <  __/ |   
\/ /_/ \__,_|_.__/|_|\__|  \/   |_|  \__,_|\___|_|\_\___|_|   
                                                              
Welcome to your habit tracket, here you can keep a record of your activities""")


def track_user():
    user_option = input("""
        What do you wanna do?
        
            1. Change to another user
            2. Create a new user
            3. Get the current user
    """)

    if user_option == "1" or user_option == "2":
        new_user = input("Enter the user name to use")

    match user_option:
        case "1":
            client.set_current_user(new_user)
            print(f"Now logged into {new_user}")
        case "2":
            response = client.create_user(username=USERNAME)
            print("Client created successfully")
        case "3":
            print(f"You're currently authenticated as {client.get_current_user()}")


def track_graph():
    global GRAPH_ID

    graph_option = input("""
        Choose an option on what you wanna do
            1. Create a new graph
            2. Change to another graph
    """)

    match graph_option:
        case "1":
            graph_id = input("Enter the graph ID to use")
            graph_name = input("Enter the graph name to use")
            unit = input("Enter the unit to use")
            color = input("Enter the color to use")

            client.create_graph(id=graph_id, graph_name=graph_name, unit=unit, color=color)

            GRAPH_ID = graph_id
            print("Graph created successfully")
        case "2":
            GRAPH_ID = input("Enter the graph ID to use")


def track_activity():
    track_option = input("""
    Choose an option on what you wanna do
    
        1. Track today's activity
        2. Update today's activity
        3. Delete today's activity
    """)

    now_str = datetime.now().strftime("%Y%m%d")

    match track_option:
        case "1":
            response = client.create_pixel(graph_id=GRAPH_ID, quantity=1, date=now_str)
        case "2":
            response = client.update_pixel(graph_id=GRAPH_ID, date=now_str, quantity=10)
        case "3":
            response = client.delete_pixel(graph_id=GRAPH_ID, date=now_str)


while True:
    main_option = input("""
    Choose what you wanna change
        1. User
        2. Graphs
        3. Activity
    """)

    match main_option:
        case "1":
            track_user()
        case "2":
            track_graph()
        case "3":
            track_activity()
