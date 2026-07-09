# Write your code here.
# Task 1
def hello():
    return("Hello!")
print(hello())

#Task 2
def greet(name):
    return(f"Hello, {name}!")

#Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return(a + b)
            case "subtract":
                return(a - b)
            case "multiply":
                return(a * b)
            case "divide":
                return(a / b)
            case "modulo":
                return(a % b)
            case "int_divide":
                return(a // b)
            case "power":
                return(a ** b)
        result = a * b
        print(result)
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
        return("You can't multiply those values!")
    #except Exception as e:
        #print(f"An error occurred: {e}")

#Task4
def data_type_conversion(data, dataType):
    try:
        match dataType:
            case "float":
                return(float(data))
            case "str":
                return(str(data))
            case "int":
                return(int(data))
    except ValueError:
        return(f"You can't convert {data} into a {dataType}.")    

#Task 5
def grade(*args):
    try:
        average = sum(args)/len(args)
        if average >= 90:
            return("A")
        elif (average >= 80) & (average <= 89):
            return("B")
        elif (average >= 70) & (average <=79):
            return("C")
        elif (average >= 60) & (average <=69):
            return("D")
        else:
            return("F")
    except Exception as e:
        return(f"Invalid data was provided.")
    
  
#Task 6
def repeat(str, count):
    emptyStr = ""
    for i in range(count):
        emptyStr = emptyStr + str

    return emptyStr
    

#Task 7
def student_scores(position, **kwargs):
    
    if position == "best":
        bestStudent = ""
        bestGrade = 0
        for key, value in kwargs.items():
            if value > bestGrade:
                bestGrade = value
                bestStudent = key
        return(bestStudent)
    if position == "mean":
        averageScore = sum(kwargs.values())/len(kwargs.values())
        return averageScore 

#Task 8
def titleize(str):
    words = str.split()
    littleWords = {"a", "on", "an", "the", "of", "and", "is","in"}
    for i, word in enumerate(words):
        if word.lower() not in littleWords:
            words[i] = word.capitalize()
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()
    
    newStr = " ".join(words)
    return newStr

#Task 9
def hangman(secret, guess):

    secretList = list(secret)
    result = ""
    for i in secretList:
        if i  in guess:
            result = result + i
        else:
            result = result + "_"
    return(result)

#Task 10
def pig_latin(str):
    words = str.split()
    
    for i, word in enumerate(words):
        if word[0] in {"a", "e", "i", "o", "u"}:
            words[i] = word + "ay"


        else:
            while word[0] not in {"a", "e", "i", "o", "u"}:
                word = word[1:] + word[0]
            if (word[0]=="u") & (word[-1]=="q"):
                word = word[1:] + word[0]
            words[i] = word + "ay"
            
    newStr = " ".join(words)
    return newStr

