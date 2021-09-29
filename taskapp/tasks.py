from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .models import *
import datetime
from django.core.mail import EmailMessage

@periodic_task(run_every=crontab(hour='23',minute='57', day_of_week="*"))
def streakupdate():
    obj = User.objects.all()
    for user in obj:
        tas = tasks.objects.filter(user=user,date=datetime.date.today(),check=True)
        if tas:
            st,create = streak.objects.get_or_create(user=user,defaults={'count': 0})
            if create:
                st.count = 1
            else:
                st.count = st.count + 1
            st.save()

@periodic_task(run_every=crontab(hour='00',minute='01', day_of_week="*"))
def dailytaskadd():
    obj = User.objects.all()
    for user in obj:
        tas = tasks.objects.filter(user=user,types='Daily')
        for ta in tas:
            tasks.objects.create(date=datetime.date.today(),user=user,types='Daily',title=ta.title,desc=ta.desc)

@periodic_task(run_every=crontab(hour='00',minute='01', day_of_week="*"))
def sendreminder():
    obj = User.objects.all()
    for user in obj:
        tas = tasks.objects.filter(user=user,types='Daily',check=False)
        for ta in tas:
            ob = ta.user
            to_email = ob.email
            subject = "Complete "+str(ta.title)+" ASAP!"
            mess = "Hello "+str(ob.username)+"\n"+"Complete task "+str(ta.title)+"\n"+"Description: "+str(ta.desc)+"\n"+"If you have already done this task, then check it on our site!"
            email = EmailMessage(subject,mess, to=[to_email])
            email.send()