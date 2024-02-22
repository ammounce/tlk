from ctypes import (POINTER, c_bool, c_byte, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (
    KPC_HubAnalogueModes,
    KPC_IOSettings,
    KPC_MonitorOutputMode,
    KPC_TriggerPortMode,
    KPC_TriggerPortPolarity,
    KPZ_WheelChangeRate,
    KPZ_WheelDirectionSense,
    KPZ_WheelMode,
    PZ_ControlModeTypes,
    PZ_InputSourceFlags)
from .definitions.structures import (
    KPC_MMIParams,
    KPC_TriggerConfig,
    PZ_FeedbackLoopConstants,
    PZ_LUTWaveParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.KCube.PiezoStrainGauge.DLL")
KPC_CanDeviceLockFrontPanel = lib.KPC_CanDeviceLockFrontPanel
KPC_CanDeviceLockFrontPanel.restype = c_bool
KPC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
# *serialNo

KPC_CheckConnection = lib.KPC_CheckConnection
KPC_CheckConnection.restype = c_bool
KPC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

KPC_ClearMessageQueue = lib.KPC_ClearMessageQueue
KPC_ClearMessageQueue.restype = None
KPC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

KPC_Close = lib.KPC_Close
KPC_Close.restype = None
KPC_Close.argtypes = [POINTER(c_char)]
# *serialNo

KPC_Disable = lib.KPC_Disable
KPC_Disable.restype = c_short
KPC_Disable.argtypes = [POINTER(c_char)]
# *serialNo

KPC_Disconnect = lib.KPC_Disconnect
KPC_Disconnect.restype = c_short
KPC_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

KPC_Enable = lib.KPC_Enable
KPC_Enable.restype = c_short
KPC_Enable.argtypes = [POINTER(c_char)]
# *serialNo

KPC_EnableLastMsgTimer = lib.KPC_EnableLastMsgTimer
KPC_EnableLastMsgTimer.restype = None
KPC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

KPC_GetDigitalOutputs = lib.KPC_GetDigitalOutputs
KPC_GetDigitalOutputs.restype = c_byte
KPC_GetDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetFeedbackLoopPIconsts = lib.KPC_GetFeedbackLoopPIconsts
KPC_GetFeedbackLoopPIconsts.restype = c_short
KPC_GetFeedbackLoopPIconsts.argtypes = [c_short, c_short, POINTER(c_char)]
# *integralTerm, *proportionalTerm, *serialNo

KPC_GetFeedbackLoopPIconstsBlock = lib.KPC_GetFeedbackLoopPIconstsBlock
KPC_GetFeedbackLoopPIconstsBlock.restype = c_short
KPC_GetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char)]
# *proportionalAndIntegralConstants, *serialNo

