from pathlib import Path
import json

class GameStats:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_status()
        self.score = 0
        
        #最高分
        self.high_score = 0

        path = Path('self.stats.score.json')
        contents = path.read_text()
        self.high_score = json.loads(contents)

    def reset_status(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def save_high_score(self):
        #if self.score > self.high_score:
        path = Path('self.stats.score.json')
        contents = json.dumps(self.high_score)
        print(f"New high score: {self.high_score}")
        print(contents)
        path.write_text(contents)
    