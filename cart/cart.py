from django.conf import settings

from main_app.models import Ingredient


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = list()
        self.cart = cart

    def add(self, ingredient_id):
        if ingredient_id not in self.cart:
            self.cart.append(ingredient_id)
        self.save()

    def save(self):
        self.session.modified = True

    # def remove(self, painting):
    #     painting_id = str(painting.id)
    #     if painting_id in self.cart:
    #         del self.cart[painting_id]
    #         self.save()
    #
    # def __iter__(self):
    #     painting_ids = self.cart.keys()
    #     paintings = Painting.objects.filter(id__in=painting_ids)
    #     cart = self.cart.copy()
    #     for painting in paintings:
    #         cart[str(painting.id)]['painting'] = painting
    #     for item in cart.values():
    #         item['price'] = int(item['price'])
    #         yield itemя
