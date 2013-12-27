import cocos
from game_config import Config

class HUDLayer(cocos.layer.Layer):
    def __init__(self):
        super( HUDLayer, self ).__init__()
        sprite = cocos.sprite.Sprite(Config.SHIP_IMAGE)
        sprite.image_anchor_x = 64
        sprite.image_anchor_y = 0
        sprite.scale = 0.5
        sprite.position = Config.WIDTH/2, 0
        self.add(sprite)        
        
        self.score = cocos.text.Label("SCORE: 0",
                                      font_name='Arial',
                                      font_size=32,
                                      anchor_x='left', anchor_y='top',
                                      color = (192,255,0,255))
        self.score.position = 10, Config.HEIGHT-10
        self.add(self.score)
        
        sprite = cocos.sprite.Sprite(Config.END_IMAGE)
        sprite.image_anchor_x = sprite.image.width/2
        sprite.image_anchor_y = sprite.image.height/2
        sprite.position = Config.WIDTH/2, Config.HEIGHT/2
        self.end_sprite = sprite
        self.add(self.end_sprite)
        
#        self.end_msg = self.create_post_game_label("You will be remembered")
#        self.end_msg.position = Config.WIDTH/2, Config.HEIGHT/2+40
#        self.add(self.end_msg)

#        self.restart_msg = self.create_post_game_label("Press SPACE to restart")
#        self.restart_msg.position = Config.WIDTH/2, Config.HEIGHT/2-40
#        self.add(self.restart_msg)
        
        self.set_post_game_info_visible(False)
        
    def create_post_game_label(self,text):
        return cocos.text.Label(text,
                                font_name='Times New Roman',
                                font_size=48,
                                anchor_x='center', anchor_y='center',
                                color = (255,0,0,255),
                                bold = True)
        
    def update_score(self,score):
        self.score.element.text = "SCORE: %d" % score
        
    def set_post_game_info_visible(self, visible):
        self.end_sprite.visible = visible
#        self.end_msg.visible = visible
#        self.restart_msg.visible = visible
        
    def stop_game(self):
        self.set_post_game_info_visible(True)
        
    def start_game(self):
        self.set_post_game_info_visible(False)
