from ctypes import (POINTER, c_bool, c_byte, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    HubAnalogueModes,
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity,
    KPZ_WheelChangeRate,
    KPZ_WheelDirectionSense,
    KPZ_WheelMode,
    PZ_ControlModeTypes,
    PZ_InputSourceFlags)
from .definitions.structures import (
    KPZ_MMIParams,
    KPZ_TriggerConfig,
    PZ_FeedbackLoopConstants,
    PZ_LUTWaveParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation,
    TPZ_IOSettings)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.KCube.Piezo.DLL")
PCC_CanDeviceLockFrontPanel = lib.PCC_CanDeviceLockFrontPanel
PCC_CanDeviceLockFrontPanel.restype = c_bool
PCC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
# *serialNo

PCC_CheckConnection = lib.PCC_CheckConnection
PCC_CheckConnection.restype = c_bool
PCC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

PCC_ClearMessageQueue = lib.PCC_ClearMessageQueue
PCC_ClearMessageQueue.restype = None
PCC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

PCC_Close = lib.PCC_Close
PCC_Close.restype = None
PCC_Close.argtypes = [POINTER(c_char)]
# *serialNo

PCC_Disable = lib.PCC_Disable
PCC_Disable.restype = c_short
PCC_Disable.argtypes = [POINTER(c_char)]
# *serialNo

PCC_Disconnect = lib.PCC_Disconnect
PCC_Disconnect.restype = c_short
PCC_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

PCC_Enable = lib.PCC_Enable
PCC_Enable.restype = c_short
PCC_Enable.argtypes = [POINTER(c_char)]
# *serialNo

PCC_EnableLastMsgTimer = lib.PCC_EnableLastMsgTimer
PCC_EnableLastMsgTimer.restype = None
PCC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

PCC_GetDigitalOutputs = lib.PCC_GetDigitalOutputs
PCC_GetDigitalOutputs.restype = c_byte
PCC_GetDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetFeedbackLoopPIconsts = lib.PCC_GetFeedbackLoopPIconsts
PCC_GetFeedbackLoopPIconsts.restype = c_short
PCC_GetFeedbackLoopPIconsts.argtypes = [c_short, c_short, POINTER(c_char)]
# *integralTerm, *proportionalTerm, *serialNo

PCC_GetFeedbackLoopPIconstsBlock = lib.PCC_GetFeedbackLoopPIconstsBlock
PCC_GetFeedbackLoopPIconstsBlock.restype = c_short
PCC_GetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char)]
# *proportionalAndIntegralConstants, *serialNo

