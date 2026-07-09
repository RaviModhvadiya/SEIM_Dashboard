import pandas as pd

from models import db

from models.log_entry import LogEntry

from services.threat_detector import detect_threat


def parse_csv(filepath, log_id):

    dataframe = pd.read_csv(filepath)

    total_rows = 0

    for _, row in dataframe.iterrows():

        log = LogEntry(

            log_id=log_id,

            event_time=row.get("Timestamp"),

            event_level=row.get("Level"),

            source=row.get("Source"),

            message=row.get("Message")

        )

        db.session.add(log)

        db.session.flush()

        detect_threat(log)

        total_rows += 1

    db.session.commit()

    return total_rows