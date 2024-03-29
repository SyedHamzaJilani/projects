# Object Oriented Programming
# Quiz Game
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def total_points(self):
        print(f"{self.name}'s total score is: {self.points}")
        return self.points

    def add_point(self):
        self.points += 1

    def ask_question(self, question_number):
        if question_number == 1:
            print(questions[0])
            check = input(f"{options[0]}\n")
            if check.lower() == "a":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is A (Ottawa)")
        elif question_number == 2:
            print(questions[1])
            check = input(f"{options[1]}\n")
            if check.lower() == "a":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is A (Issac Newton)")
        elif question_number == 3:
            print(questions[2])
            check = input(f"{options[2]}\n")
            if check.lower() == "b":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is B (Mars)")
        elif question_number == 4:
            print(questions[3])
            check = input(f"{options[3]}\n")
            if check.lower() == "b":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is B (H20)")
        elif question_number == 5:
            print(questions[4])
            check = input(f"{options[4]}\n")
            if check.lower() == "b":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is B (Jane Austen)")
        elif question_number == 6:
            print(questions[5])
            check = input(f"{options[5]}\n")
            if check.lower() == "b":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is B (Blue Whale)")
        elif question_number == 7:
            print(questions[6])
            check = input(f"{options[6]}\n")
            if check.lower() == "b":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is B (AU)")
        elif question_number == 8:
            print(questions[7])
            check = input(f"{options[7]}\n")
            if check.lower() == "b":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is B (Vincent Van Gogh)")
        elif question_number == 9:
            print(questions[8])
            check = input(f"{options[8]}\n")
            if check.lower() == "a":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
            else:
                print("Incorrect! The correct answer is a (Mount Everest)")
        elif question_number == 10:
            print(questions[9])
            check = input(f"{options[9]}\n")
            if check.lower() == "a":
                print("Correct Answer! 1 point has been added in your total score!")
                self.add_point()
                print("The Quiz has been completed!")
                if self.total_points() >= 5:
                    print(f"Congratulations, {self.name}!")
                else:
                    self.total_points()
            else:
                print("Incorrect! The correct answer is A (Nitrogen)")


questions = ["What is the capital of Canada?",
             "Who is credited with discovering gravity?",
             "Which planet is known as the 'Red Planet'?",
             "What is the chemical symbol for water?",
             "Who wrote the novel 'Pride' and 'Prejudice'?",
             "What is the largest mammal in the world?",
             "What is the chemical symbol for gold?",
             "Who painted the famous artwork 'Starry Night'?",
             "What is the tallest mountain in the world?",
             "Which gas is most abundant in Earth's atmosphere?"]

options = ["a) Ottawa   b) Toronto    c) Montreal    d) Vancouver",
           "a) Isaac Newton b) Albert Einstein  c) Galileo Galilei  d) Thomas Edison",
           "a) Venus b) Mars c) Jupiter d) Saturn",
           "a) W    b) H2O  c) O2   d) H",
           "a) Emily Brontë b) Jane Austen  c) Charles Dickens  d) Mark Twain",
           "a) Elephant b) Blue Whale   c) Giraffe  d) Hippopotamus",
           "a) Ag   b) Au   c) Fe   d) Pb",
           "a) Pablo Picasso    b) Vincent van Gogh c) Leonardo da Vinci    d) Claude Monet",
           "a) Mount Everest    b) Mount Kilimanjaro    c) Mount Fuji   d) K2",
           "a) Nitrogen b) Oxygen   c) Carbon Dioxide   d) Hydrogen"]

player_one = Player("jake")
for i in range(11):
    player_one.ask_question(i)

