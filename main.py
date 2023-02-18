

from pyswip import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer




def main():
    chatbot = ChatBot("Chatpot")
    print("Welcome to WSSU Hackathon 2023")
    print("This is a demonstration of prolog knowlegebase and chatbot")
    print("Studies have shown that not all students are aware of the resources available to them")

    # Get a response from the chatbot based on user input
    user_input = str(input("  What is your name? "))
    print(chatbot.get_response(user_input))
    name = user_input
    fellow_majors = str(input ("What is your major? I want to tell you about other fellow majors "))




    pro = Prolog()

    assertz = Functor("assertz")
    major = Functor("major", 2)
    interest = Functor("interest", 2)

    year = Functor("year", 2)

    test1 = newModule("test1")
    interestrelation = Functor("interestrelation", 2)
    call(assertz(interestrelation("gis","ds")), module=test1)
    call(assertz(interestrelation("swENG","security")), module=test1)
    call(assertz(interestrelation("security","ds")), module=test1)


    call(assertz(major("aaron","cs")), module=test1)
    call(assertz(year("aaron","grad")), module=test1)
    call(assertz(interest("aaron","gis")), module=test1)



    call(assertz(major("melinda","it")), module=test1)
    call(assertz(year("melinda","ug")), module=test1)
    call(assertz(interest("melinda","ds")), module=test1)


    call(assertz(major("tionna","cs")), module=test1)
    call(assertz(year("tionna","ug")), module=test1)
    call(assertz(interest("tionna","security")), module=test1)


    call(assertz(major("clavine","cs")), module=test1)
    call(assertz(year("clavine","ug")), module=test1)
    call(assertz(interest("clavine","unknown")), module=test1)

    call(assertz(major("lloyd","it")), module=test1)
    call(assertz(year("lloyd","ug")), module=test1)
    call(assertz(interest("lloyd","game dev")), module=test1)

    call(assertz(major("virgil","it")), module=test1)
    call(assertz(year("virgil","ug")), module=test1)
    call(assertz(interest("virgil","security")), module=test1)

    call(assertz(major("jordan","it")), module=test1)
    call(assertz(year("jordan","ug")), module=test1)
    call(assertz(interest("jordan","ds")), module=test1)

    call(assertz(major("tahron","cs")), module=test1)
    call(assertz(year("tahron","ug")), module=test1)
    call(assertz(interest("tahron","swENG")), module=test1)

    call(assertz(major("camden","cs")), module=test1)
    call(assertz(year("camden","ug")), module=test1)
    call(assertz(interest("camden","security")), module=test1)

    call(assertz(major("quentin","it")), module=test1)
    call(assertz(year("quentin","ug")), module=test1)
    call(assertz(interest("quentin","security")), module=test1)

    call(assertz(major("kai","it")), module=test1)
    call(assertz(year("kai","ug")), module=test1)
    call(assertz(interest("kai","security")), module=test1)



    print("Querying major(X,Y) for {name}...".format(name=name))
    X= Variable()
    newquery = Query(major(name,X), module=test1)
    while newquery.nextSolution():
        print(X.value)
    newquery.closeQuery()

    print("Querying all the majors of {fellow_majors}...".format(fellow_majors=fellow_majors))
    Y= Variable()
    query = Query(major(Y,fellow_majors), module=test1)
    while query.nextSolution():
        print(Y.value)
    newquery.closeQuery()


    #------------
    pro.consult('nationwide.pl')
    results = list(pro.query("interestrelation(X,Y)"))

    print("Querying interestrelation(X,Y)...")
    for result in results:
        print(result["X"] , result["Y"])
if __name__ == "__main__":
    main()
