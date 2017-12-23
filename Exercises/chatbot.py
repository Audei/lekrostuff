def chatbot(x):
    #initiation + assignment of variables
    newWord = False
    defWord = ''
    run = True
    conversation = []
    memory = {'hi': 'Hello!','hello': 'Hey', 'bye': 'Goodbye!'}
    #input
    while run:
        human = input('')
        humanIn = human.lower()
        #record in list
        conversation.append('Human: ' + human)   
        
        #if statements
        if humanIn in memory:
            botTemp = ('Bot: ' + memory[humanIn])
        else:
            defWord = humanIn
            botTemp = ('Bot: What does that mean?')
            print(botTemp)
            memory[defWord] = input('')
            conversation.append(botTemp + '\n' + 'Human: ' + memory[defWord])
            botTemp = ('Bot: Okay, I got it. ' + defWord + ' is ' + memory[defWord])
        #print bot response
        print(botTemp)
        #record in list
        conversation.append(botTemp)
        
        if botTemp == 'Bot: Goodbye!':
            run = False
            
    #writing up file
    with open('convoLog', 'w') as f:
        for foo in conversation:
            f.write(foo + '\n')
