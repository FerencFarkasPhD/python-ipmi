import constants
from . import register_message_class
from . import Message
from . import UnsignedInt
from . import UnsignedIntMask
from . import Timestamp
from . import Bitfield
from . import CompletionCode
from . import Conditional
from . import Optional
from . import RemainingBytes
from pyipmi.utils import ByteBuffer
from pyipmi.errors import DecodingError, EncodingError
from pyipmi.msgs.picmg import PicmgIdentifier, PICMG_IDENTIFIER

@register_message_class
class GetTargetUpgradeCapabilitiesReq(Message):
    __cmdid__ = constants.CMDID_HPM_GET_TARGET_UPGRADE_CAPABILITIES
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0
    __fields__ = (
            PicmgIdentifier(),
    )


@register_message_class
class GetTargetUpgradeCapabilitiesRsp(Message):
    __cmdid__ = constants.CMDID_HPM_GET_TARGET_UPGRADE_CAPABILITIES
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0
    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
            UnsignedInt('hpm_1_version', 1),
            Bitfield('capabilities', 1,
                Bitfield.Bit('firmware_upgrade_undesirable', 1),
                Bitfield.Bit('automatic_rollback_overriden', 1),
                Bitfield.Bit('ipmc_degraded_during_upgrade', 1),
                Bitfield.Bit('deferred_activation', 1),
                Bitfield.Bit('services_affected_by_upgrade', 1),
                Bitfield.Bit('manual_rollback', 1),
                Bitfield.Bit('automatic_rollback', 1),
                Bitfield.Bit('selftest', 1),
            ),
            Bitfield('timeout', 4,
                Bitfield.Bit('upgrade', 8),
                Bitfield.Bit('selftest', 8),
                Bitfield.Bit('rollback', 8),
                Bitfield.Bit('inaccessibility', 8),
            ),
            UnsignedInt('component_present', 1),
    )


@register_message_class
class GetComponentPropertiesReq(Message):
    __cmdid__ = constants.CMDID_HPM_GET_COMPONENT_PROPERTIES
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0
    __fields__ = (
            PicmgIdentifier(),
            UnsignedInt('id', 1),
            UnsignedInt('selector', 1),
    )


@register_message_class
class GetComponentPropertiesRsp(Message):
    __cmdid__ = constants.CMDID_HPM_GET_COMPONENT_PROPERTIES
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0
    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
            RemainingBytes('data'),
    )


@register_message_class
class AbortFirmwareUpgradeReq(Message):
    __cmdid__ = constants.CMDID_HPM_ABORT_FIRMWARE_UPGRADE
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0
    __fields__ = (
            PicmgIdentifier(),
    )


@register_message_class
class AbortFirmwareUpgradeRsp(Message):
    __cmdid__ = constants.CMDID_HPM_ABORT_FIRMWARE_UPGRADE
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0
    __fields__ = (
            PicmgIdentifier(),
    )
    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
    )


@register_message_class
class InitiateUpgradeActionReq(Message):
    __cmdid__ = constants.CMDID_HPM_INITIATE_UPGRADE_ACTION
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0
    __fields__ = (
            PicmgIdentifier(),
            UnsignedInt('components', 1),
            UnsignedInt('action', 1),
    )


@register_message_class
class InitiateUpgradeActionRsp(Message):
    __cmdid__ = constants.CMDID_HPM_INITIATE_UPGRADE_ACTION
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0
    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
    )


@register_message_class
class UploadFirmwareBlockReq(Message):
    __cmdid__ = constants.CMDID_HPM_UPLOAD_FIRMWARE_BLOCK
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0
    __fields__ = (
            PicmgIdentifier(),
            RemainingBytes('data'),
    )


@register_message_class
class UploadFirmwareBlockRsp(Message):
    __cmdid__ = constants.CMDID_HPM_UPLOAD_FIRMWARE_BLOCK
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0
    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
            Optional(UnsignedInt('section_offset', 4)),
            Optional(UnsignedInt('section_length', 4)),
    )


@register_message_class
class FinishFirmwareUploadReq(Message):
    __cmdid__ = constants.CMDID_HPM_FINISH_FIRMWARE_UPLOAD
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0

    __fields__ = (
            PicmgIdentifier(),
            UnsignedInt('component_id', 1),
            UnsignedInt('image_length', 4),
    )


@register_message_class
class FinishFirmwareUploadRsp(Message):
    __cmdid__ = constants.CMDID_HPM_FINISH_FIRMWARE_UPLOAD
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0

    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
    )


@register_message_class
class GetUpgradeStatusReq(Message):
    __cmdid__ = constants.CMDID_HPM_GET_UPGRADE_STATUS
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0

    __fields__ = (
            PicmgIdentifier(),
    )


@register_message_class
class GetUpgradeStatusRsp(Message):
    __cmdid__ = constants.CMDID_HPM_GET_UPGRADE_STATUS
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0
    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
            UnsignedInt('command_in_progress', 1),
            Optional(UnsignedInt('completion_estimate', 1)),
    )


@register_message_class
class ActivateFirmwareReq(Message):
    __cmdid__ = constants.CMDID_HPM_ACTIVATE_FIRMWARE
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0
    __fields__ = (
            PicmgIdentifier(),
            Optional(UnsignedInt('rollback_override_policy', 1)),
    )


@register_message_class
class ActivateFirmwareRsp(Message):
    __cmdid__ = constants.CMDID_HPM_ACTIVATE_FIRMWARE
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0

    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
    )


@register_message_class
class QuerySelftestResultsReq(Message):
    __cmdid__ = constants.CMDID_HPM_QUERY_SELFTEST_RESULTS
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0

    __fields__ = (
            PicmgIdentifier(),
    )


@register_message_class
class QuerySelftestResultsRsp(Message):
    __cmdid__ = constants.CMDID_HPM_QUERY_SELFTEST_RESULTS
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0

    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
            UnsignedInt('selftest_result_1', 1),
            UnsignedInt('selftest_result_2', 1),
    )


@register_message_class
class QueryRollbackStatusReq(Message):
    __cmdid__ = constants.CMDID_HPM_QUERY_ROLLBACK_STATUS
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0

    __fields__ = (
            PicmgIdentifier(),
    )


@register_message_class
class QueryRollbackStatusRsp(Message):
    __cmdid__ = constants.CMDID_HPM_QUERY_ROLLBACK_STATUS
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0
    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
            UnsignedInt('rollback_status', 1),
            Optional(UnsignedInt('completion_estimate', 1)),
    )


@register_message_class
class InitiateManualRollbackReq(Message):
    __cmdid__ = constants.CMDID_HPM_INITIATE_MANUAL_ROLLBACK
    __netfn__ = constants.NETFN_GROUP_EXTENSION
    __default_lun__ = 0

    __fields__ = (
            PicmgIdentifier(),
    )


@register_message_class
class InitiateManualRollbackRsp(Message):
    __cmdid__ = constants.CMDID_HPM_INITIATE_MANUAL_ROLLBACK
    __netfn__ = constants.NETFN_GROUP_EXTENSION | 1
    __default_lun__ = 0

    __fields__ = (
            CompletionCode(),
            PicmgIdentifier(),
    )
