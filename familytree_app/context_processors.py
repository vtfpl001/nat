#/home/keyurjoshi/familytree_project/familytree_app/context_processors.py
from .models import FamilyMember  # Import the appropriate model

def total_member_counts(request):
    total_family_members = FamilyMember.objects.count()
    total_males = FamilyMember.objects.filter(gender='M').count()
    total_females = FamilyMember.objects.filter(gender='F').count()

    return {
        'total_family_members': total_family_members,
        'total_males': total_males,
        'total_females': total_females,
    }

# Import the City model at the beginning of your context_processors.py
from .models import City, FamilyIdentification, FamilyMember

# Create a context processor to fetch and provide the combo box data
def combo_box_data(request):
    # Fetch distinct city and family identification values from FamilyMember
    distinct_cities = FamilyMember.objects.order_by().values('city').distinct()
    distinct_family_identifications = FamilyMember.objects.order_by().values('family_identification').distinct()

    # Convert the distinct values to lists for the combo box options
    cities = City.objects.filter(id__in=[city['city'] for city in distinct_cities])
    family_identifications = FamilyIdentification.objects.filter(id__in=[fam_id['family_identification'] for fam_id in distinct_family_identifications])

    return {
        'cities': cities,
        'family_identifications': family_identifications,
    }
