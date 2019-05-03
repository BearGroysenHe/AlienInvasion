import pygame
from pygame.sprite import Group
from settings import Settings
from alien import Alien
from ship import Ship
from button import Button
from scoreboard import Scoreboard
from game_stats import GameStats
import game_functions as gf

pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
alien = Alien(ai_settings, screen)
pygame.display.set_caption("Alien Invasion")
play_button = Button(ai_settings,screen,"play")
ship = Ship(ai_settings, screen)
bullets = Group()
aliens = Group()
stats= GameStats(ai_settings)
sb = Scoreboard(ai_settings,screen,stats)
screen.fill(ai_settings.bg_color)
play_button.draw_button()
pygame.display.flip()
while True:
	gf.check_events(ai_settings, screen, stats, sb,play_button,ship, aliens,bullets)
	if stats.game_active:
		ship.update()
		gf.update_bullets(ai_settings, screen, stats,sb,ship, aliens,bullets)
		gf.update_aliens(ai_settings,screen,stats, sb, ship, aliens,bullets)
		gf.update_screen(ai_settings, screen, stats,sb,ship, aliens, bullets,play_button)
