def auCommand(args, graph):
    if len(args) != 2:
        print('Missing argument')
    elif args[1] in graph.keys():
        print('This user already exists!')
    else:
        graph[args[1]] = []
        print("User", args[1], "added successfully")


def ruCommand(args, graph):
    if len(args) != 2:
        print('Missing argument')
    elif args[1] not in graph.keys():
        print('There is no user named', args[1])
    else:
        friendsList = graph[args[1]]  # friendsList of the user who we want to remove
        for friend in friendsList:
            graph[friend].pop(graph[friend].index(args[1]))

        del graph[args[1]]
        print(" User", args[1] ,"and its all relations have been removed successfully.")

def arCommand(args, graph):
    if len(args) != 3:
        print("Missing argument")
    elif args[1] not in graph.keys() or args[2] not in graph.keys():
        print("No user named", args[1], "or", args[2], "found!")
    elif args[2] in graph[args[1]]:
        print("A relation between", args[0], "and", args[1] ,"already exists!")
    else:
        graph[args[1]].append(args[2])
        graph[args[2]].append(args[1])
        print("A relation between", args[0], "and", args[1] ,"has been added successfully.")


def rrCommand(args, graph):
    if len(args) != 3:
        print('Missing argument')
    elif args[1] not in graph.keys() or args[2] not in graph.keys():
        print("No user named", args[0], "or", args[1] ,"found!")
    elif args[2] not in graph[args[1]]:
        print("No relation between", args[0], "and", args[1] ,"found!")
    else:
        arg1 = args[1]
        arg2 = args[2]
        graph[arg1].pop(graph[arg1].index(arg2))
        graph[arg2].pop(graph[arg2].index(arg1))
        print('A relation between', arg1, 'and', arg2, 'has been removed successfully.')


def paCommand(args, graph):
    if len(args) != 2:
        print('Missing argument')
    elif len(graph.keys()) < int(args[1]):
        print('Invalid input since n is greater than', len(graph.keys()))
    else:
        for aUser in graph.keys():
            print("User", aUser, "has", len(graph[aUser]))
        orderedKeys = (sorted(graph, key=lambda k: len(graph[k]), reverse=True))
        for i in range(int(args[1])):
            print(i + 1, orderedKeys[i], len(graph[orderedKeys[i]]))


def saCommand(args, graph):
    if len(args) != 3:
        print("Missing argument")
    elif args[1] not in graph.keys():
        print("No user named", args[1] ,"found!")
    elif len(graph[args[1]]) < int(args[2]):
        print("User",args[1] ,"has friends less than", int(args[2]))
    else:
        print("----")


def main():
    graph = {}
    with open('commandsP1.txt') as commandsP1:
        for line in commandsP1:
            args = line.split()
            if args[0] == "AU":
                auCommand(args, graph)
            elif args[0] == "RU":
                ruCommand(args, graph)
            elif args[0] == "AR":
                arCommand(args, graph)
            elif args[0] == "RR":
                rrCommand(args, graph)
            elif args[0] == "PA":
                paCommand(args, graph)
            elif args[0] == "SA":
                saCommand(args, graph)
            else:
                print("")


main()
