import logging


class Exporter():

    def export(self, sched, output_file):
        for game in sched.games:
            logging.info("Game: " + str(game))
