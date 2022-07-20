""" Signals for authors app """

from django.contrib.auth.models import User
from djoser.signals import user_registered  # Importing Djoser signal
# from django.db.models.signals import post_save  # Importing django signal
from django.dispatch import receiver

from .models import Profile


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