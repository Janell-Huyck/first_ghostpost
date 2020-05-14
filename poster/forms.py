from django import forms


# class GhostPostForm(forms.Form):
#     is_boast = forms.BooleanField(
#         required=True,
#         label="Boast or Roast?",
#         wiedget=forms.Select(),
#         choices=((True, "Boast"),
#                  (False, "Roast")))
#     title = forms.CharField(max_length=20)
#     text = forms.CharField(max_length=280)


"""
class GhostPost(models.Model):
    is_boast = models.BooleanField()
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)
    magic_string = models.CharField(max_length=6)
"""
