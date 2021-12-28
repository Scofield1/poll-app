from django.db import models


class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Option(models.Model):
    select_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option