KPC_GetFirmwareVersion = lib.KPC_GetFirmwareVersion
KPC_GetFirmwareVersion.restype = c_ulong
KPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetFrontPanelLocked = lib.KPC_GetFrontPanelLocked
KPC_GetFrontPanelLocked.restype = c_bool
KPC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetHardwareInfo = lib.KPC_GetHardwareInfo
KPC_GetHardwareInfo.restype = c_short
KPC_GetHardwareInfo.argtypes = [
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

KPC_GetHardwareInfoBlock = lib.KPC_GetHardwareInfoBlock
KPC_GetHardwareInfoBlock.restype = c_short
KPC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

KPC_GetHardwareMaxOutputVoltage = lib.KPC_GetHardwareMaxOutputVoltage
KPC_GetHardwareMaxOutputVoltage.restype = c_short
KPC_GetHardwareMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetHubAnalogInput = lib.KPC_GetHubAnalogInput
KPC_GetHubAnalogInput.restype = KPC_HubAnalogueModes
KPC_GetHubAnalogInput.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetIOSettings = lib.KPC_GetIOSettings
KPC_GetIOSettings.restype = KPC_IOSettings
KPC_GetIOSettings.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetLEDBrightness = lib.KPC_GetLEDBrightness
KPC_GetLEDBrightness.restype = c_short
KPC_GetLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetMMIParams = lib.KPC_GetMMIParams
KPC_GetMMIParams.restype = c_short
KPC_GetMMIParams.argtypes = [
    KPZ_WheelDirectionSense,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    POINTER(c_char),
    KPZ_WheelChangeRate,
    c_int16,
    KPZ_WheelMode]
# *directionSense, *displayIntensity, *positionStep, *presetPosition1, *presetPosition2, *presetVoltage1, *presetVoltage2, *serialNo, *voltageAdjustRate, *voltageStep, *wheelMode

KPC_GetMMIParamsBlock = lib.KPC_GetMMIParamsBlock
KPC_GetMMIParamsBlock.restype = c_short
KPC_GetMMIParamsBlock.argtypes = [KPC_MMIParams, POINTER(c_char)]
# *mmiParams, *serialNo

KPC_GetMMIParamsExt = lib.KPC_GetMMIParamsExt
KPC_GetMMIParamsExt.restype = c_short
KPC_GetMMIParamsExt.argtypes = [
    KPZ_WheelDirectionSense,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    POINTER(c_char),
    KPZ_WheelChangeRate,
    c_int16,
    KPZ_WheelMode]
# *directionSense, *displayDimIntensity, *displayIntensity, *displayTimeout, *positionStep, *presetPosition1, *presetPosition2, *presetVoltage1, *presetVoltage2, *serialNo, *voltageAdjustRate, *voltageStep, *wheelMode

KPC_GetMaxOutputVoltage = lib.KPC_GetMaxOutputVoltage
KPC_GetMaxOutputVoltage.restype = c_short
KPC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetMaximumTravel = lib.KPC_GetMaximumTravel
KPC_GetMaximumTravel.restype = c_long
KPC_GetMaximumTravel.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetNextMessage = lib.KPC_GetNextMessage
KPC_GetNextMessage.restype = c_bool
KPC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

KPC_GetOutputVoltage = lib.KPC_GetOutputVoltage
KPC_GetOutputVoltage.restype = c_short
KPC_GetOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetPosition = lib.KPC_GetPosition
KPC_GetPosition.restype = c_long
KPC_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetPositionControlMode = lib.KPC_GetPositionControlMode
KPC_GetPositionControlMode.restype = PZ_ControlModeTypes
KPC_GetPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetSoftwareVersion = lib.KPC_GetSoftwareVersion
KPC_GetSoftwareVersion.restype = c_ulong
KPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetStatusBits = lib.KPC_GetStatusBits
KPC_GetStatusBits.restype = c_ulong
KPC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

KPC_GetTriggerConfigParams = lib.KPC_GetTriggerConfigParams
KPC_GetTriggerConfigParams.restype = c_short
KPC_GetTriggerConfigParams.argtypes = [
    c_int32,
    c_int16,
    KPC_MonitorOutputMode,
    c_int16,
    POINTER(c_char),
    c_int16,
    KPC_TriggerPortMode,
    KPC_TriggerPortPolarity,
    KPC_TriggerPortMode,
    KPC_TriggerPortPolarity,
    c_int32]
# *lowerLimit, *monitorFilterFrequency, *monitorOutput, *monitorOutputSoftwareValue, *serialNo, *smoothingSamples, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity, *upperLimit

KPC_GetTriggerConfigParamsBlock = lib.KPC_GetTriggerConfigParamsBlock
KPC_GetTriggerConfigParamsBlock.restype = c_short
KPC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPC_TriggerConfig]
# *serialNo, *triggerConfigParams

KPC_GetVoltageSource = lib.KPC_GetVoltageSource
KPC_GetVoltageSource.restype = PZ_InputSourceFlags
KPC_GetVoltageSource.argtypes = [POINTER(c_char)]
# *serialNo

KPC_HasLastMsgTimerOverrun = lib.KPC_HasLastMsgTimerOverrun
KPC_HasLastMsgTimerOverrun.restype = c_bool
KPC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

KPC_Identify = lib.KPC_Identify
KPC_Identify.restype = None
KPC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

KPC_LoadNamedSettings = lib.KPC_LoadNamedSettings
KPC_LoadNamedSettings.restype = c_bool
KPC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

KPC_LoadSettings = lib.KPC_LoadSettings
KPC_LoadSettings.restype = c_bool
KPC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

KPC_MessageQueueSize = lib.KPC_MessageQueueSize
KPC_MessageQueueSize.restype = c_int
KPC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

KPC_Open = lib.KPC_Open
KPC_Open.restype = c_short
KPC_Open.argtypes = [POINTER(c_char)]
# *serialNo

KPC_PersistSettings = lib.KPC_PersistSettings
KPC_PersistSettings.restype = c_bool
KPC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

KPC_PollingDuration = lib.KPC_PollingDuration
KPC_PollingDuration.restype = c_long
KPC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RegisterMessageCallback = lib.KPC_RegisterMessageCallback
KPC_RegisterMessageCallback.restype = None
KPC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

