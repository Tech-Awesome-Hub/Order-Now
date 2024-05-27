from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _


from ..models.product import Product, ProductImage
from ..models.offer import Offer, OfferImage


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    photos = forms.FileField(
        widget=forms.TextInput(attrs={
            "multiple": "True",
            'type':'file',
            'name':'images'
        }),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, product):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            photo = ProductImage(product=product, photo=upload)
            photo.save()


class OfferAdminForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = "__all__"

    photos = forms.FileField(
        widget=forms.TextInput(attrs={
            "multiple": "True",
            'type':'file',
            'name':'images'
        }),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, offer):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            photo = OfferImage(offer=offer, photo=upload)
            photo.save()