import turtle
import pandas


screen=turtle.Screen()

screen.title("U.S. State Game")
image="blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")

states=data['state'].str.title().to_list()
# x_axis=data['x'].to_list()
# y_axis=data['y'].to_list()


count=0
guessed_states=[]
while len(guessed_states)<50:
    
    state_input=turtle.textinput(title=f"You have got {count}/50",prompt="Name of the state").title()
    if state_input=="Exit":
          break
    if state_input in states and state_input not in guessed_states:
            guessed_states.append(state_input)
            count+=1
            index_of_state=states.index(state_input)
            states.pop(index_of_state)
            row=data[data['state']==state_input]
            x_axis=int(row['x'])
            y_axis=int(row['y'])
            tim=turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            tim.goto(x_axis,y_axis)
            tim.write(state_input)

missing_states=pandas.DataFrame(states)
missing_states.to_csv("states_to_learn.csv")

