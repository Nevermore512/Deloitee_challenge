# from django import forms
from django.forms import ModelForm
from .models import sheet
from django.forms import widgets as Fwidgets

class FileForm(ModelForm):
    class Meta:
        model = sheet
        fields = '__all__'
        labels = {
            'name': '公司名',
            'balance_sheet': '资产负债表',
            'income': '利润表',
            'cash_flow': '现金流量表'
        }
        widgets = {
            'name': Fwidgets.Input(attrs={'class': 'c1'}),
            'balance_sheet': Fwidgets.FileInput(attrs={'class': 'wide_boxes2'}),
            'income': Fwidgets.FileInput(attrs={'class': 'wide_boxes3'}),
            'cash_flow': Fwidgets.FileInput(attrs={'class': 'wide_boxes4'}),
        }

