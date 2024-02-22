from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (TC_DisplayModes, TC_SensorTypes)
from .definitions.structures import (TC_LoopParameters, TLI_DeviceInfo, TLI_HardwareInformation)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.TCube.TEC.DLL")
TC_CheckConnection = lib.TC_CheckConnection
TC_CheckConnection.restype = c_bool
TC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

TC_ClearMessageQueue = lib.TC_ClearMessageQueue
TC_ClearMessageQueue.restype = None
TC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

TC_Close = lib.TC_Close
TC_Close.restype = None
TC_Close.argtypes = [POINTER(c_char)]
# *serialNo

TC_Disable = lib.TC_Disable
TC_Disable.restype = c_short
TC_Disable.argtypes = [POINTER(c_char)]
# *serialNo

TC_Disconnect = lib.TC_Disconnect
TC_Disconnect.restype = c_short
TC_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

TC_Enable = lib.TC_Enable
TC_Enable.restype = c_short
TC_Enable.argtypes = [POINTER(c_char)]
# *serialNo

TC_EnableLastMsgTimer = lib.TC_EnableLastMsgTimer
TC_EnableLastMsgTimer.restype = None
TC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

TC_GetCurrentLimit = lib.TC_GetCurrentLimit
TC_GetCurrentLimit.restype = c_long
TC_GetCurrentLimit.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetCurrentReading = lib.TC_GetCurrentReading
TC_GetCurrentReading.restype = c_long
TC_GetCurrentReading.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetFirmwareVersion = lib.TC_GetFirmwareVersion
TC_GetFirmwareVersion.restype = c_ulong
TC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetHWDisplayMode = lib.TC_GetHWDisplayMode
TC_GetHWDisplayMode.restype = TC_DisplayModes
TC_GetHWDisplayMode.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetHardwareInfo = lib.TC_GetHardwareInfo
TC_GetHardwareInfo.restype = c_short
TC_GetHardwareInfo.argtypes = [
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

TC_GetHardwareInfoBlock = lib.TC_GetHardwareInfoBlock
TC_GetHardwareInfoBlock.restype = c_short
TC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

TC_GetLEDBrightness = lib.TC_GetLEDBrightness
TC_GetLEDBrightness.restype = c_short
TC_GetLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetNextMessage = lib.TC_GetNextMessage
TC_GetNextMessage.restype = c_bool
TC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

TC_GetSensorType = lib.TC_GetSensorType
TC_GetSensorType.restype = TC_SensorTypes
TC_GetSensorType.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetSoftwareVersion = lib.TC_GetSoftwareVersion
TC_GetSoftwareVersion.restype = c_ulong
TC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetStatusBits = lib.TC_GetStatusBits
TC_GetStatusBits.restype = c_ulong
TC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetTempLoopParams = lib.TC_GetTempLoopParams
TC_GetTempLoopParams.restype = c_short
TC_GetTempLoopParams.argtypes = [TC_LoopParameters, POINTER(c_char)]
# *proportionalIntegralDerivativeParams, *serialNo

TC_GetTemperatureReading = lib.TC_GetTemperatureReading
TC_GetTemperatureReading.restype = c_short
TC_GetTemperatureReading.argtypes = [POINTER(c_char)]
# *serialNo

TC_GetTemperatureSet = lib.TC_GetTemperatureSet
TC_GetTemperatureSet.restype = c_short
TC_GetTemperatureSet.argtypes = [POINTER(c_char)]
# *serialNo

TC_HasLastMsgTimerOverrun = lib.TC_HasLastMsgTimerOverrun
TC_HasLastMsgTimerOverrun.restype = c_bool
TC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

TC_Identify = lib.TC_Identify
TC_Identify.restype = None
TC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

TC_LoadNamedSettings = lib.TC_LoadNamedSettings
TC_LoadNamedSettings.restype = c_bool
TC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

TC_LoadSettings = lib.TC_LoadSettings
TC_LoadSettings.restype = c_bool
TC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

TC_MessageQueueSize = lib.TC_MessageQueueSize
TC_MessageQueueSize.restype = c_int
TC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

TC_Open = lib.TC_Open
TC_Open.restype = c_short
TC_Open.argtypes = [POINTER(c_char)]
# *serialNo

TC_PersistSettings = lib.TC_PersistSettings
TC_PersistSettings.restype = c_bool
TC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

TC_PollingDuration = lib.TC_PollingDuration
TC_PollingDuration.restype = c_long
TC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

TC_RegisterMessageCallback = lib.TC_RegisterMessageCallback
TC_RegisterMessageCallback.restype = None
TC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

TC_RequestCurrentLimit = lib.TC_RequestCurrentLimit
TC_RequestCurrentLimit.restype = c_short
TC_RequestCurrentLimit.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestHWDisplayMode = lib.TC_RequestHWDisplayMode
TC_RequestHWDisplayMode.restype = c_short
TC_RequestHWDisplayMode.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestLEDBrightness = lib.TC_RequestLEDBrightness
TC_RequestLEDBrightness.restype = c_short
TC_RequestLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestReadings = lib.TC_RequestReadings
TC_RequestReadings.restype = c_short
TC_RequestReadings.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestSensorType = lib.TC_RequestSensorType
TC_RequestSensorType.restype = c_short
TC_RequestSensorType.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestSettings = lib.TC_RequestSettings
TC_RequestSettings.restype = c_short
TC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestStatus = lib.TC_RequestStatus
TC_RequestStatus.restype = c_short
TC_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestStatusBits = lib.TC_RequestStatusBits
TC_RequestStatusBits.restype = c_short
TC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestTempLoopParams = lib.TC_RequestTempLoopParams
TC_RequestTempLoopParams.restype = c_short
TC_RequestTempLoopParams.argtypes = [POINTER(c_char)]
# *serialNo

TC_RequestTemperatureSet = lib.TC_RequestTemperatureSet
TC_RequestTemperatureSet.restype = c_short
TC_RequestTemperatureSet.argtypes = [POINTER(c_char)]
# *serialNo

TC_Reset = lib.TC_Reset
TC_Reset.restype = c_short
TC_Reset.argtypes = [POINTER(c_char)]
# *serialNo

TC_SetCurrentLimit = lib.TC_SetCurrentLimit
TC_SetCurrentLimit.restype = c_short
TC_SetCurrentLimit.argtypes = [POINTER(c_char), c_long]
# *serialNo, maxCurrent

TC_SetHWDisplayMode = lib.TC_SetHWDisplayMode
TC_SetHWDisplayMode.restype = c_short
TC_SetHWDisplayMode.argtypes = [POINTER(c_char), TC_DisplayModes]
# *serialNo, mode

TC_SetLEDBrightness = lib.TC_SetLEDBrightness
TC_SetLEDBrightness.restype = c_short
TC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
# *serialNo, brightness

TC_SetSensorType = lib.TC_SetSensorType
TC_SetSensorType.restype = c_short
TC_SetSensorType.argtypes = [POINTER(c_char), TC_SensorTypes]
# *serialNo, sensor

TC_SetTempLoopParams = lib.TC_SetTempLoopParams
TC_SetTempLoopParams.restype = c_short
TC_SetTempLoopParams.argtypes = [TC_LoopParameters, POINTER(c_char)]
# *proportionalIntegralDerivativeParams, *serialNo

TC_SetTemperature = lib.TC_SetTemperature
TC_SetTemperature.restype = c_short
TC_SetTemperature.argtypes = [POINTER(c_char), c_short]
# *serialNo, temperature

TC_StartPolling = lib.TC_StartPolling
TC_StartPolling.restype = c_bool
TC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

TC_StopPolling = lib.TC_StopPolling
TC_StopPolling.restype = None
TC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

TC_TimeSinceLastMsgReceived = lib.TC_TimeSinceLastMsgReceived
TC_TimeSinceLastMsgReceived.restype = c_bool
TC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

TC_WaitForMessage = lib.TC_WaitForMessage
TC_WaitForMessage.restype = c_bool
TC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
