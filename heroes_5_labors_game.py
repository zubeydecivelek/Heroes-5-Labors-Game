with open("TaskList.txt", "r") as file:
    task_list = [i.strip("\n").split(",") for i in file.readlines()]

print("Welcome to Hero’s 5 Labors!")

heroHP = 3000
pegasusHP = 550
time = 0
Hall_Of_Fame = []

def remove_task(task_list,index):
    task_list.pop(index)
    game(task_list)


def print_remaining_tasks(task_list):
    if len(task_list)==0:
        print("Congratulations, you have completed the task.")
        name=input("What is your name : ")
        Hall_Of_Fame.append(name)
        print("Hall Of Fame\n-----------------------")
        print("|Name\t| Finish Time |\n-----------------------")
        print(f"| {name}\t| {time} hour\n-----------------------")
        #kişiyi kaydet
        exit()
    else:
        print("Here are the tasks left that hero needs to complete:\n------------------------------------------------------")
        print("| TaskName\t| ByFootDistance\t| ByPegasus\t| HPNeeded\t|\n------------------------------------------------------")
        for i in task_list:
            if i[1]=="-1":
                print(f"| {i[0]}\t\t| {i[1]} km\t\t\t\t| {i[2]} km\t| {i[3]}\t\t|")
            else:
                print(f"| {i[0]}\t\t| {i[1]} km\t\t\t| {i[2]} km\t| {i[3]}\t\t|")
        print("--------------------------------------------------------")

def print_HP(hero,pegasus):
    print("\nRemaining HP for Hero:",hero)
    print("Remaining HP for Pegasus:",pegasus,"\n")


def remainingHP(task_list,travelby,index):
    if travelby=="foot":
        passing_time=int(task_list[index][1])//20
        losthp=passing_time*10
        return passing_time,losthp
    else:
        passing_time=int(task_list[index][2])//50
        losthp=passing_time*15
        return passing_time,losthp


def game(task_list):
    global heroHP,pegasusHP,time, index
    print_HP(heroHP,pegasusHP)
    print_remaining_tasks(task_list)
    while True:
        todo = input("Where should Hero go next? ")
        tasks = [i[0].lower() for i in task_list]
        if todo.lower() in tasks:
            break
        else:
            print("Invalid input")
            continue
    for i in task_list:
        if i[0].lower()==todo.lower():
            indextask = task_list.index(i)
    while True:
        travelby = input("How do you want to travel?(Foot/Pegasus)")
        if travelby.lower()=="foot" and task_list[indextask][1]=="-1":
            print("You cannot go there by foot.")
            continue
        elif travelby.lower()=="foot" and task_list[indextask][1]!="-1":
            passing_time,losthp=remainingHP(task_list,"foot",indextask)
            time += passing_time
            heroHP-=losthp
            heroHP-=int(task_list[indextask][3])
            if heroHP>0:
                print("Hero defeated the monster.")
                print(f"Time passed : {time} hour")
                print_HP(heroHP,pegasusHP)
                break
            else:
                print("Game Over")
                exit()
        elif travelby.lower()=="pegasus" and pegasusHP-int(task_list[indextask][2])//50*15<0:
            print("Pegasus does not have enough HP.")
            continue
        elif travelby.lower()=="pegasus":
            passing_time,losthp=remainingHP(task_list,"pegasus",indextask)
            time += passing_time
            pegasusHP-=losthp
            heroHP-=int(task_list[indextask][3])
            if heroHP>0:
                print("Hero defeated the monster.")
                print(f"Time passed : {time} hour")
                print_HP(heroHP,pegasusHP)
                break
            else:
                print("Game Over")
                exit()
        else:
            print("Invalid input")
            continue
    while True:
        togohome=input("How do you want to go home?(Foot/Pegasus)")
        if togohome.lower()=="foot" and task_list[indextask][1]=="-1":
            print("You cannot go there by foot.")
            continue
        elif togohome.lower()=="foot" and task_list[indextask][1]!="-1":
            passing_time,losthp=remainingHP(task_list,"foot",indextask)
            time += passing_time
            heroHP-=losthp
            if heroHP>0:
                print("Hero arrived home.")
                print(f"Time passed : {time} hour")
                break
            else:
                print("Game Over")
                exit()
        elif togohome.lower()=="pegasus" and pegasusHP-int(task_list[indextask][2])//50*15<0:
            print("Pegasus does not have enough HP.")
            continue
        elif togohome.lower()=="pegasus":
            passing_time,losthp=remainingHP(task_list,"pegasus",indextask)
            time += passing_time
            pegasusHP-=losthp
            print("Hero arrived home.")
            print(f"Time passed : {time} hour")
            break
        else:
            print("Invalid input")
            continue

    remove_task(task_list,indextask)

game(task_list)
