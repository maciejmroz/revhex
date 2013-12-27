import cocos
import math
from game_config import Config
from cocos.actions import FadeIn 

class LinearProgress():
    def __init__(self, initial_value=0.0,velocity_scale=1.0):
        self.initial_value = initial_value
        self.velocity_scale = velocity_scale
        
    def get_value(self,time):
        return self.initial_value+self.velocity_scale*time

class InverseLinearProgress():
    def __init__(self, initial_value=10.0,velocity_scale=-1.0,cap=0.1):
        self.initial_value = initial_value
        self.velocity_scale = velocity_scale
        self.cap = cap
        
    def get_value(self,time):
        divisor = self.initial_value + self.velocity_scale * time
        if divisor <= self.cap:
            divisor = self.cap
        return 1.0/divisor

class Blockade(cocos.layer.Layer):
    def __init__(self, pattern, rotation_controller = LinearProgress(),
                 scaling_controller = LinearProgress()):
        super( Blockade, self ).__init__()
        self.pattern = pattern
        self.collision_mask = []
        self.rotation_controller = rotation_controller
        self.scaling_controller = scaling_controller
        self.lifetime = 0.0
        self.rotation_offset = 0.0
        rotation = 0.0
        for block in pattern:
            if block!=0:
                for i in xrange(block):
                    self.collision_mask.append(True)
                sprite = cocos.sprite.Sprite(Config.BLOCK_SPRITES[block-1])
                sprite.image.anchor_x = 200
                sprite.image.anchor_y = 200
                sprite.rotation = rotation
                sprite.position = Config.WIDTH/2, Config.HEIGHT/2
                sprite.opacity = 0.0
                fadein = FadeIn(1)
                sprite.do(fadein)
                rotation += block*30
                self.add(sprite)
            else:
                rotation += 30
                self.collision_mask.append(False)
        
    def update(self, dt):
        self.lifetime += dt
        self.rotation = self.rotation_offset+self.rotation_controller.get_value(self.lifetime)
        self.scale = self.scaling_controller.get_value(self.lifetime)
        
    def collide(self):
        if self.scale < 1.1:
            return False
        if self.scale > 1.15:
            return False
        rt = math.fmod(180.0-self.rotation,360.0)
        if rt < 0.0:
            rt += 360.0
        sector = int(rt/30.0)
        return self.collision_mask[sector]
