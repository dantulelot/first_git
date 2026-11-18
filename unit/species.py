class Species:
    def __init__(self, imgs: list[str], money: int, interval: int):
        self.imgs = imgs # 画像のURLリスト
        self.money = money # 賃金
        self.interval = interval # 生産間隔
        self.pause = 0 # 生産休止期間

    def image_select(self, form: str, past_time: int, present_time: int) -> str:
        """
        指定された情報に基づき表示する画像を返す
        """ 
        if form == "knockback":
            return self.imgs[2]

        elif form == "stay":
            return self.imgs[0]