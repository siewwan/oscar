from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle
from PyQt5.QtGui import QFont, QColor, QPalette
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question("The national language of Brazil", 'Portuguese', 'Brazilian', 'Spanish', 'Italian'))
questions_list.append(Question("What country has the highest life expectancy", 'Hong Kong', 'China', 'Japan', 'Korea'))
questions_list.append(Question("How many bones do we have in an ear?", '3', '1', '4','2'))
questions_list.append(Question("Who has the best point record in NBA?", 'LeBron James', 'Kareem Abdul-Jabbar', 'Michael Jordan', 'Kobe Bryant'))
questions_list.append(Question("What is the most common surname in the United States?", 'Smith', 'Oscar', 'Lucas', 'Robert'))
questions_list.append(Question("What disease commonly spread on pirate ships?", 'Scurvy', 'Stroke', 'Dengue fever', 'Malaria'))
questions_list.append(Question("What company was initially known as Blue Ribbon Sports?", 'Nike', 'Adidas', 'Puma', 'Anta'))
questions_list.append(Question("What year was the United Nations established?", '1945', '1947', '1946', '1948'))
questions_list.append(Question("How many minutes are in a full week?", '10080', '10090', '10100', '10070'))
questions_list.append(Question("Aureolin is a shade of what color?", 'Yellow', 'Blue', 'Green', 'White'))




app = QApplication([])

app.setStyle('QtCurve')

window = QWidget()
window.setWindowTitle('Memory card')

font = QFont("Helvetica [Cronyx]", 12)
app.setFont(font)

palette = QPalette()
palette.setColor(QPalette.Window, QColor(128, 0, 128))
palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
app.setPalette(palette)

width = 500
height = 300
window.resize(width, height)

lb_Question = QLabel('Questions here')
btn_OK = QPushButton('Answer')

RadioGroupBox = QGroupBox('Answer options')
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

lb_Question.setFont(QFont("Arial", 18, QFont.Bold))

btn_OK.setFont(QFont("Arial", 12))


layout_answer = QHBoxLayout()
layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans1.addWidget(rbtn_1)
layout_ans1.addWidget(rbtn_2)
layout_ans2.addWidget(rbtn_3)
layout_ans2.addWidget(rbtn_4)

layout_answer.addLayout(layout_ans1)
layout_answer.addLayout(layout_ans2)
RadioGroupBox.setLayout(layout_answer)

AnsGroupBox = QGroupBox('Test result')
lb_Result = QLabel('You are correct/ You are incorrect!')
lb_Result.setFont(QFont("Arial", 14))
lb_Result.setStyleSheet("color: red;")
lb_Correct = QLabel('The correct answer will be here!')
lb_Correct.setFont(QFont("Arial", 14))
lb_Correct.setStyleSheet("color: green;")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_card = QVBoxLayout()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=6)

layout_card.addLayout(layout_line3, stretch=1)

window.setLayout(layout_card)

def show_result():
    '''show answer panel'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    '''show question panel'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' if an answer option was selected, check and show answer panel '''
    if answers[0].isChecked():
        show_correct('You are correct!')
        window.score += 1
        print('Statistics\n-Total questions: ', window.cur_question +1, '\n-Right answers: ', window.score)
        print(f'Rating: {window.score/(window.cur_question+1)*100}%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('You are incorrect! \nThe correct answer is:')
            print('Statistics\n-Total questions: ', window.cur_question +1, '\n-Right answers: ', window.score)
            print('Rating: ', (window.score/(window.cur_question+1)*100), '%')
        


def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()
window.score = 0
window.total = 0
window.cur_question = -1
 
btn_OK.clicked.connect(click_OK)
next_question()  

window.show()
app.exec_() 
