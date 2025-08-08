from argparse import ArgumentParser
from .recleagueexporter import RecLeagueExporter
import logging
import yaml
import os

def setup_logging(debug=True):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input_config", required=True)
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser.parse_args()


def load_config(input_config):
    with open(input_config, 'r') as f:
        return yaml.safe_load(f)


def get_schedules(data):
        return data.get('schedules', [])


def get_output_file(output_dir, season, team_name, export_type):
    return os.path.join(output_dir, season, f"{team_name}.{season}.{export_type}")


def create_dir_if_not_exists(output_file):
    dir_name = os.path.dirname(output_file)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def main():
    args = parse_args()
    setup_logging(args.verbose)
    full_config = load_config(args.input_config)

    output_dir = full_config.pop("output_dir")
    season = full_config.pop("season")
    for config in get_schedules(full_config):
        team_name = config.pop("name")
        export_type = config.pop("export_type")
        sched_cfg = config.pop("schedule")
        sched_type=sched_cfg.pop("type")
        logging.info("")
        logging.info(f"==== STARTING EXPORT: {team_name} ====")
               
        output_file = get_output_file(output_dir, season, team_name, export_type)
        create_dir_if_not_exists(output_file)

        logging.info(f"Exporting {team_name}'s schedule to {output_file} with export type {export_type}")
        rls = RecLeagueExporter(sched_type, sched_cfg)
        rls.export(export_type, output_file)
        logging.info(f"==== EXPORT COMPLETE: {team_name} ====")


if __name__ == '__main__':
    main()

