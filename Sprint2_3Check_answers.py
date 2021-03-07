from tkinter import*
from tkinter import ttk
from random import*

class MathQuiz:
    def __init__(me,parent):
        
        #Widget for the Welcome Frame
        
        me.Welcome = Frame(parent)
        me.Welcome.grid(row=0, column=0)
        
        me.TitleLabel = Label(me.Welcome, text = "Welcome to Math Quiz",
                              bg = "blue", fg = "white", width = 20, padx = 30, pady = 10,
                              font = ("Time", '14', "bold italic"))
        me.TitleLabel.grid(columnspan = 2)
        
        #Name and Age Labels
        me.NameLabel = Label(me.Welcome, text = "Name", anchor = W,
                             fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
        me.NameLabel.grid(row = 2, column = 0)
        
        me.AgeLabel = Label(me.Welcome, text = "Age", anchor = W,
                            fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
        me.AgeLabel.grid(row = 3, column = 0)
        
        #Name and Age Entry
        me.NameEntry = ttk.Entry(me.Welcome, width = 20)
        me.NameEntry.grid(row=2, column = 1, columnspan = 2)
        
        me.AgeEntry = ttk.Entry(me.Welcome, width = 20)
        me.AgeEntry.grid(row=3, column = 1)
        
        #Warning, Difficulty level labels and Radio buttons
        me.WarningLabel = Label(me.Welcome, text = "", anchor=W,
                                fg = "red", width = 20, padx = 30, pady = 10)
        me.WarningLabel.grid(row=4, columnspan = 2)
        
        me.DifficultyLabel = Label(me.Welcome, text = "Choose Difficulty", anchor=W,
                                   fg = "black", width = 10, padx = 30, pady = 10,font = ("Time", '12', "bold italic"))
        me.DifficultyLabel.grid(row=5, column = 0)
        
        me.difficulty = ["Easy", "Medium", "Hard"]
        me.diff_lvl = StringVar()
        me.diff_lvl.set(0)
        me.diff_btns = []
        
        for i in range(len(me.difficulty)):
            me.rb = Radiobutton(me.Welcome, variable = me.diff_lvl, value = i, text = me.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            me.diff_btns.append(me.rb)
            me.rb.grid(row = i+6, column = 0, sticky = W)
        
        me.NextButton = ttk.Button(me.Welcome, text = 'Next', command = me.show_Questions)
        me.NextButton.grid(row = 8, column = 1) 
        
        #Widgets for Question Frame
        
        me.Questions = Frame(parent)
        #me.Questions.grid(row=0, column=1)
        
        
        me.QuestionsLabel = Label(me.Questions, text = "Answer Quiz Questions",
                              bg = "blue", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        me.QuestionsLabel.grid(columnspan = 2)
        
        me.Problems = Label(me.Questions, text = "")
        me.Problems.grid(row = 1, column = 0)
        
        me.AnswerEntry = ttk.Entry(me.Questions, width = 20)
        me.AnswerEntry.grid(row=1, column = 1)
        
        me.feedback = Label(me.Questions, text = "")
        me.feedback.grid(row = 2, column = 0)
        
        me.HomeButton = ttk.Button(me.Questions, text = 'Home', command = me.show_Welcome)
        me.HomeButton.grid(row = 8, column = 0)
        
        me.check_button = ttk.Button(me.Questions, text = 'Check answer', command = me.check_answer)
        me.check_button.grid(row=8, column=1)
        
        me.next_button = ttk.Button(me.Questions, text = 'Next question', command = me.next_question)
        me.next_button.grid(row=8, column=2)
        
    def show_Welcome(me):
        me.Questions.grid_remove()
        me.Welcome.grid()
    
    def show_Questions(me):
        try:
            if me.NameEntry.get() == "":
                me.WarningLabel.configure(text = "Please enter name")
                me.NameEntry.focus()
                
            elif me.NameEntry.get() .isalpha() == False:
                me.WarningLabel.configure(text = "Pleasae enter text")
                me.NameEntry.delete(0, END)
                me.NameEntry.focus()
                
            elif me.AgeEntry.get() == "":
                me.WarningLabel.configure(text = "Please enter age")
                me.AgeEntry.focus()
                
            elif int(me.AgeEntry.get()) > 12:
                me.WarningLabel.configure(text= "You are too old")
                me.AgeEntry.delete(0, END)
                me.AgeEntry.focus()
                
            elif int(me.AgeEntry.get()) < 0:
                me.WarningLabel.configure(text= "You are too old")
                me.AgeEntry.delete(0, END)
                me.AgeEntry.focus()
            elif int(me.AgeEntry.get()) < 7:
                me.WarningLabel.configure(text = "You are too young")
                me.AgeEntry.delete(0, END)
                me.AgeEntry.focus()
                
            else:
                me.Welcome.grid_remove()
                me.Questions.grid()
                
        except ValueError:
            me.WarningLabel.configure(text = "Please enter a number")
            me.AgeEntry.delete(0, END)
            me.AgeEntry.focus()
            
    def next_question(me):
        x = randrange(10)
        y = randrange(10)
        me.answer = x + y
            
        question_text = str(x) + " + " + str(y) + " = "
        me.Problems.configure(text = question_text)
        
    def check_answer(me):
        try:
            ans = int(me.AnswerEntry.get())
            
            if ans == me.answer:
                me.feedback.configure(text = "Correct")
                me.AnswerEntry.delete(0, END)
                me.AnswerEntry.focus()
                me.next_question()
                
            else:
                me.feedback.configure(text = "Incorrect")
                me.AnswerEntry.delete(0, END)
                me.AnswerEntry.focus()
                me.next_question()
                
        except ValueError:
            me.feedback.configure(text = "Enter a number")
            me.AnswerEntry.delete(0, END)
            me.AnswerEntry.focus()
                
                
        
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()
        
        