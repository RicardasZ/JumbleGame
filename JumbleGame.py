from tkinter import *
from PIL import ImageTk
from random import choice, shuffle
import pygame

root = Tk()
root.title('Jumble Game')
root.geometry('700x500')
root.iconbitmap(r'puzzle_icon.ico')
root.resizable(False, False)

background = ImageTk.PhotoImage(file='background_image.jpg')

canvas = Canvas(root)

canvas.pack(fill='both', expand=True)

canvas.create_image(-500, -500, image=background, anchor='nw')

menu = Menu(root)
root.config(menu=menu)
submeniu = Menu(menu, tearoff=0)

pygame.init()

click_sound = pygame.mixer.Sound('click_sound_effect.wav')

hint_index = 0

score = StringVar()
score1 = 100
correct = StringVar()
correct1 = 0
incorrect = StringVar()
incorrect1 = 0

correct.set(f'Correct answers: {correct1}')
incorrect.set(f'Incorrect answers: {incorrect1}')


def shuffler():
    global score1
    score1 -= 100
    score.set(f'Score: {score1}')

    global hint_label, hint_index
    hint_label.config(text='')
    hint_index = 0
    all_words = ['apple', 'avocado', 'banana', 'blackberry', 'blueberry', 'beet', 'broccoli', 'carrot', 'cherry',
                 'corn',
                 'cucumber', 'jalapeno',
                 'garlic', 'grape',
                 'grapefruit', 'mushroom', 'mango', 'nectarine', 'lettuce', 'onion', 'orange', 'lemon', 'lime', 'peach',
                 'pumpkin',
                 'pepper',
                 'persimmon', 'pineapple', 'papaya',
                 'raspberry', 'strawberry', 'spinach', 'tomatoe',
                 'watermelon', 'kiwi', 'zucchini']

    global word
    word = choice(all_words)
    break_apart_word = list(word)
    shuffle(break_apart_word)
    shuffled_word = ''

    for letter in break_apart_word:
        shuffled_word += letter
    func_shuffled_word.config(text=shuffled_word)

    global button_clicked
    if button_clicked:
        click_sound.play()


def on_pick_another_click():
    global button_clicked
    button_clicked = True
    shuffler()


button_clicked = False


def answer():
    global score1, correct1, incorrect1
    click_sound.play()
    if word == entry_answer.get():
        correct1 += 1
        correct.set(f'Correct answers: {correct1}')
        score1 += 200
        score.set(f'Score: {score1}')
        shuffler()
        result_label.config(text='Correct answer!', fg='green')
        entry_answer.delete(0, END)
    else:
        incorrect1 += 1
        incorrect.set(f'Incorrect answers: {incorrect1}')
        score1 -= 100
        score.set(f'Score: {score1}')
        result_label.config(text='Wrong answer, please try again.', fg='red')
        entry_answer.delete(0, END)


def hint():
    global hint_index, score1
    click_sound.play()
    if hint_index < len(word):
        hint_text = f"Hint: " + word[:hint_index + 1]
        hint_label.config(text=hint_text)
        hint_index += 1
        score1 -= 50
        score.set(f'Score: {score1}')


def info():
    info_window = Toplevel(root)
    info_window.title('Information')
    info_window.geometry('400x250')
    info_window.iconbitmap(r'puzzle_icon.ico')
    info_window.resizable(False, False)

    info_label = Label(info_window,
                       text='How to play:\nPlace letters in their right order to form correct word.\nUse button Hint if u have no clue.\nChange word by pressing Pick Another Word.\n\nCorrect answer[+100]\nIncorrect answer[-100]\nHint[-50]\nPick Another Word[-100]\n\nGood Luck!',
                       font=('Arial', 12))
    info_label.pack(pady=20)


def restart():
    global score1, correct1, incorrect1, button_clicked
    score1 = 100
    correct1 = 0
    incorrect1 = 0
    button_clicked = False

    score.set(f'Score: {score1}')
    correct.set(f'Correct answers: {correct1}')
    incorrect.set(f'Incorrect answers: {incorrect1}')
    result_label.config(text='')
    hint_label.config(text='')

    shuffler()


canvas.create_text(350, 40, text='Welcome to Jumble Game!', font=('Arial', 28), anchor='center')

func_shuffled_word = Label(root, font=('Arial', 38), bg='#af8b5e')
func_shuffled_word_window = canvas.create_window(350, 130, anchor='center', window=func_shuffled_word)

entry_answer = Entry(root, font=('Arial', 24))
entry_answer_window = canvas.create_window(350, 220, anchor='center', window=entry_answer)

answer_button = Button(root, text='Answer', command=answer, width=8, font=10)
answer_button_window = canvas.create_window(220, 270, anchor='center', window=answer_button)

pick_another_button = Button(root, text='Pick Another Word', command=on_pick_another_click, width=15, font=10)
pick_another_button_window = canvas.create_window(350, 270, anchor='center', window=pick_another_button)

hint_button = Button(root, text='Hint', command=hint, width=8, font=10)
hint_button_window = canvas.create_window(480, 270, anchor='center', window=hint_button)

hint_label = Label(root, font=("Arial", 22), bg='#af8b5e')
hint_label_window = canvas.create_window(350, 400, anchor='center', window=hint_label)

result_label = Label(root, font=('Arial', 22), bg='#af8b5e')
result_label_window = canvas.create_window(350, 330, anchor='center', window=result_label)

correct_label = Label(root, textvariable=correct, font=('Arial', 12), bg='#af8b5e')
correct_window = canvas.create_window(130, 460, anchor='w', window=correct_label)

incorrect_label = Label(root, textvariable=incorrect, font=('Arial', 12), bg='#af8b5e')
incorrect_window = canvas.create_window(300, 460, anchor='w', window=incorrect_label)

score_label = Label(root, textvariable=score, font=('Arial', 12), bg='#af8b5e')
score_window = canvas.create_window(510, 460, anchor='center', window=score_label)

menu.add_cascade(label='Menu', menu=submeniu)
submeniu.add_command(label='Info', command=info)
submeniu.add_command(label='Restart', command=restart)

shuffler()
root.mainloop()
