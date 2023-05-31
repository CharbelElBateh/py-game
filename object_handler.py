# Imports
from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'ressources/sprites/npc'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_npc = self.add_npc
        self.npc_positions = {}

        # Soldiers in room 1
        add_npc(SoldierNPC(game, pos=(18, 1.5)))
        add_npc(SoldierNPC(game, pos=(20, 1.5)))
        add_npc(SoldierNPC(game, pos=(22, 1.5)))
        add_npc(SoldierNPC(game, pos=(18, 6.5)))
        add_npc(SoldierNPC(game, pos=(20, 6.5)))
        add_npc(SoldierNPC(game, pos=(22, 6.5)))

        # Soldiers and Caco Demons in room 2
        add_npc(SoldierNPC(game, pos=(12, 13)))
        add_npc(SoldierNPC(game, pos=(12, 15)))
        add_npc(SoldierNPC(game, pos=(12, 17)))
        add_npc(SoldierNPC(game, pos=(14, 13)))
        add_npc(SoldierNPC(game, pos=(14, 17)))
        add_npc(CacoDemon(game, pos=(10, 13)))
        add_npc(CacoDemon(game, pos=(10, 15)))
        add_npc(CacoDemon(game, pos=(10, 17)))

        # Cyber and Caco Demons in room 3
        add_npc(CacoDemon(game, pos=(2.5, 24)))
        add_npc(CacoDemon(game, pos=(4.5, 24)))
        add_npc(CacoDemon(game, pos=(6.5, 24)))
        add_npc(CyberDemon(game, pos=(2.5, 26)))
        add_npc(CyberDemon(game, pos=(6.5, 26)))

        # Bosses in room 4
        add_npc(CyberBoss(game, pos=(22, 27)))
        add_npc(CacoBoss(game, pos=(22, 25)))
        add_npc(SoldierBoss(game, pos=(22, 29)))
        

    # Function that checks if the player has won
    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    # Put the npcs on the map
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)