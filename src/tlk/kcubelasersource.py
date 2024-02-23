from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KLD_TrigPolarity,
    KLD_TriggerMode,
    KLS_OpMode,
    KLS_TrigPolarity,
    KLS_TriggerMode,
    LS_InputSourceFlags)
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
    lib_path / "Thorlabs.MotionControl.KCube.LaserSource.DLL")
LS_CanDeviceLockFrontPanel = lib.LS_CanDeviceLockFrontPanel
LS_CanDeviceLockFrontPanel.restype = c_bool
LS_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
# *serialNo

LS_CheckConnection = lib.LS_CheckConnection
LS_CheckConnection.restype = c_bool
LS_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

LS_ClearMessageQueue = lib.LS_ClearMessageQueue
LS_ClearMessageQueue.restype = None
LS_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

LS_Close = lib.LS_Close
LS_Close.restype = None
LS_Close.argtypes = [POINTER(c_char)]
# *serialNo

LS_Disable = lib.LS_Disable
LS_Disable.restype = c_short
LS_Disable.argtypes = [POINTER(c_char)]
# *serialNo

LS_DisableOutput = lib.LS_DisableOutput
LS_DisableOutput.restype = c_short
LS_DisableOutput.argtypes = [POINTER(c_char)]
# *serialNo

LS_Enable = lib.LS_Enable
LS_Enable.restype = c_short
LS_Enable.argtypes = [POINTER(c_char)]
# *serialNo

LS_EnableLastMsgTimer = lib.LS_EnableLastMsgTimer
LS_EnableLastMsgTimer.restype = None
LS_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

