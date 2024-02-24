from ctypes import (POINTER, c_bool, c_char, c_float, c_int, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (LD_DisplayUnits, LD_InputSourceFlags, LD_POLARITY)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.LaserDiode.DLL")

LD_CheckConnection = lib.LD_CheckConnection
LD_CheckConnection.restype = c_bool
LD_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

LD_ClearMessageQueue = lib.LD_ClearMessageQueue
LD_ClearMessageQueue.restype = c_void_p
LD_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

LD_Close = lib.LD_Close
LD_Close.restype = c_void_p
LD_Close.argtypes = [POINTER(c_char)]
# *serialNo

LD_Disable = lib.LD_Disable
LD_Disable.restype = c_short
LD_Disable.argtypes = [POINTER(c_char)]
# *serialNo

LD_DisableOutput = lib.LD_DisableOutput
LD_DisableOutput.restype = c_short
LD_DisableOutput.argtypes = [POINTER(c_char)]
# *serialNo

LD_Enable = lib.LD_Enable
LD_Enable.restype = c_short
LD_Enable.argtypes = [POINTER(c_char)]
# *serialNo

LD_EnableLastMsgTimer = lib.LD_EnableLastMsgTimer
LD_EnableLastMsgTimer.restype = c_void_p
LD_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

LD_EnableMaxCurrentAdjust = lib.LD_EnableMaxCurrentAdjust
LD_EnableMaxCurrentAdjust.restype = c_short
LD_EnableMaxCurrentAdjust.argtypes = [POINTER(c_char), c_bool, c_bool]
# *serialNo, enableAdjust, enableDiode

LD_EnableOutput = lib.LD_EnableOutput
LD_EnableOutput.restype = c_short
LD_EnableOutput.argtypes = [POINTER(c_char)]
# *serialNo

LD_EnableTIAGainAdjust = lib.LD_EnableTIAGainAdjust
LD_EnableTIAGainAdjust.restype = c_short
LD_EnableTIAGainAdjust.argtypes = [POINTER(c_char), c_bool]
# *serialNo, enable

LD_FindTIAGain = lib.LD_FindTIAGain
LD_FindTIAGain.restype = c_short
LD_FindTIAGain.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetControlSource = lib.LD_GetControlSource
LD_GetControlSource.restype = LD_InputSourceFlags
LD_GetControlSource.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetDisplayUnits = lib.LD_GetDisplayUnits
LD_GetDisplayUnits.restype = LD_DisplayUnits
LD_GetDisplayUnits.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetFirmwareVersion = lib.LD_GetFirmwareVersion
LD_GetFirmwareVersion.restype = c_ulong
LD_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetHardwareInfo = lib.LD_GetHardwareInfo
LD_GetHardwareInfo.restype = c_short
LD_GetHardwareInfo.argtypes = [
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

LD_GetHardwareInfoBlock = lib.LD_GetHardwareInfoBlock
LD_GetHardwareInfoBlock.restype = c_short
LD_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]
# *serialNo, *hardwareInfo

LD_GetInterlockState = lib.LD_GetInterlockState
LD_GetInterlockState.restype = c_byte
LD_GetInterlockState.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetLEDBrightness = lib.LD_GetLEDBrightness
LD_GetLEDBrightness.restype = c_long
LD_GetLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetLaserDiodeCurrentReading = lib.LD_GetLaserDiodeCurrentReading
LD_GetLaserDiodeCurrentReading.restype = c_long
LD_GetLaserDiodeCurrentReading.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetLaserDiodeMaxCurrentLimit = lib.LD_GetLaserDiodeMaxCurrentLimit
LD_GetLaserDiodeMaxCurrentLimit.restype = c_long
LD_GetLaserDiodeMaxCurrentLimit.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetLaserPolarity = lib.LD_GetLaserPolarity
LD_GetLaserPolarity.restype = LD_POLARITY
LD_GetLaserPolarity.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetLaserSetPoint = lib.LD_GetLaserSetPoint
LD_GetLaserSetPoint.restype = c_long
LD_GetLaserSetPoint.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetMaxCurrentDigPot = lib.LD_GetMaxCurrentDigPot
LD_GetMaxCurrentDigPot.restype = c_long
LD_GetMaxCurrentDigPot.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetNextMessage = lib.LD_GetNextMessage
LD_GetNextMessage.restype = c_bool
LD_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]
# *serialNo, *messageType, *messageID, *messageData

LD_GetPhotoCurrentReading = lib.LD_GetPhotoCurrentReading
LD_GetPhotoCurrentReading.restype = c_long
LD_GetPhotoCurrentReading.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetSoftwareVersion = lib.LD_GetSoftwareVersion
LD_GetSoftwareVersion.restype = c_ulong
LD_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetStatusBits = lib.LD_GetStatusBits
LD_GetStatusBits.restype = c_ulong
LD_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetVoltageReading = lib.LD_GetVoltageReading
LD_GetVoltageReading.restype = c_long
LD_GetVoltageReading.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetWACalibFactor = lib.LD_GetWACalibFactor
LD_GetWACalibFactor.restype = c_float
LD_GetWACalibFactor.argtypes = [POINTER(c_char)]
# *serialNo

LD_HasLastMsgTimerOverrun = lib.LD_HasLastMsgTimerOverrun
LD_HasLastMsgTimerOverrun.restype = c_bool
LD_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

