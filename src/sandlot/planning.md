# Phases


**Player Extractor**
- Returns a dictionary of player metadata
    - Player name, player ID
- Uses regex to find player names



```text
gparser = GameParser(text).parse()

gparser.to_json("out/data.json")
gparser.to_csv("out/data.csv")
gparser.to_sql("sqlite:///db.sqlite3")

gparser.store_players("out/players.json")
gparser.store_teams("out/teams.json")


input_text: "data/game.txt"
outputs:
  json: "out/data.json"
  csv: "out/data.csv"
  sql: "sqlite:///db.sqlite3"
store:
  players: "out/players.json"
  teams: "out/teams.json"

GameParser.from_config("parser.yaml").parse()

```