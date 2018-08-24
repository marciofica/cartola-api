from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from .models import Clube, Time


class TestClube(TestCase):

    def setUp(self):
        self.clube = mommy.make(Clube, nome='Teste Clube')

    def test_record_creation(self):
        self.assertTrue(isinstance(self.clube, Clube))
        self.assertEquals(self.clube.__str__(), self.clube.nome)


class TestTime(TestCase):

    def setUp(self):
        self.clube = mommy.make(Clube, nome='Teste Clube')
        self.time = mommy.make(Time, nome='Teste Time', clube=self.clube)

    def test_record_creation(self):
        self.assertTrue(isinstance(self.time, Time))
        self.assertEquals(self.time.__str__(), self.time.nome)