LS_EnableOutput = lib.LS_EnableOutput
LS_EnableOutput.restype = c_short
LS_EnableOutput.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetControlSource = lib.LS_GetControlSource
LS_GetControlSource.restype = LS_InputSourceFlags
LS_GetControlSource.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetCurrentReading = lib.LS_GetCurrentReading
LS_GetCurrentReading.restype = c_long
LS_GetCurrentReading.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetFirmwareVersion = lib.LS_GetFirmwareVersion
LS_GetFirmwareVersion.restype = c_ulong
LS_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetFrontPanelLocked = lib.LS_GetFrontPanelLocked
LS_GetFrontPanelLocked.restype = c_bool
LS_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetHardwareInfo = lib.LS_GetHardwareInfo
LS_GetHardwareInfo.restype = c_short
LS_GetHardwareInfo.argtypes = [
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

LS_GetHardwareInfoBlock = lib.LS_GetHardwareInfoBlock
LS_GetHardwareInfoBlock.restype = c_short
LS_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

LS_GetInterlockState = lib.LS_GetInterlockState
LS_GetInterlockState.restype = c_byte
LS_GetInterlockState.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetLimits = lib.LS_GetLimits
LS_GetLimits.restype = c_short
LS_GetLimits.argtypes = [c_long, c_long, POINTER(c_char)]
# &maxCurrent, &maxPower, *serialNo

LS_GetMMIParams = lib.LS_GetMMIParams
LS_GetMMIParams.restype = c_short
LS_GetMMIParams.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetMMIParamsBlock = lib.LS_GetMMIParamsBlock
LS_GetMMIParamsBlock.restype = c_short
LS_GetMMIParamsBlock.argtypes = [KLD_MMIParams, KLS_MMIParams, POINTER(c_char)]
# *params, *params, *serialNo

LS_GetNextMessage = lib.LS_GetNextMessage
LS_GetNextMessage.restype = c_bool
LS_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

LS_GetOPMode = lib.LS_GetOPMode
LS_GetOPMode.restype = c_short
LS_GetOPMode.argtypes = [KLS_OpMode, POINTER(c_char)]
# *mode, *serialNo

LS_GetPowerReading = lib.LS_GetPowerReading
LS_GetPowerReading.restype = c_long
LS_GetPowerReading.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetPowerSet = lib.LS_GetPowerSet
LS_GetPowerSet.restype = c_long
LS_GetPowerSet.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetSoftwareVersion = lib.LS_GetSoftwareVersion
LS_GetSoftwareVersion.restype = c_ulong
LS_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

LS_GetStatusBits = lib.LS_GetStatusBits
LS_GetStatusBits.restype = c_ulong
LS_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

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

LS_GetWavelength = lib.LS_GetWavelength
LS_GetWavelength.restype = c_long
LS_GetWavelength.argtypes = [POINTER(c_char)]
# *serialNo

LS_HasLastMsgTimerOverrun = lib.LS_HasLastMsgTimerOverrun
LS_HasLastMsgTimerOverrun.restype = c_bool
LS_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

LS_Identify = lib.LS_Identify
LS_Identify.restype = None
LS_Identify.argtypes = [POINTER(c_char)]
# *serialNo

LS_LoadNamedSettings = lib.LS_LoadNamedSettings
LS_LoadNamedSettings.restype = c_bool
LS_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

LS_LoadSettings = lib.LS_LoadSettings
LS_LoadSettings.restype = c_bool
LS_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

LS_MessageQueueSize = lib.LS_MessageQueueSize
LS_MessageQueueSize.restype = c_int
LS_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

LS_Open = lib.LS_Open
LS_Open.restype = c_short
LS_Open.argtypes = [POINTER(c_char)]
# *serialNo

LS_PersistSettings = lib.LS_PersistSettings
LS_PersistSettings.restype = c_bool
LS_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

LS_PollingDuration = lib.LS_PollingDuration
LS_PollingDuration.restype = c_long
LS_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

LS_RegisterMessageCallback = lib.LS_RegisterMessageCallback
LS_RegisterMessageCallback.restype = None
LS_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

LS_RequestControlSource = lib.LS_RequestControlSource
LS_RequestControlSource.restype = c_short
LS_RequestControlSource.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestFrontPanelLocked = lib.LS_RequestFrontPanelLocked
LS_RequestFrontPanelLocked.restype = c_short
LS_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestLimits = lib.LS_RequestLimits
LS_RequestLimits.restype = c_short
LS_RequestLimits.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestMMIParams = lib.LS_RequestMMIParams
LS_RequestMMIParams.restype = c_short
LS_RequestMMIParams.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestOPMode = lib.LS_RequestOPMode
LS_RequestOPMode.restype = c_short
LS_RequestOPMode.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestReadings = lib.LS_RequestReadings
LS_RequestReadings.restype = c_short
LS_RequestReadings.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestSetPower = lib.LS_RequestSetPower
LS_RequestSetPower.restype = c_short
LS_RequestSetPower.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestSettings = lib.LS_RequestSettings
LS_RequestSettings.restype = c_short
LS_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestStatus = lib.LS_RequestStatus
LS_RequestStatus.restype = c_short
LS_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestStatusBits = lib.LS_RequestStatusBits
LS_RequestStatusBits.restype = c_short
LS_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestTrigIOParams = lib.LS_RequestTrigIOParams
LS_RequestTrigIOParams.restype = c_short
LS_RequestTrigIOParams.argtypes = [POINTER(c_char)]
# *serialNo

LS_RequestWavelength = lib.LS_RequestWavelength
LS_RequestWavelength.restype = c_short
LS_RequestWavelength.argtypes = [POINTER(c_char)]
# *serialNo

LS_SetControlSource = lib.LS_SetControlSource
LS_SetControlSource.restype = c_short
LS_SetControlSource.argtypes = [POINTER(c_char), LS_InputSourceFlags]
# *serialNo, source

LS_SetFrontPanelLock = lib.LS_SetFrontPanelLock
LS_SetFrontPanelLock.restype = c_short
LS_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
# *serialNo, locked

LS_SetMMIParams = lib.LS_SetMMIParams
LS_SetMMIParams.restype = c_short
LS_SetMMIParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, dispIntensity

LS_SetMMIParamsBlock = lib.LS_SetMMIParamsBlock
LS_SetMMIParamsBlock.restype = c_short
LS_SetMMIParamsBlock.argtypes = [KLD_MMIParams, KLS_MMIParams, POINTER(c_char)]
# *params, *params, *serialNo

LS_SetOPMode = lib.LS_SetOPMode
LS_SetOPMode.restype = c_short
LS_SetOPMode.argtypes = [POINTER(c_char), KLS_OpMode]
# *serialNo, mode

LS_SetPower = lib.LS_SetPower
LS_SetPower.restype = c_short
LS_SetPower.argtypes = [POINTER(c_char), c_long]
# *serialNo, power

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

LS_StartPolling = lib.LS_StartPolling
LS_StartPolling.restype = c_bool
LS_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

LS_StopPolling = lib.LS_StopPolling
LS_StopPolling.restype = None
LS_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

LS_TimeSinceLastMsgReceived = lib.LS_TimeSinceLastMsgReceived
LS_TimeSinceLastMsgReceived.restype = c_bool
LS_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

LS_WaitForMessage = lib.LS_WaitForMessage
LS_WaitForMessage.restype = c_bool
LS_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
