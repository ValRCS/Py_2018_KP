import pq.gui as gui


def parse_args():
    return 0


def main():
    if parse_args() != 0:
        return 1

    return gui.run()