LD_Identify = lib.LD_Identify
LD_Identify.restype = c_void_p
LD_Identify.argtypes = [POINTER(c_char)]
# *serialNo

LD_LoadNamedSettings = lib.LD_LoadNamedSettings
LD_LoadNamedSettings.restype = c_bool
LD_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

LD_LoadSettings = lib.LD_LoadSettings
LD_LoadSettings.restype = c_bool
LD_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

LD_MessageQueueSize = lib.LD_MessageQueueSize
LD_MessageQueueSize.restype = c_int
LD_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

LD_Open = lib.LD_Open
LD_Open.restype = c_short
LD_Open.argtypes = [POINTER(c_char)]
# *serialNo

LD_PersistSettings = lib.LD_PersistSettings
LD_PersistSettings.restype = c_bool
LD_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

LD_PollingDuration = lib.LD_PollingDuration
LD_PollingDuration.restype = c_long
LD_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

LD_RegisterMessageCallback = lib.LD_RegisterMessageCallback
LD_RegisterMessageCallback.restype = c_void_p
LD_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNo, void

LD_RequestControlSource = lib.LD_RequestControlSource
LD_RequestControlSource.restype = c_short
LD_RequestControlSource.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestDisplay = lib.LD_RequestDisplay
LD_RequestDisplay.restype = c_short
LD_RequestDisplay.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestLaserDiodeMaxCurrentLimit = lib.LD_RequestLaserDiodeMaxCurrentLimit
LD_RequestLaserDiodeMaxCurrentLimit.restype = c_short
LD_RequestLaserDiodeMaxCurrentLimit.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestLaserPolarity = lib.LD_RequestLaserPolarity
LD_RequestLaserPolarity.restype = c_short
LD_RequestLaserPolarity.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestLaserSetPoint = lib.LD_RequestLaserSetPoint
LD_RequestLaserSetPoint.restype = c_short
LD_RequestLaserSetPoint.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestMaxCurrentDigPot = lib.LD_RequestMaxCurrentDigPot
LD_RequestMaxCurrentDigPot.restype = c_short
LD_RequestMaxCurrentDigPot.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestReadings = lib.LD_RequestReadings
LD_RequestReadings.restype = c_short
LD_RequestReadings.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestSettings = lib.LD_RequestSettings
LD_RequestSettings.restype = c_short
LD_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestStatus = lib.LD_RequestStatus
LD_RequestStatus.restype = c_short
LD_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestStatusBits = lib.LD_RequestStatusBits
LD_RequestStatusBits.restype = c_short
LD_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestWACalibFactor = lib.LD_RequestWACalibFactor
LD_RequestWACalibFactor.restype = c_short
LD_RequestWACalibFactor.argtypes = [POINTER(c_char)]
# *serialNo

LD_SetClosedLoopMode = lib.LD_SetClosedLoopMode
LD_SetClosedLoopMode.restype = c_short
LD_SetClosedLoopMode.argtypes = [POINTER(c_char)]
# *serialNo

LD_SetControlSource = lib.LD_SetControlSource
LD_SetControlSource.restype = c_short
LD_SetControlSource.argtypes = [POINTER(c_char), LD_InputSourceFlags]
# *serialNo, source

LD_SetDisplayUnits = lib.LD_SetDisplayUnits
LD_SetDisplayUnits.restype = c_short
LD_SetDisplayUnits.argtypes = [POINTER(c_char), LD_DisplayUnits]
# *serialNo, units

LD_SetLEDBrightness = lib.LD_SetLEDBrightness
LD_SetLEDBrightness.restype = c_short
LD_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
# *serialNo, brightness

LD_SetLaserPolarity = lib.LD_SetLaserPolarity
LD_SetLaserPolarity.restype = c_short
LD_SetLaserPolarity.argtypes = [POINTER(c_char), LD_POLARITY]
# *serialNo, polarity

LD_SetLaserSetPoint = lib.LD_SetLaserSetPoint
LD_SetLaserSetPoint.restype = c_short
LD_SetLaserSetPoint.argtypes = [POINTER(c_char), c_long]
# *serialNo, laserDiodeCurrent

LD_SetMaxCurrentDigPot = lib.LD_SetMaxCurrentDigPot
LD_SetMaxCurrentDigPot.restype = c_short
LD_SetMaxCurrentDigPot.argtypes = [POINTER(c_char), c_long]
# *serialNo, maxCurrent

LD_SetOpenLoopMode = lib.LD_SetOpenLoopMode
LD_SetOpenLoopMode.restype = c_short
LD_SetOpenLoopMode.argtypes = [POINTER(c_char)]
# *serialNo

LD_SetWACalibFactor = lib.LD_SetWACalibFactor
LD_SetWACalibFactor.restype = c_short
LD_SetWACalibFactor.argtypes = [POINTER(c_char), c_float]
# *serialNo, calibFactor

LD_StartPolling = lib.LD_StartPolling
LD_StartPolling.restype = c_bool
LD_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

LD_StopPolling = lib.LD_StopPolling
LD_StopPolling.restype = c_void_p
LD_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

LD_TimeSinceLastMsgReceived = lib.LD_TimeSinceLastMsgReceived
LD_TimeSinceLastMsgReceived.restype = c_bool
LD_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]
# *serialNo, &lastUpdateTimeMS

LD_WaitForMessage = lib.LD_WaitForMessage
LD_WaitForMessage.restype = c_bool
LD_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]
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
