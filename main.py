import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_data = pd.read_csv("50_states.csv")
us_states = all_data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
									prompt="What's another state's name or exit to end game?").title()
	if answer_state == "Exit":
		break
	if answer_state in us_states:
		guessed_states.append(answer_state)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = all_data[all_data.state == answer_state]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(answer_state)


# states to learn.csv

miss_states = [state for state in us_states if state not in guessed_states]
miss_dict = {"Missed States": miss_states}

df = pd.DataFrame(miss_dict)
df.to_csv("learn.csv")
