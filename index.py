def start():
    content = {}

    def askAndReturnSearchTerm():
        return 'oi'
    
    content["searchTerm"] = askAndReturnSearchTerm()

    print(content)

start()
