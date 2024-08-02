from django import forms
from .models import Either, Comment

class EitherForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '질문을 입력하세요',
            }
        )
    )
    a = forms.CharField(
        label = '보기 A',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '보기 A를 입력하세요',
            }
        )
    )

    b = forms.CharField(
        label = '보기 B',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '보기 B를 입력하세요',
            }
        )
    )

    class Meta():
        model = Either
        fields = '__all__'

class CommentForm(forms.ModelForm):
    A = 'A'
    B = 'B'
    Choice = [
        (A, 'A'),
        (B, 'B'),
    ]
    choice = forms.ChoiceField(
        label = '답변',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        ), choices=Choice
    )

    content = forms.CharField(
        label = '내용',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '댓글을 입력하세요',
            }
        )
    )

    class Meta():
        model = Comment
        fields = ('content', 'choice', )