KPC_RequestActualPosition = lib.KPC_RequestActualPosition
KPC_RequestActualPosition.restype = c_short
KPC_RequestActualPosition.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestDigitalOutputs = lib.KPC_RequestDigitalOutputs
KPC_RequestDigitalOutputs.restype = c_short
KPC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestFeedbackLoopPIconsts = lib.KPC_RequestFeedbackLoopPIconsts
KPC_RequestFeedbackLoopPIconsts.restype = c_bool
KPC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestFrontPanelLocked = lib.KPC_RequestFrontPanelLocked
KPC_RequestFrontPanelLocked.restype = c_short
KPC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestHardwareMaxOutputVoltage = lib.KPC_RequestHardwareMaxOutputVoltage
KPC_RequestHardwareMaxOutputVoltage.restype = c_bool
KPC_RequestHardwareMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestIOSettings = lib.KPC_RequestIOSettings
KPC_RequestIOSettings.restype = c_bool
KPC_RequestIOSettings.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestLEDBrightness = lib.KPC_RequestLEDBrightness
KPC_RequestLEDBrightness.restype = c_bool
KPC_RequestLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestMMIParams = lib.KPC_RequestMMIParams
KPC_RequestMMIParams.restype = c_bool
KPC_RequestMMIParams.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestMaxOutputVoltage = lib.KPC_RequestMaxOutputVoltage
KPC_RequestMaxOutputVoltage.restype = c_bool
KPC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestMaximumTravel = lib.KPC_RequestMaximumTravel
KPC_RequestMaximumTravel.restype = c_short
KPC_RequestMaximumTravel.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestOutputVoltage = lib.KPC_RequestOutputVoltage
KPC_RequestOutputVoltage.restype = c_short
KPC_RequestOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestPosition = lib.KPC_RequestPosition
KPC_RequestPosition.restype = c_short
KPC_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestPositionControlMode = lib.KPC_RequestPositionControlMode
KPC_RequestPositionControlMode.restype = c_bool
KPC_RequestPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestSettings = lib.KPC_RequestSettings
KPC_RequestSettings.restype = c_short
KPC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestStatus = lib.KPC_RequestStatus
KPC_RequestStatus.restype = c_short
KPC_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestStatusBits = lib.KPC_RequestStatusBits
KPC_RequestStatusBits.restype = c_short
KPC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestTriggerConfigParams = lib.KPC_RequestTriggerConfigParams
KPC_RequestTriggerConfigParams.restype = c_short
KPC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
# *serialNo

KPC_RequestVoltageSource = lib.KPC_RequestVoltageSource
KPC_RequestVoltageSource.restype = c_bool
KPC_RequestVoltageSource.argtypes = [POINTER(c_char)]
# *serialNo

KPC_ResetParameters = lib.KPC_ResetParameters
KPC_ResetParameters.restype = c_short
KPC_ResetParameters.argtypes = [POINTER(c_char)]
# *serialNo

KPC_SetDigitalOutputs = lib.KPC_SetDigitalOutputs
KPC_SetDigitalOutputs.restype = c_short
KPC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
# *serialNo, outputsBits

KPC_SetFeedbackLoopPIconsts = lib.KPC_SetFeedbackLoopPIconsts
KPC_SetFeedbackLoopPIconsts.restype = c_short
KPC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short]
# *serialNo, integralTerm, proportionalTerm

KPC_SetFeedbackLoopPIconstsBlock = lib.KPC_SetFeedbackLoopPIconstsBlock
KPC_SetFeedbackLoopPIconstsBlock.restype = c_short
KPC_SetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char)]
# *proportionalAndIntegralConstants, *serialNo

KPC_SetFrontPanelLock = lib.KPC_SetFrontPanelLock
KPC_SetFrontPanelLock.restype = c_short
KPC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
# *serialNo, locked

KPC_SetHardwareMaxOutputVoltage = lib.KPC_SetHardwareMaxOutputVoltage
KPC_SetHardwareMaxOutputVoltage.restype = c_short
KPC_SetHardwareMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, hardwareMaxVoltage

KPC_SetHubAnalogInput = lib.KPC_SetHubAnalogInput
KPC_SetHubAnalogInput.restype = c_short
KPC_SetHubAnalogInput.argtypes = [POINTER(c_char), KPC_HubAnalogueModes]
# *serialNo, hubAnalogInput

KPC_SetIOSettings = lib.KPC_SetIOSettings
KPC_SetIOSettings.restype = c_short
KPC_SetIOSettings.argtypes = [POINTER(c_char), KPC_IOSettings]
# *serialNo, ioSettings

KPC_SetLEDBrightness = lib.KPC_SetLEDBrightness
KPC_SetLEDBrightness.restype = c_short
KPC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
# *serialNo, brightness

KPC_SetLUTwaveParams = lib.KPC_SetLUTwaveParams
KPC_SetLUTwaveParams.restype = c_short
KPC_SetLUTwaveParams.argtypes = [PZ_LUTWaveParameters, POINTER(c_char)]
# *LUTwaveParams, *serialNo

