# -*- coding: utf-8 -*-
import xadmin
from .models import CityDict, CourseOrg, Teacher
from utils.common import get_attribute_list_from_doc


class CityDictAdmin(object):
    list_display = get_attribute_list_from_doc(CityDict.__doc__)
    search_fields = get_attribute_list_from_doc(CityDict.__doc__)
    list_filter = get_attribute_list_from_doc(CityDict.__doc__)


class CourseOrgAdmin(object):
    list_display = get_attribute_list_from_doc(CourseOrg.__doc__)
    search_fields = get_attribute_list_from_doc(CourseOrg.__doc__)
    list_filter = get_attribute_list_from_doc(CourseOrg.__doc__)


class TeacherAdmin(object):
    list_display = get_attribute_list_from_doc(Teacher.__doc__)
    search_fields = get_attribute_list_from_doc(Teacher.__doc__)
    list_filter = get_attribute_list_from_doc(Teacher.__doc__)


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)