import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import switch
from esphome.const import (
    ENTITY_CATEGORY_CONFIG,
)
from . import MhiAcCtrl, CONF_MHI_AC_CTRL_ID

CONF_ACTIVE_MODE = "active_mode"
CONF_SILENT_OPERATION = "silent_operation"

TYPES = [
    CONF_ACTIVE_MODE,
    CONF_SILENT_OPERATION,
]

MhiActiveMode = cg.global_ns.class_("MhiActiveMode", cg.Component, switch.Switch)
MhiSilentOperation = cg.global_ns.class_("MhiSilentOperation", switch.Switch)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(MhiAcCtrl),
            cv.GenerateID(CONF_MHI_AC_CTRL_ID): cv.use_id(MhiAcCtrl),
            cv.Optional(CONF_ACTIVE_MODE): switch.switch_schema(
                class_=MhiActiveMode,
                entity_category=ENTITY_CATEGORY_CONFIG,
                icon="mdi:connection",
            ),
            cv.Optional(CONF_SILENT_OPERATION): switch.switch_schema(
                class_=MhiSilentOperation,
                icon="mdi:fan-chevron-down",
            ),
        }
    )
)


async def setup_conf(config, key, hub):
    if key in config:
        conf = config[key]
        swi = await switch.new_switch(conf)
        cg.add(getattr(hub, f"set_{key}_switch")(swi))


async def to_code(config):
    paren = await cg.get_variable(config[CONF_MHI_AC_CTRL_ID])
    for key in TYPES:
        await setup_conf(config, key, paren)
