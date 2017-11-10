
def count_words(filename):
    """
    function to count words in the file provided
    :param filename: expects txt file
    :return: str - word count
    """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file '{}' does not exist".format(filename)
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file '{}' has about {} words. ".format(filename, num_words))


filename = 'alice.txt'
count_words(filename)