from django.db import models


class Modal(models.Model):

    '''
        To add content on the Index.html page as a Bootstrap modal with adjustable text and icon and shape
    '''

    title = models.CharField(max_length=100)
    desc  = models.TextField()
    
    icon_code = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Enter the icon code from https://remixicon.com like "ri-calculator-fill"')
        
    color_code = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Enter your favorite icon color like "#29cc61"'
        )

    def __str__(self) -> str:
        return self.title
