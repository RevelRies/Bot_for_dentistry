from Bot_for_dentistry.DentistryWebsite.hello.models import Person

def get_all_users():
    qs_users = Person.objects.all()
    users = [(user.id, f'Имя: {user.name}, Возраст: {user.age}') for user in qs_users]
    dt = {}
    return dt.update(*users)