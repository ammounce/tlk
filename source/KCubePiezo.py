from c_types import (POINTER, c_bool, c_byte, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
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


class KCubePiezo(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.KCube.Piezo.DLL")

        self.PCC_CanDeviceLockFrontPanel = self.lib.PCC_CanDeviceLockFrontPanel
        self.PCC_CanDeviceLockFrontPanel.restype = c_bool
        self.PCC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_CheckConnection = self.lib.PCC_CheckConnection
        self.PCC_CheckConnection.restype = c_bool
        self.PCC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_ClearMessageQueue = self.lib.PCC_ClearMessageQueue
        self.PCC_ClearMessageQueue.restype = None
        self.PCC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_Close = self.lib.PCC_Close
        self.PCC_Close.restype = None
        self.PCC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_Disable = self.lib.PCC_Disable
        self.PCC_Disable.restype = c_short
        self.PCC_Disable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_Disconnect = self.lib.PCC_Disconnect
        self.PCC_Disconnect.restype = c_short
        self.PCC_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_Enable = self.lib.PCC_Enable
        self.PCC_Enable.restype = c_short
        self.PCC_Enable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_EnableLastMsgTimer = self.lib.PCC_EnableLastMsgTimer
        self.PCC_EnableLastMsgTimer.restype = None
        self.PCC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.PCC_GetDigitalOutputs = self.lib.PCC_GetDigitalOutputs
        self.PCC_GetDigitalOutputs.restype = c_byte
        self.PCC_GetDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetFeedbackLoopPIconsts = self.lib.PCC_GetFeedbackLoopPIconsts
        self.PCC_GetFeedbackLoopPIconsts.restype = c_short
        self.PCC_GetFeedbackLoopPIconsts.argtypes = [c_short, c_short, POINTER(c_char)]
        # *integralTerm, *proportionalTerm, *serialNo

        self.PCC_GetFeedbackLoopPIconstsBlock = self.lib.PCC_GetFeedbackLoopPIconstsBlock
        self.PCC_GetFeedbackLoopPIconstsBlock.restype = c_short
        self.PCC_GetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char)]
        # *proportionalAndIntegralConstants, *serialNo

        self.PCC_GetFirmwareVersion = self.lib.PCC_GetFirmwareVersion
        self.PCC_GetFirmwareVersion.restype = c_ulong
        self.PCC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetFrontPanelLocked = self.lib.PCC_GetFrontPanelLocked
        self.PCC_GetFrontPanelLocked.restype = c_bool
        self.PCC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetHardwareInfo = self.lib.PCC_GetHardwareInfo
        self.PCC_GetHardwareInfo.restype = c_short
        self.PCC_GetHardwareInfo.argtypes = [
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

        self.PCC_GetHardwareInfoBlock = self.lib.PCC_GetHardwareInfoBlock
        self.PCC_GetHardwareInfoBlock.restype = c_short
        self.PCC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.PCC_GetHubAnalogInput = self.lib.PCC_GetHubAnalogInput
        self.PCC_GetHubAnalogInput.restype = HubAnalogueModes
        self.PCC_GetHubAnalogInput.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetIOSettings = self.lib.PCC_GetIOSettings
        self.PCC_GetIOSettings.restype = TPZ_IOSettings
        self.PCC_GetIOSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetLEDBrightness = self.lib.PCC_GetLEDBrightness
        self.PCC_GetLEDBrightness.restype = c_short
        self.PCC_GetLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetMMIParams = self.lib.PCC_GetMMIParams
        self.PCC_GetMMIParams.restype = c_short
        self.PCC_GetMMIParams.argtypes = [KPZ_WheelDirectionSense, c_int16, c_int32,
                                          c_int32, POINTER(c_char), KPZ_WheelChangeRate, c_int32, KPZ_WheelMode]
        # *directionSense, *displayIntensity, *presetVoltage1, *presetVoltage2, *serialNo, *voltageAdjustRate, *voltageStep, *wheelMode

        self.PCC_GetMMIParamsBlock = self.lib.PCC_GetMMIParamsBlock
        self.PCC_GetMMIParamsBlock.restype = c_short
        self.PCC_GetMMIParamsBlock.argtypes = [KPZ_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.PCC_GetMMIParamsExt = self.lib.PCC_GetMMIParamsExt
        self.PCC_GetMMIParamsExt.restype = c_short
        self.PCC_GetMMIParamsExt.argtypes = [
            KPZ_WheelDirectionSense,
            c_int16,
            c_int16,
            c_int16,
            c_int32,
            c_int32,
            POINTER(c_char),
            KPZ_WheelChangeRate,
            c_int32,
            KPZ_WheelMode]
        # *directionSense, *displayDimIntensity, *displayIntensity, *displayTimeout, *presetVoltage1, *presetVoltage2, *serialNo, *voltageAdjustRate, *voltageStep, *wheelMode

        self.PCC_GetMaxOutputVoltage = self.lib.PCC_GetMaxOutputVoltage
        self.PCC_GetMaxOutputVoltage.restype = c_short
        self.PCC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetNextMessage = self.lib.PCC_GetNextMessage
        self.PCC_GetNextMessage.restype = c_bool
        self.PCC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.PCC_GetOutputVoltage = self.lib.PCC_GetOutputVoltage
        self.PCC_GetOutputVoltage.restype = c_short
        self.PCC_GetOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetPosition = self.lib.PCC_GetPosition
        self.PCC_GetPosition.restype = c_long
        self.PCC_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetPositionControlMode = self.lib.PCC_GetPositionControlMode
        self.PCC_GetPositionControlMode.restype = PZ_ControlModeTypes
        self.PCC_GetPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetSoftwareVersion = self.lib.PCC_GetSoftwareVersion
        self.PCC_GetSoftwareVersion.restype = c_ulong
        self.PCC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetStatusBits = self.lib.PCC_GetStatusBits
        self.PCC_GetStatusBits.restype = c_ulong
        self.PCC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_GetTriggerConfigParams = self.lib.PCC_GetTriggerConfigParams
        self.PCC_GetTriggerConfigParams.restype = c_short
        self.PCC_GetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KPZ_TriggerPortMode,
            KPZ_TriggerPortPolarity,
            KPZ_TriggerPortMode,
            KPZ_TriggerPortPolarity]
        # *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity

        self.PCC_GetTriggerConfigParamsBlock = self.lib.PCC_GetTriggerConfigParamsBlock
        self.PCC_GetTriggerConfigParamsBlock.restype = c_short
        self.PCC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPZ_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.PCC_GetVoltageSource = self.lib.PCC_GetVoltageSource
        self.PCC_GetVoltageSource.restype = PZ_InputSourceFlags
        self.PCC_GetVoltageSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_HasLastMsgTimerOverrun = self.lib.PCC_HasLastMsgTimerOverrun
        self.PCC_HasLastMsgTimerOverrun.restype = c_bool
        self.PCC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_Identify = self.lib.PCC_Identify
        self.PCC_Identify.restype = None
        self.PCC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_LoadNamedSettings = self.lib.PCC_LoadNamedSettings
        self.PCC_LoadNamedSettings.restype = c_bool
        self.PCC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.PCC_LoadSettings = self.lib.PCC_LoadSettings
        self.PCC_LoadSettings.restype = c_bool
        self.PCC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_MessageQueueSize = self.lib.PCC_MessageQueueSize
        self.PCC_MessageQueueSize.restype = c_int
        self.PCC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_Open = self.lib.PCC_Open
        self.PCC_Open.restype = c_short
        self.PCC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_PersistSettings = self.lib.PCC_PersistSettings
        self.PCC_PersistSettings.restype = c_bool
        self.PCC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_PollingDuration = self.lib.PCC_PollingDuration
        self.PCC_PollingDuration.restype = c_long
        self.PCC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RegisterMessageCallback = self.lib.PCC_RegisterMessageCallback
        self.PCC_RegisterMessageCallback.restype = None
        self.PCC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.PCC_RequestActualPosition = self.lib.PCC_RequestActualPosition
        self.PCC_RequestActualPosition.restype = c_short
        self.PCC_RequestActualPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestDigitalOutputs = self.lib.PCC_RequestDigitalOutputs
        self.PCC_RequestDigitalOutputs.restype = c_short
        self.PCC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestFeedbackLoopPIconsts = self.lib.PCC_RequestFeedbackLoopPIconsts
        self.PCC_RequestFeedbackLoopPIconsts.restype = c_bool
        self.PCC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestFrontPanelLocked = self.lib.PCC_RequestFrontPanelLocked
        self.PCC_RequestFrontPanelLocked.restype = c_short
        self.PCC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestIOSettings = self.lib.PCC_RequestIOSettings
        self.PCC_RequestIOSettings.restype = c_bool
        self.PCC_RequestIOSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestLEDBrightness = self.lib.PCC_RequestLEDBrightness
        self.PCC_RequestLEDBrightness.restype = c_bool
        self.PCC_RequestLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestMMIParams = self.lib.PCC_RequestMMIParams
        self.PCC_RequestMMIParams.restype = c_bool
        self.PCC_RequestMMIParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestMaxOutputVoltage = self.lib.PCC_RequestMaxOutputVoltage
        self.PCC_RequestMaxOutputVoltage.restype = c_bool
        self.PCC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestOutputVoltage = self.lib.PCC_RequestOutputVoltage
        self.PCC_RequestOutputVoltage.restype = c_short
        self.PCC_RequestOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestPosition = self.lib.PCC_RequestPosition
        self.PCC_RequestPosition.restype = c_short
        self.PCC_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestPositionControlMode = self.lib.PCC_RequestPositionControlMode
        self.PCC_RequestPositionControlMode.restype = c_short
        self.PCC_RequestPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestSettings = self.lib.PCC_RequestSettings
        self.PCC_RequestSettings.restype = c_short
        self.PCC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestStatus = self.lib.PCC_RequestStatus
        self.PCC_RequestStatus.restype = c_short
        self.PCC_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestStatusBits = self.lib.PCC_RequestStatusBits
        self.PCC_RequestStatusBits.restype = c_short
        self.PCC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestTriggerConfigParams = self.lib.PCC_RequestTriggerConfigParams
        self.PCC_RequestTriggerConfigParams.restype = c_bool
        self.PCC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_RequestVoltageSource = self.lib.PCC_RequestVoltageSource
        self.PCC_RequestVoltageSource.restype = c_bool
        self.PCC_RequestVoltageSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_SetDigitalOutputs = self.lib.PCC_SetDigitalOutputs
        self.PCC_SetDigitalOutputs.restype = c_short
        self.PCC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.PCC_SetFeedbackLoopPIconsts = self.lib.PCC_SetFeedbackLoopPIconsts
        self.PCC_SetFeedbackLoopPIconsts.restype = c_short
        self.PCC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short]
        # *serialNo, integralTerm, proportionalTerm

        self.PCC_SetFeedbackLoopPIconstsBlock = self.lib.PCC_SetFeedbackLoopPIconstsBlock
        self.PCC_SetFeedbackLoopPIconstsBlock.restype = c_short
        self.PCC_SetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char)]
        # *proportionalAndIntegralConstants, *serialNo

        self.PCC_SetFrontPanelLock = self.lib.PCC_SetFrontPanelLock
        self.PCC_SetFrontPanelLock.restype = c_short
        self.PCC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, locked

        self.PCC_SetHubAnalogInput = self.lib.PCC_SetHubAnalogInput
        self.PCC_SetHubAnalogInput.restype = c_short
        self.PCC_SetHubAnalogInput.argtypes = [POINTER(c_char), HubAnalogueModes]
        # *serialNo, hubAnalogInput

        self.PCC_SetIOSettings = self.lib.PCC_SetIOSettings
        self.PCC_SetIOSettings.restype = c_short
        self.PCC_SetIOSettings.argtypes = [POINTER(c_char), TPZ_IOSettings]
        # *serialNo, ioSettings

        self.PCC_SetLEDBrightness = self.lib.PCC_SetLEDBrightness
        self.PCC_SetLEDBrightness.restype = c_short
        self.PCC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
        # *serialNo, brightness

        self.PCC_SetLUTwaveParams = self.lib.PCC_SetLUTwaveParams
        self.PCC_SetLUTwaveParams.restype = c_short
        self.PCC_SetLUTwaveParams.argtypes = [PZ_LUTWaveParameters, POINTER(c_char)]
        # *LUTwaveParams, *serialNo

        self.PCC_SetLUTwaveSample = self.lib.PCC_SetLUTwaveSample
        self.PCC_SetLUTwaveSample.restype = c_short
        self.PCC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, index, value

        self.PCC_SetMMIParams = self.lib.PCC_SetMMIParams
        self.PCC_SetMMIParams.restype = c_short
        self.PCC_SetMMIParams.argtypes = [
            POINTER(c_char),
            KPZ_WheelDirectionSense,
            c_int16,
            c_int32,
            c_int32,
            KPZ_WheelChangeRate,
            c_int32,
            KPZ_WheelMode]
        # *serialNo, directionSense, displayIntensity, presetVoltage1, presetVoltage2, voltageAdjustRate, voltageStep, wheelMode

        self.PCC_SetMMIParamsBlock = self.lib.PCC_SetMMIParamsBlock
        self.PCC_SetMMIParamsBlock.restype = c_short
        self.PCC_SetMMIParamsBlock.argtypes = [KPZ_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.PCC_SetMMIParamsExt = self.lib.PCC_SetMMIParamsExt
        self.PCC_SetMMIParamsExt.restype = c_short
        self.PCC_SetMMIParamsExt.argtypes = [
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

        self.PCC_SetMaxOutputVoltage = self.lib.PCC_SetMaxOutputVoltage
        self.PCC_SetMaxOutputVoltage.restype = c_short
        self.PCC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, maxVoltage

        self.PCC_SetOutputVoltage = self.lib.PCC_SetOutputVoltage
        self.PCC_SetOutputVoltage.restype = c_short
        self.PCC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, volts

        self.PCC_SetPosition = self.lib.PCC_SetPosition
        self.PCC_SetPosition.restype = c_short
        self.PCC_SetPosition.argtypes = [POINTER(c_char), c_long]
        # *serialNo, position

        self.PCC_SetPositionControlMode = self.lib.PCC_SetPositionControlMode
        self.PCC_SetPositionControlMode.restype = c_short
        self.PCC_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
        # *serialNo, mode

        self.PCC_SetPositionToTolerance = self.lib.PCC_SetPositionToTolerance
        self.PCC_SetPositionToTolerance.restype = c_short
        self.PCC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_long, c_long]
        # *serialNo, position, tolerance

        self.PCC_SetTriggerConfigParams = self.lib.PCC_SetTriggerConfigParams
        self.PCC_SetTriggerConfigParams.restype = c_short
        self.PCC_SetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KPZ_TriggerPortMode,
            KPZ_TriggerPortPolarity,
            KPZ_TriggerPortMode,
            KPZ_TriggerPortPolarity]
        # *serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

        self.PCC_SetTriggerConfigParamsBlock = self.lib.PCC_SetTriggerConfigParamsBlock
        self.PCC_SetTriggerConfigParamsBlock.restype = c_short
        self.PCC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPZ_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.PCC_SetVoltageSource = self.lib.PCC_SetVoltageSource
        self.PCC_SetVoltageSource.restype = c_short
        self.PCC_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]
        # *serialNo, source

        self.PCC_SetZero = self.lib.PCC_SetZero
        self.PCC_SetZero.restype = c_bool
        self.PCC_SetZero.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_StartLUTwave = self.lib.PCC_StartLUTwave
        self.PCC_StartLUTwave.restype = c_short
        self.PCC_StartLUTwave.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_StartPolling = self.lib.PCC_StartPolling
        self.PCC_StartPolling.restype = c_bool
        self.PCC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.PCC_StopLUTwave = self.lib.PCC_StopLUTwave
        self.PCC_StopLUTwave.restype = c_short
        self.PCC_StopLUTwave.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_StopPolling = self.lib.PCC_StopPolling
        self.PCC_StopPolling.restype = None
        self.PCC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PCC_TimeSinceLastMsgReceived = self.lib.PCC_TimeSinceLastMsgReceived
        self.PCC_TimeSinceLastMsgReceived.restype = c_bool
        self.PCC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.PCC_WaitForMessage = self.lib.PCC_WaitForMessage
        self.PCC_WaitForMessage.restype = c_bool
        self.PCC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
