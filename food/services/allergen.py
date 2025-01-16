from children.models import Child


def check_user_children(user, child_id):
    children = user.children.all()
    child = Child.objects.get(id=child_id)
    if child in children:
        return True
    return False
