# -*- coding: utf-8 -*-
import xadmin
from .models import Course, Lesson, Video, CourseResource
from utils.common import get_attribute_list_from_doc


class CourseAdmin(object):
    list_display = get_attribute_list_from_doc(Course.__doc__)
    search_fields = get_attribute_list_from_doc(Course.__doc__)
    list_filter = get_attribute_list_from_doc(Course.__doc__)


class LessonAdmin(object):
    list_display = get_attribute_list_from_doc(Lesson.__doc__)
    search_fields = get_attribute_list_from_doc(Lesson.__doc__)
    list_filter = get_attribute_list_from_doc(Lesson.__doc__)


class VideoAdmin(object):
    list_display = get_attribute_list_from_doc(Video.__doc__)
    search_fields = get_attribute_list_from_doc(Video.__doc__)
    list_filter = get_attribute_list_from_doc(Video.__doc__)


class CourseResourceAdmin(object):
    list_display = get_attribute_list_from_doc(CourseResource.__doc__)
    search_fields = get_attribute_list_from_doc(CourseResource.__doc__)
    list_filter = get_attribute_list_from_doc(CourseResource.__doc__)


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)