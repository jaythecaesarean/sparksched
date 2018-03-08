from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from .models import Student, Parent, PersonalInfo, NameInfo, StudentParent, AddressInfo, ExtraInfo,NationalityInfo




class NameInfoInline(NestedStackedInline):
    model = NameInfo
    extra = 1
    max_num = 2

class AddressInfoInline(NestedStackedInline):
    model = AddressInfo
    extra = 1
    max_num = 2

class ExtraInfoInline(NestedStackedInline):
    model = ExtraInfo
    max_num = 1

class PersonalInfoInline(NestedStackedInline):
    model = PersonalInfo
    inlines = [NameInfoInline, AddressInfoInline, ExtraInfoInline]


@admin.register(PersonalInfo)
class PersonalInfoAdmin(NestedModelAdmin):
    model = PersonalInfo
    inlines = [NameInfoInline, AddressInfoInline, ExtraInfoInline]

# @admin.register(NationalityInfo)
class NationalityInfo(admin.ModelAdmin):
    model = NationalityInfo



class StudentParentInline(NestedTabularInline):
    model = StudentParent
    extra = 1    

class ParentInline(NestedStackedInline):
    model = Parent
    inlines = [StudentParentInline,]

class StudentInline(NestedTabularInline):
    model = Student
    extra = 1
    max_num = 4
    inlines = [StudentParentInline,]

@admin.register(Parent)
class ParentAdmin(NestedModelAdmin):
    model = Parent
    inlines = [StudentParentInline, PersonalInfoInline]