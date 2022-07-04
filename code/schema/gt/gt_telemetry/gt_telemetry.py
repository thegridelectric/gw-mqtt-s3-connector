"""gt.telemetry.110 type"""

from schema.errors import MpSchemaError
from schema.gt.gt_telemetry.gt_telemetry_base import (
    GtTelemetryBase,
)


class GtTelemetry(GtTelemetryBase):
    def check_for_errors(self):
        errors = self.derived_errors() + self.hand_coded_errors()
        if len(errors) > 0:
            raise MpSchemaError(f" Errors making making gt.telemetry.110 for {self}: {errors}")

    def hand_coded_errors(self):
        return []
