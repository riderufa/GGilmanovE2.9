from django.db import models
from django.core.mail import send_mail
from datetime import timedelta, datetime, timezone
import time, threading

# Create your models here.
class Mail(models.Model):
    subject = models.CharField(max_length=50)
    text = models.TextField()
    email = models.EmailField()
    second = models.SmallIntegerField()
    publish = models.DateTimeField(auto_now_add=True)

    @property
    def published(self):
        return self.publish + timedelta(seconds=self.second)

    @property
    def send(self):
        return self.published < datetime.now(timezone.utc)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        def send_mail_sleep(subject, text, email, second):
            time.sleep(second)
            send_mail(subject, text, '3434455@mail.ru', [email], fail_silently=False)

        t = threading.Thread(target=send_mail_sleep, args=(self.subject, self.text, self.email, self.second))
        # threads.append(t)
        t.start()
