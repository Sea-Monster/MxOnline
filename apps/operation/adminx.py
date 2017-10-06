# -*- coding: utf-8 -*-
import xadmin
from utils.common import get_attribute_list_from_doc
from .models import UserAsk, UserCourse, UserMessage, CourseComments, UserFavorite


class UserAskAdmin(object):
    list_display = get_attribute_list_from_doc(UserAsk.__doc__)
    search_fields = get_attribute_list_from_doc(UserAsk.__doc__)
    list_filter = get_attribute_list_from_doc(UserAsk.__doc__)


class UserCourseAdmin(object):
    list_display = get_attribute_list_from_doc(UserCourse.__doc__)
    search_fields = get_attribute_list_from_doc(UserCourse.__doc__)
    list_filter = get_attribute_list_from_doc(UserCourse.__doc__)


class UserMessageAdmin(object):
    list_display = get_attribute_list_from_doc(UserMessage.__doc__)
    search_fields = get_attribute_list_from_doc(UserMessage.__doc__)
    list_filter = get_attribute_list_from_doc(UserMessage.__doc__)


class CourseCommentsAdmin(object):
    list_display = get_attribute_list_from_doc(CourseComments.__doc__)
    search_fields = get_attribute_list_from_doc(CourseComments.__doc__)
    list_filter = get_attribute_list_from_doc(CourseComments.__doc__)


class UserFavoriteAdmin(object):
    list_display = get_attribute_list_from_doc(UserFavorite.__doc__)
    search_fields = get_attribute_list_from_doc(UserFavorite.__doc__)
    list_filter = get_attribute_list_from_doc(UserFavorite.__doc__)


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)