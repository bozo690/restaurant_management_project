from django.db import models

   class ContactSubmission(models.Model):
        """
        Represents a single submission from the contact form.
        """
        mame=models.CharField(max_length=100)
        email=models.EmailField()
        message=models.TextField()
        created_at=models.DateTimeField(auto_now_add=True)
        

        def __str__(self):
            return f"Message from{self.name} on  {self.created_at.strftime('%Y-%Ym-%d')} "





