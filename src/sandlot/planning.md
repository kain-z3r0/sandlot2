# Phases


1. Text loader
2. Line filter
3. Transformer
4. 






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