from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        fields = ('title', 'description', 'preview', 'category', 'price')

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title').lower()
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f"Нельзя использовать слово '{word}' в названии продукта.")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description').lower()
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError(f"Нельзя использовать слово '{word}' в описании продукта.")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_number', 'version_title', 'is_active')