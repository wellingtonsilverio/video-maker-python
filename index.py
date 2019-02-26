def start():
    content = {}

    def askAndReturnSearchTerm():
        return input('Type your search term : ') 
    content["searchTerm"] = askAndReturnSearchTerm()


    def askAndReturnSearchTerm():
        prefixes = ('Who i', 'Who are', 'Who')
        for i in range(len(prefixes)):
            print( prefixes[i-1] )
        selectPrefix = int(input('Choose your search: '))
        return prefixes[selectPrefix]
    content["selectedPrefixText"] = askAndReturnSearchTerm()
    print(content)


start()
