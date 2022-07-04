"""Makes gt.sh.node.120 type"""
import json
from typing import Optional

from schema.gt.gt_sh_node.gt_sh_node import GtShNode
from schema.errors import MpSchemaError
from schema.enums.actor_class.actor_class_map import (
    ActorClass,
    ActorClassMap,
)
from schema.enums.role.role_map import (
    Role,
    RoleMap,
)


class GtShNode_Maker:
    type_alias = "gt.sh.node.120"

    def __init__(self,
                 actor_class: ActorClass,
                 role: Role,
                 sh_node_id: str,
                 alias: str,
                 component_id: Optional[str],
                 display_name: Optional[str],
                 reporting_sample_period_s: Optional[int]):

        gw_tuple = GtShNode(
            ComponentId=component_id,
            DisplayName=display_name,
            ActorClass=actor_class,
            Role=role,
            ReportingSamplePeriodS=reporting_sample_period_s,
            ShNodeId=sh_node_id,
            Alias=alias,
            #
        )
        gw_tuple.check_for_errors()
        self.tuple = gw_tuple

    @classmethod
    def tuple_to_type(cls, tuple: GtShNode) -> str:
        tuple.check_for_errors()
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtShNode:
        try:
            d = json.loads(t)
        except TypeError:
            raise MpSchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise MpSchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict) -> GtShNode:
        new_d = {}
        for key in d.keys():
            new_d[key] = d[key]
        if "TypeAlias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing TypeAlias")
        if "ComponentId" not in new_d.keys():
            new_d["ComponentId"] = None
        if "DisplayName" not in new_d.keys():
            new_d["DisplayName"] = None
        if "ActorClassGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ActorClassGtEnumSymbol")
        new_d["ActorClass"] = ActorClassMap.gt_to_local(new_d["ActorClassGtEnumSymbol"])
        if "RoleGtEnumSymbol" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing RoleGtEnumSymbol")
        new_d["Role"] = RoleMap.gt_to_local(new_d["RoleGtEnumSymbol"])
        if "ReportingSamplePeriodS" not in new_d.keys():
            new_d["ReportingSamplePeriodS"] = None
        if "ShNodeId" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing ShNodeId")
        if "Alias" not in new_d.keys():
            raise MpSchemaError(f"dict {new_d} missing Alias")

        gw_tuple = GtShNode(
            TypeAlias=new_d["TypeAlias"],
            ComponentId=new_d["ComponentId"],
            DisplayName=new_d["DisplayName"],
            ActorClass=new_d["ActorClass"],
            Role=new_d["Role"],
            ReportingSamplePeriodS=new_d["ReportingSamplePeriodS"],
            ShNodeId=new_d["ShNodeId"],
            Alias=new_d["Alias"],
            #
        )
        gw_tuple.check_for_errors()
        return gw_tuple
