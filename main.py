from turtle import Turtle, Screen
import pandas
s = Screen()
answer = Screen()
answer.setup(400, 300)
turtle = Turtle()

s.setup(725, 491)
s.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

game_is_one = True


def get_mouse_cor(x, y):
    print(x)


turtle.onclick(get_mouse_cor)
data = pandas.read_csv("/Users/ytouate/PycharmProjects/Us game/50_states.csv")
# getting the states as a list
states_list = data["state"].tolist()
for i in range(len(states_list)):
    states_list[i] = states_list[i].lower()
# generating the x cor && and the y cor
x_cor = data["x"].tolist()
y_cor = data["y"].tolist()

# gather a dict contains all the needed info
data_dict = {
    "state": states_list,
    "x_cor": x_cor,
    "y_cor": y_cor
}
# generating the turtle to write with
text = Turtle()
text.penup()
text.hideturtle()

j = 0
while game_is_one:
    var = answer.textinput("Guess the state", "ENTER A US STATE\n")
    var = var.lower()
    if var in states_list:
        j = states_list.index(var)
        text.goto(data_dict["x_cor"][j], data_dict["y_cor"][j])
        text.write(f"{var}", align='center', font=('Arial', 15, 'normal'))
    else:
        game_is_one = False

s.exitonclick()
