from c_types import (POINTER, c_bool, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (
    KIM_Channels,
    KIM_DirectionSense,
    KIM_FBSignalMode,
    KIM_JogMode,
    KIM_JoysticModes,
    KIM_LimitSwitchModes,
    KIM_Stages,
    KIM_TravelDirection,
    KIM_TrigModes,
    KIM_TrigPolarities)
from .definitions.structures import (
    KIM_DriveOPParameters,
    KIM_FeedbackSigParams,
    KIM_HomeParameters,
    KIM_JogParameters,
    KIM_LimitSwitchParameters,
    KIM_MMIChannelParameters,
    KIM_MMIParameters,
    KIM_TrigIOConfig,
    KIM_TrigParamsParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class KCubeInertialMotor(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.KCube.DCServo.dll")

        self.KIM_CanDeviceLockFrontPanel = self.lib.KIM_CanDeviceLockFrontPanel
        self.KIM_CanDeviceLockFrontPanel.restype = c_bool
        self.KIM_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_CheckConnection = self.lib.KIM_CheckConnection
        self.KIM_CheckConnection.restype = c_bool
        self.KIM_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_ClearMessageQueue = self.lib.KIM_ClearMessageQueue
        self.KIM_ClearMessageQueue.restype = None
        self.KIM_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_Close = self.lib.KIM_Close
        self.KIM_Close.restype = None
        self.KIM_Close.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_Disable = self.lib.KIM_Disable
        self.KIM_Disable.restype = c_short
        self.KIM_Disable.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_DisableChannel = self.lib.KIM_DisableChannel
        self.KIM_DisableChannel.restype = c_short
        self.KIM_DisableChannel.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_Disconnect = self.lib.KIM_Disconnect
        self.KIM_Disconnect.restype = c_short
        self.KIM_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_Enable = self.lib.KIM_Enable
        self.KIM_Enable.restype = c_short
        self.KIM_Enable.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_EnableChannel = self.lib.KIM_EnableChannel
        self.KIM_EnableChannel.restype = c_short
        self.KIM_EnableChannel.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_EnableLastMsgTimer = self.lib.KIM_EnableLastMsgTimer
        self.KIM_EnableLastMsgTimer.restype = None
        self.KIM_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNumber, enable, lastMsgTimeout

        self.KIM_GetAbsoluteMoveParameters = self.lib.KIM_GetAbsoluteMoveParameters
        self.KIM_GetAbsoluteMoveParameters.restype = c_short
        self.KIM_GetAbsoluteMoveParameters.argtypes = [c_int32, POINTER(c_char), KIM_Channels]
        # &absoluteMove, *serialNumber, channel

        self.KIM_GetCurrentPosition = self.lib.KIM_GetCurrentPosition
        self.KIM_GetCurrentPosition.restype = c_int32
        self.KIM_GetCurrentPosition.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_GetDriveOPParameters = self.lib.KIM_GetDriveOPParameters
        self.KIM_GetDriveOPParameters.restype = c_short
        self.KIM_GetDriveOPParameters.argtypes = [c_int16, c_int32, c_int32, POINTER(c_char), KIM_Channels]
        # &maxVoltage, &stepAcceleration, &stepRate, *serialNumber, channel

        self.KIM_GetDriveOPParametersStruct = self.lib.KIM_GetDriveOPParametersStruct
        self.KIM_GetDriveOPParametersStruct.restype = c_short
        self.KIM_GetDriveOPParametersStruct.argtypes = [KIM_DriveOPParameters, POINTER(c_char), KIM_Channels]
        # &driveOPParameters, *serialNumber, channel

        self.KIM_GetFeedbackSigParameters = self.lib.KIM_GetFeedbackSigParameters
        self.KIM_GetFeedbackSigParameters.restype = c_short
        self.KIM_GetFeedbackSigParameters.argtypes = [c_int32, KIM_FBSignalMode, POINTER(c_char), KIM_Channels]
        # &encoderConst, &feedbackSignalMode, *serialNumber, channel

        self.KIM_GetFeedbackSigParametersStruct = self.lib.KIM_GetFeedbackSigParametersStruct
        self.KIM_GetFeedbackSigParametersStruct.restype = c_short
        self.KIM_GetFeedbackSigParametersStruct.argtypes = [KIM_FeedbackSigParams, POINTER(c_char), KIM_Channels]
        # &fbSigParameters, *serialNumber, channel

        self.KIM_GetFirmwareVersion = self.lib.KIM_GetFirmwareVersion
        self.KIM_GetFirmwareVersion.restype = c_ulong
        self.KIM_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_GetFrontPanelLocked = self.lib.KIM_GetFrontPanelLocked
        self.KIM_GetFrontPanelLocked.restype = c_bool
        self.KIM_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_GetHardwareInfo = self.lib.KIM_GetHardwareInfo
        self.KIM_GetHardwareInfo.restype = c_short
        self.KIM_GetHardwareInfo.argtypes = [
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
        # *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numChannels, *serialNumber, *type, sizeOfModelNo, sizeOfNotes

        self.KIM_GetHardwareInfoBlock = self.lib.KIM_GetHardwareInfoBlock
        self.KIM_GetHardwareInfoBlock.restype = c_short
        self.KIM_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNumber

        self.KIM_GetHomeParameters = self.lib.KIM_GetHomeParameters
        self.KIM_GetHomeParameters.restype = c_short
        self.KIM_GetHomeParameters.argtypes = [
            KIM_TravelDirection,
            KIM_TravelDirection,
            c_int32,
            c_int32,
            POINTER(c_char),
            KIM_Channels]
        # &homeDirection, &homeLimitSwitch, &homeOffset, &homeStepRate, *serialNumber, channel

        self.KIM_GetHomeParametersStruct = self.lib.KIM_GetHomeParametersStruct
        self.KIM_GetHomeParametersStruct.restype = c_short
        self.KIM_GetHomeParametersStruct.argtypes = [KIM_HomeParameters, POINTER(c_char), KIM_Channels]
        # &homeParameters, *serialNumber, channel

        self.KIM_GetJogParameters = self.lib.KIM_GetJogParameters
        self.KIM_GetJogParameters.restype = c_short
        self.KIM_GetJogParameters.argtypes = [KIM_JogMode, c_int32,
                                              c_int32, c_int32, c_int32, POINTER(c_char), KIM_Channels]
        # &jogMode, &jogStepAcceleration, &jogStepRate, &jogStepSizeFwd, &jogStepSizeRev, *serialNumber, channel

        self.KIM_GetJogParametersStruct = self.lib.KIM_GetJogParametersStruct
        self.KIM_GetJogParametersStruct.restype = c_short
        self.KIM_GetJogParametersStruct.argtypes = [KIM_JogParameters, POINTER(c_char), KIM_Channels]
        # &jogParameters, *serialNumber, channel

        self.KIM_GetLimitSwitchParameters = self.lib.KIM_GetLimitSwitchParameters
        self.KIM_GetLimitSwitchParameters.restype = c_short
        self.KIM_GetLimitSwitchParameters.argtypes = [KIM_LimitSwitchModes,
                                                      KIM_LimitSwitchModes, c_int16, POINTER(c_char), KIM_Channels]
        # &forwardLimit, &reverseLimit, &stageID, *serialNumber, channel

        self.KIM_GetLimitSwitchParametersStruct = self.lib.KIM_GetLimitSwitchParametersStruct
        self.KIM_GetLimitSwitchParametersStruct.restype = c_short
        self.KIM_GetLimitSwitchParametersStruct.argtypes = [KIM_LimitSwitchParameters, POINTER(c_char), KIM_Channels]
        # &limitSwitchParameters, *serialNumber, channel

        self.KIM_GetMMIChannelParameters = self.lib.KIM_GetMMIChannelParameters
        self.KIM_GetMMIChannelParameters.restype = c_short
        self.KIM_GetMMIChannelParameters.argtypes = [c_int32, c_int32, POINTER(c_char), KIM_Channels]
        # &presetPos1, &presetPos2, *serialNumber, channel

        self.KIM_GetMMIChannelParametersStruct = self.lib.KIM_GetMMIChannelParametersStruct
        self.KIM_GetMMIChannelParametersStruct.restype = c_short
        self.KIM_GetMMIChannelParametersStruct.argtypes = [KIM_MMIChannelParameters, POINTER(c_char), KIM_Channels]
        # &mmiParameters, *serialNumber, channel

        self.KIM_GetMMIDeviceParameters = self.lib.KIM_GetMMIDeviceParameters
        self.KIM_GetMMIDeviceParameters.restype = c_short
        self.KIM_GetMMIDeviceParameters.argtypes = [
            KIM_DirectionSense,
            c_int32,
            KIM_JoysticModes,
            c_int32,
            c_int32,
            c_int32,
            POINTER(c_char),
            KIM_Channels]
        # &directionSense, &displayIntensity, &joystickMode, &maxStepRate, &presetPos1, &presetPos2, *serialNumber, channel

        self.KIM_GetMMIDeviceParametersStruct = self.lib.KIM_GetMMIDeviceParametersStruct
        self.KIM_GetMMIDeviceParametersStruct.restype = c_short
        self.KIM_GetMMIDeviceParametersStruct.argtypes = [KIM_MMIParameters, POINTER(c_char)]
        # &mmiParameters, *serialNumber

        self.KIM_GetNextMessage = self.lib.KIM_GetNextMessage
        self.KIM_GetNextMessage.restype = c_bool
        self.KIM_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNumber

        self.KIM_GetRelativeMoveParameter = self.lib.KIM_GetRelativeMoveParameter
        self.KIM_GetRelativeMoveParameter.restype = c_short
        self.KIM_GetRelativeMoveParameter.argtypes = [c_int32, POINTER(c_char), KIM_Channels]
        # &relativeMoveStep, *serialNumber, channel

        self.KIM_GetSoftwareVersion = self.lib.KIM_GetSoftwareVersion
        self.KIM_GetSoftwareVersion.restype = c_ulong
        self.KIM_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_GetStageType = self.lib.KIM_GetStageType
        self.KIM_GetStageType.restype = KIM_Stages
        self.KIM_GetStageType.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_GetStatusBits = self.lib.KIM_GetStatusBits
        self.KIM_GetStatusBits.restype = c_ulong
        self.KIM_GetStatusBits.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_GetTrigIOParameters = self.lib.KIM_GetTrigIOParameters
        self.KIM_GetTrigIOParameters.restype = c_short
        self.KIM_GetTrigIOParameters.argtypes = [
            KIM_TrigModes,
            KIM_TrigPolarities,
            KIM_TrigModes,
            KIM_TrigPolarities,
            KIM_Channels,
            KIM_Channels,
            POINTER(c_char)]
        # &trig1Mode, &trig1Polarity, &trig2Mode, &trig2Polarity, &trigChannel1, &trigChannel2, *serialNumber

        self.KIM_GetTrigIOParametersStruct = self.lib.KIM_GetTrigIOParametersStruct
        self.KIM_GetTrigIOParametersStruct.restype = c_short
        self.KIM_GetTrigIOParametersStruct.argtypes = [KIM_TrigIOConfig, POINTER(c_char)]
        # &trigIOParameters, *serialNumber

        self.KIM_GetTrigParamsParameters = self.lib.KIM_GetTrigParamsParameters
        self.KIM_GetTrigParamsParameters.restype = c_short
        self.KIM_GetTrigParamsParameters.argtypes = [
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            POINTER(c_char),
            KIM_Channels]
        # &intervalFwd, &intervalRev, &numberOfCycles, &numberOfPulsesFwd, &numberOfPulsesRev, &pulseWidth, &startPosFwd, &startPosRev, *serialNumber, channel

        self.KIM_GetTrigParamsParametersStruct = self.lib.KIM_GetTrigParamsParametersStruct
        self.KIM_GetTrigParamsParametersStruct.restype = c_short
        self.KIM_GetTrigParamsParametersStruct.argtypes = [KIM_TrigParamsParameters, POINTER(c_char), KIM_Channels]
        # &trigParameters, *serialNumber, channel

        self.KIM_HasLastMsgTimerOverrun = self.lib.KIM_HasLastMsgTimerOverrun
        self.KIM_HasLastMsgTimerOverrun.restype = c_bool
        self.KIM_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_Home = self.lib.KIM_Home
        self.KIM_Home.restype = c_short
        self.KIM_Home.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_Identify = self.lib.KIM_Identify
        self.KIM_Identify.restype = None
        self.KIM_Identify.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_IsDualChannelMode = self.lib.KIM_IsDualChannelMode
        self.KIM_IsDualChannelMode.restype = c_bool
        self.KIM_IsDualChannelMode.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_LoadNamedSettings = self.lib.KIM_LoadNamedSettings
        self.KIM_LoadNamedSettings.restype = c_bool
        self.KIM_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNumber, *settingsName

        self.KIM_LoadSettings = self.lib.KIM_LoadSettings
        self.KIM_LoadSettings.restype = c_bool
        self.KIM_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_MessageQueueSize = self.lib.KIM_MessageQueueSize
        self.KIM_MessageQueueSize.restype = c_int
        self.KIM_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_MoveAbsolute = self.lib.KIM_MoveAbsolute
        self.KIM_MoveAbsolute.restype = c_short
        self.KIM_MoveAbsolute.argtypes = [POINTER(c_char), KIM_Channels, c_int32]
        # *serialNumber, channel, position

        self.KIM_MoveJog = self.lib.KIM_MoveJog
        self.KIM_MoveJog.restype = c_short
        self.KIM_MoveJog.argtypes = [POINTER(c_char), KIM_Channels, KIM_TravelDirection]
        # *serialNumber, channel, jogDirection

        self.KIM_MoveRelative = self.lib.KIM_MoveRelative
        self.KIM_MoveRelative.restype = c_short
        self.KIM_MoveRelative.argtypes = [POINTER(c_char), KIM_Channels, c_int32]
        # *serialNumber, channel, stepSize

        self.KIM_MoveStop = self.lib.KIM_MoveStop
        self.KIM_MoveStop.restype = c_short
        self.KIM_MoveStop.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_Open = self.lib.KIM_Open
        self.KIM_Open.restype = c_short
        self.KIM_Open.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_PersistSettings = self.lib.KIM_PersistSettings
        self.KIM_PersistSettings.restype = c_bool
        self.KIM_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_PollingDuration = self.lib.KIM_PollingDuration
        self.KIM_PollingDuration.restype = c_long
        self.KIM_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_RegisterMessageCallback = self.lib.KIM_RegisterMessageCallback
        self.KIM_RegisterMessageCallback.restype = None
        self.KIM_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNumber, void

        self.KIM_RequestAbsoluteMoveParameters = self.lib.KIM_RequestAbsoluteMoveParameters
        self.KIM_RequestAbsoluteMoveParameters.restype = c_short
        self.KIM_RequestAbsoluteMoveParameters.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestCurrentPosition = self.lib.KIM_RequestCurrentPosition
        self.KIM_RequestCurrentPosition.restype = c_short
        self.KIM_RequestCurrentPosition.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestDriveOPParameters = self.lib.KIM_RequestDriveOPParameters
        self.KIM_RequestDriveOPParameters.restype = c_short
        self.KIM_RequestDriveOPParameters.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestFeedbackSigParameters = self.lib.KIM_RequestFeedbackSigParameters
        self.KIM_RequestFeedbackSigParameters.restype = c_short
        self.KIM_RequestFeedbackSigParameters.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestFrontPanelLocked = self.lib.KIM_RequestFrontPanelLocked
        self.KIM_RequestFrontPanelLocked.restype = c_short
        self.KIM_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_RequestHomeParameters = self.lib.KIM_RequestHomeParameters
        self.KIM_RequestHomeParameters.restype = c_short
        self.KIM_RequestHomeParameters.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestJogParameters = self.lib.KIM_RequestJogParameters
        self.KIM_RequestJogParameters.restype = c_short
        self.KIM_RequestJogParameters.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestLimitSwitchParameters = self.lib.KIM_RequestLimitSwitchParameters
        self.KIM_RequestLimitSwitchParameters.restype = c_short
        self.KIM_RequestLimitSwitchParameters.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestMMIParameters = self.lib.KIM_RequestMMIParameters
        self.KIM_RequestMMIParameters.restype = c_short
        self.KIM_RequestMMIParameters.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestRelativeMoveParameter = self.lib.KIM_RequestRelativeMoveParameter
        self.KIM_RequestRelativeMoveParameter.restype = c_short
        self.KIM_RequestRelativeMoveParameter.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_RequestSettings = self.lib.KIM_RequestSettings
        self.KIM_RequestSettings.restype = c_short
        self.KIM_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_RequestStageType = self.lib.KIM_RequestStageType
        self.KIM_RequestStageType.restype = c_short
        self.KIM_RequestStageType.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_RequestStatus = self.lib.KIM_RequestStatus
        self.KIM_RequestStatus.restype = c_short
        self.KIM_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_RequestStatusBits = self.lib.KIM_RequestStatusBits
        self.KIM_RequestStatusBits.restype = c_short
        self.KIM_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_RequestTrigIOParameters = self.lib.KIM_RequestTrigIOParameters
        self.KIM_RequestTrigIOParameters.restype = c_short
        self.KIM_RequestTrigIOParameters.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_RequestTrigParamsParameters = self.lib.KIM_RequestTrigParamsParameters
        self.KIM_RequestTrigParamsParameters.restype = c_short
        self.KIM_RequestTrigParamsParameters.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

        self.KIM_Reset = self.lib.KIM_Reset
        self.KIM_Reset.restype = c_short
        self.KIM_Reset.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_SetAbsoluteMoveParameters = self.lib.KIM_SetAbsoluteMoveParameters
        self.KIM_SetAbsoluteMoveParameters.restype = c_short
        self.KIM_SetAbsoluteMoveParameters.argtypes = [c_int32, POINTER(c_char), KIM_Channels]
        # &absoluteMove, *serialNumber, channel

        self.KIM_SetDriveOPParameters = self.lib.KIM_SetDriveOPParameters
        self.KIM_SetDriveOPParameters.restype = c_short
        self.KIM_SetDriveOPParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int16, c_int32, c_int32]
        # *serialNumber, channel, maxVoltage, stepAcceleration, stepRate

        self.KIM_SetDriveOPParametersStruct = self.lib.KIM_SetDriveOPParametersStruct
        self.KIM_SetDriveOPParametersStruct.restype = c_short
        self.KIM_SetDriveOPParametersStruct.argtypes = [KIM_DriveOPParameters, POINTER(c_char), KIM_Channels]
        # &driveOPParameters, *serialNumber, channel

        self.KIM_SetDualChannelMode = self.lib.KIM_SetDualChannelMode
        self.KIM_SetDualChannelMode.restype = c_short
        self.KIM_SetDualChannelMode.argtypes = [POINTER(c_char), c_bool]
        # *serialNumber, enableDualChannel

        self.KIM_SetFeedbackSigParameters = self.lib.KIM_SetFeedbackSigParameters
        self.KIM_SetFeedbackSigParameters.restype = c_short
        self.KIM_SetFeedbackSigParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int32, KIM_FBSignalMode]
        # *serialNumber, channel, encoderConst, feedbackSignalMode

        self.KIM_SetFeedbackSigParametersStruct = self.lib.KIM_SetFeedbackSigParametersStruct
        self.KIM_SetFeedbackSigParametersStruct.restype = c_short
        self.KIM_SetFeedbackSigParametersStruct.argtypes = [KIM_FeedbackSigParams, POINTER(c_char), KIM_Channels]
        # &fbSigParameters, *serialNumber, channel

        self.KIM_SetFrontPanelLock = self.lib.KIM_SetFrontPanelLock
        self.KIM_SetFrontPanelLock.restype = c_short
        self.KIM_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
        # *serialNumber, locked

        self.KIM_SetHomeParameters = self.lib.KIM_SetHomeParameters
        self.KIM_SetHomeParameters.restype = c_short
        self.KIM_SetHomeParameters.argtypes = [
            POINTER(c_char),
            KIM_Channels,
            KIM_TravelDirection,
            KIM_TravelDirection,
            c_int32,
            c_int32]
        # *serialNumber, channel, homeDirection, homeLimitSwitch, homeOffset, homeStepRate

        self.KIM_SetHomeParametersStruct = self.lib.KIM_SetHomeParametersStruct
        self.KIM_SetHomeParametersStruct.restype = c_short
        self.KIM_SetHomeParametersStruct.argtypes = [KIM_HomeParameters, POINTER(c_char), KIM_Channels]
        # &homeParameters, *serialNumber, channel

        self.KIM_SetJogParameters = self.lib.KIM_SetJogParameters
        self.KIM_SetJogParameters.restype = c_short
        self.KIM_SetJogParameters.argtypes = [
            POINTER(c_char),
            KIM_Channels,
            KIM_JogMode,
            c_int32,
            c_int32,
            c_int32,
            c_int32]
        # *serialNumber, channel, jogMode, jogStepAcceleration, jogStepRate, jogStepSizeFwd, jogStepSizeRev

        self.KIM_SetJogParametersStruct = self.lib.KIM_SetJogParametersStruct
        self.KIM_SetJogParametersStruct.restype = c_short
        self.KIM_SetJogParametersStruct.argtypes = [KIM_JogParameters, POINTER(c_char), KIM_Channels]
        # &jogParameters, *serialNumber, channel

        self.KIM_SetLimitSwitchParameters = self.lib.KIM_SetLimitSwitchParameters
        self.KIM_SetLimitSwitchParameters.restype = c_short
        self.KIM_SetLimitSwitchParameters.argtypes = [
            POINTER(c_char),
            KIM_Channels,
            KIM_LimitSwitchModes,
            KIM_LimitSwitchModes,
            c_int16]
        # *serialNumber, channel, forwardLimit, reverseLimit, stageID

        self.KIM_SetLimitSwitchParametersStruct = self.lib.KIM_SetLimitSwitchParametersStruct
        self.KIM_SetLimitSwitchParametersStruct.restype = c_short
        self.KIM_SetLimitSwitchParametersStruct.argtypes = [KIM_LimitSwitchParameters, POINTER(c_char), KIM_Channels]
        # &limitSwitchParameters, *serialNumber, channel

        self.KIM_SetMMIChannelParameters = self.lib.KIM_SetMMIChannelParameters
        self.KIM_SetMMIChannelParameters.restype = c_short
        self.KIM_SetMMIChannelParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int32, c_int32]
        # *serialNumber, channel, presetPos1, presetPos2

        self.KIM_SetMMIChannelParametersStruct = self.lib.KIM_SetMMIChannelParametersStruct
        self.KIM_SetMMIChannelParametersStruct.restype = c_short
        self.KIM_SetMMIChannelParametersStruct.argtypes = [KIM_MMIChannelParameters, POINTER(c_char), KIM_Channels]
        # &mmiParameters, *serialNumber, channel

        self.KIM_SetMMIDeviceParameters = self.lib.KIM_SetMMIDeviceParameters
        self.KIM_SetMMIDeviceParameters.restype = c_short
        self.KIM_SetMMIDeviceParameters.argtypes = [
            POINTER(c_char), KIM_DirectionSense, c_int16, KIM_JoysticModes, c_int32]
        # *serialNumber, directionSense, displayIntensity, joystickMode, maxStepRate

        self.KIM_SetMMIDeviceParametersStruct = self.lib.KIM_SetMMIDeviceParametersStruct
        self.KIM_SetMMIDeviceParametersStruct.restype = c_short
        self.KIM_SetMMIDeviceParametersStruct.argtypes = [KIM_MMIParameters, POINTER(c_char)]
        # &mmiParameters, *serialNumber

        self.KIM_SetPosition = self.lib.KIM_SetPosition
        self.KIM_SetPosition.restype = c_short
        self.KIM_SetPosition.argtypes = [POINTER(c_char), KIM_Channels, c_long]
        # *serialNumber, channel, position

        self.KIM_SetRelativeMoveParameter = self.lib.KIM_SetRelativeMoveParameter
        self.KIM_SetRelativeMoveParameter.restype = c_short
        self.KIM_SetRelativeMoveParameter.argtypes = [c_int32, POINTER(c_char), KIM_Channels]
        # &relativeMove, *serialNumber, channel

        self.KIM_SetStageType = self.lib.KIM_SetStageType
        self.KIM_SetStageType.restype = c_short
        self.KIM_SetStageType.argtypes = [POINTER(c_char), KIM_Stages]
        # *serialNumber, stageType

        self.KIM_SetTrigIOParameters = self.lib.KIM_SetTrigIOParameters
        self.KIM_SetTrigIOParameters.restype = c_short
        self.KIM_SetTrigIOParameters.argtypes = [
            POINTER(c_char),
            KIM_TrigModes,
            KIM_TrigPolarities,
            KIM_TrigModes,
            KIM_TrigPolarities,
            KIM_Channels,
            KIM_Channels]
        # *serialNumber, trig1Mode, trig1Polarity, trig2Mode, trig2Polarity, trigChannel1, trigChannel2

        self.KIM_SetTrigIOParametersStruct = self.lib.KIM_SetTrigIOParametersStruct
        self.KIM_SetTrigIOParametersStruct.restype = c_short
        self.KIM_SetTrigIOParametersStruct.argtypes = [KIM_TrigIOConfig, POINTER(c_char)]
        # &trigIOParameters, *serialNumber

        self.KIM_SetTrigParamsParameters = self.lib.KIM_SetTrigParamsParameters
        self.KIM_SetTrigParamsParameters.restype = c_short
        self.KIM_SetTrigParamsParameters.argtypes = [
            KIM_TrigParamsParameters,
            POINTER(c_char),
            KIM_Channels,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32]
        # &trigParameters, *serialNumber, channel, intervalFwd, intervalRev, numberOfCycles, numberOfPulsesFwd, numberOfPulsesRev, pulseWidth, startPosFwd, startPosRev

        self.KIM_SetTrigParamsParametersStruct = self.lib.KIM_SetTrigParamsParametersStruct
        self.KIM_SetTrigParamsParametersStruct.restype = c_short
        self.KIM_SetTrigParamsParametersStruct.argtypes = [KIM_TrigParamsParameters, POINTER(c_char), KIM_Channels]
        # &trigParameters, *serialNumber, channel

        self.KIM_StartPolling = self.lib.KIM_StartPolling
        self.KIM_StartPolling.restype = c_bool
        self.KIM_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNumber, milliseconds

        self.KIM_StopPolling = self.lib.KIM_StopPolling
        self.KIM_StopPolling.restype = None
        self.KIM_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_SupportsDualChannelMode = self.lib.KIM_SupportsDualChannelMode
        self.KIM_SupportsDualChannelMode.restype = c_bool
        self.KIM_SupportsDualChannelMode.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_SupportsStageType = self.lib.KIM_SupportsStageType
        self.KIM_SupportsStageType.restype = c_bool
        self.KIM_SupportsStageType.argtypes = [POINTER(c_char)]
        # *serialNumber

        self.KIM_TimeSinceLastMsgReceived = self.lib.KIM_TimeSinceLastMsgReceived
        self.KIM_TimeSinceLastMsgReceived.restype = c_bool
        self.KIM_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNumber

        self.KIM_WaitForMessage = self.lib.KIM_WaitForMessage
        self.KIM_WaitForMessage.restype = c_bool
        self.KIM_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNumber

        self.KIM_ZeroPosition = self.lib.KIM_ZeroPosition
        self.KIM_ZeroPosition.restype = c_short
        self.KIM_ZeroPosition.argtypes = [POINTER(c_char), KIM_Channels]
        # *serialNumber, channel

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
