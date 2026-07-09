import pandas as pd

from models import db
from models.log_entry import LogEntry


def parse_csv(filepath, log_id):

    dataframe = pd.read_csv(filepath)

    for _, row in dataframe.iterrows():

        log = LogEntry(

            log_id=log_id,

            event_time=row.get("Timestamp"),

            event_level=row.get("Level"),

            source=row.get("Source"),

            message=row.get("Message")

        )

        db.session.add(log)

    db.session.commit()

    return len(dataframe)