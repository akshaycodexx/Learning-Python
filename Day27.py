#kon banega crore pati using list data type to store the question therir ans 
#display the final score 

Questions=[
    "who was the Pm of India?",
    "What is the capital of india?",
    "Who wrote the National Anthem of india?",
    "Full name of mahatma Gandhi",
    "Which planet is know is the red planet"
    
]

Options=[
      ["1. Jawaharlal Nehru", "2. Lal Bahadur Shastri", "3. Indira Gandhi", "4. Rajiv Gandhi"],
    ["1. Mumbai", "2. New Delhi", "3. Kolkata", "4. Chennai"],
    ["1. Bankim Chandra Chatterjee", "2. Rabindranath Tagore", "3. Sarojini Naidu", "4. Subhas Chandra Bose"],
    ["1. Mohandas Karamchand Gandhi", "2. Mohanlal Karamchand Gandhi", "3. Murlidhar Gandhi", "4. Manohar Karamchand Gandhi"],
    ["1. Earth", "2. Venus", "3. Mars", "4. Jupiter"]
    
]
Correct_Ans=[1,2,2,1,3]

Score=0
def Ask_question():
    global Score
    for i in range(len(Questions)):
        print(Questions[i])
        for option in Options[i]:
            print(option)
        answer=int(input("Enter the correct Option: "))
        if(answer==Correct_Ans[i]):
            print("Correct ans!")
            Score+=1
        else:
            print("Wrong Ans!")


#function to display the Score

def Display():
    print(f"Your Score is {Score} out of {len(Questions)}")


def main():
    print("WellCome to KBC!")
    Ask_question()
    Display()






#run the game
if __name__ == "__main__":
    main()
    