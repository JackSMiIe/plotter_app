from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'phone_model', 'service', 'comment']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (___) ___-__-__'
            }),
            'phone_model': forms.Select(attrs={
                'class': 'form-select'
            }),
            'service': forms.Select(attrs={
                'class': 'form-select'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Дополнительные комментарии'
            }),
        }

    # Дополнительная валидация телефона
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone:
            digits = [c for c in phone if c.isdigit()]
            if len(digits) != 11:
                raise forms.ValidationError("Введите корректный номер телефона в формате +7 (XXX) XXX-XX-XX")
        return phone
