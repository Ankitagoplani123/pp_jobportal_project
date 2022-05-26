from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login as auth_login
from .forms import *
from .models import *
from django.views import View


class Homepage(View):
    def get(self, request):
        return render(request=request,
                      template_name='main/home.html')


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request=request,
                      template_name="main/login.html",
                      context={"form": form})

    def post(self, request):
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged In ')
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, 'Invalid username or password.')
        else:
            messages.add_message(request, messages.INFO, 'Invalid username or password.')


class Logout(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect('/')


class Registeration(View):
    def get(self, request):
        form = SignUpForm
        return render(request=request,
                      template_name="main/register.html",
                      context={"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            email = form.cleaned_data.get('email')
            mob = form.cleaned_data.get('mobile')
            messages.success(request, 'Your account created successfully!')
            auth_login(request, user)
            p = Register(username=username, email=email, mobile=mob)
            p.save()
            return redirect('/')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")


class Jobs(View):
    def get(self, request, company_id=None, username=None):
        reg = Register.objects.get(username=username)
        company_ids = list(reg.profile.jobs_applied.values_list('pk', flat=True))
        if company_id:
            profile = reg.profile
            companydetail = CompanyDetails.objects.get(pk=company_id)
            if not profile:
                redirect('/profile')
            else:
                if company_id in company_ids:
                    profile.jobs_applied.remove(companydetail)
                else:
                    profile.jobs_applied.add(companydetail)
        data = CompanyDetails.objects.all()
        form1 = ApplyForm
        company_ids = list(reg.profile.jobs_applied.values_list('pk', flat=True))
        context = {"data": data, "form": form1, "company_ids": company_ids}
        return render(request=request, template_name="main/profiles.html", context=context)


class Profile(View):
    def get(self, request, username):
        reg = Register.objects.get(username=username)
        form = BioForm(instance=reg.profile)
        return render(request, 'main/profile.html', {'form': form})

    def post(self, request, username):
        reg = Register.objects.get(username=username)
        if reg.profile:
            ed_id = reg.profile.experience_details_id
        else:
            ed_id = None
        form = BioForm(request.POST, instance=reg.profile)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            highest_degree = form.cleaned_data.get("highest_degree")
            gender = form.cleaned_data.get("gender")
            is_fresher = form.cleaned_data.get("is_fresher")
            marital_status = form.cleaned_data.get("marital_status")
            if reg.profile is None:
                ins = ProfileForm.objects.create(first_name=first_name, last_name=last_name, gender=gender,
                                                 highest_degree=highest_degree, is_fresher=is_fresher,
                                                 marital_status=marital_status)
                reg.profile = ins
                reg.save()
            else:
                first_name = form.cleaned_data.get("first_name")
                last_name = form.cleaned_data.get("last_name")
                highest_degree = form.cleaned_data.get("highest_degree")
                gender = form.cleaned_data.get("gender")
                is_fresher = form.cleaned_data.get("is_fresher")
                marital_status = form.cleaned_data.get("marital_status")
                profile_obj = reg.profile
                profile_obj.first_name = first_name
                profile_obj.last_name = last_name
                profile_obj.gender = gender
                profile_obj.highest_degree = highest_degree
                profile_obj.is_fresher = is_fresher
                profile_obj.marital_status = marital_status
                profile_obj.experience_details_id = ed_id
                profile_obj.save()
        return redirect('/job_details/{}'.format(username))


class Experience(View):
    def get(self, request, username):
        reg = Register.objects.get(username=username)
        ed = reg.profile.experience_details
        if reg.profile.is_fresher:
            return redirect('/')
        form = AluForm(instance=ed)
        return render(request, 'main/job_detail.html', {'form': form})

    def post(self, request, username):
        reg = Register.objects.get(username=username)
        ed = reg.profile.experience_details
        if reg.profile.is_fresher:
            return redirect('main:homepage')
        form = AluForm(instance=ed)

        form = AluForm(request.POST, instance=ed)
        if form.is_valid():
            if not ed:
                ed = ExperienceDetails.objects.create(
                    first_company=form.cleaned_data.get("first_company"),
                    current_company=form.cleaned_data.get("current_company"),
                    experience=form.cleaned_data.get("experience"),
                    job_post=form.cleaned_data.get("job_post")
                )
                profile_obj = reg.profile
                profile_obj.experience_details = ed
                profile_obj.save()
            else:
                ed.first_company = form.cleaned_data.get("first_company")
                ed.current_company = form.cleaned_data.get("current_company")
                ed.experience = form.cleaned_data.get("experience")
                ed.job_post = form.cleaned_data.get("job_post")
                ed.save()
        return redirect('/')
