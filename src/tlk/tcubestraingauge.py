from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_uint, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (TSG_Display_Modes, TSG_Hub_Analogue_Modes)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation, TSG_IOSettings)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.StrainGauge.DLL")

SG_CheckConnection = lib.SG_CheckConnection
SG_CheckConnection.restype = c_bool
SG_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

SG_ClearMessageQueue = lib.SG_ClearMessageQueue
SG_ClearMessageQueue.restype = c_void_p
SG_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

SG_Close = lib.SG_Close
SG_Close.restype = c_void_p
SG_Close.argtypes = [POINTER(c_char)]
# *serialNo

SG_Disable = lib.SG_Disable
SG_Disable.restype = c_short
SG_Disable.argtypes = [POINTER(c_char)]
# *serialNo

SG_Disconnect = lib.SG_Disconnect
SG_Disconnect.restype = c_short
SG_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

SG_Enable = lib.SG_Enable
SG_Enable.restype = c_short
SG_Enable.argtypes = [POINTER(c_char)]
# *serialNo

SG_EnableLastMsgTimer = lib.SG_EnableLastMsgTimer
SG_EnableLastMsgTimer.restype = c_void_p
SG_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

SG_GetDisplayMode = lib.SG_GetDisplayMode
SG_GetDisplayMode.restype = TSG_Display_Modes
SG_GetDisplayMode.argtypes = [POINTER(c_char)]
# *serialNo

SG_GetFirmwareVersion = lib.SG_GetFirmwareVersion
SG_GetFirmwareVersion.restype = c_ulong
SG_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

SG_GetForceCalib = lib.SG_GetForceCalib
SG_GetForceCalib.restype = c_uint
SG_GetForceCalib.argtypes = [POINTER(c_char)]
# *serialNo

SG_GetHardwareInfo = lib.SG_GetHardwareInfo
SG_GetHardwareInfo.restype = c_short
SG_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    POINTER(c_char),
    c_ulong,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]
# *serialNo, *modelNo, sizeOfModelNo, *type, *numChannels, *notes, sizeOfNotes, *firmwareVersion, *hardwareVersion, *modificationState

SG_GetHardwareInfoBlock = lib.SG_GetHardwareInfoBlock
SG_GetHardwareInfoBlock.restype = c_short
SG_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]
# *serialNo, *hardwareInfo

SG_GetHubAnalogOutput = lib.SG_GetHubAnalogOutput
SG_GetHubAnalogOutput.restype = TSG_Hub_Analogue_Modes
SG_GetHubAnalogOutput.argtypes = [POINTER(c_char)]
# *serialNo

SG_GetHubBay = lib.SG_GetHubBay
SG_GetHubBay.restype = POINTER(c_char)
SG_GetHubBay.argtypes = [POINTER(c_char)]
# *serialNo

SG_GetIOsettingsBlock = lib.SG_GetIOsettingsBlock
SG_GetIOsettingsBlock.restype = c_short
SG_GetIOsettingsBlock.argtypes = [POINTER(c_char), TSG_IOSettings]
# *serialNo, *inputOutputSettings

SG_GetLEDBrightness = lib.SG_GetLEDBrightness
SG_GetLEDBrightness.restype = c_short
SG_GetLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

SG_GetMaximumTravel = lib.SG_GetMaximumTravel
SG_GetMaximumTravel.restype = c_long
SG_GetMaximumTravel.argtypes = [POINTER(c_char)]
# *serialNo

SG_GetNextMessage = lib.SG_GetNextMessage
SG_GetNextMessage.restype = c_bool
SG_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]
# *serialNo, *messageType, *messageID, *messageData

SG_GetReading = lib.SG_GetReading
SG_GetReading.restype = c_short
SG_GetReading.argtypes = [POINTER(c_char), c_bool]
# *serialNo, smoothed

SG_GetReadingExt = lib.SG_GetReadingExt
SG_GetReadingExt.restype = c_int
SG_GetReadingExt.argtypes = [POINTER(c_char), c_bool, c_bool]
# *serialNo, clipReadng, *overrange

SG_GetSoftwareVersion = lib.SG_GetSoftwareVersion
SG_GetSoftwareVersion.restype = c_ulong
SG_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

SG_GetStatusBits = lib.SG_GetStatusBits
SG_GetStatusBits.restype = c_ulong
SG_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

SG_HasLastMsgTimerOverrun = lib.SG_HasLastMsgTimerOverrun
SG_HasLastMsgTimerOverrun.restype = c_bool
SG_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

SG_Identify = lib.SG_Identify
SG_Identify.restype = c_void_p
SG_Identify.argtypes = [POINTER(c_char)]
# *serialNo

SG_LoadNamedSettings = lib.SG_LoadNamedSettings
SG_LoadNamedSettings.restype = c_bool
SG_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

SG_LoadSettings = lib.SG_LoadSettings
SG_LoadSettings.restype = c_bool
SG_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

