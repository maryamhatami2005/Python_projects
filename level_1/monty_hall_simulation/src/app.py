import streamlit as st
from monty_hall import simulate_game
import time

column1, column2, colmn3 = st.columns([0.5,2,0.5])
st.set_page_config(layout="wide")
column2.image("/home/mary/project_based_python/projects/level_1/monty_hall_simulation/images/header.jpg", width = 1000)
st.title("📈Monty Hall Simulation📉")


num_games = st.number_input("Enter number of games to simulate",
                min_value=1, max_value=100000,
                value = 100)

col1, col2 = st.columns(2)
col1.subheader("Win Percentage without Switching")
col2.subheader("Win Percentage with Switching")

chart1 = col1.line_chart(x=None, y=None, height= 400)
chart2 = col2.line_chart(x=None, y=None, height = 400)

wins_no_switch = 0
wins_switch = 0
for i in range(num_games):
    num_wins_without_switching, num_wins_with_switching = simulate_game(1)
    wins_no_switch += num_wins_without_switching
    wins_switch += num_wins_with_switching
    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
    time.sleep(0.01)