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
from .models.orders import Order, OrderItem
from .models.vendors import Vendor
from .models.filters import Filter, FilterUpdate
from .models.cart import CartItem
from .models.shipping_loc import ShippingLocations

class ProductPhotoInline(admin.TabularInline):
    model = ProductImage
    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
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
    fields = ("showphoto_thumbnail",)
    readonly_fields = ("showphoto_thumbnail",)
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
       
class ShippingLocationsAdmin(admin.ModelAdmin):
    list_display = ['customer', 'full_name',]
    search_fields = ['name']

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    fields = ['order']
    readonly_fields = ['order',]
    extra = 0
    max_num = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    model = Order
    inlines = [ OrderItemInline, ]

    readonly_fieldsets = (
        (None, {
            'fields': ('customer','status','order','date')
        }),
    )
    readonly_fields = ['customer','status'] 
    # ,'payment_option'

    search_fields = ['customer__name', 'customer__email']
    list_filter = ['status', ]

    list_display = ['pk','customer','status','date','product']
    ordering = ('-date',)
    list_editable = ["status"]


# admin.site.register(Order, OrderAdmin)

# Register your models here.
admin.site.register(SubCategory, Sub_CategoryAdmin)
admin.site.register(Filter, FiltersAdmin)
admin.site.register(ShippingLocations, ShippingLocationsAdmin)
admin.site.register(FilterUpdate)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Vendor)
admin.site.register(ProductType)

