import turtle
import pandas

screen = turtle.Screen()
screen.title("Ro Country Guessing game")

image = 'romania_judete.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("ro_states_pos.csv")
game_is_running = True
guessed_states = []
correct_answers = 0
list_states = data["States"].tolist()
while game_is_running:
    screen_input = screen.textinput(title=f"{correct_answers}/{len(list_states)}", prompt="What is another state name").title()
    if screen_input in list_states:
        guessed_states.append(screen_input)
        correct_answers += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["States"] == screen_input]
        t.goto(state_data.X.item(), state_data.Y.item())
        t.write(arg=screen_input,font=("Arial", 15, "normal"), align="center")
        t.showturtle()
        if correct_answers == len(list_states):
            game_is_running = False
            print("You guessed all of them")
    if screen_input == "Exit":
        missed_states = [st for st in list_states if st not in guessed_states]
        print(f"You missed the following states:{missed_states}")
        game_is_running = False



screen.mainloop()
