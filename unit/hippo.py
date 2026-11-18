from .species import Species

class Hippo(Species):
    def image_select(self, form, past_time, present_time):
        super().image_select(form, past_time, present_time)
        return self.imgs