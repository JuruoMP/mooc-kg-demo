# coding: utf-8

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=32)
    duration = models.IntegerField()
    teacher = models.CharField(max_length=32)

class Concept(models.Model):
    name = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    detail = models.CharField(max_length=256)

class Relation(models.Model):
    concept1 = models.ForeignKey(Concept, on_delete=models.CASCADE)
    concept2 = models.ForeignKey(Concept, on_delete=models.CASCADE)
    detail = models.CharField(max_length=64)

class LessonConcept(models.Model):
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    lesson_idx = models.IntegerField()
    importance = models.IntegerField()
