from django.contrib import admin

from wallets.models import Wallet


@admin.register(Wallet)
class FoodgramUserAdmin(admin.ModelAdmin):
    """Админ-зона кошелька."""

    model = Wallet
    list_display = ('id', 'amount', 'created_at', 'updated_at')
