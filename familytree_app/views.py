#/home/keyurjoshi/familytree_project/familytree_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import FamilyMember, FamilyIdentification, City
from .forms import FamilyMemberForm
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Photo  # Import the Photo model from your models.py file

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import FamilyMember
from .forms import FamilyMemberForm





from django.shortcuts import render
from django.utils import timezone
from .models import FamilyMember

from django.shortcuts import render
from familytree_app.models import FamilyMember

def home(request):

    total_family_members = FamilyMember.objects.count()
    total_males = FamilyMember.objects.filter(gender='M').count()
    total_females = FamilyMember.objects.filter(gender='F').count()



    photos = Photo.objects.all()
    msgkinds = msgKind.objects.all()
    instructions_list = instructions.objects.all()


    context = {
        'photos': photos,
        'total_family_members': total_family_members,
        'total_males': total_males,
        'total_females': total_females,
        'msgkinds': msgkinds,  # Include msgkinds in the context
        'instructions_list': instructions_list,  # Add this line


    }

    return render(request, 'familytree_app/home.html', context)



def family_member_list(request):
    family_members = FamilyMember.objects.all().order_by('-id')

    # Paginate the family members
    paginator = Paginator(family_members, 10)  # 10 members per page
    page_number = request.GET.get('page')
    family_members = paginator.get_page(page_number)



    return render(request, 'familytree_app/family_member_list.html', {
       'family_members': family_members,
    })



def family_member_detail(request, pk):
    family_member = get_object_or_404(FamilyMember, pk=pk)
    return render(request, 'familytree_app/family_member_detail.html', {'family_member': family_member})




@login_required
def family_member_create(request):
    # Check if the user has the required permissions
    if request.user.is_superuser or request.user.is_staff or request.user.username.startswith('add888'):
        if request.method == 'POST':
            form = FamilyMemberForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('familytree_app:family_member_list')
        else:
            form = FamilyMemberForm()
        return render(request, 'familytree_app/family_member_form.html', {'form': form})
    else:
        messages.error(request, 'You do not have permission to add new family members.')
        return redirect('familytree_app:family_member_list')



@login_required
def family_member_update(request, pk):
    family_member = get_object_or_404(FamilyMember, pk=pk)



    # Check if the user has the required permissions
    if request.user.is_superuser or request.user.is_staff or request.user.username.startswith('edit444'):
        if request.method == 'POST':
            form = FamilyMemberForm(request.POST, instance=family_member)
            if form.is_valid():
                updated_member = form.save()
                return redirect('familytree_app:family_member_detail', pk=updated_member.pk)
        else:
            form = FamilyMemberForm(instance=family_member)
        return render(request, 'familytree_app/family_member_form.html', {'form': form})
    else:
        messages.error(request, 'You do not have permission to edit this family member.')
        return redirect('familytree_app:family_member_list')




@login_required
def family_member_delete(request, pk):
    family_member = get_object_or_404(FamilyMember, pk=pk)

    # Check if the user has the required permissions
    if request.user.is_superuser or request.user.is_staff or request.user.username.startswith('del777'):
        if request.method == 'POST':
            family_member.delete()
            return redirect('familytree_app:family_member_list')
        return render(request, 'familytree_app/family_member_confirm_delete.html', {'family_member': family_member})
    else:
        messages.error(request, 'You do not have permission to delete this family member.')
        return redirect('familytree_app:family_member_list')


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FamilyMemberForm
from .models import FamilyMember

@login_required
def family_member_add_child(request, pk):
    parent_member = get_object_or_404(FamilyMember, pk=pk)

    # Check if the user is a superuser or admin
    if request.user.is_superuser or request.user.is_staff or request.user.username.startswith('add888'):
        if request.method == 'POST':
            child_form = FamilyMemberForm(request.POST)
            if child_form.is_valid():
                child = child_form.save(commit=False)
                child.parent = parent_member
                child.surname = parent_member.surname
                child.family_identification = parent_member.family_identification
                child.old_location = parent_member.old_location
                child.save()

                action = request.POST.get('action')  # Get the action from the form

                if action == 'save':
                    return redirect('familytree_app:family_member_detail', pk=parent_member.pk)
                elif action == 'save_and_add_more':
                    child_form = FamilyMemberForm(initial={
                        'surname': parent_member.surname,
                        'family_identification': parent_member.family_identification,
                        'address': parent_member.address,
                        'city': parent_member.city,
                        'old_location': parent_member.old_location,
                        'parent': parent_member.id,
                    })
                    child_form.fields['spouse'].widget.attrs['disabled'] = True
                    child_form.fields['parent'].widget.attrs['disabled'] = True
                    child_form.fields['surname'].widget.attrs['readonly'] = True  # Make the surname field read-only
                    child_form.fields['family_identification'].widget.attrs['readonly'] = True  # Make the family_identification field read-only

        else:
            child_form = FamilyMemberForm(initial={
                'surname': parent_member.surname,
                'address': parent_member.address,
                'city': parent_member.city,

                'family_identification': parent_member.family_identification,
                'old_location': parent_member.old_location,
                'parent': parent_member.id,
            })
            child_form.fields['spouse'].widget.attrs['disabled'] = True
            child_form.fields['parent'].widget.attrs['disabled'] = True
            child_form.fields['surname'].widget.attrs['readonly'] = True  # Make the surname field read-only
            child_form.fields['family_identification'].widget.attrs['readonly'] = True  # Make the family_identification field read-only

        return render(request, 'familytree_app/family_member_add_child.html', {
            'parent_member': parent_member,
            'child_form': child_form,
        })
    else:
        messages.error(request, 'You do not have permission to add a child to this family member.')
        return redirect('familytree_app:family_member_list')




