def start():
    content = {}

    def askAndReturnSearchTerm():
        return input('Type your search term : ') 
    
    content["searchTerm"] = askAndReturnSearchTerm()

    print(content)


start()
