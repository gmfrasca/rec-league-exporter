from argparse import ArgumentParser
from .recleagueexporter import RecLeagueExporter
import logging
import yaml


def setup_logging(debug=True):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-e", "--export_type", required=True)
    parser.add_argument("-o", "--output_file", required=True)
    parser.add_argument("-i", "--input_config", required=True)
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_args()


def get_sched_config(input_config):
    with open(input_config, 'r') as f:
        data = yaml.safe_load(f)
        return data.get('schedule', {})


def main():
    args = parse_args()
    setup_logging(args.verbose)
    sched_cfg = get_sched_config(args.input_config)
    sched_type=sched_cfg.pop("type")
    rls = RecLeagueExporter(sched_type, sched_cfg)
    rls.export(args.export_type, args.output_file)



if __name__ == '__main__':
    main()

