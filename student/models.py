from django.db import models

# Create your models here.


class EntryLanguageInfo(models.Model):
    ENGLISH = 'EN'
    THAI = 'TH'
    LANGUAGE = (
        (ENGLISH, 'English'),
        (THAI, 'Thai'),
    )
    entry_language = models.CharField(
                max_length=2,
                choices=LANGUAGE,
                default=THAI,
            )

    class Meta:
        abstract = True

class NameInfo(EntryLanguageInfo):
    name_reference_number = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class AddressInfo(EntryLanguageInfo):
    address_reference_number = models.CharField(max_length=10, blank=True, null=True)
    plot_house_number = models.CharField(max_length=20, blank=True, null=True)
    building_mu = models.CharField(max_length=50, blank=True, null=True)
    street_road = models.CharField(max_length=50, blank=True, null=True)
    khet_tambon = models.CharField(max_length=50, blank=True, null=True)
    kwaeng_amphoe = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)


class NationalityInfo(EntryLanguageInfo):
    name = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50)


class ExtraInfo(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    RELATIONSHIP_TO_STUDENT = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    birthdate = models.DateField( blank=True, null=True)
    nationality = models.ForeignKey(
                NationalityInfo, 
                related_name='nationality', 
                on_delete=models.CASCADE, 
                blank=True, 
                null=True
            )
    national_id_card_number =  models.CharField(max_length=20, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(
                max_length=20,
                choices=RELATIONSHIP_TO_STUDENT,
                default=MALE,
            )


class PersonalInfo(models.Model):
    reference_number = models.CharField(max_length=50)
    name_en = models.ForeignKey(
                NameInfo, 
                related_name='student_name_en',
                on_delete=models.CASCADE,
                blank=True, null=True
            )
    name_th = models.ForeignKey(
                NameInfo, 
                related_name='student_name_th',
                on_delete=models.CASCADE,
                blank=True, null=True
            )
    address_en = models.ForeignKey(
                AddressInfo, 
                related_name='address_en',
                on_delete=models.CASCADE,
                blank=True, null=True
            )
    address_th = models.ForeignKey(
                AddressInfo, 
                related_name='address_th',
                on_delete=models.CASCADE,
                blank=True, null=True
            )

    extra_info = models.ForeignKey(
                AddressInfo, 
                on_delete=models.CASCADE,
                blank=True, null=True
            )
    

class Student(models.Model):
    personal_info = models.ForeignKey(
                PersonalInfo, 
                on_delete=models.CASCADE,
                blank=True, null=True
            )

class Parent(models.Model):
    personal_info = models.ForeignKey(
                PersonalInfo, 
                on_delete=models.CASCADE,
                blank=True, null=True
            )


class StudentParent(models.Model):
    MOTHER = 'mother'
    FATHER = 'father'
    OTHER = 'other'
    RELATIONSHIP_TO_STUDENT = (
        (MOTHER, 'Mother'),
        (FATHER, 'Father'),
        (OTHER, 'Other'),
    )

    student = models.ForeignKey(
                Student, 
                on_delete=models.CASCADE,
                blank=True, null=True
            )
    parent = models.ForeignKey(
                Parent, 
                on_delete=models.CASCADE,
                blank=True, null=True
            )
    relationship = models.CharField(
                max_length=20,
                choices=RELATIONSHIP_TO_STUDENT,
                default=MOTHER,
            )

    


