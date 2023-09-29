from django import forms
from catalog.models import Product, Version
from config import settings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'preview', 'category', 'price')

    def clean_title(self):
        title = self.cleaned_data.get('title').lower()
        if title in settings.FORBIDDEN_WORDS:
            raise forms.ValidationError(f"Нельзя использовать запрещенные слова в названии продукта.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description').lower()
        if description in settings.FORBIDDEN_WORDS:
            raise forms.ValidationError(f"Нельзя использовать  запрещенные слова в описании продукта.")
        return description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_number', 'version_title', 'is_active')

    # def clean(self):
    #     cleaned_data = super(VersionForm, self).clean()
    #     #self.validate_unique()
    #     if not cleaned_data.is_valid():
    #         raise forms.ValidationError(f"Может быть только одна активная версия продукта")
    #     return cleaned_data
