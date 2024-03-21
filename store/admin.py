from django.contrib import admin
from django.utils.html import mark_safe
from django.template.loader import get_template
from django.utils.translation import gettext as _

from .models.product import Product, ProductImage
from .models.offer import Offer, OfferImage
from .forms.image_form import ProductAdminForm, OfferAdminForm
from .models.category import Category
from .models.sub_category import SubCategory
from .models.product_type import ProductType
from .models.customer import Customer
from .models.orders import Order
from .models.vendors import Vendor
from .models.filters import Filter

class ProductPhotoInline(admin.TabularInline):
    model = ProductImage
    # fields = ("showphoto_thumbnail",)
    # readonly_fields = ("showphoto_thumbnail",)
    max_num = 0

    def showphoto_thumbnail(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("store/admin/show_thumbnail.html")
        return tpl.render({"photo": instance.photo})

    showphoto_thumbnail.short_description = _("Thumbnail")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)

class OfferPhotoInline(admin.TabularInline):
    model = OfferImage
    # fields = ("showphoto_thumbnail",)
    # readonly_fields = ("showphoto_thumbnail",)
    max_num = 0

    def showphoto_thumbnail(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("store/admin/show_thumbnail.html")
        return tpl.render({"photo": instance.photo})

    showphoto_thumbnail.short_description = _("Thumbnail")


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    form = OfferAdminForm
    inlines = [OfferPhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


class FiltersAdmin(admin.ModelAdmin):
    list_display = ['name']

class AdminProduct(admin.ModelAdmin):
    # search_fields = ['name', 'category']
    list_display = ['name', 'price', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class OrderItemInline(admin.StackedInline):
    model = 'OrderItem'
    fields = ['product']
    readonly_fields = ['product',]
    extra = 0
    max_num = 0

class OrderAdmin(admin.ModelAdmin):

    list_display = ['pk', 'user', 'status', 'created', 'list_products']

    def list_products(self, obj):
        # each obj will be an Order obj/instance/row
        to_return = '<ul>'
        # I'm assuming that there is a name field under the event.Product model. If not change accordingly.
        to_return += '\n'.join('<li>{}</li>'.format(prod_name) for prod_name in obj.items.values_list('product__name', flat=True))
        to_return += '</ul>'
        return mark_safe(to_return)

class OrderAdmin(admin.ModelAdmin):

    model = Order
    inlines = [ OrderItemInline, ]

    readonly_fieldsets = (
        (None, {
            'fields': ('user','status','order','created')
        }),
    )
    readonly_fields = ['user','status','payment_option']

    search_fields = ['user__name', 'user__email']
    list_filter = ['status', ]

    list_display = ['pk','user','status','created','product']
    ordering = ('-created',)


# admin.site.register(Order, OrderAdmin)

# Register your models here.
admin.site.register(SubCategory, Sub_CategoryAdmin)
admin.site.register(Filter, FiltersAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Vendor)
admin.site.register(ProductType)