PCC_GetFirmwareVersion = lib.PCC_GetFirmwareVersion
PCC_GetFirmwareVersion.restype = c_ulong
PCC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetFrontPanelLocked = lib.PCC_GetFrontPanelLocked
PCC_GetFrontPanelLocked.restype = c_bool
PCC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetHardwareInfo = lib.PCC_GetHardwareInfo
PCC_GetHardwareInfo.restype = c_short
PCC_GetHardwareInfo.argtypes = [
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

PCC_GetHardwareInfoBlock = lib.PCC_GetHardwareInfoBlock
PCC_GetHardwareInfoBlock.restype = c_short
PCC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

PCC_GetHubAnalogInput = lib.PCC_GetHubAnalogInput
PCC_GetHubAnalogInput.restype = HubAnalogueModes
PCC_GetHubAnalogInput.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetIOSettings = lib.PCC_GetIOSettings
PCC_GetIOSettings.restype = TPZ_IOSettings
PCC_GetIOSettings.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetLEDBrightness = lib.PCC_GetLEDBrightness
PCC_GetLEDBrightness.restype = c_short
PCC_GetLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetMMIParams = lib.PCC_GetMMIParams
PCC_GetMMIParams.restype = c_short
PCC_GetMMIParams.argtypes = [
    KPZ_WheelDirectionSense,
    c_int16,
    c_int32,
    c_int32,
    POINTER(c_char),
    KPZ_WheelChangeRate,
    c_int32,
    KPZ_WheelMode]
# *directionSense, *displayIntensity, *presetVoltage1, *presetVoltage2, *serialNo, *voltageAdjustRate, *voltageStep, *wheelMode

PCC_GetMMIParamsBlock = lib.PCC_GetMMIParamsBlock
PCC_GetMMIParamsBlock.restype = c_short
PCC_GetMMIParamsBlock.argtypes = [KPZ_MMIParams, POINTER(c_char)]
# *mmiParams, *serialNo

PCC_GetMMIParamsExt = lib.PCC_GetMMIParamsExt
PCC_GetMMIParamsExt.restype = c_short
PCC_GetMMIParamsExt.argtypes = [KPZ_WheelDirectionSense, c_int16, c_int16, c_int16,
                                c_int32, c_int32, POINTER(c_char), KPZ_WheelChangeRate, c_int32, KPZ_WheelMode]
# *directionSense, *displayDimIntensity, *displayIntensity, *displayTimeout, *presetVoltage1, *presetVoltage2, *serialNo, *voltageAdjustRate, *voltageStep, *wheelMode

PCC_GetMaxOutputVoltage = lib.PCC_GetMaxOutputVoltage
PCC_GetMaxOutputVoltage.restype = c_short
PCC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetNextMessage = lib.PCC_GetNextMessage
PCC_GetNextMessage.restype = c_bool
PCC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

PCC_GetOutputVoltage = lib.PCC_GetOutputVoltage
PCC_GetOutputVoltage.restype = c_short
PCC_GetOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetPosition = lib.PCC_GetPosition
PCC_GetPosition.restype = c_long
PCC_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetPositionControlMode = lib.PCC_GetPositionControlMode
PCC_GetPositionControlMode.restype = PZ_ControlModeTypes
PCC_GetPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetSoftwareVersion = lib.PCC_GetSoftwareVersion
PCC_GetSoftwareVersion.restype = c_ulong
PCC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetStatusBits = lib.PCC_GetStatusBits
PCC_GetStatusBits.restype = c_ulong
PCC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PCC_GetTriggerConfigParams = lib.PCC_GetTriggerConfigParams
PCC_GetTriggerConfigParams.restype = c_short
PCC_GetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity,
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity]
# *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity

PCC_GetTriggerConfigParamsBlock = lib.PCC_GetTriggerConfigParamsBlock
PCC_GetTriggerConfigParamsBlock.restype = c_short
PCC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPZ_TriggerConfig]
# *serialNo, *triggerConfigParams

PCC_GetVoltageSource = lib.PCC_GetVoltageSource
PCC_GetVoltageSource.restype = PZ_InputSourceFlags
PCC_GetVoltageSource.argtypes = [POINTER(c_char)]
# *serialNo

PCC_HasLastMsgTimerOverrun = lib.PCC_HasLastMsgTimerOverrun
PCC_HasLastMsgTimerOverrun.restype = c_bool
PCC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

PCC_Identify = lib.PCC_Identify
PCC_Identify.restype = None
PCC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

PCC_LoadNamedSettings = lib.PCC_LoadNamedSettings
PCC_LoadNamedSettings.restype = c_bool
PCC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

PCC_LoadSettings = lib.PCC_LoadSettings
PCC_LoadSettings.restype = c_bool
PCC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

PCC_MessageQueueSize = lib.PCC_MessageQueueSize
PCC_MessageQueueSize.restype = c_int
PCC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

PCC_Open = lib.PCC_Open
PCC_Open.restype = c_short
PCC_Open.argtypes = [POINTER(c_char)]
# *serialNo

PCC_PersistSettings = lib.PCC_PersistSettings
PCC_PersistSettings.restype = c_bool
PCC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

PCC_PollingDuration = lib.PCC_PollingDuration
PCC_PollingDuration.restype = c_long
PCC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RegisterMessageCallback = lib.PCC_RegisterMessageCallback
PCC_RegisterMessageCallback.restype = None
PCC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

