from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group, User
from django.forms import ModelForm


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user


class SocialSignupForm(SignupForm):

    def save(self, request):
        user = super(SocialSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


class UpdateProfileForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'groups',
        ]