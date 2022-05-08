from django.test import TestCase
from .models import Url

class UrlTestCase(TestCase):
    def setUp(self):
        qs = Url.objects.create(
            long_url = "www.google.com",   
        )
        
    def test_exists(self):
        qs = Url.objects.all()
        self.assertTrue(qs.exists()) 
        
    def test_count(self):
        cnt = Url.objects.count()
        self.assertEquals(cnt,1)        
    
    ## Continue
    