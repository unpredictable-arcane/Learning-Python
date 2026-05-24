questions = [
    ["Who is the missile man of India?", "Vikram Sarabhai", "A.P.J. Abdul kalam", "Homi J. Bhabha", "Rabindranath Tagore", 2],
    ["Who is the World Chess Champion 2026?", "Rameshbabu Praggnanandhaa", "Javokhir Sindarov", "Gukesh Dommaraju", "Magnus Carlsen", 3],
    ["Who is the creator of Linux?", "Ken Thompson", " Mati Aharoni", "Linus Torvalds", "Dennis Ritchie", 3],
    ["Who is the World's Strongest Man 2017?", "Brian shaw", "Hafthor Bjornsson", "Paul Anderson", "Eddie Hall", 4],
    ["Who is the CTO of palantir?", "Lauren Friedman Stat", "Shyam Sankar", "Peter Thiel", "Alex Karp", 2]
]

prizes = [3000, 30000, 300000, 3000000, 30000000]

i = 0
for question in questions: 
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was questions[5]")
        print("Better luck next time!")
        break
    print(f"You won {prizes[i]}")
    i +=1