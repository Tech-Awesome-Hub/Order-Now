from django.db import models
from .vendors import Vendor

class Offer(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60, default='some text..')
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,default=1 )
    show = models.BooleanField(default=False)
   
    @property
    def image_url(self):
        try:
            result = []
            photos = self.photos.all()
            if len(photos) > 0 :
                for photo in photos:
                    result.append(photo.photo)
        except:
            result = []
        return result
    
    @property
    def image(self):
        return self.image_url[0]
    
    @staticmethod
    def get_offers_by_id(ids):
        return Offer.objects.filter (id__in=ids)
    
    @staticmethod
    def get_all_offers():
        return Offer.objects.all()

    @staticmethod
    def get_all_offer_by_vendorid(vendor_id):
        if vendor_id:
            return Vendor.objects.filter (vendor=vendor_id)
        else:
            return Vendor.get_all_products()
        
    def __str__(self):
            return self.name

class OfferImage(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE,default='', related_name='photos')
    photo = models.ImageField(upload_to='uploads/offer')
    description = models.CharField(max_length=60, default='some text..')

    def __str__(self):
        return self.offer.name