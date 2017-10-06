# -*- coding: utf-8 -*-
import re


def get_attribute_list_from_doc(doc):
    """
    根据models的类的__doc__获取其models属性列表
    :type doc: str
    :param doc:
    :return: 
    """
    # print('doc: ' + doc)
    match_obj = re.match(r'\w+\((.+)\)', doc)
    if match_obj:
        attr_list_str = match_obj.group(1)
        attr_list = attr_list_str.split(', ')
        return attr_list
    else:
        return []