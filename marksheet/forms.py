from django import forms

class mahajan(forms.Form):
    n1=forms.IntegerField(label="enter the first marks", max_value="200",min_value="1")
    n2=forms.IntegerField(label="enter the second marks")
    n3=forms.IntegerField(label="enter the third marks")
    n4=forms.IntegerField(label="enter the fourth marks")
    n5=forms.IntegerField(label="enter the fifth marks")

