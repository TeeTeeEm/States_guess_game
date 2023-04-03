import turtle, pandas
from name_shower import Name

screen = turtle.Screen()
screen.title("US STATES Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states.state.tolist()
score = 0
missing_states = []
guessed_states = []

while score <= 50:
    answer = screen.textinput(title=f"{score}/50 State correct", prompt="What's the State's name?").title()
    if answer == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        missed = pandas.DataFrame(missing_states)
        missed.to_csv("Missed_states")
        break

    if (states.state == answer).any():
        guessed_states.append(answer)
        score += 1
        x_cor = states[states.state == answer].x
        y_cor = states[states.state == answer].y
        name_shower = Name()
        name_shower.move(int(x_cor), int(y_cor))
        name_shower.correct(answer)

screen.exitonclick()
