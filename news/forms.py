from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_category',
            'title',
            'text',
            'category_type',
        ]


class PostForms(forms.Form):
    title = forms.CharField(label='Заголовок')
    text = forms.CharField(label='Текст')
    category_type = forms.ModelChoiceField(label='Метка', queryset=Post.objects.all())
    post_category = forms.ModelChoiceField(label='Категория', queryset=Post.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        if title is not None and len(title) < 20:
            raise ValidationError({
                'title': 'Описание не может быть менее 20 символов.'
            })

        if title[0].islower():
            raise ValidationError({
                'title': 'Описание не может начинаться с маленькой буквы.'
            })

        if text == title:
            raise ValidationError(
                'Описание не должно быть идентично тексту поста.'
            )

        return cleaned_data

