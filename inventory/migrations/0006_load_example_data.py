# Generated by Django 4.1 on 2022-09-26 17:01

from django.db import migrations
from django.contrib.auth.management import create_permissions

def upload_example_data(apps, schema_editor):
    # Ensure permissions have been created
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None

    # Get model classes

    User = apps.get_model('auth', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    Building = apps.get_model('inventory', 'Building')
    Spot = apps.get_model('inventory', 'Spot')
    ArtItem = apps.get_model('inventory', 'ArtItem')
    ArtLocation = apps.get_model('inventory', 'ArtLocation')
    ArtBorrowingRequest = apps.get_model('inventory', 'ArtBorrowingRequest')


    # Users

    admin = User.objects.create_superuser('admin', 'admin@amsterdam.nl', 'admin!12345')
    admin.save()

    janneke = User.objects.create_user('janneke', 'janneke@amsterdam.nl', 'janneke!12345', first_name='Janneke', last_name='de Jong')
    janneke.save()

    jeroen = User.objects.create_user('jeroen', 'jeroen@amsterdam.nl', 'jeroen!12345', first_name='Jeroen', last_name='Jansen')
    jeroen.save()

    sjoerd = User.objects.create_user('sjoerd', 'sjoerd@amsterdam.nl', 'sjoerd!12345', first_name='Sjoerd', last_name='de Vries')
    sjoerd.save()

    # Groups

    municipality_workers = Group.objects.create(name='municipality_workers')
    municipality_workers.user_set.add(janneke)
    municipality_workers.user_set.add(jeroen)
    municipality_workers_permissions = Permission.objects.filter(codename__in=[
        'view_building', 'view_spot', 'view_artitem', 'view_artlocation', 'view_artborrowingrequest', 'add_artborrowingrequest'])
    municipality_workers.permissions.set(municipality_workers_permissions)
    municipality_workers.save()

    art_managers = Group.objects.create(name='art_managers')
    art_managers.user_set.add(sjoerd)
    art_managers_permissions = Permission.objects.filter(codename__in=[
        'view_building', 'add_building', 'change_building', 'delete_building',
        'view_spot', 'add_spot', 'change_spot', 'delete_spot',
        'view_artitem', 'add_artitem', 'change_artitem', 'delete_artitem',
        'view_artlocation', 'add_artlocation', 'change_artlocation', 'delete_artlocation',
        'view_artborrowingrequest', 'delete_artborrowingrequest'])
    art_managers.permissions.set(art_managers_permissions)
    art_managers.save()

    # Buildings and related spots

    pompwater = Building.objects.create(address='Pompwater 100, 1025JS, Amsterdam')
    pompwater.save()
    pompwater_spot1 = Spot.objects.create(building=pompwater, room='P23', floor=0, details='Spatious room')
    pompwater_spot1.save()
    pompwater_spot2 = Spot.objects.create(building=pompwater, room='P102', floor=1, details='Open spaces')
    pompwater_spot2.save()

    utrechtweg = Building.objects.create(address='Utrechtweg 34, 1045XC, Amsterdam')
    utrechtweg.save()
    utrechtweg_spot1 = Spot.objects.create(building=utrechtweg, room='U43', floor=5, details='Canteen')
    utrechtweg_spot1.save()
    
    bomen = Building.objects.create(address='Bomen 13, 1015AB, Amsterdam')
    bomen.save()
    bomen_spot1 = Spot.objects.create(building=bomen, room='B01', floor=0)
    bomen_spot1.save()
    bomen_spot2 = Spot.objects.create(building=bomen, room='B02', floor=0)
    bomen_spot2.save()
    bomen_spot3 = Spot.objects.create(building=bomen, room='B03', floor=0)
    bomen_spot3.save()

    # Art items

    import datetime

    night_watch = ArtItem.objects.create(name="The Night Watch", author="Rembrandt van Rijn", creation_date=datetime.date(1642, 1, 1), photo="the_nightwatch_by_rembrandt.webp")
    night_watch.save()
    milkmaid = ArtItem.objects.create(name="The Milkmaid", author="Johannes Vermeer", creation_date=datetime.date(1660, 1, 1), photo="vermeer_-_the_milkmaid.webp")
    milkmaid.save()
    van_gogh= ArtItem.objects.create(name="Self-Portrait", author="Vincent Van Gogh", creation_date=datetime.date(1887, 1, 1), photo="van_gogh.webp")
    van_gogh.save()
    worship = ArtItem.objects.create(name="Worship of the Golden Calf", author="Lucas van Leyden", creation_date=datetime.date(1530, 1, 1), photo="lucas_van_leyden.webp")
    worship.save()
    rembrandt = ArtItem.objects.create(name="Self-Portrait", author="Rembrandt van Rijn", creation_date=datetime.date(1659, 1, 1), photo="Rembrandt_van_Rijn_-_Self-Portrait.jpeg")
    rembrandt.save()

    # Art locations and borrowing request

    rembrandt_request_by_janneke = ArtBorrowingRequest.objects.create(art_item=rembrandt, spot=bomen_spot3, start_date=datetime.date(2021, 2, 10), requester=janneke, request_text='I would love to have this painting in my office at Bomen')
    rembrandt_request_by_janneke.save()

    worship_request_by_jeroen = ArtBorrowingRequest.objects.create(art_item=worship, spot=utrechtweg_spot1, start_date=datetime.date(2020, 1, 1), end_date=datetime.date(2030, 1, 1), requester=jeroen, request_text='Hey Sjoerd, could I have this one for 10 years?')
    worship_request_by_jeroen.save()

    worship_at_utrechtweg = ArtLocation(art_item=worship, spot=utrechtweg_spot1, start_date=datetime.date(2020, 1, 1), end_date=datetime.date(2025, 1, 1), responsible_person=jeroen, request=worship_request_by_jeroen)
    worship_at_utrechtweg.save()


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_rename_reqester_artborrowingrequest_requester'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(upload_example_data),
    ]
