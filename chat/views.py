from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserRelation, Messages
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSerializer
from django.contrib import messages as django_messages 
from .models import Room 
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import User, UserRelation, Messages



# Create your views here.
def home(request):
    return render(request, 'home.html')


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Roles, Profile
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile
from decimal import Decimal, InvalidOperation
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
# Initialize roles and admin
def initialize_roles_and_admin():
    if Roles.objects.count() < 1:
        Roles.objects.bulk_create([
            Roles(name='Admin'),
            Roles(name='User'),
        ])
    
    if Profile.objects.count() < 1:
        Profile.objects.create(
            name='Admin',
            username='admin',
            password=make_password('admin@123'),  # Hash the password
            role=Roles.objects.get(pk=1)
        )


from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile  # Ensure Profile is correctly imported
from django.views.decorators.http import require_POST

def login(request):
    content = {'title': 'Login'}
    initialize_roles_and_admin()

    if request.method == 'POST':
        username = request.POST.get('username', '').lower()
        password = request.POST.get('password', '')

        profile = Profile.objects.filter(username=username).first()

        if profile and check_password(password, profile.password):  # Check hashed password
            request.session['account_name'] = profile.name
            request.session['account_id'] = profile.id
            request.session['account_role'] = profile.role_id

            # Create a Django user object for session management
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
            
            # Redirect based on user role
            return redirect('admin-train' if profile.role_id == 1 else 'profile')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html', content)

@require_POST
def update_profile(request):
    profile = Profile.objects.get(user=request.user)  # Adjust as needed for user identification
    profile.height = request.POST.get('height')
    profile.caste = request.POST.get('caste')
    profile.mother_tongue = request.POST.get('mother_tongue')
    profile.city = request.POST.get('city')
    profile.annual_income = request.POST.get('annual_income')
    profile.marriage_status = request.POST.get('marriage_status')
    profile.save()
    return redirect('profile_page')

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Profile, Roles
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Profile


def signup(request):
    content = {'title': 'Sign up'}
    initialize_roles_and_admin()  # Make sure this function initializes necessary roles and admin

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        mobile = request.POST['mobile']

        # Additional profile fields
        name = request.POST['name']
        gender = request.POST['gender']
        mother_tongue = request.POST['motherTongue']
        religion = request.POST['religion']
        caste = request.POST['caste']
        marriage_status = request.POST['marriageStatus']
        height = request.POST['height']
        horoscope = request.POST['horoscope']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        degree = request.POST['degree']
        employed_in = request.POST['employedIn']
        occupation = request.POST['occupation']
        annual_income = request.POST['annualIncome']
        career_about = request.POST['careerAbout']
        family_type = request.POST['familyType']
        father_occupation = request.POST['fatherOccupation']
        mother_occupation = request.POST['motherOccupation']
        brother_count = request.POST['brotherCount']
        family_living_in = request.POST['familyLivingIn']
        contact_address = request.POST['contactAddress']
        about_family = request.POST['aboutFamily']

        # Check for existing username
        if User.objects.filter(username=username).exists():
            messages.error(request, f"{username} already exists.")
        elif User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, f"A user with this email already exists.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            # Create a new user
            user = User.objects.create_user(username=username, email=request.POST['email'], password=password)
            user.save()

            # Create the profile
            profile = Profile(
                name=name.title(),
                username=username,
                password=make_password(password),  # Hash the password
                role=Roles.objects.get(pk=2),  # Assuming the default role is 2
                mobile=mobile,
                gender=gender,
                mother_tongue=mother_tongue,
                religion=religion,
                caste=caste,
                marriage_status=marriage_status,
                height=height,
                horoscope=horoscope,
                country=country,
                state=state,
                city=city,
                degree=degree,
                employed_in=employed_in,
                occupation=occupation,
                annual_income=annual_income,
                career_about=career_about,
                family_type=family_type,
                father_occupation=father_occupation,
                mother_occupation=mother_occupation,
                brother_count=brother_count,
                family_living_in=family_living_in,
                contact_address=contact_address,
                about_family=about_family
            )
            profile.save()

            # Log the user in after registration
            auth_login(request, user)
            messages.success(request, 'Account created and profile updated. You are now logged in.')
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, 'signup.html', content)

@login_required
def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'profile_detail.html', {'profile': profile})

def logout(request):
    request.session.flush()  # Clear the session
    messages.success(request, "You have been logged out.")
    return HttpResponseRedirect(reverse('login'))

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Profile

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(username=request.user.username)
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect(reverse('homepage'))

    return render(request, 'profile.html', {'profile': profile, 'title': 'Profile'})



# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Profile
'''
@login_required
def matches(request):
    try:
        # Fetch the current user's profile
        user_profile = Profile.objects.get(username=request.user.username)
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect(reverse('homepage'))

    # Filter profiles based on the gender preference of the current user's profile
    if user_profile.gender == 'Male':
        profiles = Profile.objects.filter(gender='Female')
    elif user_profile.gender == 'Female':
        profiles = Profile.objects.filter(gender='Male')
    else:
        profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
        'title': 'Matches'
    }
    return render(request, 'matches.html', context)'''



def navbar_card(request):
    
    return render(request, 'navbar_card.html')

def upgrade_card(request):
    
    return render(request, 'upgrade_card.html')

def looking_for(request):
    
    return render(request, 'looking_for.html')

def search(request):
    
    return render(request, 'search.html')
def upgrade(request):
    
    return render(request, 'upgrade.html')
def messagess(request):
    
    return render(request, 'messagess.html')

@login_required(login_url="loginpage")
def notification(request):
    friends_data = UserRelation.objects.all()
    friends_list = []
    for obj in friends_data:
        if obj.user.username == request.user.username:
            friend_dict = {"username": obj.friend.username, "accepted": obj.accepted}
            friends_list.append(friend_dict)

    request_list = []
    for obj in friends_data:
        if obj.friend.username == request.user.username:
            if not obj.accepted:
                request_dict = {"username": obj.user.username}
                request_list.append(request_dict)

    data = {
        "email": request.user.email,
        "username": request.user.username,
        "friends": friends_list,
        "requests": request_list,
    }
    return render(
        request,
        "notification.html",
        {
            "data": data,
        },
    )

    
# views.py








def LogoutPage(request):
    logout(request)
    return redirect("login")


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect("homepage")

    error_message = ""
    email = ""

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")

        try:
            # Fetch the user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            error_message = "Email not found. Please check your Email."
            return render(request, "loginpage.html", {"error_message": error_message, "email": email})

        # Authenticate the user with Django's system
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("homepage")
        else:
            error_message = "Incorrect password. Please try again."

    return render(request, "loginpage.html", {"error_message": error_message, "email": email})
    


def LogoutPage(request):
    logout(request)
    return redirect("loginpage")

@login_required(login_url="loginpage")
def userprofile(request, username):
    if username == request.user.username:
        return redirect("/")
    friend_dict = {}
    request_dict = {}
    friend_dict["accepted"] = False
    request_dict["accepted"] = False
    friend_dict["name"] = ""
    send_request = False
    not_accepted = False
    me_not_accepted = False
    is_friend = False
    try:
        user = User.objects.get(username=username)
        friends_data = UserRelation.objects.all()
        for obj in friends_data:
            if obj.user.username == request.user.username:
                if obj.friend.username == username:
                    friend_dict = {
                        "name": obj.friend.username,
                        "accepted": obj.accepted,
                    }
        for obj in friends_data:
            if obj.friend.username == request.user.username:
                if obj.user.username == username:
                    if obj.accepted:
                        me_not_accepted = False
                    else:
                        me_not_accepted = True

    except User.DoesNotExist:
        messages.error(request, "User does not exist.")
        return render(request, "friend.html")

    if friend_dict["name"] == "":
        if me_not_accepted == True:
            print("me not accepted")
        else:
            print("not a friend")
            send_request = True

    elif friend_dict["accepted"] == False:
        print("not_accepted")
        not_accepted = True

    else:
        print("friend")
        is_friend = True
    print("send_request = ", send_request)
    print("not_accepted = ", not_accepted)
    print("me_not_accepted = ", me_not_accepted)
    print("is_friend = ", is_friend)
    # You can now access user details, such as username, email, etc.
    user_details = {
        "username": user.username,
        "email": user.email,
        "send_request": send_request,
        "not_accepted": not_accepted,
        "is_friend": is_friend,
        "me_not_accepted": me_not_accepted,
    }

    return render(request, "friend.html", {"user_details": user_details})


@login_required(login_url="loginpage")
def EditProfile(request):
    success_message = None
    error_message = None

    if request.method == "POST":
        new_email = request.POST.get("email")
        new_username = request.POST.get("username")

        # Check if the new username is already taken
        if (
            new_username != request.user.username
            and User.objects.filter(username=new_username).exists()
        ):
            error_message = "Username already exists. Please choose a different one."
        elif (
            new_email != request.user.email
            and User.objects.filter(email=new_email).exists()
        ):
            error_message = "Email address already associated with another account. Please choose a different one."
        else:
            # Update email and username
            # print(request.user.id)
            request.user.email = new_email
            request.user.username = new_username
            request.user.save()
            success_message = "Profile updated successfully."

    # Pre-fill the form with the user's existing data
    initial_data = {
        "email": request.user.email,
        "username": request.user.username,
    }

    return render(
        request,
        "edit.html",
        {
            "initial_data": initial_data,
            "success_message": success_message,
            "error_message": error_message,
        },
    )


