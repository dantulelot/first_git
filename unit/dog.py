from .species import Species

class Dog(Species):
    def image_select(self, form, past_time, present_time):
        super().image_select(form, past_time, present_time)
        return self.imgs