PCC_RequestActualPosition = lib.PCC_RequestActualPosition
PCC_RequestActualPosition.restype = c_short
PCC_RequestActualPosition.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestDigitalOutputs = lib.PCC_RequestDigitalOutputs
PCC_RequestDigitalOutputs.restype = c_short
PCC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestFeedbackLoopPIconsts = lib.PCC_RequestFeedbackLoopPIconsts
PCC_RequestFeedbackLoopPIconsts.restype = c_bool
PCC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestFrontPanelLocked = lib.PCC_RequestFrontPanelLocked
PCC_RequestFrontPanelLocked.restype = c_short
PCC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestIOSettings = lib.PCC_RequestIOSettings
PCC_RequestIOSettings.restype = c_bool
PCC_RequestIOSettings.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestLEDBrightness = lib.PCC_RequestLEDBrightness
PCC_RequestLEDBrightness.restype = c_bool
PCC_RequestLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestMMIParams = lib.PCC_RequestMMIParams
PCC_RequestMMIParams.restype = c_bool
PCC_RequestMMIParams.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestMaxOutputVoltage = lib.PCC_RequestMaxOutputVoltage
PCC_RequestMaxOutputVoltage.restype = c_bool
PCC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestOutputVoltage = lib.PCC_RequestOutputVoltage
PCC_RequestOutputVoltage.restype = c_short
PCC_RequestOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestPosition = lib.PCC_RequestPosition
PCC_RequestPosition.restype = c_short
PCC_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestPositionControlMode = lib.PCC_RequestPositionControlMode
PCC_RequestPositionControlMode.restype = c_short
PCC_RequestPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestSettings = lib.PCC_RequestSettings
PCC_RequestSettings.restype = c_short
PCC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestStatus = lib.PCC_RequestStatus
PCC_RequestStatus.restype = c_short
PCC_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestStatusBits = lib.PCC_RequestStatusBits
PCC_RequestStatusBits.restype = c_short
PCC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestTriggerConfigParams = lib.PCC_RequestTriggerConfigParams
PCC_RequestTriggerConfigParams.restype = c_bool
PCC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
# *serialNo

PCC_RequestVoltageSource = lib.PCC_RequestVoltageSource
PCC_RequestVoltageSource.restype = c_bool
PCC_RequestVoltageSource.argtypes = [POINTER(c_char)]
# *serialNo

PCC_SetDigitalOutputs = lib.PCC_SetDigitalOutputs
PCC_SetDigitalOutputs.restype = c_short
PCC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
# *serialNo, outputsBits

PCC_SetFeedbackLoopPIconsts = lib.PCC_SetFeedbackLoopPIconsts
PCC_SetFeedbackLoopPIconsts.restype = c_short
PCC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short]
# *serialNo, integralTerm, proportionalTerm

PCC_SetFeedbackLoopPIconstsBlock = lib.PCC_SetFeedbackLoopPIconstsBlock
PCC_SetFeedbackLoopPIconstsBlock.restype = c_short
PCC_SetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char)]
# *proportionalAndIntegralConstants, *serialNo

PCC_SetFrontPanelLock = lib.PCC_SetFrontPanelLock
PCC_SetFrontPanelLock.restype = c_short
PCC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
# *serialNo, locked

PCC_SetHubAnalogInput = lib.PCC_SetHubAnalogInput
PCC_SetHubAnalogInput.restype = c_short
PCC_SetHubAnalogInput.argtypes = [POINTER(c_char), HubAnalogueModes]
# *serialNo, hubAnalogInput

PCC_SetIOSettings = lib.PCC_SetIOSettings
PCC_SetIOSettings.restype = c_short
PCC_SetIOSettings.argtypes = [POINTER(c_char), TPZ_IOSettings]
# *serialNo, ioSettings

PCC_SetLEDBrightness = lib.PCC_SetLEDBrightness
PCC_SetLEDBrightness.restype = c_short
PCC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
# *serialNo, brightness

PCC_SetLUTwaveParams = lib.PCC_SetLUTwaveParams
PCC_SetLUTwaveParams.restype = c_short
PCC_SetLUTwaveParams.argtypes = [PZ_LUTWaveParameters, POINTER(c_char)]
# *LUTwaveParams, *serialNo

PCC_SetLUTwaveSample = lib.PCC_SetLUTwaveSample
PCC_SetLUTwaveSample.restype = c_short
PCC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, index, value

