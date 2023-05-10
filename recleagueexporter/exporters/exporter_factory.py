from recleagueexporter.exporters.benchapp_csv_exporter import BenchappCsvExporter
from recleagueexporter.exporters.ics_exporter import IcsExporter
from recleagueexporter.exporters.exporter import Exporter


class ExporterFactory(object):

    def create(exporter_type, **kwargs):
        if exporter_type == 'csv':
            return BenchappCsvExporter(**kwargs)
        elif exporter_type == 'ics':
            return IcsExporter(**kwargs)
        elif exporter_type == 'debug':
            return Exporter(**kwargs)
        else:
            raise ValueError("Exporter type '{0}' not found"
                             .format(exporter_type))

    create = staticmethod(create)
