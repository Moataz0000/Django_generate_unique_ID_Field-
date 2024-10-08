import uuid 
from django.db import models
import random
import string




class GenerateUniqueIDField(models.CharField):
    
    """
    Generate Random Unique ID characters and digits Field
    """
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 8
        kwargs['unique'] = True
        super().__init__(*args, **kwargs)
        
    
    def generate_unique_id(length=8) -> str:
        characters = string.ascii_letters + string.digits    
        return ''.join(random.choices(characters, k=length))
    
    
    def pre_save(self,model_instance, add):
        """
        pre_save method is used to ensure that a unique product ID is generated
        before the object is saved to the database.
        """
        
        value = getattr(model_instance, self.attname)
        # Only generate if the value doesn't already exist
        if not value:
            value = self.generate_unique_id()
            
            # Ensure the generated ID is unique by checking the database
            while model_instance.__class__.objects.filter(**{self.attname: value}).exists():
                value = self.generate_unique_id()
                
            setattr(model_instance, self.attname, value)    
        return value