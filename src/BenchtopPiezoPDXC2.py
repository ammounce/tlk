from c_types import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (
    MOT_TravelDirection,
    PDXC2_TriggerModes,
    PZ_AmpOutParameters,
    PZ_ControlModeTypes,
    PZ_StageAxisParameters)
from .definitions.structures import (
    PDXC2_ClosedLoopParameters,
    PDXC2_JogParameters,
    PDXC2_OpenLoopMoveParameters,
    PDXC2_TriggerParams,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class BenchtopPiezoPDXC2(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "")

        self.PDXC2_CheckConnection = self.lib.PDXC2_CheckConnection
        self.PDXC2_CheckConnection.restype = c_bool
        self.PDXC2_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_ClearMessageQueue = self.lib.PDXC2_ClearMessageQueue
        self.PDXC2_ClearMessageQueue.restype = c_short
        self.PDXC2_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_Close = self.lib.PDXC2_Close
        self.PDXC2_Close.restype = None
        self.PDXC2_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_Disable = self.lib.PDXC2_Disable
        self.PDXC2_Disable.restype = c_short
        self.PDXC2_Disable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_Disconnect = self.lib.PDXC2_Disconnect
        self.PDXC2_Disconnect.restype = c_short
        self.PDXC2_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_Enable = self.lib.PDXC2_Enable
        self.PDXC2_Enable.restype = c_short
        self.PDXC2_Enable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_EnableLastMsgTimer = self.lib.PDXC2_EnableLastMsgTimer
        self.PDXC2_EnableLastMsgTimer.restype = None
        self.PDXC2_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.PDXC2_GetAbnormalMoveDetectionEnabled = self.lib.PDXC2_GetAbnormalMoveDetectionEnabled
        self.PDXC2_GetAbnormalMoveDetectionEnabled.restype = c_bool
        self.PDXC2_GetAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_GetAmpOutParams = self.lib.PDXC2_GetAmpOutParams
        self.PDXC2_GetAmpOutParams.restype = c_short
        self.PDXC2_GetAmpOutParams.argtypes = [PZ_AmpOutParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_GetClosedLoopParams = self.lib.PDXC2_GetClosedLoopParams
        self.PDXC2_GetClosedLoopParams.restype = c_short
        self.PDXC2_GetClosedLoopParams.argtypes = [PDXC2_ClosedLoopParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_GetClosedLoopTarget = self.lib.PDXC2_GetClosedLoopTarget
        self.PDXC2_GetClosedLoopTarget.restype = c_int
        self.PDXC2_GetClosedLoopTarget.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_GetExternalTriggerConfig = self.lib.PDXC2_GetExternalTriggerConfig
        self.PDXC2_GetExternalTriggerConfig.restype = PDXC2_TriggerModes
        self.PDXC2_GetExternalTriggerConfig.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_GetExternalTriggerParams = self.lib.PDXC2_GetExternalTriggerParams
        self.PDXC2_GetExternalTriggerParams.restype = c_short
        self.PDXC2_GetExternalTriggerParams.argtypes = [PDXC2_TriggerParams, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_GetExternalTriggerTarget = self.lib.PDXC2_GetExternalTriggerTarget
        self.PDXC2_GetExternalTriggerTarget.restype = c_int
        self.PDXC2_GetExternalTriggerTarget.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_GetFirmwareVersion = self.lib.PDXC2_GetFirmwareVersion
        self.PDXC2_GetFirmwareVersion.restype = c_ulong
        self.PDXC2_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_GetHardwareInfo = self.lib.PDXC2_GetHardwareInfo
        self.PDXC2_GetHardwareInfo.restype = c_short
        self.PDXC2_GetHardwareInfo.argtypes = [
            c_ulong,
            c_long,
            POINTER(c_char),
            c_long,
            POINTER(c_char),
            c_long,
            POINTER(c_char),
            c_long,
            c_ulong,
            c_ulong]
        # *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numChannels, *serialNo, *type, sizeOfModelNo, sizeOfNotes

        self.PDXC2_GetHardwareInfoBlock = self.lib.PDXC2_GetHardwareInfoBlock
        self.PDXC2_GetHardwareInfoBlock.restype = c_short
        self.PDXC2_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.PDXC2_GetJogParams = self.lib.PDXC2_GetJogParams
        self.PDXC2_GetJogParams.restype = c_short
        self.PDXC2_GetJogParams.argtypes = [PDXC2_JogParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_GetNextMessage = self.lib.PDXC2_GetNextMessage
        self.PDXC2_GetNextMessage.restype = c_bool
        self.PDXC2_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.PDXC2_GetOpenLoopMoveParams = self.lib.PDXC2_GetOpenLoopMoveParams
        self.PDXC2_GetOpenLoopMoveParams.restype = c_short
        self.PDXC2_GetOpenLoopMoveParams.argtypes = [PDXC2_OpenLoopMoveParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_GetPosition = self.lib.PDXC2_GetPosition
        self.PDXC2_GetPosition.restype = c_short
        self.PDXC2_GetPosition.argtypes = [c_int32, POINTER(c_char)]
        # *position, *serialNo

        self.PDXC2_GetPositionControlMode = self.lib.PDXC2_GetPositionControlMode
        self.PDXC2_GetPositionControlMode.restype = PZ_ControlModeTypes
        self.PDXC2_GetPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_GetSoftwareVersion = self.lib.PDXC2_GetSoftwareVersion
        self.PDXC2_GetSoftwareVersion.restype = c_ulong
        self.PDXC2_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_GetStageAxisParams = self.lib.PDXC2_GetStageAxisParams
        self.PDXC2_GetStageAxisParams.restype = c_short
        self.PDXC2_GetStageAxisParams.argtypes = [PZ_StageAxisParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_GetStatusBits = self.lib.PDXC2_GetStatusBits
        self.PDXC2_GetStatusBits.restype = c_ulong
        self.PDXC2_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_HasLastMsgTimerOverrun = self.lib.PDXC2_HasLastMsgTimerOverrun
        self.PDXC2_HasLastMsgTimerOverrun.restype = c_bool
        self.PDXC2_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_Home = self.lib.PDXC2_Home
        self.PDXC2_Home.restype = c_short
        self.PDXC2_Home.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_Identify = self.lib.PDXC2_Identify
        self.PDXC2_Identify.restype = None
        self.PDXC2_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_LoadNamedSettings = self.lib.PDXC2_LoadNamedSettings
        self.PDXC2_LoadNamedSettings.restype = c_bool
        self.PDXC2_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.PDXC2_LoadSettings = self.lib.PDXC2_LoadSettings
        self.PDXC2_LoadSettings.restype = c_bool
        self.PDXC2_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_MessageQueueSize = self.lib.PDXC2_MessageQueueSize
        self.PDXC2_MessageQueueSize.restype = c_int
        self.PDXC2_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_MoveJog = self.lib.PDXC2_MoveJog
        self.PDXC2_MoveJog.restype = c_short
        self.PDXC2_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, jogDirection

        self.PDXC2_MoveStart = self.lib.PDXC2_MoveStart
        self.PDXC2_MoveStart.restype = c_short
        self.PDXC2_MoveStart.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_MoveStop = self.lib.PDXC2_MoveStop
        self.PDXC2_MoveStop.restype = c_short
        self.PDXC2_MoveStop.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_Open = self.lib.PDXC2_Open
        self.PDXC2_Open.restype = c_short
        self.PDXC2_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_PersistSettings = self.lib.PDXC2_PersistSettings
        self.PDXC2_PersistSettings.restype = c_bool
        self.PDXC2_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_PollingDuration = self.lib.PDXC2_PollingDuration
        self.PDXC2_PollingDuration.restype = c_long
        self.PDXC2_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_PulseParamsAcquireStart = self.lib.PDXC2_PulseParamsAcquireStart
        self.PDXC2_PulseParamsAcquireStart.restype = c_short
        self.PDXC2_PulseParamsAcquireStart.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RegisterMessageCallback = self.lib.PDXC2_RegisterMessageCallback
        self.PDXC2_RegisterMessageCallback.restype = c_short
        self.PDXC2_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.PDXC2_RequestAbnormalMoveDetectionEnabled = self.lib.PDXC2_RequestAbnormalMoveDetectionEnabled
        self.PDXC2_RequestAbnormalMoveDetectionEnabled.restype = c_short
        self.PDXC2_RequestAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestAmpOutParams = self.lib.PDXC2_RequestAmpOutParams
        self.PDXC2_RequestAmpOutParams.restype = c_short
        self.PDXC2_RequestAmpOutParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestClosedLoopParams = self.lib.PDXC2_RequestClosedLoopParams
        self.PDXC2_RequestClosedLoopParams.restype = c_short
        self.PDXC2_RequestClosedLoopParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestClosedLoopTarget = self.lib.PDXC2_RequestClosedLoopTarget
        self.PDXC2_RequestClosedLoopTarget.restype = c_short
        self.PDXC2_RequestClosedLoopTarget.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestExternalTriggerConfig = self.lib.PDXC2_RequestExternalTriggerConfig
        self.PDXC2_RequestExternalTriggerConfig.restype = c_short
        self.PDXC2_RequestExternalTriggerConfig.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestExternalTriggerParams = self.lib.PDXC2_RequestExternalTriggerParams
        self.PDXC2_RequestExternalTriggerParams.restype = c_short
        self.PDXC2_RequestExternalTriggerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestExternalTriggerTarget = self.lib.PDXC2_RequestExternalTriggerTarget
        self.PDXC2_RequestExternalTriggerTarget.restype = c_short
        self.PDXC2_RequestExternalTriggerTarget.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestJogParams = self.lib.PDXC2_RequestJogParams
        self.PDXC2_RequestJogParams.restype = c_short
        self.PDXC2_RequestJogParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestOpenLoopMoveParams = self.lib.PDXC2_RequestOpenLoopMoveParams
        self.PDXC2_RequestOpenLoopMoveParams.restype = c_short
        self.PDXC2_RequestOpenLoopMoveParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestPosition = self.lib.PDXC2_RequestPosition
        self.PDXC2_RequestPosition.restype = c_short
        self.PDXC2_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestPositionControlMode = self.lib.PDXC2_RequestPositionControlMode
        self.PDXC2_RequestPositionControlMode.restype = c_bool
        self.PDXC2_RequestPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestSettings = self.lib.PDXC2_RequestSettings
        self.PDXC2_RequestSettings.restype = c_short
        self.PDXC2_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestStageAxisParams = self.lib.PDXC2_RequestStageAxisParams
        self.PDXC2_RequestStageAxisParams.restype = c_short
        self.PDXC2_RequestStageAxisParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestStatus = self.lib.PDXC2_RequestStatus
        self.PDXC2_RequestStatus.restype = c_short
        self.PDXC2_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_RequestStatusBits = self.lib.PDXC2_RequestStatusBits
        self.PDXC2_RequestStatusBits.restype = c_short
        self.PDXC2_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_ResetParameters = self.lib.PDXC2_ResetParameters
        self.PDXC2_ResetParameters.restype = c_short
        self.PDXC2_ResetParameters.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_SetAbnormalMoveDetectionEnabled = self.lib.PDXC2_SetAbnormalMoveDetectionEnabled
        self.PDXC2_SetAbnormalMoveDetectionEnabled.restype = c_short
        self.PDXC2_SetAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, isEnabled

        self.PDXC2_SetAmpOutParams = self.lib.PDXC2_SetAmpOutParams
        self.PDXC2_SetAmpOutParams.restype = c_short
        self.PDXC2_SetAmpOutParams.argtypes = [PZ_AmpOutParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_SetClosedLoopParams = self.lib.PDXC2_SetClosedLoopParams
        self.PDXC2_SetClosedLoopParams.restype = c_short
        self.PDXC2_SetClosedLoopParams.argtypes = [PDXC2_ClosedLoopParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_SetClosedLoopTarget = self.lib.PDXC2_SetClosedLoopTarget
        self.PDXC2_SetClosedLoopTarget.restype = c_short
        self.PDXC2_SetClosedLoopTarget.argtypes = [POINTER(c_char), c_int]
        # *serialNo, target

        self.PDXC2_SetExternalTriggerConfig = self.lib.PDXC2_SetExternalTriggerConfig
        self.PDXC2_SetExternalTriggerConfig.restype = c_short
        self.PDXC2_SetExternalTriggerConfig.argtypes = [POINTER(c_char), PDXC2_TriggerModes]
        # *serialNo, mode

        self.PDXC2_SetExternalTriggerParams = self.lib.PDXC2_SetExternalTriggerParams
        self.PDXC2_SetExternalTriggerParams.restype = c_short
        self.PDXC2_SetExternalTriggerParams.argtypes = [PDXC2_TriggerParams, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_SetJogParams = self.lib.PDXC2_SetJogParams
        self.PDXC2_SetJogParams.restype = c_short
        self.PDXC2_SetJogParams.argtypes = [PDXC2_JogParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_SetOpenLoopMoveParams = self.lib.PDXC2_SetOpenLoopMoveParams
        self.PDXC2_SetOpenLoopMoveParams.restype = c_short
        self.PDXC2_SetOpenLoopMoveParams.argtypes = [PDXC2_OpenLoopMoveParameters, POINTER(c_char)]
        # *params, *serialNo

        self.PDXC2_SetPositionControlMode = self.lib.PDXC2_SetPositionControlMode
        self.PDXC2_SetPositionControlMode.restype = c_short
        self.PDXC2_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
        # *serialNo, mode

        self.PDXC2_StartPolling = self.lib.PDXC2_StartPolling
        self.PDXC2_StartPolling.restype = c_bool
        self.PDXC2_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.PDXC2_StopPolling = self.lib.PDXC2_StopPolling
        self.PDXC2_StopPolling.restype = None
        self.PDXC2_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PDXC2_TimeSinceLastMsgReceived = self.lib.PDXC2_TimeSinceLastMsgReceived
        self.PDXC2_TimeSinceLastMsgReceived.restype = c_bool
        self.PDXC2_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.PDXC2_WaitForMessage = self.lib.PDXC2_WaitForMessage
        self.PDXC2_WaitForMessage.restype = c_bool
        self.PDXC2_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.TLI_BuildDeviceList = self.lib.TLI_BuildDeviceList
        self.TLI_BuildDeviceList.restype = c_short
        self.TLI_BuildDeviceList.argtypes = [None, None]
        # , void

        self.TLI_GetDeviceInfo = self.lib.TLI_GetDeviceInfo
        self.TLI_GetDeviceInfo.restype = c_short
        self.TLI_GetDeviceInfo.argtypes = [TLI_DeviceInfo, POINTER(c_char), POINTER(c_char)]
        # *info, *serialNo, *serialNumber

        self.TLI_GetDeviceList = self.lib.TLI_GetDeviceList
        self.TLI_GetDeviceList.restype = c_short
        self.TLI_GetDeviceList.argtypes = [SafeArray]
        # **stringsReceiver

        self.TLI_GetDeviceListByType = self.lib.TLI_GetDeviceListByType
        self.TLI_GetDeviceListByType.restype = c_short
        self.TLI_GetDeviceListByType.argtypes = [SafeArray, c_int]
        # **stringsReceiver, typeID

        self.TLI_GetDeviceListByTypeExt = self.lib.TLI_GetDeviceListByTypeExt
        self.TLI_GetDeviceListByTypeExt.restype = c_short
        self.TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char), c_ulong, c_int]
        # *receiveBuffer, sizeOfBuffer, typeID

        self.TLI_GetDeviceListByTypes = self.lib.TLI_GetDeviceListByTypes
        self.TLI_GetDeviceListByTypes.restype = c_short
        self.TLI_GetDeviceListByTypes.argtypes = [SafeArray, c_int, c_int]
        # **stringsReceiver, *typeIDs, length

        self.TLI_GetDeviceListByTypesExt = self.lib.TLI_GetDeviceListByTypesExt
        self.TLI_GetDeviceListByTypesExt.restype = c_short
        self.TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_int, c_int, c_ulong]
        # *receiveBuffer, *typeIDs, length, sizeOfBuffer

        self.TLI_GetDeviceListExt = self.lib.TLI_GetDeviceListExt
        self.TLI_GetDeviceListExt.restype = c_short
        self.TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_ulong]
        # *receiveBuffer, sizeOfBuffer

        self.TLI_GetDeviceListSize = self.lib.TLI_GetDeviceListSize
        self.TLI_GetDeviceListSize.restype = c_short
        self.TLI_GetDeviceListSize.argtypes = [None]
        #

        self.TLI_InitializeSimulations = self.lib.TLI_InitializeSimulations
        self.TLI_InitializeSimulations.restype = None
        self.TLI_InitializeSimulations.argtypes = [None]
        #

        self.TLI_ScanEthernetRange = self.lib.TLI_ScanEthernetRange
        self.TLI_ScanEthernetRange.restype = c_short
        self.TLI_ScanEthernetRange.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(c_char), c_int, c_int, c_ulong]
        # *endIPAddress, *foundAddressesBuffer, *startIPAddress, openTimeout, portNo, sizeOfBuffer
