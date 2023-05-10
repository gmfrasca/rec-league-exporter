from recleagueexporter.exporters.exporter import Exporter
import parsedatetime as pdt
import datetime
import ics

import warnings
from tzlocal import get_localzone
warnings.filterwarnings("ignore", module='parsedatetime')
warnings.filterwarnings("ignore", module='arrow')


class IcsExporter(Exporter):

    def __init__(self):
        super(IcsExporter, self).__init__()
        self.pdt_cal = pdt.Calendar()

    def export(self, sched, output_file):
        ics_cal = ics.Calendar()

        for game in sched.games:
            e = self._convert_to_ics_event(game)
            ics_cal.events.add(e)

        with open(output_file, 'w') as f:
            f.writelines(ics_cal.serialize_iter())

    def _convert_to_ics_event(self, game):
        e = ics.Event()
        e.name = "{} at {}".format(game.awayteam, game.hometeam)
        e.description = "{} at {}".format(game.awayteam, game.hometeam)
        e.begin, parsed = self.pdt_cal.parseDT(datetimeString=game.full_gametime_str, tzinfo=get_localzone())
        e.duration = datetime.timedelta(minutes=75)  # TODO
        return e

        

