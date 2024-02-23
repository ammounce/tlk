from ctypes import (POINTER, c_bool, c_char, c_double, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (MOT_TravelDirection, POL_PaddleBits, POL_Paddles, PolarizerParameters)
from .definitions.structures import (TLI_DeviceInfo)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.Polarizer.DLL")
MPC_CheckConnection = lib.MPC_CheckConnection
MPC_CheckConnection.restype = c_bool
MPC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

MPC_ClearMessageQueue = lib.MPC_ClearMessageQueue
MPC_ClearMessageQueue.restype = None
MPC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

MPC_Close = lib.MPC_Close
MPC_Close.restype = None
MPC_Close.argtypes = [POINTER(c_char)]
# *serialNo

MPC_EnableLastMsgTimer = lib.MPC_EnableLastMsgTimer
MPC_EnableLastMsgTimer.restype = None
MPC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

MPC_GetEnabledPaddles = lib.MPC_GetEnabledPaddles
MPC_GetEnabledPaddles.restype = POL_PaddleBits
MPC_GetEnabledPaddles.argtypes = [POINTER(c_char)]
# *serialNo

MPC_GetFirmwareVersion = lib.MPC_GetFirmwareVersion
MPC_GetFirmwareVersion.restype = c_ulong
MPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

MPC_GetHardwareInfo = lib.MPC_GetHardwareInfo
MPC_GetHardwareInfo.restype = c_short
MPC_GetHardwareInfo.argtypes = [
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
# *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numchannels, *serialNo, *type, sizeOfModelNo, sizeOfNotes

MPC_GetHomeOffset = lib.MPC_GetHomeOffset
MPC_GetHomeOffset.restype = c_double
MPC_GetHomeOffset.argtypes = [POINTER(c_char)]
# *serialNo

MPC_GetJogSize = lib.MPC_GetJogSize
MPC_GetJogSize.restype = c_double
MPC_GetJogSize.argtypes = [POINTER(c_char), POL_Paddles]
# *serialNo, paddle

MPC_GetMaxTravel = lib.MPC_GetMaxTravel
MPC_GetMaxTravel.restype = c_double
MPC_GetMaxTravel.argtypes = [POINTER(c_char)]
# *serialNo

MPC_GetNextMessage = lib.MPC_GetNextMessage
MPC_GetNextMessage.restype = c_bool
MPC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

MPC_GetPaddleCount = lib.MPC_GetPaddleCount
MPC_GetPaddleCount.restype = c_int
MPC_GetPaddleCount.argtypes = [POINTER(c_char)]
# *serialNo

MPC_GetPolParams = lib.MPC_GetPolParams
MPC_GetPolParams.restype = c_short
MPC_GetPolParams.argtypes = [PolarizerParameters, POINTER(c_char)]
# *polParams, *serialNo

MPC_GetPosition = lib.MPC_GetPosition
MPC_GetPosition.restype = c_double
MPC_GetPosition.argtypes = [POINTER(c_char), POL_Paddles]
# *serialNo, paddle

MPC_GetSoftwareVersion = lib.MPC_GetSoftwareVersion
MPC_GetSoftwareVersion.restype = c_ulong
MPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

MPC_GetStatusBits = lib.MPC_GetStatusBits
MPC_GetStatusBits.restype = c_ulong
MPC_GetStatusBits.argtypes = [POINTER(c_char), POL_Paddles]
# *serialNo, paddle

MPC_GetStepsPerDegree = lib.MPC_GetStepsPerDegree
MPC_GetStepsPerDegree.restype = c_double
MPC_GetStepsPerDegree.argtypes = [POINTER(c_char)]
# *serialNo

MPC_GetVelocity = lib.MPC_GetVelocity
MPC_GetVelocity.restype = c_short
MPC_GetVelocity.argtypes = [POINTER(c_char)]
# *serialNo

MPC_HasLastMsgTimerOverrun = lib.MPC_HasLastMsgTimerOverrun
MPC_HasLastMsgTimerOverrun.restype = c_bool
MPC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

MPC_Home = lib.MPC_Home
MPC_Home.restype = c_short
MPC_Home.argtypes = [POINTER(c_char), POL_Paddles]
# *serialNo, paddle

MPC_Identify = lib.MPC_Identify
MPC_Identify.restype = None
MPC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

MPC_IsPaddleEnabled = lib.MPC_IsPaddleEnabled
MPC_IsPaddleEnabled.restype = c_bool
MPC_IsPaddleEnabled.argtypes = [POINTER(c_char), POL_Paddles]
# *serialNo, paddle

MPC_Jog = lib.MPC_Jog
MPC_Jog.restype = c_short
MPC_Jog.argtypes = [POINTER(c_char), MOT_TravelDirection, POL_Paddles]
# *serialNo, direction, paddle

MPC_LoadNamedSettings = lib.MPC_LoadNamedSettings
MPC_LoadNamedSettings.restype = c_bool
MPC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

MPC_LoadSettings = lib.MPC_LoadSettings
MPC_LoadSettings.restype = c_bool
MPC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

MPC_MessageQueueSize = lib.MPC_MessageQueueSize
MPC_MessageQueueSize.restype = c_int
MPC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

MPC_MoveRelative = lib.MPC_MoveRelative
MPC_MoveRelative.restype = c_short
MPC_MoveRelative.argtypes = [POINTER(c_char), POL_Paddles, c_double]
# *serialNo, paddle, position

MPC_MoveToPosition = lib.MPC_MoveToPosition
MPC_MoveToPosition.restype = c_short
MPC_MoveToPosition.argtypes = [POINTER(c_char), POL_Paddles, c_double]
# *serialNo, paddle, position

MPC_Open = lib.MPC_Open
MPC_Open.restype = c_short
MPC_Open.argtypes = [POINTER(c_char)]
# *serialNo

MPC_PersistSettings = lib.MPC_PersistSettings
MPC_PersistSettings.restype = c_bool
MPC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

MPC_PollingDuration = lib.MPC_PollingDuration
MPC_PollingDuration.restype = c_long
MPC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

MPC_RegisterMessageCallback = lib.MPC_RegisterMessageCallback
MPC_RegisterMessageCallback.restype = None
MPC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

MPC_RequestPolParams = lib.MPC_RequestPolParams
MPC_RequestPolParams.restype = c_short
MPC_RequestPolParams.argtypes = [POINTER(c_char)]
# *serialNo

MPC_RequestSettings = lib.MPC_RequestSettings
MPC_RequestSettings.restype = c_short
MPC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

MPC_RequestStatus = lib.MPC_RequestStatus
MPC_RequestStatus.restype = c_short
MPC_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

MPC_ResetParameters = lib.MPC_ResetParameters
MPC_ResetParameters.restype = c_bool
MPC_ResetParameters.argtypes = [POINTER(c_char)]
# *serialNo

MPC_SetEnabledPaddles = lib.MPC_SetEnabledPaddles
MPC_SetEnabledPaddles.restype = c_int
MPC_SetEnabledPaddles.argtypes = [POINTER(c_char), POL_PaddleBits]
# *serialNo, paddles

MPC_SetHomeOffset = lib.MPC_SetHomeOffset
MPC_SetHomeOffset.restype = c_short
MPC_SetHomeOffset.argtypes = [POINTER(c_char), c_double]
# *serialNo, homeOffset

MPC_SetJogSize = lib.MPC_SetJogSize
MPC_SetJogSize.restype = c_short
MPC_SetJogSize.argtypes = [POINTER(c_char), c_double, POL_Paddles]
# *serialNo, jogSize, paddle

MPC_SetPolParams = lib.MPC_SetPolParams
MPC_SetPolParams.restype = c_short
MPC_SetPolParams.argtypes = [PolarizerParameters, POINTER(c_char)]
# *polParams, *serialNo

MPC_SetVelocity = lib.MPC_SetVelocity
MPC_SetVelocity.restype = c_short
MPC_SetVelocity.argtypes = [POINTER(c_char), c_short]
# *serialNo, velocity

MPC_StartPolling = lib.MPC_StartPolling
MPC_StartPolling.restype = c_bool
MPC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

MPC_Stop = lib.MPC_Stop
MPC_Stop.restype = c_short
MPC_Stop.argtypes = [POINTER(c_char), POL_Paddles]
# *serialNo, paddle

MPC_StopPolling = lib.MPC_StopPolling
MPC_StopPolling.restype = None
MPC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

MPC_TimeSinceLastMsgReceived = lib.MPC_TimeSinceLastMsgReceived
MPC_TimeSinceLastMsgReceived.restype = c_bool
MPC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

MPC_WaitForMessage = lib.MPC_WaitForMessage
MPC_WaitForMessage.restype = c_bool
MPC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = [None, None]
# , void

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
TLI_GetDeviceListSize.argtypes = [None]
#

TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = None
TLI_InitializeSimulations.argtypes = [None]
#
