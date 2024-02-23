from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
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


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "MotionControl.Benchtop.Piezo.DLL")

PDXC2_CheckConnection = lib.PDXC2_CheckConnection
PDXC2_CheckConnection.restype = c_bool
PDXC2_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_ClearMessageQueue = lib.PDXC2_ClearMessageQueue
PDXC2_ClearMessageQueue.restype = c_short
PDXC2_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_Close = lib.PDXC2_Close
PDXC2_Close.restype = c_void_p
PDXC2_Close.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_Disable = lib.PDXC2_Disable
PDXC2_Disable.restype = c_short
PDXC2_Disable.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_Disconnect = lib.PDXC2_Disconnect
PDXC2_Disconnect.restype = c_short
PDXC2_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_Enable = lib.PDXC2_Enable
PDXC2_Enable.restype = c_short
PDXC2_Enable.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_EnableLastMsgTimer = lib.PDXC2_EnableLastMsgTimer
PDXC2_EnableLastMsgTimer.restype = c_void_p
PDXC2_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

PDXC2_GetAbnormalMoveDetectionEnabled = lib.PDXC2_GetAbnormalMoveDetectionEnabled
PDXC2_GetAbnormalMoveDetectionEnabled.restype = c_bool
PDXC2_GetAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_GetAmpOutParams = lib.PDXC2_GetAmpOutParams
PDXC2_GetAmpOutParams.restype = c_short
PDXC2_GetAmpOutParams.argtypes = [PZ_AmpOutParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_GetClosedLoopParams = lib.PDXC2_GetClosedLoopParams
PDXC2_GetClosedLoopParams.restype = c_short
PDXC2_GetClosedLoopParams.argtypes = [PDXC2_ClosedLoopParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_GetClosedLoopTarget = lib.PDXC2_GetClosedLoopTarget
PDXC2_GetClosedLoopTarget.restype = c_int
PDXC2_GetClosedLoopTarget.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_GetExternalTriggerConfig = lib.PDXC2_GetExternalTriggerConfig
PDXC2_GetExternalTriggerConfig.restype = PDXC2_TriggerModes
PDXC2_GetExternalTriggerConfig.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_GetExternalTriggerParams = lib.PDXC2_GetExternalTriggerParams
PDXC2_GetExternalTriggerParams.restype = c_short
PDXC2_GetExternalTriggerParams.argtypes = [PDXC2_TriggerParams, POINTER(c_char)]
# *params, *serialNo

PDXC2_GetExternalTriggerTarget = lib.PDXC2_GetExternalTriggerTarget
PDXC2_GetExternalTriggerTarget.restype = c_int
PDXC2_GetExternalTriggerTarget.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_GetFirmwareVersion = lib.PDXC2_GetFirmwareVersion
PDXC2_GetFirmwareVersion.restype = c_ulong
PDXC2_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_GetHardwareInfo = lib.PDXC2_GetHardwareInfo
PDXC2_GetHardwareInfo.restype = c_short
PDXC2_GetHardwareInfo.argtypes = [
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

PDXC2_GetHardwareInfoBlock = lib.PDXC2_GetHardwareInfoBlock
PDXC2_GetHardwareInfoBlock.restype = c_short
PDXC2_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

PDXC2_GetJogParams = lib.PDXC2_GetJogParams
PDXC2_GetJogParams.restype = c_short
PDXC2_GetJogParams.argtypes = [PDXC2_JogParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_GetNextMessage = lib.PDXC2_GetNextMessage
PDXC2_GetNextMessage.restype = c_bool
PDXC2_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

PDXC2_GetOpenLoopMoveParams = lib.PDXC2_GetOpenLoopMoveParams
PDXC2_GetOpenLoopMoveParams.restype = c_short
PDXC2_GetOpenLoopMoveParams.argtypes = [PDXC2_OpenLoopMoveParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_GetPosition = lib.PDXC2_GetPosition
PDXC2_GetPosition.restype = c_short
PDXC2_GetPosition.argtypes = [c_int32, POINTER(c_char)]
# *position, *serialNo

PDXC2_GetPositionControlMode = lib.PDXC2_GetPositionControlMode
PDXC2_GetPositionControlMode.restype = PZ_ControlModeTypes
PDXC2_GetPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_GetSoftwareVersion = lib.PDXC2_GetSoftwareVersion
PDXC2_GetSoftwareVersion.restype = c_ulong
PDXC2_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_GetStageAxisParams = lib.PDXC2_GetStageAxisParams
PDXC2_GetStageAxisParams.restype = c_short
PDXC2_GetStageAxisParams.argtypes = [PZ_StageAxisParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_GetStatusBits = lib.PDXC2_GetStatusBits
PDXC2_GetStatusBits.restype = c_ulong
PDXC2_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_HasLastMsgTimerOverrun = lib.PDXC2_HasLastMsgTimerOverrun
PDXC2_HasLastMsgTimerOverrun.restype = c_bool
PDXC2_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_Home = lib.PDXC2_Home
PDXC2_Home.restype = c_short
PDXC2_Home.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_Identify = lib.PDXC2_Identify
PDXC2_Identify.restype = c_void_p
PDXC2_Identify.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_LoadNamedSettings = lib.PDXC2_LoadNamedSettings
PDXC2_LoadNamedSettings.restype = c_bool
PDXC2_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

PDXC2_LoadSettings = lib.PDXC2_LoadSettings
PDXC2_LoadSettings.restype = c_bool
PDXC2_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_MessageQueueSize = lib.PDXC2_MessageQueueSize
PDXC2_MessageQueueSize.restype = c_int
PDXC2_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_MoveJog = lib.PDXC2_MoveJog
PDXC2_MoveJog.restype = c_short
PDXC2_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, jogDirection

PDXC2_MoveStart = lib.PDXC2_MoveStart
PDXC2_MoveStart.restype = c_short
PDXC2_MoveStart.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_MoveStop = lib.PDXC2_MoveStop
PDXC2_MoveStop.restype = c_short
PDXC2_MoveStop.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_Open = lib.PDXC2_Open
PDXC2_Open.restype = c_short
PDXC2_Open.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_PersistSettings = lib.PDXC2_PersistSettings
PDXC2_PersistSettings.restype = c_bool
PDXC2_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_PollingDuration = lib.PDXC2_PollingDuration
PDXC2_PollingDuration.restype = c_long
PDXC2_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_PulseParamsAcquireStart = lib.PDXC2_PulseParamsAcquireStart
PDXC2_PulseParamsAcquireStart.restype = c_short
PDXC2_PulseParamsAcquireStart.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RegisterMessageCallback = lib.PDXC2_RegisterMessageCallback
PDXC2_RegisterMessageCallback.restype = c_short
PDXC2_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNo, void

PDXC2_RequestAbnormalMoveDetectionEnabled = lib.PDXC2_RequestAbnormalMoveDetectionEnabled
PDXC2_RequestAbnormalMoveDetectionEnabled.restype = c_short
PDXC2_RequestAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestAmpOutParams = lib.PDXC2_RequestAmpOutParams
PDXC2_RequestAmpOutParams.restype = c_short
PDXC2_RequestAmpOutParams.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestClosedLoopParams = lib.PDXC2_RequestClosedLoopParams
PDXC2_RequestClosedLoopParams.restype = c_short
PDXC2_RequestClosedLoopParams.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestClosedLoopTarget = lib.PDXC2_RequestClosedLoopTarget
PDXC2_RequestClosedLoopTarget.restype = c_short
PDXC2_RequestClosedLoopTarget.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestExternalTriggerConfig = lib.PDXC2_RequestExternalTriggerConfig
PDXC2_RequestExternalTriggerConfig.restype = c_short
PDXC2_RequestExternalTriggerConfig.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestExternalTriggerParams = lib.PDXC2_RequestExternalTriggerParams
PDXC2_RequestExternalTriggerParams.restype = c_short
PDXC2_RequestExternalTriggerParams.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestExternalTriggerTarget = lib.PDXC2_RequestExternalTriggerTarget
PDXC2_RequestExternalTriggerTarget.restype = c_short
PDXC2_RequestExternalTriggerTarget.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestJogParams = lib.PDXC2_RequestJogParams
PDXC2_RequestJogParams.restype = c_short
PDXC2_RequestJogParams.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestOpenLoopMoveParams = lib.PDXC2_RequestOpenLoopMoveParams
PDXC2_RequestOpenLoopMoveParams.restype = c_short
PDXC2_RequestOpenLoopMoveParams.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestPosition = lib.PDXC2_RequestPosition
PDXC2_RequestPosition.restype = c_short
PDXC2_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestPositionControlMode = lib.PDXC2_RequestPositionControlMode
PDXC2_RequestPositionControlMode.restype = c_bool
PDXC2_RequestPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestSettings = lib.PDXC2_RequestSettings
PDXC2_RequestSettings.restype = c_short
PDXC2_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestStageAxisParams = lib.PDXC2_RequestStageAxisParams
PDXC2_RequestStageAxisParams.restype = c_short
PDXC2_RequestStageAxisParams.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestStatus = lib.PDXC2_RequestStatus
PDXC2_RequestStatus.restype = c_short
PDXC2_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_RequestStatusBits = lib.PDXC2_RequestStatusBits
PDXC2_RequestStatusBits.restype = c_short
PDXC2_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_ResetParameters = lib.PDXC2_ResetParameters
PDXC2_ResetParameters.restype = c_short
PDXC2_ResetParameters.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_SetAbnormalMoveDetectionEnabled = lib.PDXC2_SetAbnormalMoveDetectionEnabled
PDXC2_SetAbnormalMoveDetectionEnabled.restype = c_short
PDXC2_SetAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char), c_bool]
# *serialNo, isEnabled

PDXC2_SetAmpOutParams = lib.PDXC2_SetAmpOutParams
PDXC2_SetAmpOutParams.restype = c_short
PDXC2_SetAmpOutParams.argtypes = [PZ_AmpOutParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_SetClosedLoopParams = lib.PDXC2_SetClosedLoopParams
PDXC2_SetClosedLoopParams.restype = c_short
PDXC2_SetClosedLoopParams.argtypes = [PDXC2_ClosedLoopParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_SetClosedLoopTarget = lib.PDXC2_SetClosedLoopTarget
PDXC2_SetClosedLoopTarget.restype = c_short
PDXC2_SetClosedLoopTarget.argtypes = [POINTER(c_char), c_int]
# *serialNo, target

PDXC2_SetExternalTriggerConfig = lib.PDXC2_SetExternalTriggerConfig
PDXC2_SetExternalTriggerConfig.restype = c_short
PDXC2_SetExternalTriggerConfig.argtypes = [POINTER(c_char), PDXC2_TriggerModes]
# *serialNo, mode

PDXC2_SetExternalTriggerParams = lib.PDXC2_SetExternalTriggerParams
PDXC2_SetExternalTriggerParams.restype = c_short
PDXC2_SetExternalTriggerParams.argtypes = [PDXC2_TriggerParams, POINTER(c_char)]
# *params, *serialNo

PDXC2_SetJogParams = lib.PDXC2_SetJogParams
PDXC2_SetJogParams.restype = c_short
PDXC2_SetJogParams.argtypes = [PDXC2_JogParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_SetOpenLoopMoveParams = lib.PDXC2_SetOpenLoopMoveParams
PDXC2_SetOpenLoopMoveParams.restype = c_short
PDXC2_SetOpenLoopMoveParams.argtypes = [PDXC2_OpenLoopMoveParameters, POINTER(c_char)]
# *params, *serialNo

PDXC2_SetPositionControlMode = lib.PDXC2_SetPositionControlMode
PDXC2_SetPositionControlMode.restype = c_short
PDXC2_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
# *serialNo, mode

PDXC2_StartPolling = lib.PDXC2_StartPolling
PDXC2_StartPolling.restype = c_bool
PDXC2_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

PDXC2_StopPolling = lib.PDXC2_StopPolling
PDXC2_StopPolling.restype = c_void_p
PDXC2_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

PDXC2_TimeSinceLastMsgReceived = lib.PDXC2_TimeSinceLastMsgReceived
PDXC2_TimeSinceLastMsgReceived.restype = c_bool
PDXC2_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

PDXC2_WaitForMessage = lib.PDXC2_WaitForMessage
PDXC2_WaitForMessage.restype = c_bool
PDXC2_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
#

TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [TLI_DeviceInfo, POINTER(c_char), POINTER(c_char)]
# *info, *serialNo, *serialNumber

TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = [SafeArray]
# **stringsReceiver

TLI_GetDeviceListByType = lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype = c_short
TLI_GetDeviceListByType.argtypes = [SafeArray, c_int]
# **stringsReceiver, typeID

TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char), c_ulong, c_int]
# *receiveBuffer, sizeOfBuffer, typeID

TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = [SafeArray, c_int, c_int]
# **stringsReceiver, *typeIDs, length

TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_int, c_int, c_ulong]
# *receiveBuffer, *typeIDs, length, sizeOfBuffer

TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_ulong]
# *receiveBuffer, sizeOfBuffer

TLI_GetDeviceListSize = lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype = c_short
#

TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p
#

TLI_ScanEthernetRange = lib.TLI_ScanEthernetRange
TLI_ScanEthernetRange.restype = c_short
TLI_ScanEthernetRange.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(c_char), c_int, c_int, c_ulong]
# *endIPAddress, *foundAddressesBuffer, *startIPAddress, openTimeout, portNo, sizeOfBuffer
