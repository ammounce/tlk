from c_types import (POINTER, c_bool, c_byte, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
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


class KCubePiezoStrainGauge(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.KCube.PiezoStrainGauge.DLL")

        self.KPC_CanDeviceLockFrontPanel = self.lib.KPC_CanDeviceLockFrontPanel
        self.KPC_CanDeviceLockFrontPanel.restype = c_bool
        self.KPC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_CheckConnection = self.lib.KPC_CheckConnection
        self.KPC_CheckConnection.restype = c_bool
        self.KPC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_ClearMessageQueue = self.lib.KPC_ClearMessageQueue
        self.KPC_ClearMessageQueue.restype = None
        self.KPC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_Close = self.lib.KPC_Close
        self.KPC_Close.restype = None
        self.KPC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_Disable = self.lib.KPC_Disable
        self.KPC_Disable.restype = c_short
        self.KPC_Disable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_Disconnect = self.lib.KPC_Disconnect
        self.KPC_Disconnect.restype = c_short
        self.KPC_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_Enable = self.lib.KPC_Enable
        self.KPC_Enable.restype = c_short
        self.KPC_Enable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_EnableLastMsgTimer = self.lib.KPC_EnableLastMsgTimer
        self.KPC_EnableLastMsgTimer.restype = None
        self.KPC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.KPC_GetDigitalOutputs = self.lib.KPC_GetDigitalOutputs
        self.KPC_GetDigitalOutputs.restype = c_byte
        self.KPC_GetDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetFeedbackLoopPIconsts = self.lib.KPC_GetFeedbackLoopPIconsts
        self.KPC_GetFeedbackLoopPIconsts.restype = c_short
        self.KPC_GetFeedbackLoopPIconsts.argtypes = [c_short, c_short, POINTER(c_char)]
        # *integralTerm, *proportionalTerm, *serialNo

        self.KPC_GetFeedbackLoopPIconstsBlock = self.lib.KPC_GetFeedbackLoopPIconstsBlock
        self.KPC_GetFeedbackLoopPIconstsBlock.restype = c_short
        self.KPC_GetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char)]
        # *proportionalAndIntegralConstants, *serialNo

        self.KPC_GetFirmwareVersion = self.lib.KPC_GetFirmwareVersion
        self.KPC_GetFirmwareVersion.restype = c_ulong
        self.KPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetFrontPanelLocked = self.lib.KPC_GetFrontPanelLocked
        self.KPC_GetFrontPanelLocked.restype = c_bool
        self.KPC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetHardwareInfo = self.lib.KPC_GetHardwareInfo
        self.KPC_GetHardwareInfo.restype = c_short
        self.KPC_GetHardwareInfo.argtypes = [
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

        self.KPC_GetHardwareInfoBlock = self.lib.KPC_GetHardwareInfoBlock
        self.KPC_GetHardwareInfoBlock.restype = c_short
        self.KPC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.KPC_GetHardwareMaxOutputVoltage = self.lib.KPC_GetHardwareMaxOutputVoltage
        self.KPC_GetHardwareMaxOutputVoltage.restype = c_short
        self.KPC_GetHardwareMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetHubAnalogInput = self.lib.KPC_GetHubAnalogInput
        self.KPC_GetHubAnalogInput.restype = KPC_HubAnalogueModes
        self.KPC_GetHubAnalogInput.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetIOSettings = self.lib.KPC_GetIOSettings
        self.KPC_GetIOSettings.restype = KPC_IOSettings
        self.KPC_GetIOSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetLEDBrightness = self.lib.KPC_GetLEDBrightness
        self.KPC_GetLEDBrightness.restype = c_short
        self.KPC_GetLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetMMIParams = self.lib.KPC_GetMMIParams
        self.KPC_GetMMIParams.restype = c_short
        self.KPC_GetMMIParams.argtypes = [
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

        self.KPC_GetMMIParamsBlock = self.lib.KPC_GetMMIParamsBlock
        self.KPC_GetMMIParamsBlock.restype = c_short
        self.KPC_GetMMIParamsBlock.argtypes = [KPC_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.KPC_GetMMIParamsExt = self.lib.KPC_GetMMIParamsExt
        self.KPC_GetMMIParamsExt.restype = c_short
        self.KPC_GetMMIParamsExt.argtypes = [
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

        self.KPC_GetMaxOutputVoltage = self.lib.KPC_GetMaxOutputVoltage
        self.KPC_GetMaxOutputVoltage.restype = c_short
        self.KPC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetMaximumTravel = self.lib.KPC_GetMaximumTravel
        self.KPC_GetMaximumTravel.restype = c_long
        self.KPC_GetMaximumTravel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetNextMessage = self.lib.KPC_GetNextMessage
        self.KPC_GetNextMessage.restype = c_bool
        self.KPC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.KPC_GetOutputVoltage = self.lib.KPC_GetOutputVoltage
        self.KPC_GetOutputVoltage.restype = c_short
        self.KPC_GetOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetPosition = self.lib.KPC_GetPosition
        self.KPC_GetPosition.restype = c_long
        self.KPC_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetPositionControlMode = self.lib.KPC_GetPositionControlMode
        self.KPC_GetPositionControlMode.restype = PZ_ControlModeTypes
        self.KPC_GetPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetSoftwareVersion = self.lib.KPC_GetSoftwareVersion
        self.KPC_GetSoftwareVersion.restype = c_ulong
        self.KPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetStatusBits = self.lib.KPC_GetStatusBits
        self.KPC_GetStatusBits.restype = c_ulong
        self.KPC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_GetTriggerConfigParams = self.lib.KPC_GetTriggerConfigParams
        self.KPC_GetTriggerConfigParams.restype = c_short
        self.KPC_GetTriggerConfigParams.argtypes = [
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

        self.KPC_GetTriggerConfigParamsBlock = self.lib.KPC_GetTriggerConfigParamsBlock
        self.KPC_GetTriggerConfigParamsBlock.restype = c_short
        self.KPC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPC_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.KPC_GetVoltageSource = self.lib.KPC_GetVoltageSource
        self.KPC_GetVoltageSource.restype = PZ_InputSourceFlags
        self.KPC_GetVoltageSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_HasLastMsgTimerOverrun = self.lib.KPC_HasLastMsgTimerOverrun
        self.KPC_HasLastMsgTimerOverrun.restype = c_bool
        self.KPC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_Identify = self.lib.KPC_Identify
        self.KPC_Identify.restype = None
        self.KPC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_LoadNamedSettings = self.lib.KPC_LoadNamedSettings
        self.KPC_LoadNamedSettings.restype = c_bool
        self.KPC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.KPC_LoadSettings = self.lib.KPC_LoadSettings
        self.KPC_LoadSettings.restype = c_bool
        self.KPC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_MessageQueueSize = self.lib.KPC_MessageQueueSize
        self.KPC_MessageQueueSize.restype = c_int
        self.KPC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_Open = self.lib.KPC_Open
        self.KPC_Open.restype = c_short
        self.KPC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_PersistSettings = self.lib.KPC_PersistSettings
        self.KPC_PersistSettings.restype = c_bool
        self.KPC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_PollingDuration = self.lib.KPC_PollingDuration
        self.KPC_PollingDuration.restype = c_long
        self.KPC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RegisterMessageCallback = self.lib.KPC_RegisterMessageCallback
        self.KPC_RegisterMessageCallback.restype = None
        self.KPC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.KPC_RequestActualPosition = self.lib.KPC_RequestActualPosition
        self.KPC_RequestActualPosition.restype = c_short
        self.KPC_RequestActualPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestDigitalOutputs = self.lib.KPC_RequestDigitalOutputs
        self.KPC_RequestDigitalOutputs.restype = c_short
        self.KPC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestFeedbackLoopPIconsts = self.lib.KPC_RequestFeedbackLoopPIconsts
        self.KPC_RequestFeedbackLoopPIconsts.restype = c_bool
        self.KPC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestFrontPanelLocked = self.lib.KPC_RequestFrontPanelLocked
        self.KPC_RequestFrontPanelLocked.restype = c_short
        self.KPC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestHardwareMaxOutputVoltage = self.lib.KPC_RequestHardwareMaxOutputVoltage
        self.KPC_RequestHardwareMaxOutputVoltage.restype = c_bool
        self.KPC_RequestHardwareMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestIOSettings = self.lib.KPC_RequestIOSettings
        self.KPC_RequestIOSettings.restype = c_bool
        self.KPC_RequestIOSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestLEDBrightness = self.lib.KPC_RequestLEDBrightness
        self.KPC_RequestLEDBrightness.restype = c_bool
        self.KPC_RequestLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestMMIParams = self.lib.KPC_RequestMMIParams
        self.KPC_RequestMMIParams.restype = c_bool
        self.KPC_RequestMMIParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestMaxOutputVoltage = self.lib.KPC_RequestMaxOutputVoltage
        self.KPC_RequestMaxOutputVoltage.restype = c_bool
        self.KPC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestMaximumTravel = self.lib.KPC_RequestMaximumTravel
        self.KPC_RequestMaximumTravel.restype = c_short
        self.KPC_RequestMaximumTravel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestOutputVoltage = self.lib.KPC_RequestOutputVoltage
        self.KPC_RequestOutputVoltage.restype = c_short
        self.KPC_RequestOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestPosition = self.lib.KPC_RequestPosition
        self.KPC_RequestPosition.restype = c_short
        self.KPC_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestPositionControlMode = self.lib.KPC_RequestPositionControlMode
        self.KPC_RequestPositionControlMode.restype = c_bool
        self.KPC_RequestPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestSettings = self.lib.KPC_RequestSettings
        self.KPC_RequestSettings.restype = c_short
        self.KPC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestStatus = self.lib.KPC_RequestStatus
        self.KPC_RequestStatus.restype = c_short
        self.KPC_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestStatusBits = self.lib.KPC_RequestStatusBits
        self.KPC_RequestStatusBits.restype = c_short
        self.KPC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestTriggerConfigParams = self.lib.KPC_RequestTriggerConfigParams
        self.KPC_RequestTriggerConfigParams.restype = c_short
        self.KPC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_RequestVoltageSource = self.lib.KPC_RequestVoltageSource
        self.KPC_RequestVoltageSource.restype = c_bool
        self.KPC_RequestVoltageSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_ResetParameters = self.lib.KPC_ResetParameters
        self.KPC_ResetParameters.restype = c_short
        self.KPC_ResetParameters.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_SetDigitalOutputs = self.lib.KPC_SetDigitalOutputs
        self.KPC_SetDigitalOutputs.restype = c_short
        self.KPC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.KPC_SetFeedbackLoopPIconsts = self.lib.KPC_SetFeedbackLoopPIconsts
        self.KPC_SetFeedbackLoopPIconsts.restype = c_short
        self.KPC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short]
        # *serialNo, integralTerm, proportionalTerm

        self.KPC_SetFeedbackLoopPIconstsBlock = self.lib.KPC_SetFeedbackLoopPIconstsBlock
        self.KPC_SetFeedbackLoopPIconstsBlock.restype = c_short
        self.KPC_SetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char)]
        # *proportionalAndIntegralConstants, *serialNo

        self.KPC_SetFrontPanelLock = self.lib.KPC_SetFrontPanelLock
        self.KPC_SetFrontPanelLock.restype = c_short
        self.KPC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, locked

        self.KPC_SetHardwareMaxOutputVoltage = self.lib.KPC_SetHardwareMaxOutputVoltage
        self.KPC_SetHardwareMaxOutputVoltage.restype = c_short
        self.KPC_SetHardwareMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, hardwareMaxVoltage

        self.KPC_SetHubAnalogInput = self.lib.KPC_SetHubAnalogInput
        self.KPC_SetHubAnalogInput.restype = c_short
        self.KPC_SetHubAnalogInput.argtypes = [POINTER(c_char), KPC_HubAnalogueModes]
        # *serialNo, hubAnalogInput

        self.KPC_SetIOSettings = self.lib.KPC_SetIOSettings
        self.KPC_SetIOSettings.restype = c_short
        self.KPC_SetIOSettings.argtypes = [POINTER(c_char), KPC_IOSettings]
        # *serialNo, ioSettings

        self.KPC_SetLEDBrightness = self.lib.KPC_SetLEDBrightness
        self.KPC_SetLEDBrightness.restype = c_short
        self.KPC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
        # *serialNo, brightness

        self.KPC_SetLUTwaveParams = self.lib.KPC_SetLUTwaveParams
        self.KPC_SetLUTwaveParams.restype = c_short
        self.KPC_SetLUTwaveParams.argtypes = [PZ_LUTWaveParameters, POINTER(c_char)]
        # *LUTwaveParams, *serialNo

        self.KPC_SetLUTwaveSample = self.lib.KPC_SetLUTwaveSample
        self.KPC_SetLUTwaveSample.restype = c_short
        self.KPC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, index, value

        self.KPC_SetMMIParams = self.lib.KPC_SetMMIParams
        self.KPC_SetMMIParams.restype = c_short
        self.KPC_SetMMIParams.argtypes = [
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

        self.KPC_SetMMIParamsBlock = self.lib.KPC_SetMMIParamsBlock
        self.KPC_SetMMIParamsBlock.restype = c_short
        self.KPC_SetMMIParamsBlock.argtypes = [KPC_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.KPC_SetMMIParamsExt = self.lib.KPC_SetMMIParamsExt
        self.KPC_SetMMIParamsExt.restype = c_short
        self.KPC_SetMMIParamsExt.argtypes = [
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

        self.KPC_SetMaxOutputVoltage = self.lib.KPC_SetMaxOutputVoltage
        self.KPC_SetMaxOutputVoltage.restype = c_short
        self.KPC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, maxVoltage

        self.KPC_SetOutputVoltage = self.lib.KPC_SetOutputVoltage
        self.KPC_SetOutputVoltage.restype = c_short
        self.KPC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, volts

        self.KPC_SetPosition = self.lib.KPC_SetPosition
        self.KPC_SetPosition.restype = c_short
        self.KPC_SetPosition.argtypes = [POINTER(c_char), c_long]
        # *serialNo, position

        self.KPC_SetPositionControlMode = self.lib.KPC_SetPositionControlMode
        self.KPC_SetPositionControlMode.restype = c_short
        self.KPC_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
        # *serialNo, mode

        self.KPC_SetPositionToTolerance = self.lib.KPC_SetPositionToTolerance
        self.KPC_SetPositionToTolerance.restype = c_short
        self.KPC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_long, c_long]
        # *serialNo, position, tolerance

        self.KPC_SetTriggerConfigParams = self.lib.KPC_SetTriggerConfigParams
        self.KPC_SetTriggerConfigParams.restype = c_short
        self.KPC_SetTriggerConfigParams.argtypes = [
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

        self.KPC_SetTriggerConfigParamsBlock = self.lib.KPC_SetTriggerConfigParamsBlock
        self.KPC_SetTriggerConfigParamsBlock.restype = c_short
        self.KPC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPC_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.KPC_SetVoltageSource = self.lib.KPC_SetVoltageSource
        self.KPC_SetVoltageSource.restype = c_short
        self.KPC_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]
        # *serialNo, source

        self.KPC_SetZero = self.lib.KPC_SetZero
        self.KPC_SetZero.restype = c_bool
        self.KPC_SetZero.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_StartLUTwave = self.lib.KPC_StartLUTwave
        self.KPC_StartLUTwave.restype = c_short
        self.KPC_StartLUTwave.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_StartPolling = self.lib.KPC_StartPolling
        self.KPC_StartPolling.restype = c_bool
        self.KPC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.KPC_StopLUTwave = self.lib.KPC_StopLUTwave
        self.KPC_StopLUTwave.restype = c_short
        self.KPC_StopLUTwave.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_StopPolling = self.lib.KPC_StopPolling
        self.KPC_StopPolling.restype = None
        self.KPC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KPC_TimeSinceLastMsgReceived = self.lib.KPC_TimeSinceLastMsgReceived
        self.KPC_TimeSinceLastMsgReceived.restype = c_bool
        self.KPC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.KPC_WaitForMessage = self.lib.KPC_WaitForMessage
        self.KPC_WaitForMessage.restype = c_bool
        self.KPC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.TLI_BuildDeviceList = self.lib.TLI_BuildDeviceList
        self.TLI_BuildDeviceList.restype = c_short
        self.TLI_BuildDeviceList.argtypes = [None, None]
        # , void

        self.TLI_GetDeviceInfo = self.lib.TLI_GetDeviceInfo
        self.TLI_GetDeviceInfo.restype = c_short
        self.TLI_GetDeviceInfo.argtypes = [TLI_DeviceInfo, POINTER(c_char), POINTER(c_char)]
        # *info, *serialNo, *serialNumber

        self.TLI_GetDeviceList = self.lib.TLI_GetDeviceList
        self.TLI_GetDeviceList.restype = c_short
        self.TLI_GetDeviceList.argtypes = [SafeArray]
        # **stringsReceiver

        self.TLI_GetDeviceListByType = self.lib.TLI_GetDeviceListByType
        self.TLI_GetDeviceListByType.restype = c_short
        self.TLI_GetDeviceListByType.argtypes = [SafeArray, c_int]
        # **stringsReceiver, typeID

        self.TLI_GetDeviceListByTypeExt = self.lib.TLI_GetDeviceListByTypeExt
        self.TLI_GetDeviceListByTypeExt.restype = c_short
        self.TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char), c_ulong, c_int]
        # *receiveBuffer, sizeOfBuffer, typeID

        self.TLI_GetDeviceListByTypes = self.lib.TLI_GetDeviceListByTypes
        self.TLI_GetDeviceListByTypes.restype = c_short
        self.TLI_GetDeviceListByTypes.argtypes = [SafeArray, c_int, c_int]
        # **stringsReceiver, *typeIDs, length

        self.TLI_GetDeviceListByTypesExt = self.lib.TLI_GetDeviceListByTypesExt
        self.TLI_GetDeviceListByTypesExt.restype = c_short
        self.TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_int, c_int, c_ulong]
        # *receiveBuffer, *typeIDs, length, sizeOfBuffer

        self.TLI_GetDeviceListExt = self.lib.TLI_GetDeviceListExt
        self.TLI_GetDeviceListExt.restype = c_short
        self.TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_ulong]
        # *receiveBuffer, sizeOfBuffer

        self.TLI_GetDeviceListSize = self.lib.TLI_GetDeviceListSize
        self.TLI_GetDeviceListSize.restype = c_short
        self.TLI_GetDeviceListSize.argtypes = [None]
        #

        self.TLI_InitializeSimulations = self.lib.TLI_InitializeSimulations
        self.TLI_InitializeSimulations.restype = None
        self.TLI_InitializeSimulations.argtypes = [None]
        #
