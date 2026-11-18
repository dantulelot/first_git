from .species import Species

class NekoWall(Species):
    def image_select(self, form: str, past_time: int, present_time: int) -> str:
        super().image_select(form, past_time, present_time)
        return self.imgs