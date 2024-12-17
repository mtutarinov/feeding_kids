from django.conf import settings

from food.models import Ingredient


class Cart:
    """Осуществляет функционал корзины."""
    def __init__(self, request):
        """Инициализация."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = list()
        self.cart = cart

    def add(self, ingredient_id):
        """Добавляет ингредиент в корзину."""
        if ingredient_id not in self.cart:
            self.cart.append(ingredient_id)
        self.save()

    def save(self):
        """Сохраняет сессию."""
        self.session.modified = True

    def remove(self, ingredient_id):
        """Удаляет ингредиент из корзины. """
        self.cart.remove(ingredient_id)
        self.save()


