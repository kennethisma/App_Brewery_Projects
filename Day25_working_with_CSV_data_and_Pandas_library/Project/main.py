from turtle import Screen, Turtle, write, xcor, ycor
import turtle
import pandas

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state = Turtle()
state.hideturtle()
state.penup()


data = pandas.read_csv("50_states.csv")
list_state = data["state"].to_list()
amount_state = len(list_state)

answers = []
amount_answers = len(answers)

while amount_answers < amount_state:

    input_state = screen.textinput(
        f"{len(answers)}/{amount_state}", "What's another state name?").title()

    guessed_state = data[data.state == input_state]

    if input_state in answers:
        continue

    if input_state in list_state:
        answers.append(input_state)

        data_xcor = guessed_state["x"]
        data_ycor = guessed_state["y"]

        state.goto(x=int(data_xcor), y=int(data_ycor))
        state.write(arg=input_state)

    if input_state == "Exit":
        not_guessed = []

        for state in list_state:
            if state not in answers:
                not_guessed.append(state)

        to_learn = {"States to learn": not_guessed}

        states_to_learn = pandas.DataFrame(to_learn)
        states_to_learn.to_csv("states_to_learn.csv")
        break


screen.exitonclick()