from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def login_view(request):
    # Your login logic here
    next_url = request.GET.get('next', 'familytree_app:home')
    return redirect(next_url)

def logout_view(request):
    # Your logout logic here
    next_url = request.GET.get('next', 'familytree_app:home')
    logout(request)
    return redirect(next_url)




from django.shortcuts import render
from .models import FamilyMember

def view_all_roots(request):
    roots = FamilyMember.objects.filter(parent=None).order_by('-id')


   # Paginate the family members
    paginator = Paginator(roots, 10)  # 10 members per page
    page_number = request.GET.get('page')
    roots = paginator.get_page(page_number)



    return render(request, 'familytree_app/view_all.html', {'members': roots, 'title': 'All Roots'})





def view_all_leaves(request):
    leaves = FamilyMember.objects.exclude(children__isnull=False).order_by('-id')


   # Paginate the family members
    paginator = Paginator(leaves, 10)  # 10 members per page
    page_number = request.GET.get('page')
    leaves = paginator.get_page(page_number)




    return render(request, 'familytree_app/view_all.html', {'members': leaves, 'title': 'All Leaves'})








def search_by_name(request):
    search_query = request.GET.get('search')
    selected_city = request.GET.get('selected_city')
    selected_family_identification = request.GET.get('selected_family_identification')


    family_members = FamilyMember.objects.all().order_by('-id')

    if selected_city:
        family_members = family_members.filter(city_id=selected_city)

    if selected_family_identification:
        family_members = family_members.filter(family_identification_id=selected_family_identification)

    if search_query:
        search_query = search_query.strip()
        family_members = family_members.filter(
            Q(full_name__icontains=search_query) |
            Q(full_name__icontains=search_query.replace(" ", "")) |  # Add missing comma here
            Q(id__icontains=search_query) |
            Q(surname__icontains=search_query) |
            Q(address__icontains=search_query) |
            Q(mobile__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(old_location__icontains=search_query) |
            Q(education__icontains=search_query) |
            Q(work_type__icontains=search_query) |
            Q(remarks__icontains=search_query)
        ).order_by('-id')
    else:
        family_members = family_members.all()

    # Get all cities and family identifications
    cities = City.objects.all()
    family_identifications = FamilyIdentification.objects.all()

    # Paginate the family members
    paginator = Paginator(family_members, 10)  # 10 members per page
    page_number = request.GET.get('page')
    family_members = paginator.get_page(page_number)

    return render(request, 'familytree_app/family_member_list.html', {
        'family_members': family_members,
        'family_identifications': family_identifications,
        'cities': cities,
        'selected_city': selected_city,
        'selected_family_identification': selected_family_identification,
    })





def filter_by_gender(request):
    selected_gender = request.GET.get('selected_gender')

    family_members = FamilyMember.objects.all().order_by('-id')

    if selected_gender:
        family_members = family_members.filter(gender=selected_gender)


    # Paginate the family members
    paginator = Paginator(family_members, 10)  # 10 members per page
    page_number = request.GET.get('page')
    family_members = paginator.get_page(page_number)





    return render(request, 'familytree_app/family_member_list.html', {
        'family_members': family_members,
    })


























def view_child_tree(request, member_id):
    root_member = get_object_or_404(FamilyMember, pk=member_id)
    child_tree = FamilyMember.objects.filter(parent=root_member)

    return render(request, 'familytree_app/view_child_tree.html', {'root_member': root_member, 'child_tree': child_tree})







# familytree_app/views.py

from django.shortcuts import render, get_object_or_404
from .models import msgKind, sandesha

# ... your existing views ...

def msgk_list(request):
    msgkinds = msgKind.objects.all()
    return render(request, 'familytree_app/msgk_list.html', {'msgkinds': msgkinds})

def msgkind_entries(request, msgkind_id):
    msgkind = get_object_or_404(msgKind, pk=msgkind_id)
    entries = sandesha.objects.filter(msgType=msgkind)
    return render(request, 'familytree_app/msgkind_entries.html', {'msgkind': msgkind, 'entries': entries})

def sandesha_detail(request, sandesha_id):
    sandesha_entry = get_object_or_404(sandesha, pk=sandesha_id)
    return render(request, 'familytree_app/sandesha_detail.html', {'sandesha_entry': sandesha_entry})



# familytree_app/views.py
from django.shortcuts import render
from .models import instructions

def instructions_view(request):
    instructions_list = instructions.objects.all()
    return render(request, 'familytree_app/instructions.html', {'instructions_list': instructions_list})


