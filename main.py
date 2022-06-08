import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("50_states.csv")
choices = []

while len(choices) < 50:

    answer_state = screen.textinput(title=f"{len(choices)}/50 States Correct", prompt="What's another State name?")
    if answer_state:
        answer_state = answer_state.title()
    if answer_state == 'Exit':
        all_states = states["state"].to_list()
        missed_states = [state for state in all_states if state not in choices]
        all_missed_states = pd.DataFrame(missed_states)
        all_missed_states.to_csv("states_to_learn.csv")
        break
    if answer_state not in choices and sum(states["state"] == answer_state):
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = states[states["state"] == answer_state]
        xcor = int(state_data["x"])
        ycor = int(state_data["y"])
        new_turtle.goto(xcor, ycor)
        new_turtle.write(answer_state)
        choices.append(answer_state)
