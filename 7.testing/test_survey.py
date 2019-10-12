import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Fuzhounese', 'Chinese', 'English']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response('Fuzhouness')
        self.assertIn('Fuzhouness', self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        self.assertIn('English', self.my_survey.responses)
    
if __name__ == '__main__':
    unittest.main()