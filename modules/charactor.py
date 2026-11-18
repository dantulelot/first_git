from unit.species import Species

class ImgOutput:
    def imgOutput(self):
        return self.img

class Charactor(ImgOutput):
    def __init__(self, id: int, species: Species, hp: int, attack: int, defense: int, speed: int, territory: list[int], range: list[int], knockback: int):
        """定数"""
        self.id = id
        self.species = species # 対応するキャラの挙動インスタンス
        self.index = [0, 0] # 座標,上下はノックバック等に利用
        self.img = None # 画像
        self.hp = hp
        self.ap = attack
        self.bp = defense
        self.sp = speed
        self.territory = territory # 感知範囲(リスト)
        self.range = range # 射程
        """変数"""
        self.knockback = knockback # 残りのノックバック回数
        self.attackale = True # 攻撃可能かどうか
        self.form = "normal" # 状態：待機/移動/攻撃中/攻撃/攻撃後/ノックバック/衝撃波/昇天
        self.buff = [] # バフ/デバフ
        self.start_time = None # 起点時刻

    def update(self, present_time: int, territories: list[int]):
        # 画像の更新
        self.img = self.species.image_select(self.form, self.start_time, present_time)
        # 攻撃するかどうかの判定
        for target in territories:
            if max(self.territory[0], target[0]) <= min(self.territory[1], target[1]):
                self.form = "attack"
                break # 一つでも引っ掛かれば他の判定は必要ないため

    def update_time(self, new_time):
        self.start_time = new_time

class friend(Charactor):
    def __init__(self, id: int, species: Species, hp: int, attack: int, defense: int, speed: int, territory: list[int], range: list[int], knockback: int):
        super().__init__(id, species, hp, attack, defense, speed, territory, range, knockback)

class enemy(Charactor):
    def __init__(self, id: int, species: Species, hp: int, attack: int, defense: int, speed: int, territory: list[int], range: list[int], reward: int, knockback: int):
        super().__init__(id, species, hp, attack, defense, speed, territory, range, knockback)
        self.reward = reward # 獲得賞金

class Attack(ImgOutput):
    """
    攻撃クラス:攻撃という現象の属性を持つ
    """
    def __init__(self, range: list[int, int], damege: int, buff: list[str]):
        self.img = None # 画像
        self.range = range # 攻撃範囲
        self.damege = damege # ダメージ
        self.buff = [] # バフ/デバフ