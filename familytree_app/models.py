#/home/keyurjoshi/familytree_project/familytree_app/models.py
from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Check for duplicates based on the 'name' field
        duplicates = City.objects.filter(name=self.name).exclude(pk=self.pk)
        if duplicates.exists():
            raise ValueError("A city with the same name already exists.")
        super().save(*args, **kwargs)





class FamilyIdentification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




    def save(self, *args, **kwargs):
        # Check for duplicates based on the 'name' field
        duplicates = FamilyIdentification.objects.filter(name=self.name).exclude(pk=self.pk)
        if duplicates.exists():
            raise ValueError("A family identification with the same name already exists.")
        super().save(*args, **kwargs)





class FamilyMember(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    surname = models.CharField(max_length=100, verbose_name="અટક")
    full_name = models.CharField(max_length=100, verbose_name="નામ")
    # Gender field
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="જન્મ તારીખ")
    address = models.TextField(null=True, blank=True, verbose_name="સરનામુ")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    old_location = models.CharField(max_length=100, null=True, blank=True, verbose_name="મૂળ વતન")
    education = models.CharField(max_length=100, null=True, blank=True, verbose_name="અભ્યાસ")
    work_type = models.CharField(max_length=100, null=True, blank=True)
    family_identification = models.ForeignKey(FamilyIdentification, on_delete=models.CASCADE, verbose_name="ગોત્ર")
    remarks = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    spouse = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='husband_or_wife')
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.full_name



    def save(self, *args, **kwargs):
        # Check for duplicates based on specific fields
        duplicates = FamilyMember.objects.filter(
            surname=self.surname,
            full_name=self.full_name,
            city=self.city,
            family_identification=self.family_identification,
            parent=self.parent
        ).exclude(pk=self.pk)

        if duplicates.exists():
            # If duplicates exist, do not save the record
            raise ValueError("A family member with the same details already exists.")

        super().save(*args, **kwargs)




    # If the family member is male and has a spouse, link the spouse back to him
        if self.gender == 'M' and self.spouse:
            self.spouse.spouse = self
            self.spouse.surname=self.surname
            self.spouse.city=self.city
            self.spouse.address=self.address
            self.spouse.family_identification=self.family_identification
            self.spouse.save()





from django.db import models

class Photo(models.Model):
    description = models.CharField(max_length=255)
    photo_url = models.ImageField(upload_to='photos/')
    # Add other fields as needed, e.g., upload date, admin who uploaded, etc.

    def __str__(self):
        return self.description




class msgKind(models.Model):
    msgK = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.msgK




class sandesha(models.Model):
    photo_url = models.ImageField(upload_to='photos/', null=True, blank=True)
    msgType = models.ForeignKey(msgKind, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    msg = models.TextField(null=True, blank=True)

    signatureP = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class instructions(models.Model):
    srNo = models.CharField(max_length=5, unique=True)
    msg = models.CharField(max_length=500)

    def __str__(self):
        return self.msg


class comments(models.Model):
    msg = models.CharField(max_length=500)
    mobile = models.CharField(max_length=15, null=True, blank=True, unique=True)
    surname = models.CharField(max_length=100, verbose_name="અટક")
    name = models.CharField(max_length=100, verbose_name="નામ")
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.msg



from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
