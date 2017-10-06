# -*- coding: utf-8 -*-
import xadmin
from  .models import EmailVerifyRecord, Banner
from utils.common import get_attribute_list_from_doc


class EmailVerifyRecordAdmin1(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    get_attribute_list_from_doc(EmailVerifyRecord.__doc__)

    # 查询条件（被搜索的字段）
    search_fields = get_attribute_list_from_doc(EmailVerifyRecord.__doc__)
    # 过滤条件
    list_filter = get_attribute_list_from_doc(EmailVerifyRecord.__doc__)


class BannerAdmin(object):
    list_display = get_attribute_list_from_doc(Banner.__doc__)
    search_fields = get_attribute_list_from_doc(Banner.__doc__)
    list_filter = get_attribute_list_from_doc(Banner.__doc__)

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin1)
xadmin.site.register(Banner, BannerAdmin)