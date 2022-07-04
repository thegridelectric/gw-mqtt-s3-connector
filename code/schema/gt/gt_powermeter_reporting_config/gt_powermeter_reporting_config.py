"""gt.powermeter.reporting.config.100 type"""

from schema.errors import MpSchemaError
from schema.gt.gt_powermeter_reporting_config.gt_powermeter_reporting_config_base import (
    GtPowermeterReportingConfigBase,
)


class GtPowermeterReportingConfig(GtPowermeterReportingConfigBase):
    def check_for_errors(self):
        errors = self.derived_errors() + self.hand_coded_errors()
        if len(errors) > 0:
            raise MpSchemaError(
                f" Errors making making gt.powermeter.reporting.config.100 for {self}: {errors}"
            )

    def hand_coded_errors(self):
        return []