KPC_SetLUTwaveSample = lib.KPC_SetLUTwaveSample
KPC_SetLUTwaveSample.restype = c_short
KPC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, index, value

KPC_SetMMIParams = lib.KPC_SetMMIParams
KPC_SetMMIParams.restype = c_short
KPC_SetMMIParams.argtypes = [
    POINTER(c_char),
    KPZ_WheelDirectionSense,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    KPZ_WheelChangeRate,
    c_int16,
    KPZ_WheelMode]
# *serialNo, directionSense, displayIntensity, positionStep, presetPosition1, presetPosition2, presetVoltage1, presetVoltage2, voltageAdjustRate, voltageStep, wheelMode

KPC_SetMMIParamsBlock = lib.KPC_SetMMIParamsBlock
KPC_SetMMIParamsBlock.restype = c_short
KPC_SetMMIParamsBlock.argtypes = [KPC_MMIParams, POINTER(c_char)]
# *mmiParams, *serialNo

KPC_SetMMIParamsExt = lib.KPC_SetMMIParamsExt
KPC_SetMMIParamsExt.restype = c_short
KPC_SetMMIParamsExt.argtypes = [
    POINTER(c_char),
    c_int16,
    KPZ_WheelDirectionSense,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    c_int16,
    KPZ_WheelChangeRate,
    c_int16,
    KPZ_WheelMode]
# *serialNo, PositionStep, directionSense, displayDimIntensity, displayIntensity, displayTimeout, presetPositiion1, presetPosition2, presetVoltage1, presetVoltage2, voltageAdjustRate, voltageStep, wheelMode

KPC_SetMaxOutputVoltage = lib.KPC_SetMaxOutputVoltage
KPC_SetMaxOutputVoltage.restype = c_short
KPC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, maxVoltage

KPC_SetOutputVoltage = lib.KPC_SetOutputVoltage
KPC_SetOutputVoltage.restype = c_short
KPC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, volts

KPC_SetPosition = lib.KPC_SetPosition
KPC_SetPosition.restype = c_short
KPC_SetPosition.argtypes = [POINTER(c_char), c_long]
# *serialNo, position

KPC_SetPositionControlMode = lib.KPC_SetPositionControlMode
KPC_SetPositionControlMode.restype = c_short
KPC_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
# *serialNo, mode

KPC_SetPositionToTolerance = lib.KPC_SetPositionToTolerance
KPC_SetPositionToTolerance.restype = c_short
KPC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_long, c_long]
# *serialNo, position, tolerance

KPC_SetTriggerConfigParams = lib.KPC_SetTriggerConfigParams
KPC_SetTriggerConfigParams.restype = c_short
KPC_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    c_int32,
    c_int16,
    KPC_MonitorOutputMode,
    c_int16,
    c_int16,
    KPC_TriggerPortMode,
    KPC_TriggerPortPolarity,
    KPC_TriggerPortMode,
    KPC_TriggerPortPolarity,
    c_int32]
# *serialNo, lowerLimit, monitorFilterFrequency, monitorOutput, monitorOutputSoftwareValue, smoothingSamples, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity, upperLimit

KPC_SetTriggerConfigParamsBlock = lib.KPC_SetTriggerConfigParamsBlock
KPC_SetTriggerConfigParamsBlock.restype = c_short
KPC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPC_TriggerConfig]
# *serialNo, *triggerConfigParams

KPC_SetVoltageSource = lib.KPC_SetVoltageSource
KPC_SetVoltageSource.restype = c_short
KPC_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]
# *serialNo, source

KPC_SetZero = lib.KPC_SetZero
KPC_SetZero.restype = c_bool
KPC_SetZero.argtypes = [POINTER(c_char)]
# *serialNo

KPC_StartLUTwave = lib.KPC_StartLUTwave
KPC_StartLUTwave.restype = c_short
KPC_StartLUTwave.argtypes = [POINTER(c_char)]
# *serialNo

KPC_StartPolling = lib.KPC_StartPolling
KPC_StartPolling.restype = c_bool
KPC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

KPC_StopLUTwave = lib.KPC_StopLUTwave
KPC_StopLUTwave.restype = c_short
KPC_StopLUTwave.argtypes = [POINTER(c_char)]
# *serialNo

KPC_StopPolling = lib.KPC_StopPolling
KPC_StopPolling.restype = None
KPC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

KPC_TimeSinceLastMsgReceived = lib.KPC_TimeSinceLastMsgReceived
KPC_TimeSinceLastMsgReceived.restype = c_bool
KPC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

KPC_WaitForMessage = lib.KPC_WaitForMessage
KPC_WaitForMessage.restype = c_bool
KPC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
