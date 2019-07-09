# coding: utf-8

from django.http import HttpResponse
from kg_demo.models import Course, Concept, Relation, LessonConcept
from kg_demo.common import *

def add_course(course_name, duration=0, teacher=''):
    courses = Course.objects.filter(name=course_name, duration=duration, teacher=teacher)
    if not courses:
        course = Course(name=course_name, duration=duration, teacher=teacher)
        course.save()

def add_concept(concept_name, course, concept_detail):
    concepts = Concept.objects.filter(course=course, concept_name=concept_name)
    if concepts:
        concept = concepts[0]
        concept.detail = concept_detail
    else:
        concept = Concept(name=concept_name, course=course, detail=concept_detail)
    concept.save()

def add_relation(concept1, concept2, detail=''):
    relations = Relation.objects.filter(concept1=concept1, concept2=concept2, detail=detail)
    if relations:
        relation = relations[0]
        relation.detail = detail
    else:
        relation = Relation(concept1=concept1, concept2=concept2, detail=detail)
    relation.save()

def add_lesson_concept(concept, lesson_idx, importance=-1):
    record = LessonConcept(concept=concept, lesson_idx=lesson_idx)
    if record:
        record.importance = importance
    else:
        record = LessonConcept(concept=concept, lesson_idx=lesson_idx, importance=importance)
    record.save()

def find_concept(concept_name=None, course=None):
    if concept_name is None and course is None:
        raise ValueError("Concept name or course must be given in find_concept")
    if not isinstance(course, Course):
        assert isinstance(course, str)
        courses = Course.objects.filter(name=course)
        if not course:
            raise ValueError("Course name not exist")
        course = courses[0]
    restrictions = {'course': course}
    if concept_name:
        restrictions['name'] = concept_name
    concepts = Concept.objects.filter(**restrictions)
    if len(concepts) > 1:
        raise ValueError("Multiple concept found in find_concept")
    return concepts[0]

def find_concept_appearance(course, lesson_idx=-1):
    if isinstance(course, str):
        courses = Course.objects.filter(name=course)
        if len(courses) > 1:
            course = courses[0]
        else:
            raise ValueError("Multiple couse record found in find_concept_appearance")
    appearances = LessonConcept.objects.filter(concept__course=course)
    return appearances

def get_concept_relations(concept_list):
    relations = []
    n_concepts = len(concept_list)
    for i in range(0, n_concepts):
        for j in range(i+1, n_concepts):
            relations += Relation.objects.filter(concept1=concept_list[i], concept2=concept_list[j])
            relations += Relation.objects.filter(concept1=concept_list[j], concept2=concept_list[i])
    return relations
