from django.db import models
from django.utils import timezone
from datetime import datetime


class GhostPost(models.Model):
    is_boast = models.BooleanField()
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0, editable=False)
    down_votes = models.IntegerField(default=0, editable=False)
    submission_time = models.DateTimeField(
        auto_now_add=True, editable=False, null=False, blank=False)
    magic_string = models.CharField(max_length=6, editable=False)
    score = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            self.magic_string = "aaaaaa"
        self.score = self.up_votes - self.down_votes
        super(GhostPost, self).save()

    def score(self):
        score = self.up_votes - self.down_votes
        return score
