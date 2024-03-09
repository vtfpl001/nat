from django.contrib import admin
from django import forms
from .models import City, FamilyIdentification, FamilyMember

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the parent field to display ID - full_name

        self.fields['parent'].label_from_instance = lambda obj: f'{obj.id} - {obj.full_name}'
        self.fields['spouse'].label_from_instance = lambda obj: f'{obj.id} - {obj.full_name}'

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    form = FamilyMemberForm
    list_display = ('id', 'full_name', 'parent', 'spouse')  # Add 'id' to the list_display

admin.site.register(City)
admin.site.register(FamilyIdentification)

from django.contrib import admin
from .models import Photo
from .models import msgKind
from .models import sandesha
from .models import comments
from .models import instructions
from .models import UserProfile

admin.site.register(Photo)
admin.site.register(msgKind)
admin.site.register(sandesha)
admin.site.register(comments)
admin.site.register(instructions)
admin.site.register(UserProfile)