SG_MessageQueueSize = lib.SG_MessageQueueSize
SG_MessageQueueSize.restype = c_int
SG_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

SG_Open = lib.SG_Open
SG_Open.restype = c_short
SG_Open.argtypes = [POINTER(c_char)]
# *serialNo

SG_PersistSettings = lib.SG_PersistSettings
SG_PersistSettings.restype = c_bool
SG_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

SG_PollingDuration = lib.SG_PollingDuration
SG_PollingDuration.restype = c_long
SG_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

SG_RegisterMessageCallback = lib.SG_RegisterMessageCallback
SG_RegisterMessageCallback.restype = c_void_p
SG_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNo, void

SG_RequestDisplayMode = lib.SG_RequestDisplayMode
SG_RequestDisplayMode.restype = c_short
SG_RequestDisplayMode.argtypes = [POINTER(c_char)]
# *serialNo

SG_RequestForceCalib = lib.SG_RequestForceCalib
SG_RequestForceCalib.restype = c_short
SG_RequestForceCalib.argtypes = [POINTER(c_char)]
# *serialNo

SG_RequestHubAnalogOutput = lib.SG_RequestHubAnalogOutput
SG_RequestHubAnalogOutput.restype = c_short
SG_RequestHubAnalogOutput.argtypes = [POINTER(c_char)]
# *serialNo

SG_RequestIOsettings = lib.SG_RequestIOsettings
SG_RequestIOsettings.restype = c_short
SG_RequestIOsettings.argtypes = [POINTER(c_char)]
# *serialNo

SG_RequestLEDBrightness = lib.SG_RequestLEDBrightness
SG_RequestLEDBrightness.restype = c_short
SG_RequestLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

SG_RequestMaximumTravel = lib.SG_RequestMaximumTravel
SG_RequestMaximumTravel.restype = c_short
SG_RequestMaximumTravel.argtypes = [POINTER(c_char)]
# *serialNo

SG_RequestReading = lib.SG_RequestReading
SG_RequestReading.restype = c_short
SG_RequestReading.argtypes = [POINTER(c_char)]
# *serialNo

SG_RequestSettings = lib.SG_RequestSettings
SG_RequestSettings.restype = c_short
SG_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

SG_RequestStatus = lib.SG_RequestStatus
SG_RequestStatus.restype = c_short
SG_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

SG_SetDisplayMode = lib.SG_SetDisplayMode
SG_SetDisplayMode.restype = c_short
SG_SetDisplayMode.argtypes = [POINTER(c_char), TSG_Display_Modes]
# *serialNo, mode

SG_SetForceCalib = lib.SG_SetForceCalib
SG_SetForceCalib.restype = c_short
SG_SetForceCalib.argtypes = [POINTER(c_char), c_uint]
# *serialNo, forceCalibration

SG_SetHubAnalogOutput = lib.SG_SetHubAnalogOutput
SG_SetHubAnalogOutput.restype = c_short
SG_SetHubAnalogOutput.argtypes = [POINTER(c_char), TSG_Hub_Analogue_Modes]
# *serialNo, hubAnalogOutput

SG_SetIOsettings = lib.SG_SetIOsettings
SG_SetIOsettings.restype = c_short
SG_SetIOsettings.argtypes = [POINTER(c_char), TSG_Hub_Analogue_Modes, TSG_Display_Modes, c_uint]
# *serialNo, hubAnalogOutput, displayMode, calibrationForce

SG_SetIOsettingsBlock = lib.SG_SetIOsettingsBlock
SG_SetIOsettingsBlock.restype = c_short
SG_SetIOsettingsBlock.argtypes = [POINTER(c_char), TSG_IOSettings]
# *serialNo, *inputOutputSettings

SG_SetLEDBrightness = lib.SG_SetLEDBrightness
SG_SetLEDBrightness.restype = c_short
SG_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
# *serialNo, brightness

SG_SetZero = lib.SG_SetZero
SG_SetZero.restype = c_short
SG_SetZero.argtypes = [POINTER(c_char)]
# *serialNo

SG_StartPolling = lib.SG_StartPolling
SG_StartPolling.restype = c_bool
SG_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

SG_StopPolling = lib.SG_StopPolling
SG_StopPolling.restype = c_void_p
SG_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

SG_TimeSinceLastMsgReceived = lib.SG_TimeSinceLastMsgReceived
SG_TimeSinceLastMsgReceived.restype = c_bool
SG_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]
# *serialNo, &lastUpdateTimeMS

SG_WaitForMessage = lib.SG_WaitForMessage
SG_WaitForMessage.restype = c_bool
SG_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]
# *serialNo, *messageType, *messageID, *messageData

TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = [c_void_p]
# void

TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [POINTER(c_char), POINTER(c_char), TLI_DeviceInfo]
# *serialNo, *serialNumber, *info

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
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_ulong, c_int, c_int]
# *receiveBuffer, sizeOfBuffer, *typeIDs, length

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
