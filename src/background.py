import cocos
from game_config import Config

class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super( BackgroundLayer, self ).__init__()
        sprite = cocos.sprite.Sprite(Config.BACKGROUND_IMAGE)
        sprite.image_anchor_x = 0
        sprite.image_anchor_y = 0
        sprite.position = 0, 0
        sprite.scale = 1.0
        self.add(sprite)