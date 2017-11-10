class AnonymousSurvey():
    """
    Collect anonymous answers to a survey question
    """

    def __init__(self, question):
        """
        Store a question and prepare to store responses
        :param question: str
        """
        self.question = question
        self.responses = []

    def show_question(self):
        """
        Show the survey question
        :return: str
        """
        print(self.question)

    def store_response(self, new_response):
        """
        Store a single response and append it to the list
        :param new_response: str
        :return: None
        """
        self.responses.append(new_response)

    def show_results(self):
        """
        Show all the responses
        :return: strings
        """
        print("Survey results:")
        for response in self.responses:
            print("- " + response)