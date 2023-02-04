from django import forms
class StudentForm(forms.Form):
    name=forms.CharField(max_length=60)
    marks=forms.IntegerField();

class StudentloginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.IntegerField(widget=forms.PasswordInput)
'''
def starts_with_s(value):
    if value[0].lower()!='s':
        raise forms.ValidationError('name should starts with s or S only')
'''
from django.core import validators
class feedbackForm(forms.Form):
    #name=forms.CharField(validators=[starts_with_s])
   # name=forms.CharField(validators=[validators.RegexValidator('[ASGZ].*')])
    #rollno=forms.IntegerField(validators=[validators.RegexValidator('[6-9]\d{5}')])
    #email=forms.EmailField(validators=[validators.EmailValidator])
    #feedback=forms.CharField(widget=forms.Textarea)
    #feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MinLengthValidator(10),validators.MaxLengthValidator(30)])

    name = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(widget=forms.PasswordInput)
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea);

    def clean(self):
        print('total form validation...is getting done')
        total_cleaned_data=super().clean()

        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['repassword']
        if pwd!=rpwd:
            raise forms.ValidationError('password not matching')
        if len(pwd)<5 or len(pwd)>20:
            raise forms.ValidationError('password must be in limit')
        if len(rpwd)<5 or len(rpwd)>20:
            raise forms.ValidationError('repassword must be in limit')
        inputname=total_cleaned_data['name']
        if inputname[0].lower()!='s':
            raise forms.ValidationError('Name should starts with s')

        inputroll=total_cleaned_data['rollno']
        if inputroll<=0:
            raise forms.ValidationError('roll no should not be 0')
        inputfeeback=total_cleaned_data['feedback'];
        if len(inputfeeback)<10 or len(inputfeeback)>30:
            raise forms.ValidationError('feedback should be in limit')









''' def clean_name(self):
        print('validating name-field....')
        inputname=self.cleaned_data['name']
        if len(inputname)<5:
            raise forms.ValidationError('min.no of chars should be 5...')
        return inputname
    def clean_rollno(self):
        rollno=self.cleaned_data['rollno']
        if (rollno)==0:
            raise forms.ValidationError('rollno cannot be empty')
        return rollno
    def clean_email(self):
        email=self.cleaned_data['email']
        if len(email)<8:
            raise forms.ValidationError('Enter valid email')
        return email
    def clean_feedback(self):
        feedback=self.cleaned_data['feedback']
        if len(feedback)<6:
            raise forms.ValidationError('Enter some texts')
        return feedback  '''