@login_required(login_url="loginpage")
def userprofile(request, username):
    if username == request.user.username:
        return redirect("/")
    friend_dict = {}
    request_dict = {}
    friend_dict["accepted"] = False
    request_dict["accepted"] = False
    friend_dict["name"] = ""
    send_request = False
    not_accepted = False
    me_not_accepted = False
    is_friend = False
    try:
        user = User.objects.get(username=username)
        friends_data = UserRelation.objects.all()
        for obj in friends_data:
            if obj.user.username == request.user.username:
                if obj.friend.username == username:
                    friend_dict = {
                        "name": obj.friend.username,
                        "accepted": obj.accepted,
                    }
        for obj in friends_data:
            if obj.friend.username == request.user.username:
                if obj.user.username == username:
                    if obj.accepted:
                        me_not_accepted = False
                    else:
                        me_not_accepted = True

    except User.DoesNotExist:
        messages.error(request, "User does not exist.")
        return render(request, "friend.html")

    if friend_dict["name"] == "":
        if me_not_accepted == True:
            print("me not accepted")
        else:
            print("not a friend")
            send_request = True

    elif friend_dict["accepted"] == False:
        print("not_accepted")
        not_accepted = True

    else:
        print("friend")
        is_friend = True
    print("send_request = ", send_request)
    print("not_accepted = ", not_accepted)
    print("me_not_accepted = ", me_not_accepted)
    print("is_friend = ", is_friend)
    # You can now access user details, such as username, email, etc.
    user_details = {
        "username": user.username,
        "email": user.email,
        "send_request": send_request,
        "not_accepted": not_accepted,
        "is_friend": is_friend,
        "me_not_accepted": me_not_accepted,
    }

    return render(request, "friend.html", {"user_details": user_details})


