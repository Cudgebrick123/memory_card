from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

class Question():
   def __init__(
      self, question, right_answer,
      wrong1, wrong2, wrong3):
         self.question = question
         self.right_answer = right_answer
         self.wrong1 = wrong1
         self.wrong2 = wrong2
         self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.resize(400, 320)
text = QLabel('Какой национальности не существует')
text2 = QPushButton("Ответить")


      

RadioGroupBox = QGroupBox("варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_result = QLabel("прав ты или нет")
lb_Correct = QLabel("ответ будет тут!")
ans_v = QVBoxLayout()


ans_v.addWidget(lb_result, alignment=(Qt.AlignLeft))
ans_v.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(ans_v)


layout_line1 = QHBoxLayout()
layout_line2= QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.show()
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(text2, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.setSpacing(5)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]




def show_result():
   RadioGroupBox.hide()
   AnsGroupBox.show()
   text2.setText("Следующий вопрос")

def show_question():
   AnsGroupBox.hide()
   RadioGroupBox.show()
   text2.setText("Ответить")
   RadioGroup.setExclusive(False) 
   rbtn_1.setChecked(False)
   rbtn_2.setChecked(False)
   rbtn_3.setChecked(False)
   rbtn_4.setChecked(False)
   RadioGroup.setExclusive(True)



def start_test():
   if text2.text() == "Ответить":
      check_answer()
   else:
      next_question()
      
def ask(q:Question):
   shuffle(answers)
   answers[0].setText(q.right_answer)
   answers[1].setText(q.wrong1)
   answers[2].setText(q.wrong2)
   answers[3].setText(q.wrong3)
   text.setText(q.question)
   lb_Correct.setText(q.right_answer)
   show_question()

def show_correct(ans):
   lb_result.setText(ans)
   show_result()

main_win.cur_question = -1



def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ',main_win.total, '\n-Правильных ответов: ', main_win.score)
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)
      
def check_answer(): 
    if answers[0].isChecked():
        show_correct('ВЕРНО')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('НЕВЕРНО')
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')


question_list = []
q1 = Question(
      "Государственный язык Бразилии", 
"Португальский",
      "Русский", "Немецкий", "Итальянский")
question_list.append(q1)


question_list.append(
   Question("Цвет травы",
   "Зелёный", "Яблоки", "красный", "Чёрный")
)

question_list.append(
Question("Сколько весит 1кг ваты",
         "1кг", "4тб", "слон", "42кг")
      )
         


question_list.append(
   Question("Как зовут сына главного героя в the forest",
   "Тимми", "Гарри", "Томас", "Иван")
)


question_list.append(
   Question("Начало зимней распродажи в steam",
   "19 декабря", "24 июня", "13 мая", "8 января")
)


question_list.append(
   Question("Сколько фигур в шахматах",
   "32", "36", "42", "28")
)

text2.clicked.connect(start_test)
main_win.score = 0
main_win.total = 0

next_question()
main_win.setLayout(layout_card)
main_win.show()
app.exec_()