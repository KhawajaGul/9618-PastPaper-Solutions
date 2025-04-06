'                                               APPENDING TO A FILE'
'TO add to the end of an existing file'

# file = open('file2', 'a')
# file.write("Appending will not result in overwriting")
# file.close()


'APPEND WILL ALSO CREATE NON EXISTANT FILES'
file = open('Fizza.txt', 'a')
file.write("APpending will create a new file as well")
file.close()