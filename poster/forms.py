from django import forms


class GhostPostForm(forms.Form):
    CHOICES = ((True, 'Boast'), (False, 'Roast'))
    is_boast = forms.ChoiceField(
        label='Boast or Roast?',
        widget=forms.RadioSelect,
        initial=True,
        choices=CHOICES)
    title = forms.CharField(max_length=20)
    text = forms.CharField(max_length=280)


class ToggleViewForm(forms.Form):
    VIEW_CHOICES = (('time', 'Sort by Time'), ('score', 'Sort by Score'))
    view = forms.ChoiceField(initial='time', choices=VIEW_CHOICES)


"""
class GhostPost(models.Model):
    is_boast = models.BooleanField()
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)
"""
