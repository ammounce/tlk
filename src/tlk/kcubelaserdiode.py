from ctypes import (POINTER, c_bool, c_char, c_float, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KLD_RAMPUP,
    KLD_TrigPolarity,
    KLD_TriggerMode,
    KLS_TrigPolarity,
    KLS_TriggerMode,
    LD_DisplayUnits,
    LD_InputSourceFlags,
    LD_POLARITY)
from .definitions.structures import (
    KLD_MMIParams,
    KLD_TrigIOParams,
    KLS_MMIParams,
    KLS_TrigIOParams,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.KCube.LaserDiode.dll")
LD_CanDeviceLockFrontPanel = lib.LD_CanDeviceLockFrontPanel
LD_CanDeviceLockFrontPanel.restype = c_bool
LD_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
# *serialNo

LD_CheckConnection = lib.LD_CheckConnection
LD_CheckConnection.restype = c_bool
LD_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

LD_ClearMessageQueue = lib.LD_ClearMessageQueue
LD_ClearMessageQueue.restype = None
LD_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

LD_Close = lib.LD_Close
LD_Close.restype = None
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
LD_EnableLastMsgTimer.restype = None
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

LD_GetFrontPanelLocked = lib.LD_GetFrontPanelLocked
LD_GetFrontPanelLocked.restype = c_bool
LD_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetHardwareInfo = lib.LD_GetHardwareInfo
LD_GetHardwareInfo.restype = c_short
LD_GetHardwareInfo.argtypes = [
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

LD_GetHardwareInfoBlock = lib.LD_GetHardwareInfoBlock
LD_GetHardwareInfoBlock.restype = c_short
LD_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

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
LD_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

LD_GetPhotoCurrentReading = lib.LD_GetPhotoCurrentReading
LD_GetPhotoCurrentReading.restype = c_long
LD_GetPhotoCurrentReading.argtypes = [POINTER(c_char)]
# *serialNo

LD_GetRampupMode = lib.LD_GetRampupMode
LD_GetRampupMode.restype = KLD_RAMPUP
LD_GetRampupMode.argtypes = [POINTER(c_char)]
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
LD_Identify.restype = None
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
LD_RegisterMessageCallback.restype = None
LD_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

LD_RequestControlSource = lib.LD_RequestControlSource
LD_RequestControlSource.restype = c_short
LD_RequestControlSource.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestDisplay = lib.LD_RequestDisplay
LD_RequestDisplay.restype = c_short
LD_RequestDisplay.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestFrontPanelLocked = lib.LD_RequestFrontPanelLocked
LD_RequestFrontPanelLocked.restype = c_short
LD_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestLaserPolarity = lib.LD_RequestLaserPolarity
LD_RequestLaserPolarity.restype = c_short
LD_RequestLaserPolarity.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestLaserSetPoint = lib.LD_RequestLaserSetPoint
LD_RequestLaserSetPoint.restype = c_short
LD_RequestLaserSetPoint.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestMaxCurrent = lib.LD_RequestMaxCurrent
LD_RequestMaxCurrent.restype = c_short
LD_RequestMaxCurrent.argtypes = [POINTER(c_char)]
# *serialNo

LD_RequestRampupMode = lib.LD_RequestRampupMode
LD_RequestRampupMode.restype = c_short
LD_RequestRampupMode.argtypes = [POINTER(c_char)]
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

LD_SetFrontPanelLock = lib.LD_SetFrontPanelLock
LD_SetFrontPanelLock.restype = c_short
LD_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
# *serialNo, locked

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

LD_SetMaxCurrent = lib.LD_SetMaxCurrent
LD_SetMaxCurrent.restype = c_short
LD_SetMaxCurrent.argtypes = [POINTER(c_char), c_long]
# *serialNo, maxCurrent

LD_SetOpenLoopMode = lib.LD_SetOpenLoopMode
LD_SetOpenLoopMode.restype = c_short
LD_SetOpenLoopMode.argtypes = [POINTER(c_char)]
# *serialNo

LD_SetRampupMode = lib.LD_SetRampupMode
LD_SetRampupMode.restype = c_short
LD_SetRampupMode.argtypes = [POINTER(c_char), KLD_RAMPUP]
# *serialNo, rampupMode

LD_SetWACalibFactor = lib.LD_SetWACalibFactor
LD_SetWACalibFactor.restype = c_short
LD_SetWACalibFactor.argtypes = [POINTER(c_char), c_float]
# *serialNo, calibFactor

LD_StartPolling = lib.LD_StartPolling
LD_StartPolling.restype = c_bool
LD_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

LD_StopFindTIAGain = lib.LD_StopFindTIAGain
LD_StopFindTIAGain.restype = c_short
LD_StopFindTIAGain.argtypes = [POINTER(c_char)]
# *serialNo

LD_StopPolling = lib.LD_StopPolling
LD_StopPolling.restype = None
LD_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

LD_TimeSinceLastMsgReceived = lib.LD_TimeSinceLastMsgReceived
LD_TimeSinceLastMsgReceived.restype = c_bool
LD_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

LD_WaitForMessage = lib.LD_WaitForMessage
LD_WaitForMessage.restype = c_bool
LD_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

LS_GetMMIParams = lib.LS_GetMMIParams
LS_GetMMIParams.restype = c_short
LS_GetMMIParams.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetMMIParamsBlock = lib.LS_GetMMIParamsBlock
LS_GetMMIParamsBlock.restype = c_short
LS_GetMMIParamsBlock.argtypes = [KLD_MMIParams, KLS_MMIParams, POINTER(c_char)]
# *params, *params, *serialNo

LS_GetTrigIOParams = lib.LS_GetTrigIOParams
LS_GetTrigIOParams.restype = c_short
LS_GetTrigIOParams.argtypes = [
    KLD_TriggerMode,
    KLS_TriggerMode,
    KLD_TriggerMode,
    KLS_TriggerMode,
    KLD_TrigPolarity,
    KLS_TrigPolarity,
    KLD_TrigPolarity,
    KLS_TrigPolarity,
    POINTER(c_char)]
# *mode1, *mode1, *mode2, *mode2, *polarity1, *polarity1, *polarity2, *polarity2, *serialNo

LS_GetTrigIOParamsBlock = lib.LS_GetTrigIOParamsBlock
LS_GetTrigIOParamsBlock.restype = c_short
LS_GetTrigIOParamsBlock.argtypes = [KLD_TrigIOParams, KLS_TrigIOParams, POINTER(c_char)]
# *params, *params, *serialNo

LS_RequestMMIParams = lib.LS_RequestMMIParams
LS_RequestMMIParams.restype = c_short
LS_RequestMMIParams.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestTrigIOParams = lib.LS_RequestTrigIOParams
LS_RequestTrigIOParams.restype = c_short
LS_RequestTrigIOParams.argtypes = [POINTER(c_char)]
# *serialNo

LS_SetMMIParams = lib.LS_SetMMIParams
LS_SetMMIParams.restype = c_short
LS_SetMMIParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, dispIntensity

LS_SetMMIParamsBlock = lib.LS_SetMMIParamsBlock
LS_SetMMIParamsBlock.restype = c_short
LS_SetMMIParamsBlock.argtypes = [KLD_MMIParams, KLS_MMIParams, POINTER(c_char)]
# *params, *params, *serialNo

LS_SetTrigIOParams = lib.LS_SetTrigIOParams
LS_SetTrigIOParams.restype = c_short
LS_SetTrigIOParams.argtypes = [
    POINTER(c_char),
    KLD_TriggerMode,
    KLS_TriggerMode,
    KLD_TriggerMode,
    KLS_TriggerMode,
    KLD_TrigPolarity,
    KLS_TrigPolarity,
    KLD_TrigPolarity,
    KLS_TrigPolarity]
# *serialNo, mode1, mode1, mode2, mode2, polarity1, polarity1, polarity2, polarity2

LS_SetTrigIOParamsBlock = lib.LS_SetTrigIOParamsBlock
LS_SetTrigIOParamsBlock.restype = c_short
LS_SetTrigIOParamsBlock.argtypes = [KLD_TrigIOParams, KLS_TrigIOParams, POINTER(c_char)]
# *params, *params, *serialNo

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
