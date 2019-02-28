import inquirer

def start():
    content = {}
    choices = ['Who is', 'What is', 'The history of']
    
    def askAndReturnSearchTermAndPrefix():
        questions = [
            inquirer.Text('searchTerm', message="Type your search term"),
            inquirer.List('prefix',
                  message="Choose one option",
                  choices=choices,
              ),
            ]
        return inquirer.prompt(questions)
    
    content = askAndReturnSearchTermAndPrefix()


    print(content)


start()