@login_required(login_url="loginpage")
def add_friend(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = request.user
        friend = User.objects.get(username=username)
        accepted = False
        print("starts")
        exists = UserRelation.objects.filter(user=user, friend=friend).exists()
        print("sts")
        if exists:
            print("star")
            return HttpResponseRedirect(
                request.META.get("HTTP_REFERER", reverse("homepage"))
            )
        user_relation = UserRelation(user=user, friend=friend, accepted=accepted)
        user_relation.save()
        messages.success(request, "Request sended successfully.")

        return redirect("homepage")
    else:
        return redirect("homepage")
    
@login_required(login_url="loginpage")
def accept_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = request.user
        friend = User.objects.get(username=username)
        accepted = True

        exists = UserRelation.objects.filter(user=user, friend=friend).exists()
        print("sts")
        if exists:
            return HttpResponseRedirect(
                request.META.get("HTTP_REFERER", reverse("homepage"))
            )
        user_relation = UserRelation(user=user, friend=friend, accepted=accepted)
        user_relation.save()

        user_relation_revrse = UserRelation.objects.get(user=friend, friend=user)
        user_relation_revrse.accepted = True
        user_relation_revrse.save()
        messages.success(request, "Friend Added successfully.")

        return redirect("homepage")
    else:
        return redirect("homepage")

@login_required(login_url="loginpage")
def delete_friend(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = request.user
        friend = User.objects.get(username=username)
        try:
            print("starts")
            exists = UserRelation.objects.filter(user=user, friend=friend).exists()
            print("sts")
            if exists:
                pass
            else:
                return HttpResponseRedirect(
                    request.META.get("HTTP_REFERER", reverse("homepage"))
                )
            user_relation = UserRelation.objects.get(user=user, friend=friend)
            user_relation.delete()

            user_relation_reverse = UserRelation.objects.get(user=friend, friend=user)
            user_relation_reverse.delete()
            messages.success(request, "Friend deleted successfully.")

        except UserRelation.DoesNotExist:
            messages.success(request, "Request deleted successfully.")
            pass
        return redirect("homepage")
    else:
        return redirect("homepage")
    
@login_required(login_url="loginpage")
def delete_friend(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = request.user
        friend = User.objects.get(username=username)
        try:
            print("starts")
            exists = UserRelation.objects.filter(user=user, friend=friend).exists()
            print("sts")
            if exists:
                pass
            else:
                return HttpResponseRedirect(
                    request.META.get("HTTP_REFERER", reverse("home"))
                )
            user_relation = UserRelation.objects.get(user=user, friend=friend)
            user_relation.delete()

            user_relation_reverse = UserRelation.objects.get(user=friend, friend=user)
            user_relation_reverse.delete()
            messages.success(request, "Friend deleted successfully.")

        except UserRelation.DoesNotExist:
            messages.success(request, "Request deleted successfully.")
            pass
        return redirect("homepage")
    else:
        return redirect("homepage")
    
    

@login_required(login_url="login")
@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == "GET":
        messages = Messages.objects.filter(
            sender_name=sender, receiver_name=receiver, seen=False
        )
        serializer = MessageSerializer(
            messages, many=True, context={"request": request}
        )
        for message in messages:
            message.seen = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@login_required(login_url="loginpage")
def chat(request, username):
    try:
        usersen = request.user
        friend = User.objects.get(username=username)
        exists = UserRelation.objects.filter(
            user=request.user, friend=friend, accepted=True
        ).exists()

        if not exists:
            django_messages.error(
                request, "You are not able to chat with this user."
            )
            return redirect("homepage")
    except User.DoesNotExist:
        return redirect("homepage")

    messages = Messages.objects.filter(
        sender_name=usersen, receiver_name=friend
    ) | Messages.objects.filter(sender_name=friend, receiver_name=usersen)

    if request.method == "GET":
        return render(
            request,
            "chat.html",
            {
                "messages": messages,
                "curr_user": usersen,
                "friend": friend,
            },
        )
    
    if request.method == "POST":
        message_text = request.POST.get("message")
        if message_text:
            # Use the correct field name here
            Messages.objects.create(
                sender_name=usersen,
                receiver_name=friend,
                description=message_text,
                timestamp=timezone.now()  # Ensure timestamp is set correctly
            )
            return redirect(request.path)
        else:
            django_messages.error(request, "Message cannot be empty.")
            return redirect(request.path)

    return HttpResponse("Method not allowed", status=405)

@login_required(login_url="loginpage")
def HomePage(request):
    friends_data = UserRelation.objects.all()
    friends_list = []
    for obj in friends_data:
        if obj.user.username == request.user.username:
            friend_dict = {"username": obj.friend.username, "accepted": obj.accepted}
            friends_list.append(friend_dict)

    request_list = []
    for obj in friends_data:
        if obj.friend.username == request.user.username:
            if not obj.accepted:
                request_dict = {"username": obj.user.username}
                request_list.append(request_dict)

    data = {
        "email": request.user.email,
        "username": request.user.username,
        "friends": friends_list,
        "requests": request_list,
    }
    return render(
        request,
        "homepage.html",
        {
            "data": data,
        },
    )


from .models import User, Profile  # Make sure to import both User and Profile models

@login_required(login_url="loginpage")
def searchpage(request):
    if request.method == "GET":
        query = request.GET.get("q", "").strip()  # Strip whitespace from query
        
        if query:
            users = User.objects.filter(username__icontains=query)
            profiles = Profile.objects.filter(name__icontains=query)  # Search by name in Profile
            
            if users or profiles:
                return render(
                    request,
                    "searchpage.html",
                    {
                        "query": query,
                        "users": users,
                        "profiles": profiles,
                        "user": request.user.username,
                    }
                )
            else:
                not_found_message = f'No users or profiles found for "{query}"'
                return render(
                    request,
                    "searchpage.html",
                    {
                        "query": query,
                        "not_found_message": not_found_message,
                        "user": request.user.username,
                    }
                )

    return render(request, "searchpage.html", {"user": request.user.username})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import User, Profile
@login_required(login_url="loginpage")
def matches(request):
    query = request.GET.get("q", "").strip()  # Get and strip whitespace from the query

    try:
        # Fetch the current user's profile based on the username field
        user_profile = Profile.objects.get(username=request.user.username)
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect(reverse('homepage'))

    if not query:
        # Apply gender-based filtering if no search query is provided
        if user_profile.gender == 'Male':
            profiles = Profile.objects.filter(gender='Female')
        elif user_profile.gender == 'Female':
            profiles = Profile.objects.filter(gender='Male')
        else:
            profiles = Profile.objects.all()
    else:
        # If there is a query, filter users and profiles based on the query
        users = User.objects.filter(username__icontains=query)
        profiles = Profile.objects.filter(name__icontains=query)

        # Ensure that only profiles that match the user's gender preference are shown
        if user_profile.gender == 'Male':
            profiles = profiles.filter(gender='Female')
        elif user_profile.gender == 'Female':
            profiles = profiles.filter(gender='Male')

        if users or profiles:
            return render(
                request,
                "matches.html",
                {
                    "query": query,
                    "users": users,
                    "profiles": profiles,
                    "user": request.user.username,
                }
            )
        else:
            not_found_message = f'No users or profiles found for "{query}"'
            return render(
                request,
                "matches.html",
                {
                    "query": query,
                    "not_found_message": not_found_message,
                    "user": request.user.username,
                }
            )

    return render(
        request,
        "matches.html",
        {
            "query": query,
            "profiles": profiles,
            "user": request.user.username,
            "title": "Matches"
        }
    )
