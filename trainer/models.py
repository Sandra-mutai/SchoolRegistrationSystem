from django.db import models
 

class Trainer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=16)
    age=models.PositiveSmallIntegerField()
    email=models.EmailField(max_length=30)
    phone_number=models.CharField(max_length=15)
    id_number=models.CharField(max_length=12)
    lessons=models.CharField(max_length=20)
    salary=models.CharField(max_length=6)
    # bank_account =models.CharField(max_length=6)
    nationality=models.CharField(max_length=10)
    courses=models.CharField(max_length=17)
    company=models.CharField(max_length=15)
    image=models.ImageField(null=True)
    resume=models.FileField(max_length=100)
    contract=models.FileField(max_length=100)
    COUNTRY_CHOICES=(
        (u'Kenya','Kenya'),
        (u'Uganda','Uganda'),
        (u'Rwanda','Rwanda')
    )
    country=models.CharField(max_length=8,choices=COUNTRY_CHOICES)

    NATIONALITY_CHOICES=(
     ("Kenyan","Kenyan"),
     ("Rwandese","Rwandese"),
     ("Ugandan","Ugandan"),
     ("Sudanese","Sudanese"),
     ("South Sudanese","South Sudanese"),
     ("Somalia","Somalia"),
    )
    nationality=models.CharField(max_length=15,choices=NATIONALITY_CHOICES,null=True)

    GENDER_CHOICES=(
        (u'Male','Male'),
        (u'Female','Female'),
        (u'Others','Others')
    )
    gender=models.CharField(max_length=8,choices=GENDER_CHOICES,null=True)

    def __str__(self):
        return self.first_name


