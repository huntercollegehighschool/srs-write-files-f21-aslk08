import shelve
import random

shelfFile = shelve.open('uscapitals')  # open file containing dictionary of US Capitals
capitals = shelfFile['capitals']  # stored dictionary

quizNum = 1

# .txt file names (you can modify if you wish, but careful how you do it)
quizname = 'quiz' + str(quizNum) + '.txt'
answerfile = 'answers' + str(quizNum) + '.txt'

# 1. Open 2 files that you will write to, a quiz and an answer key file
# <var> = open(<string>, 'w')
quiz = open(quizname, "w")
answer = open(answerfile, "w")


# 2. Write headings on both files
# <filevariable>.write(<string>)
quiz.write("Quiz 1")
answer.write("Answer 1\n")


# the following creates a list of states, and then puts them in a random order
states = list(capitals.keys())
random.shuffle(states)  # reorder states for each quiz

for questionNum in range(50):
  correct = capitals[states[questionNum]]  # find correct capital from capitals dictionary; states[questionNum] is current state
  wrong = list(capitals.values())  # start with all capitals
  wrong.remove(correct)
  ans = random.sample(wrong, 3)
  ans.append(correct)
  random.shuffle(ans)

  quiz.write(f"\n\nQuestion {questionNum + 1}: What is the captial of {states[questionNum]}")

  let = ["A", "B", "C", "D"]
  cap = []
  for a in range(4):
    quiz.write(f"\n\t{let[a]}. {ans[a]}")
    cap.append(ans[a])

  answer.write(f"{questionNum+1}. {let[cap.index(correct)]}, {correct}\n")
      


answer.close()
quiz.close()


# Hopefully you were able to generate one 50 question quiz. Can you modify this to generate multiple 50 question quizzes (hint: it does involve a loop)