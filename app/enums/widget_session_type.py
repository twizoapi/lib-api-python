from enum import Enum, unique


@unique
class WidgetSessionType(Enum):
    """
        Different widgetSession types.
    """
    RECIPIENT = 0
    BACKUPCODE = 1
    BOTH = 2
