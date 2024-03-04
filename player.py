import json
from datetime import datetime



class Player:
    def __init__(self, first_name, last_name, date_of_birth , id):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth 
        self.id = id
        

class ChessTournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, current_round=1, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.description = description
        self.rounds = []
        self.registered_players = []

    def add_round(self, round_name):
        round_instance = TournamentRound(round_name)
        self.rounds.append(round_instance)

    def register_player(self, player):
        self.registered_players.append(player)


class TournamentRound:
    def __init__(self, name):
        self.name = name
        self.start_datetime = None
        self.end_datetime = None
        self.matches = []

    def start_round(self):
        self.start_datetime = datetime.now()

    def end_round(self):
        self.end_datetime = datetime.now()

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)

class Match:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.scores = {player1: 0, player2: 0}

    def set_winner(self, winner):
        loser = next(player for player in self.players if player != winner)
        self.scores[winner] = 1
        self.scores[loser] = 0

    def set_draw(self):
        for player in self.players:
            self.scores[player] = 0.5


# Exemple d'utilisation
player1 = Player("Doe", "John", "1990-01-01")
player2 = Player("Smith", "Alice", "1992-05-15")

tournament = ChessTournament("Chess Masters", "New York", "2024-02-17", "2024-02-25")
tournament.add_round("Round 1")
tournament.register_player(player1)
tournament.register_player(player2)

round1 = tournament.rounds[0]
round1.start_round()
round1.add_match(player1, player2)
match = round1.matches[0]
match.set_winner(player1)
round1.end_round()            

# Serialisation en JSON
def serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj.__dict__

tournament_data = json.dumps(tournament, default=serialize, indent=4)
print(tournament_data)