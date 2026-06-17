from django.db import models

class Notes(models.Model):
    class NoteType(models.TextChoices):
        GENERAL = 'general', 'General'
        MEETING = 'meeting', 'Meeting'
        CALL = 'call', 'Call'
        EMAIL = 'email', 'Email'
        
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='notes')
    deal = models.ForeignKey('deals.Deal', on_delete=models.CASCADE, related_name='notes', null=True, blank=True)

    note_type = models.CharField(max_length=20, choices=NoteType.choices, default=NoteType.GENERAL)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.note_type} - {self.client}"
