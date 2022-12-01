import logging


class Logger:

    log = logging.getLogger()
    log.setLevel(logging.INFO)

    cli_logs = logging.StreamHandler()

    file_logs = logging.FileHandler('tests.log')
    file_logs.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    cli_logs.setFormatter(formatter)
    file_logs.setFormatter(formatter)

    log.addHandler(cli_logs)
    log.addHandler(file_logs)
