from recleagueexporter.exporters.exporter import Exporter
import parsedatetime as pdt
import csv

EVENT_TYPES = ["GAME", "SCRIMMAGE", "DROP-IN", "PRACTICE", "EVENT"]
GAME_TYPES = ["PRE-SEASON", "REGULAR", "PLAYOFF", "TOURNAMENT"]
CSV_HEADER = ['type', 'game_type', 'title', 'home', 'away', 'date', 'time', 'duration', 'location', 'address', 'notes']


class BenchappCsvExporter(Exporter):

    def __init__(self):
        super(BenchappCsvExporter, self).__init__()

    def export(self, sched, output_file):
        game_list = self._convert_to_list(sched)
        with open(output_file, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
            writer.writerows(list(game_list))
                        
    def _convert_to_list(self, sched):
        cal = pdt.Calendar()
        for game in sched.games:
            date_obj, parse_status = cal.parse(game.date)
            date = "{0}/{1}/{2}".format(date_obj[2], date_obj[1], date_obj[0])
            game_data = {
                    "type": EVENT_TYPES[0],  # TODO
                    "game_type": GAME_TYPES[1],  # TODO
                    "home": game.hometeam,
                    "away": game.awayteam,
                    "date": date,
                    "time": game.time,
                    "duration": "1:15",  # TODO
            }
            yield game_data
