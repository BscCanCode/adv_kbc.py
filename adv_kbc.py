questions=[["1.Which City is known as capital of INDIA?","New_Delhi","Chennai","Kolkata","Bengaluru",1],
           ["1.Which City is known as capital of INDIA?","New_Delhi","Chennai","Kolkata","Bengaluru",1],
           ["1.Which City is known as capital of INDIA?","New_Delhi","Chennai","Kolkata","Bengaluru",1],
           ["1.Which City is known as capital of INDIA?","New_Delhi","Chennai","Kolkata","Bengaluru",1],
           ["1.Which City is known as capital of INDIA?","New_Delhi","Chennai","Kolkata","Bengaluru",1],
           ["1.Which City is known as capital of INDIA?","New_Delhi","Chennai","Kolkata","Bengaluru",1],
           ["1.Which City is known as capital of INDIA?","New_Delhi","Chennai","Kolkata","Bengaluru",1]]
levels=[1000,5000,10000,50000,100000,150000,200000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(question[0])
    print(f"1.{question[1]}\t2.{question[2]}\n3.{question[3]}\t4.{question[4]}")
    try:
        reply=int(input("Enter the input between 1-4:"))
        if 0<reply<=4:
            if reply==question[5]:
                print(f"Answer is correct,you won Rs.{levels[i]}")
                if i==2:
                    money=10000
                elif i==4:
                    money=100000
                elif i==6:
                    money=200000
            else:
                print("Answer is incorrect!")
                print(f"Amount you are taking home is Rs.{money}")
                break
        else:
            print("Input out of range 1-4")
            break
    except ValueError:
        print("Strings value not accepted")
        break
