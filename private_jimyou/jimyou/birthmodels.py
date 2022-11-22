from jp_birthday.models import BirthdayModel

class ModelsTest(BirthdayModel):
    class Meta:
        app_label = 'jp_birthday'
        ordering = ('pk',)