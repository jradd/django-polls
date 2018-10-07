from django.contrib.admin import AdminSite


class MyAdmin(AdminSite):
  site_header = 'myadmin'
  site_title  = 'myAdmin'


admin_site = MyAdmin(name='admin')
