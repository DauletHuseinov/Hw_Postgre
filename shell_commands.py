from employee.models import *
from django.db.models import Q, Subquery


passport_1 = Passport.objects.create(employee=Employee.objects.create(name='Husein', birth_date='2002-02-23', position='Senior', salary=70000, work_experience=2), inn='24546466565577', id_card=2367857)
passport_2 = Passport.objects.create(employee=Employee.objects.create(name='Daulet', birth_date='2006-02-27', position='Manager', salary=20000, work_experience=4), inn='23483048845445', id_card=2323557)
passport_3 = Passport.objects.create(employee=Employee.objects.create(name='Ha1sse', birth_date='2006-07-11', position='Director', salary=500000, work_experience=7), inn='23483048845445', id_card=2324557)
passport_4 = Passport.objects.create(employee=Employee.objects.create(name='Ikk', birth_date='1990-12-12', position='Junior', salary=1000, work_experience=1), inn='26673048845445', id_card=2356557)
#

work_project_1 = WorkProject.objects.create(project_name='Codify CRM')
work_project_2 = WorkProject.objects.create(project_name='2GIS')
work_project_3 = WorkProject.objects.create(project_name='Yandex')
work_project_4 = WorkProject.objects.create(project_name='Google')

membership_1 = Membership.objects.create(employee=passport_1, work_project=work_project_1)
membership_2 = Membership.objects.create(employee=passport_2, work_project=work_project_2)
membership_3 = Membership.objects.create(employee=passport_3, work_project=work_project_3)
membership_4 = Membership.objects.create(employee=passport_4, work_project=work_project_4)
#  Не смог выполнить задание с Shell
# client_1 = Client.objects.create(name='buster', birth_date='2000-01-01', address='Исанова', phone_number=343355335)
# client_2 = Client.objects.create(name='Mihail', birth_date='2002-11-16', address='7 Микрорайон', phone_number=3436455335)
# client_3 = Client.objects.create(name='Иллл', birth_date='2000-01-01', address='Аламудин', phone_number=36555335)
#
# vip_client = VIPClient.objects.create(name='VIP', birth_date='1990-12-12', address='Бишкек', phone_number=535654477, vip_status_start='2002-03-23', donation_amount=4000)