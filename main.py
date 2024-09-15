from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])# створення додатку

from main_window import *
from menu_window import *

main_window.show()

class Question:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

q1 = Question('Авто', 'car', 'carer', 'curary', 'mashina')
q2 = Question('Ноутбук', 'lapton', 'latonp', 'latou', 'lanin')
q3 = Question('Вода', 'water', 'Kwas', 'Witer', 'Winder')
q4 = Question('Стол', 'table', 'turbo', 'tible', 'turblenin')
q5 = Question('Вікно', 'window', 'wikno', 'dzerkalo', 'lunka')
q6 = Question('Балкон', 'balkon', 'burkule', 'bilkon', 'barkle')

questions = [q1, q2, q3, q4]
radio_btns = [r_btn1, r_btn2, r_btn3, r_btn4]

count_right = 0
count_wrong = 0
count_all = 0

def new_question():
    global cur_quest
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_right.setText(cur_quest.answer)

    shuffle(radio_btns)
    radio_btns[0].setText(cur_quest.answer)
    radio_btns[1].setText(cur_quest.wrong_ans1)
    radio_btns[2].setText(cur_quest.wrong_ans2)
    radio_btns[3].setText(cur_quest.wrong_ans3)

new_question()

def check_ans():
    global count_all, count_right, count_wrong
    radio_button_group.setExclusive(False)
    for btn in radio_btns:
        if btn.isChecked():
            if btn.text() == cur_quest.answer:
                count_right += 1
                count_all += 1
                lbl_correct.setText("Правильно")
                btn.setChecked(False)
                break
    else:
        lbl_correct.setText("Неправильно")
        btn.setChecked(False)
        count_wrong += 1
        count_all += 1
radio_button_group.setExclusive(True)

def next_question():
    if btn_answer.text() == 'Відповісти':
        check_ans()
        answer_group_box.hide()
        result_group_box.show()
        btn_answer.setText('Наступне запитання')
    elif btn_answer.text() == 'Наступне запитання':
        new_question()
        result_group_box.hide()
        answer_group_box.show()
        btn_answer.setText('Відповісти')










def to_menu():
    main_window.hide()
    menu_window.show()

def to_main():
    menu_window.hide()
    main_window.show()

btn_answer.clicked.connect(next_question)
btn_menu.clicked.connect(to_menu)
btn_back.clicked.connect(to_main)
app.exec_()