PCC_SetMMIParams = lib.PCC_SetMMIParams
PCC_SetMMIParams.restype = c_short
PCC_SetMMIParams.argtypes = [
    POINTER(c_char),
    KPZ_WheelDirectionSense,
    c_int16,
    c_int32,
    c_int32,
    KPZ_WheelChangeRate,
    c_int32,
    KPZ_WheelMode]
# *serialNo, directionSense, displayIntensity, presetVoltage1, presetVoltage2, voltageAdjustRate, voltageStep, wheelMode

PCC_SetMMIParamsBlock = lib.PCC_SetMMIParamsBlock
PCC_SetMMIParamsBlock.restype = c_short
PCC_SetMMIParamsBlock.argtypes = [KPZ_MMIParams, POINTER(c_char)]
# *mmiParams, *serialNo

PCC_SetMMIParamsExt = lib.PCC_SetMMIParamsExt
PCC_SetMMIParamsExt.restype = c_short
PCC_SetMMIParamsExt.argtypes = [
    POINTER(c_char),
    KPZ_WheelDirectionSense,
    c_int16,
    c_int16,
    c_int16,
    c_int32,
    c_int32,
    KPZ_WheelChangeRate,
    c_int32,
    KPZ_WheelMode]
# *serialNo, directionSense, displayDimIntensity, displayIntensity, displayTimeout, presetVoltage1, presetVoltage2, voltageAdjustRate, voltageStep, wheelMode

PCC_SetMaxOutputVoltage = lib.PCC_SetMaxOutputVoltage
PCC_SetMaxOutputVoltage.restype = c_short
PCC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, maxVoltage

PCC_SetOutputVoltage = lib.PCC_SetOutputVoltage
PCC_SetOutputVoltage.restype = c_short
PCC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, volts

PCC_SetPosition = lib.PCC_SetPosition
PCC_SetPosition.restype = c_short
PCC_SetPosition.argtypes = [POINTER(c_char), c_long]
# *serialNo, position

PCC_SetPositionControlMode = lib.PCC_SetPositionControlMode
PCC_SetPositionControlMode.restype = c_short
PCC_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
# *serialNo, mode

PCC_SetPositionToTolerance = lib.PCC_SetPositionToTolerance
PCC_SetPositionToTolerance.restype = c_short
PCC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_long, c_long]
# *serialNo, position, tolerance

PCC_SetTriggerConfigParams = lib.PCC_SetTriggerConfigParams
PCC_SetTriggerConfigParams.restype = c_short
PCC_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity,
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity]
# *serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

PCC_SetTriggerConfigParamsBlock = lib.PCC_SetTriggerConfigParamsBlock
PCC_SetTriggerConfigParamsBlock.restype = c_short
PCC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPZ_TriggerConfig]
# *serialNo, *triggerConfigParams

PCC_SetVoltageSource = lib.PCC_SetVoltageSource
PCC_SetVoltageSource.restype = c_short
PCC_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]
# *serialNo, source

PCC_SetZero = lib.PCC_SetZero
PCC_SetZero.restype = c_bool
PCC_SetZero.argtypes = [POINTER(c_char)]
# *serialNo

PCC_StartLUTwave = lib.PCC_StartLUTwave
PCC_StartLUTwave.restype = c_short
PCC_StartLUTwave.argtypes = [POINTER(c_char)]
# *serialNo

PCC_StartPolling = lib.PCC_StartPolling
PCC_StartPolling.restype = c_bool
PCC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

PCC_StopLUTwave = lib.PCC_StopLUTwave
PCC_StopLUTwave.restype = c_short
PCC_StopLUTwave.argtypes = [POINTER(c_char)]
# *serialNo

PCC_StopPolling = lib.PCC_StopPolling
PCC_StopPolling.restype = None
PCC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

PCC_TimeSinceLastMsgReceived = lib.PCC_TimeSinceLastMsgReceived
PCC_TimeSinceLastMsgReceived.restype = c_bool
PCC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

PCC_WaitForMessage = lib.PCC_WaitForMessage
PCC_WaitForMessage.restype = c_bool
PCC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
