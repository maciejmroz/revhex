#defaults write com.apple.versioner.python Prefer-32-Bit -bool yes

import cocos
from hud import HUDLayer
from logic import ControlLayer
from background import BackgroundLayer
from game_config import Config
    
if __name__ == "__main__":
    cocos.director.director.init(width = Config.WIDTH,
                                 height = Config.HEIGHT)
    hud = HUDLayer()
    control_layer = ControlLayer(hud)
    background = BackgroundLayer()
    main_scene = cocos.scene.Scene (background, control_layer, hud)
    cocos.director.director.run (main_scene)
