from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_uint, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (FF_Positions)
from .definitions.structures import (FF_IOSettings, TLI_DeviceInfo)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.FilterFlipper.DLL")

FF_CheckConnection = lib.FF_CheckConnection
FF_CheckConnection.restype = c_bool
FF_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

FF_ClearMessageQueue = lib.FF_ClearMessageQueue
FF_ClearMessageQueue.restype = c_void_p
FF_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

FF_Close = lib.FF_Close
FF_Close.restype = c_void_p
FF_Close.argtypes = [POINTER(c_char)]
# *serialNo

FF_EnableLastMsgTimer = lib.FF_EnableLastMsgTimer
FF_EnableLastMsgTimer.restype = c_void_p
FF_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

FF_GetFirmwareVersion = lib.FF_GetFirmwareVersion
FF_GetFirmwareVersion.restype = c_ulong
FF_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

FF_GetHardwareInfo = lib.FF_GetHardwareInfo
FF_GetHardwareInfo.restype = c_short
FF_GetHardwareInfo.argtypes = [
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

FF_GetIOSettings = lib.FF_GetIOSettings
FF_GetIOSettings.restype = c_short
FF_GetIOSettings.argtypes = [POINTER(c_char), FF_IOSettings]
# *serialNo, *settings

FF_GetNextMessage = lib.FF_GetNextMessage
FF_GetNextMessage.restype = c_bool
FF_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

FF_GetNumberPositions = lib.FF_GetNumberPositions
FF_GetNumberPositions.restype = c_int
FF_GetNumberPositions.argtypes = [POINTER(c_char)]
# *serialNo

FF_GetPosition = lib.FF_GetPosition
FF_GetPosition.restype = FF_Positions
FF_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

FF_GetSoftwareVersion = lib.FF_GetSoftwareVersion
FF_GetSoftwareVersion.restype = c_ulong
FF_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

FF_GetStatusBits = lib.FF_GetStatusBits
FF_GetStatusBits.restype = c_ulong
FF_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

FF_GetTransitTime = lib.FF_GetTransitTime
FF_GetTransitTime.restype = c_uint
FF_GetTransitTime.argtypes = [POINTER(c_char)]
# *serialNo

FF_HasLastMsgTimerOverrun = lib.FF_HasLastMsgTimerOverrun
FF_HasLastMsgTimerOverrun.restype = c_bool
FF_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

FF_Home = lib.FF_Home
FF_Home.restype = c_short
FF_Home.argtypes = [POINTER(c_char)]
# *serialNo

FF_Identify = lib.FF_Identify
FF_Identify.restype = c_void_p
FF_Identify.argtypes = [POINTER(c_char)]
# *serialNo

FF_LoadNamedSettings = lib.FF_LoadNamedSettings
FF_LoadNamedSettings.restype = c_bool
FF_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

FF_LoadSettings = lib.FF_LoadSettings
FF_LoadSettings.restype = c_bool
FF_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

FF_MessageQueueSize = lib.FF_MessageQueueSize
FF_MessageQueueSize.restype = c_int
FF_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

FF_MoveToPosition = lib.FF_MoveToPosition
FF_MoveToPosition.restype = c_short
FF_MoveToPosition.argtypes = [POINTER(c_char), FF_Positions]
# *serialNo, position

FF_Open = lib.FF_Open
FF_Open.restype = c_short
FF_Open.argtypes = [POINTER(c_char)]
# *serialNo

FF_PersistSettings = lib.FF_PersistSettings
FF_PersistSettings.restype = c_bool
FF_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

FF_PollingDuration = lib.FF_PollingDuration
FF_PollingDuration.restype = c_long
FF_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

FF_RegisterMessageCallback = lib.FF_RegisterMessageCallback
FF_RegisterMessageCallback.restype = c_void_p
FF_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNo, void

FF_RequestIOSettings = lib.FF_RequestIOSettings
FF_RequestIOSettings.restype = c_short
FF_RequestIOSettings.argtypes = [POINTER(c_char)]
# *serialNo

FF_RequestSettings = lib.FF_RequestSettings
FF_RequestSettings.restype = c_short
FF_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

FF_RequestStatus = lib.FF_RequestStatus
FF_RequestStatus.restype = c_short
FF_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

FF_SetIOSettings = lib.FF_SetIOSettings
FF_SetIOSettings.restype = c_short
FF_SetIOSettings.argtypes = [POINTER(c_char), FF_IOSettings]
# *serialNo, *settings

FF_SetTransitTime = lib.FF_SetTransitTime
FF_SetTransitTime.restype = c_short
FF_SetTransitTime.argtypes = [POINTER(c_char), c_uint]
# *serialNo, transitTime

FF_StartPolling = lib.FF_StartPolling
FF_StartPolling.restype = c_bool
FF_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

FF_StopPolling = lib.FF_StopPolling
FF_StopPolling.restype = c_void_p
FF_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

FF_TimeSinceLastMsgReceived = lib.FF_TimeSinceLastMsgReceived
FF_TimeSinceLastMsgReceived.restype = c_bool
FF_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

FF_WaitForMessage = lib.FF_WaitForMessage
FF_WaitForMessage.restype = c_bool
FF_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
