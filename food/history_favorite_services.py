class ActionManager:

    @staticmethod
    def get(model, user):
        return model.objects.filter(user=user).distinct('user', 'dish')

    @staticmethod
    def add(model, user, dish_id):
        model.objects.create(user=user, dish_id=dish_id)

    @staticmethod
    def delete(model, user, dish_id):
        model.objects.filter(user=user, dish_id=dish_id).delete()




