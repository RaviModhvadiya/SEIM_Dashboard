from models import db
from models.alert import Alert


def create_alert(log_entry,
                 alert_type,
                 severity,
                 description):

    alert = Alert(

        log_entry_id=log_entry.id,

        alert_type=alert_type,

        severity=severity,

        description=description

    )

    db.session.add(alert)


def detect_threat(log_entry):

    message = str(log_entry.message).lower()

    level = str(log_entry.event_level).lower()

    source = str(log_entry.source).lower()

    if "failed login" in message:

        create_alert(

            log_entry,

            "Failed Login",

            "Medium",

            "Failed login attempt detected."

        )

    if "malware" in message:

        create_alert(

            log_entry,

            "Malware",

            "Critical",

            "Possible malware activity."

        )

    if "blocked connection" in message:

        create_alert(

            log_entry,

            "Firewall Block",

            "High",

            "Firewall blocked suspicious traffic."

        )

    if "powershell" in message:

        create_alert(

            log_entry,

            "PowerShell Execution",

            "High",

            "PowerShell execution detected."

        )

    if level == "critical":

        create_alert(

            log_entry,

            "Critical Event",

            "Critical",

            "Critical event detected."

        )

    if "security" in source:

        create_alert(

            log_entry,

            "Security Event",

            "Low",

            "Security log generated."

        )