""" Models for authors app """

from django.contrib.auth.models import User
from django.db import models
from djoser.signals import user_registered  # Importing Djoser signal
# from django.db.models.signals import post_save  # Importing django signal
from django.dispatch import receiver


def upload_to(instance, filename):
    return f'users/avatars/{filename}'


class Profile(models.Model):
    """ Profile model """
    user = models.OneToOneField(User, verbose_name='Автор', on_delete=models.CASCADE, primary_key=True)
    bday = models.DateField(verbose_name='Дата рождения')
    avatar = models.ImageField(verbose_name='Превью', upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        """ String representation for profile model """
        return f'{self.user.username} profile <{self.user.first_name} {self.user.last_name} ({self.bday})>'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('pk',)


# using a decorator, we will describe a trigger for creating a user profile after creating the user itself
@receiver(user_registered, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(user_registered, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# in database (postgresql) it should look like:
# -------------------------------------------------------------
# create or replace function create_profile_on_user_insert()
# returns trigger as $$
# begin
    # insert into public.authors_profile(user_id, bday, avatar)
    # values(new.id, null, null);
    # return new;
# end;
# $$ language 'plpgsql' volatile
# cost 100;
#
# create trigger create_profile_on_user_insert_trigger
# after insert on public.auth_user
# for each row
# execute procedure create_profile_on_user_insert();
