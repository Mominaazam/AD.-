from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from .models import Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm
from rest_framework.permissions import AllowAny

from rest_framework.authentication import BaseAuthentication
from rest_framework import generics
from .models import U_user, role, permission, Internal_User, role_permission, user_meta
from .serializers import U_userSerializer, RoleSerializer, PermissionSerializer, InternalUserSerializer, RolePermissionSerializer, MetaUserSerializer

from .models import Property_Owner_meta, Property_Owner, Property, Property_meta, Property_Bills, Bills, Sector, Zone, Society, Property_Type
from .serializers import Property_OwnerSerializer, Property_Owner_metaSerializer, PropertySerializer, Property_metaSerializer, Property_BillsSerializer, BillsSerializer, SectorSerializer, SocietySerializer, ZoneSerializer, Property_TypeSerializer

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = None

    topics = None
    room_count = None
    room_messages = None

    context = {'topics': topics,
               'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)




def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = None
    room_messages = None
    topics = None
    context = {'user': user, 'rooms': rooms,
               'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})




# Corrected import statement in studybud/urls.py
#from base import views

class U_userCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    queryset = U_user.objects.all()
    serializer_class = U_userSerializer


class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]

class RoleRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]

class PermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [AllowAny]

class PermissionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [AllowAny]

class InternalUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Internal_User.objects.all()
    serializer_class = InternalUserSerializer
    permission_classes = [AllowAny]

class RolePermissionListCreateAPIView(generics.ListCreateAPIView):
    queryset = role_permission.objects.all()
    serializer_class = RolePermissionSerializer
    permission_classes = [AllowAny]

class MetaUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = user_meta.objects.all()
    serializer_class = MetaUserSerializer
    permission_classes = [AllowAny]




class PropertyOwnerListCreatAPIView(generics.ListCreateAPIView):
    queryset = Property_Owner.objects.all()
    serializer_class = Property_OwnerSerializer
    permission_classes = [AllowAny]
        
    
class PropertyOwnerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_Owner.objects.all()
    serializer_class = Property_OwnerSerializer
    permission_classes = [AllowAny]

class PropertyOwnermetaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_Owner_meta.objects.all()
    serializer_class = Property_Owner_metaSerializer
    permission_classes = [AllowAny]

class PropertyOwnermetaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_Owner_meta.objects.all()
    serializer_class = Property_Owner_metaSerializer
    permission_classes = [AllowAny]


class PropertyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]

class PropertyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [AllowAny]



class PropertymetaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_meta.objects.all()
    serializer_class = Property_metaSerializer
    permission_classes = [AllowAny]

class PropertymetaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property_meta.objects.all()
    serializer_class = Property_metaSerializer
    permission_classes = [AllowAny]


class PropertyBillsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property_Bills.objects.all()
    serializer_class = Property_BillsSerializer
    permission_classes = [AllowAny]

class PropertyBillsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]

class BillsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [AllowAny]
    
class BillsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]

class SectorListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    permission_classes = [AllowAny]

class SectorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]


class ZoneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [AllowAny]

class ZoneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]


class SocietyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]

class SocietyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]


class PropertyTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]

class PropertyTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Society.objects.all()
    serializer_class = SocietySerializer
    permission_classes = [AllowAny]


