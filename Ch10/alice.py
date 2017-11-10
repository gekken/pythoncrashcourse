filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file '{}' does not exist".format(filename)
    print(msg)
else:
    # Count the number of approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file '{}' has about {} words. ".format(filename, num_words))