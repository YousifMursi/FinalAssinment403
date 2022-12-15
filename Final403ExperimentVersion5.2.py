from psychopy import visual, core, event, monitors
import os
import random
import csv

#the user is presnted with color and text as stimuli, user options are correct or incorrect, the experiment measures the users reaction time to the two stimulus

#set the directory
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# create a window to draw stimuli on
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920 , 1080])
win = visual.Window(
size=[600, 600],
fullscr=False, 
monitor=mon,
color='black',
units='pix')

# create some text to display instructions
instructions = visual.TextStim(
    win=win,
    text="Press 'c' for correct and 'i' for incorrect when the screen color and text match. Press any key to begin",
    color="blue",
)

# create a list of colors to use as stimuli
colors = ["green", "blue", "red", "orange", "purple","yellow", "pink"]

# create a list of words to use as stimuli
words = ["GREEN", "BLUE", "RED", "ORANGE", "PURPLE","YELLOW", "PINK"]

# create a clock to keep track of time
clock = core.Clock()

# create variables to track response time, average reaction time, and correct response
reaction_time = 0
average_reaction_time = 0
correct_response = 0
Trials=30

# create a list to store data in
data = []

# display instructions
instructions.draw()
win.flip()

# wait for the user to press a key to begin
event.waitKeys()

# run the experiment for 20 trials
for i in range(30):
    # randomly choose a color and word from the lists
    color = colors[random.randint(0, len(colors) - 1)]
    word = words[random.randint(0, len(words) - 1)]

    # create a stimuli using the chosen color and word
    color_stimulus = visual.Rect(
        win=win,
        width=400,
        height=400,
        fillColor=color,
        lineColor=color,
    )
    word_stimulus = visual.TextStim(
        win=win,
        text=word,
        color="white",
    )

    # display the stimuli
    color_stimulus.draw()
    word_stimulus.draw()
    win.flip()

    # start the clock
    clock.reset()

    # wait for a response
    response = event.waitKeys(keyList=["c", "i"])

    # stop the clock
    reaction_time = clock.getTime()

    # if the response was "c" and the color and word matched, mark the response as correct
    if response[0] == "c" and color == word:
        correct_response = 1
    else:
        correct_response = 0

    # add the response data to the list
    data.append([reaction_time, correct_response])

    # calculate the average reaction time
    if len(data) > 1:
        total_reaction_time = sum([d[0] for d in data])
        average_reaction_time = total_reaction_time / len(data)
        
#input data into a csv file
with open(os.path.join(data_dir, 'FinalExpData.csv'), 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Trial", "reaction_time", "correct_response"])
    for i in range(len(data)):
        writer.writerow([i + 1, data[i][0], data[i][1]])
        
# Close the window
win.close()