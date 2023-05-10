from recleagueparser.schedules import ScheduleFactory
from recleagueexporter.exporters import ExporterFactory

class RecLeagueExporter(object):

    def __init__(self, schedule_type, schedule_cfg):
        self.sched = ScheduleFactory.create(schedule_type, **schedule_cfg)

    def export(self, export_type, output_file):
        exporter = ExporterFactory.create(export_type)
        exporter.export(self.sched, output_file)
