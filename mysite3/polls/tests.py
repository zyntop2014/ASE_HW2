from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone
#from django.test import TestCase

from .models import Question

from django.test import TestCase



class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
	    """
	    was_published_recently() should return False for questions whose
	    pub_date is older than 1 day.
	    """
	    time = timezone.now() - datetime.timedelta(days=30)
	    old_question = Question(pub_date=time)
	    self.assertIs(old_question.was_published_recently(), False)

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="which class is the most difficult", pub_date = timezone.now())
	
        
    def test_question_name(self):
        """Animals that can speak are correctly identified"""
        q = Question.objects.get(question_text= "which class is the most difficult")
	
        self.assertEqual(q.question_text ,  "which class is the most difficult")

    def create_question(self, title="only a test", pub_date = timezone.now()):
        return Question.objects.create(question_text= "which class is the most difficult", pub_date=pub_date)

    def test_whatever_creation(self):
        w = self.create_question()
        self.assertTrue(isinstance(w, Question))
        

        

        
