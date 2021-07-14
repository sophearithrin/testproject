from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

sdafsdfsdf
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Fruit(models.Model):
    fruit_name = models.ForeignKey(Question, on_delete=models.CASCADE)
    sweetness_level = models.CharField(max_length=200)


class Car(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
    fruit_id = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    car_brand = models.CharField(max_length=200)


class Lambo(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
    fruit_id = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_brand = models.CharField(max_length=200)
