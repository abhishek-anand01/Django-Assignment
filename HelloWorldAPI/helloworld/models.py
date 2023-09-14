from django.db import models

class Person(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    """
    Model representing a person.

    This model stores information about individuals, including their first name
    and last name.

    Attributes:
        first_name (str): The first name of the person (maximum length: 50 characters).
        last_name (str): The last name of the person (maximum length: 50 characters).

    Methods:
        __str__(): Returns a string representation of the person in the format
            "First Name Last Name".
    """
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        app_label = 'helloworld'