import turtle
import pandas as pd
from states import States

# Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
prompt = "Guess a state"
score = 0
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
learn_file = "states_to_learn.csv"

state_obj = States()

while len(guessed_states) < 50:
    states_df = pd.read_csv('50_states.csv')  # import CSV
    states_dict = states_df.set_index('state').T.to_dict('list')  # This changes the index of the dictionary to State
    # (our column header) which can contain our coordinates, rather than each column header being an item in the
    # dictionary
    answer_state = screen.textinput(title=f"{score}/50", prompt=prompt)  # Capture guess
    if answer_state is None:
        state_obj.add_state(state="Thanks for playing", font_size=20, colour="Blue")
        to_learn_list = [state for state in states_dict.keys() if state not in guessed_states]  # Include state if not
        # in guessed states
        to_learn_df = pd.DataFrame(to_learn_list) # turn list into dataframe
        to_learn_df.to_csv(learn_file, index=False, header=["States to learn"])
        print(to_learn_df)
        break
    answer_state_titled = answer_state.title()  # Convert guess to Title case

    matching_state = answer_state in states_dict  # returns true if player answer in dict
    if answer_state_titled in guessed_states:
        prompt = "You've already guessed this state"
    elif answer_state_titled in states_dict:
        current_x, current_y = states_dict[answer_state_titled]  # assign coordinates from dictionary entry for answer
        guessed_states.append(answer_state_titled)
        state_obj.add_state(state=answer_state_titled, x=current_x, y=current_y)
        prompt = "Guess a state"
        score += 1
    else:
        prompt = "Incorrect, try again"

if len(guessed_states) == 50:
    state_obj.add_state(state="You guessed all the states!", font_size=20, colour="Blue")

screen.exitonclick()
