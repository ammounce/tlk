from ctypes import (POINTER, c_bool, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
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


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.DCServo.dll")

KIM_CanDeviceLockFrontPanel = lib.KIM_CanDeviceLockFrontPanel
KIM_CanDeviceLockFrontPanel.restype = c_bool
KIM_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_CheckConnection = lib.KIM_CheckConnection
KIM_CheckConnection.restype = c_bool
KIM_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_ClearMessageQueue = lib.KIM_ClearMessageQueue
KIM_ClearMessageQueue.restype = c_void_p
KIM_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_Close = lib.KIM_Close
KIM_Close.restype = c_void_p
KIM_Close.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_Disable = lib.KIM_Disable
KIM_Disable.restype = c_short
KIM_Disable.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_DisableChannel = lib.KIM_DisableChannel
KIM_DisableChannel.restype = c_short
KIM_DisableChannel.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_Disconnect = lib.KIM_Disconnect
KIM_Disconnect.restype = c_short
KIM_Disconnect.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_Enable = lib.KIM_Enable
KIM_Enable.restype = c_short
KIM_Enable.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_EnableChannel = lib.KIM_EnableChannel
KIM_EnableChannel.restype = c_short
KIM_EnableChannel.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_EnableLastMsgTimer = lib.KIM_EnableLastMsgTimer
KIM_EnableLastMsgTimer.restype = c_void_p
KIM_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNumber, enable, lastMsgTimeout

KIM_GetAbsoluteMoveParameters = lib.KIM_GetAbsoluteMoveParameters
KIM_GetAbsoluteMoveParameters.restype = c_short
KIM_GetAbsoluteMoveParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int32]
# *serialNumber, channel, &absoluteMove

KIM_GetCurrentPosition = lib.KIM_GetCurrentPosition
KIM_GetCurrentPosition.restype = c_int32
KIM_GetCurrentPosition.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_GetDriveOPParameters = lib.KIM_GetDriveOPParameters
KIM_GetDriveOPParameters.restype = c_short
KIM_GetDriveOPParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int16, c_int32, c_int32]
# *serialNumber, channel, &maxVoltage, &stepRate, &stepAcceleration

KIM_GetDriveOPParametersStruct = lib.KIM_GetDriveOPParametersStruct
KIM_GetDriveOPParametersStruct.restype = c_short
KIM_GetDriveOPParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_DriveOPParameters]
# *serialNumber, channel, &driveOPParameters

KIM_GetFeedbackSigParameters = lib.KIM_GetFeedbackSigParameters
KIM_GetFeedbackSigParameters.restype = c_short
KIM_GetFeedbackSigParameters.argtypes = [POINTER(c_char), KIM_Channels, KIM_FBSignalMode, c_int32]
# *serialNumber, channel, &feedbackSignalMode, &encoderConst

KIM_GetFeedbackSigParametersStruct = lib.KIM_GetFeedbackSigParametersStruct
KIM_GetFeedbackSigParametersStruct.restype = c_short
KIM_GetFeedbackSigParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_FeedbackSigParams]
# *serialNumber, channel, &fbSigParameters

KIM_GetFirmwareVersion = lib.KIM_GetFirmwareVersion
KIM_GetFirmwareVersion.restype = c_ulong
KIM_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_GetFrontPanelLocked = lib.KIM_GetFrontPanelLocked
KIM_GetFrontPanelLocked.restype = c_bool
KIM_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_GetHardwareInfo = lib.KIM_GetHardwareInfo
KIM_GetHardwareInfo.restype = c_short
KIM_GetHardwareInfo.argtypes = [
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
# *serialNumber, *modelNo, sizeOfModelNo, *type, *numChannels, *notes, sizeOfNotes, *firmwareVersion, *hardwareVersion, *modificationState

KIM_GetHardwareInfoBlock = lib.KIM_GetHardwareInfoBlock
KIM_GetHardwareInfoBlock.restype = c_short
KIM_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]
# *serialNumber, *hardwareInfo

KIM_GetHomeParameters = lib.KIM_GetHomeParameters
KIM_GetHomeParameters.restype = c_short
KIM_GetHomeParameters.argtypes = [
    POINTER(c_char),
    KIM_Channels,
    KIM_TravelDirection,
    KIM_TravelDirection,
    c_int32,
    c_int32]
# *serialNumber, channel, &homeDirection, &homeLimitSwitch, &homeStepRate, &homeOffset

KIM_GetHomeParametersStruct = lib.KIM_GetHomeParametersStruct
KIM_GetHomeParametersStruct.restype = c_short
KIM_GetHomeParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_HomeParameters]
# *serialNumber, channel, &homeParameters

KIM_GetJogParameters = lib.KIM_GetJogParameters
KIM_GetJogParameters.restype = c_short
KIM_GetJogParameters.argtypes = [POINTER(c_char), KIM_Channels, KIM_JogMode, c_int32, c_int32, c_int32, c_int32]
# *serialNumber, channel, &jogMode, &jogStepSizeFwd, &jogStepSizeRev, &jogStepRate, &jogStepAcceleration

KIM_GetJogParametersStruct = lib.KIM_GetJogParametersStruct
KIM_GetJogParametersStruct.restype = c_short
KIM_GetJogParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_JogParameters]
# *serialNumber, channel, &jogParameters

KIM_GetLimitSwitchParameters = lib.KIM_GetLimitSwitchParameters
KIM_GetLimitSwitchParameters.restype = c_short
KIM_GetLimitSwitchParameters.argtypes = [
    POINTER(c_char),
    KIM_Channels,
    KIM_LimitSwitchModes,
    KIM_LimitSwitchModes,
    c_int16]
# *serialNumber, channel, &forwardLimit, &reverseLimit, &stageID

KIM_GetLimitSwitchParametersStruct = lib.KIM_GetLimitSwitchParametersStruct
KIM_GetLimitSwitchParametersStruct.restype = c_short
KIM_GetLimitSwitchParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_LimitSwitchParameters]
# *serialNumber, channel, &limitSwitchParameters

KIM_GetMMIChannelParameters = lib.KIM_GetMMIChannelParameters
KIM_GetMMIChannelParameters.restype = c_short
KIM_GetMMIChannelParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int32, c_int32]
# *serialNumber, channel, &presetPos1, &presetPos2

KIM_GetMMIChannelParametersStruct = lib.KIM_GetMMIChannelParametersStruct
KIM_GetMMIChannelParametersStruct.restype = c_short
KIM_GetMMIChannelParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_MMIChannelParameters]
# *serialNumber, channel, &mmiParameters

KIM_GetMMIDeviceParameters = lib.KIM_GetMMIDeviceParameters
KIM_GetMMIDeviceParameters.restype = c_short
KIM_GetMMIDeviceParameters.argtypes = [
    POINTER(c_char),
    KIM_Channels,
    KIM_JoysticModes,
    c_int32,
    KIM_DirectionSense,
    c_int32,
    c_int32,
    c_int32]
# *serialNumber, channel, &joystickMode, &maxStepRate, &directionSense, &presetPos1, &presetPos2, &displayIntensity

KIM_GetMMIDeviceParametersStruct = lib.KIM_GetMMIDeviceParametersStruct
KIM_GetMMIDeviceParametersStruct.restype = c_short
KIM_GetMMIDeviceParametersStruct.argtypes = [POINTER(c_char), KIM_MMIParameters]
# *serialNumber, &mmiParameters

KIM_GetNextMessage = lib.KIM_GetNextMessage
KIM_GetNextMessage.restype = c_bool
KIM_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]
# *serialNumber, *messageType, *messageID, *messageData

KIM_GetRelativeMoveParameter = lib.KIM_GetRelativeMoveParameter
KIM_GetRelativeMoveParameter.restype = c_short
KIM_GetRelativeMoveParameter.argtypes = [POINTER(c_char), KIM_Channels, c_int32]
# *serialNumber, channel, &relativeMoveStep

KIM_GetSoftwareVersion = lib.KIM_GetSoftwareVersion
KIM_GetSoftwareVersion.restype = c_ulong
KIM_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_GetStageType = lib.KIM_GetStageType
KIM_GetStageType.restype = KIM_Stages
KIM_GetStageType.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_GetStatusBits = lib.KIM_GetStatusBits
KIM_GetStatusBits.restype = c_ulong
KIM_GetStatusBits.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_GetTrigIOParameters = lib.KIM_GetTrigIOParameters
KIM_GetTrigIOParameters.restype = c_short
KIM_GetTrigIOParameters.argtypes = [
    POINTER(c_char),
    KIM_TrigModes,
    KIM_TrigPolarities,
    KIM_Channels,
    KIM_TrigModes,
    KIM_TrigPolarities,
    KIM_Channels]
# *serialNumber, &trig1Mode, &trig1Polarity, &trigChannel1, &trig2Mode, &trig2Polarity, &trigChannel2

KIM_GetTrigIOParametersStruct = lib.KIM_GetTrigIOParametersStruct
KIM_GetTrigIOParametersStruct.restype = c_short
KIM_GetTrigIOParametersStruct.argtypes = [POINTER(c_char), KIM_TrigIOConfig]
# *serialNumber, &trigIOParameters

KIM_GetTrigParamsParameters = lib.KIM_GetTrigParamsParameters
KIM_GetTrigParamsParameters.restype = c_short
KIM_GetTrigParamsParameters.argtypes = [
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
# *serialNumber, channel, &startPosFwd, &intervalFwd, &numberOfPulsesFwd, &startPosRev, &intervalRev, &numberOfPulsesRev, &pulseWidth, &numberOfCycles

KIM_GetTrigParamsParametersStruct = lib.KIM_GetTrigParamsParametersStruct
KIM_GetTrigParamsParametersStruct.restype = c_short
KIM_GetTrigParamsParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_TrigParamsParameters]
# *serialNumber, channel, &trigParameters

KIM_HasLastMsgTimerOverrun = lib.KIM_HasLastMsgTimerOverrun
KIM_HasLastMsgTimerOverrun.restype = c_bool
KIM_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_Home = lib.KIM_Home
KIM_Home.restype = c_short
KIM_Home.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_Identify = lib.KIM_Identify
KIM_Identify.restype = c_void_p
KIM_Identify.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_IsDualChannelMode = lib.KIM_IsDualChannelMode
KIM_IsDualChannelMode.restype = c_bool
KIM_IsDualChannelMode.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_LoadNamedSettings = lib.KIM_LoadNamedSettings
KIM_LoadNamedSettings.restype = c_bool
KIM_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNumber, *settingsName

KIM_LoadSettings = lib.KIM_LoadSettings
KIM_LoadSettings.restype = c_bool
KIM_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_MessageQueueSize = lib.KIM_MessageQueueSize
KIM_MessageQueueSize.restype = c_int
KIM_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_MoveAbsolute = lib.KIM_MoveAbsolute
KIM_MoveAbsolute.restype = c_short
KIM_MoveAbsolute.argtypes = [POINTER(c_char), KIM_Channels, c_int32]
# *serialNumber, channel, position

KIM_MoveJog = lib.KIM_MoveJog
KIM_MoveJog.restype = c_short
KIM_MoveJog.argtypes = [POINTER(c_char), KIM_Channels, KIM_TravelDirection]
# *serialNumber, channel, jogDirection

KIM_MoveRelative = lib.KIM_MoveRelative
KIM_MoveRelative.restype = c_short
KIM_MoveRelative.argtypes = [POINTER(c_char), KIM_Channels, c_int32]
# *serialNumber, channel, stepSize

KIM_MoveStop = lib.KIM_MoveStop
KIM_MoveStop.restype = c_short
KIM_MoveStop.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_Open = lib.KIM_Open
KIM_Open.restype = c_short
KIM_Open.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_PersistSettings = lib.KIM_PersistSettings
KIM_PersistSettings.restype = c_bool
KIM_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_PollingDuration = lib.KIM_PollingDuration
KIM_PollingDuration.restype = c_long
KIM_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_RegisterMessageCallback = lib.KIM_RegisterMessageCallback
KIM_RegisterMessageCallback.restype = c_void_p
KIM_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNumber, void

KIM_RequestAbsoluteMoveParameters = lib.KIM_RequestAbsoluteMoveParameters
KIM_RequestAbsoluteMoveParameters.restype = c_short
KIM_RequestAbsoluteMoveParameters.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestCurrentPosition = lib.KIM_RequestCurrentPosition
KIM_RequestCurrentPosition.restype = c_short
KIM_RequestCurrentPosition.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestDriveOPParameters = lib.KIM_RequestDriveOPParameters
KIM_RequestDriveOPParameters.restype = c_short
KIM_RequestDriveOPParameters.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestFeedbackSigParameters = lib.KIM_RequestFeedbackSigParameters
KIM_RequestFeedbackSigParameters.restype = c_short
KIM_RequestFeedbackSigParameters.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestFrontPanelLocked = lib.KIM_RequestFrontPanelLocked
KIM_RequestFrontPanelLocked.restype = c_short
KIM_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_RequestHomeParameters = lib.KIM_RequestHomeParameters
KIM_RequestHomeParameters.restype = c_short
KIM_RequestHomeParameters.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestJogParameters = lib.KIM_RequestJogParameters
KIM_RequestJogParameters.restype = c_short
KIM_RequestJogParameters.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestLimitSwitchParameters = lib.KIM_RequestLimitSwitchParameters
KIM_RequestLimitSwitchParameters.restype = c_short
KIM_RequestLimitSwitchParameters.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestMMIParameters = lib.KIM_RequestMMIParameters
KIM_RequestMMIParameters.restype = c_short
KIM_RequestMMIParameters.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestRelativeMoveParameter = lib.KIM_RequestRelativeMoveParameter
KIM_RequestRelativeMoveParameter.restype = c_short
KIM_RequestRelativeMoveParameter.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_RequestSettings = lib.KIM_RequestSettings
KIM_RequestSettings.restype = c_short
KIM_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_RequestStageType = lib.KIM_RequestStageType
KIM_RequestStageType.restype = c_short
KIM_RequestStageType.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_RequestStatus = lib.KIM_RequestStatus
KIM_RequestStatus.restype = c_short
KIM_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_RequestStatusBits = lib.KIM_RequestStatusBits
KIM_RequestStatusBits.restype = c_short
KIM_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_RequestTrigIOParameters = lib.KIM_RequestTrigIOParameters
KIM_RequestTrigIOParameters.restype = c_short
KIM_RequestTrigIOParameters.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_RequestTrigParamsParameters = lib.KIM_RequestTrigParamsParameters
KIM_RequestTrigParamsParameters.restype = c_short
KIM_RequestTrigParamsParameters.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

KIM_Reset = lib.KIM_Reset
KIM_Reset.restype = c_short
KIM_Reset.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_SetAbsoluteMoveParameters = lib.KIM_SetAbsoluteMoveParameters
KIM_SetAbsoluteMoveParameters.restype = c_short
KIM_SetAbsoluteMoveParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int32]
# *serialNumber, channel, &absoluteMove

KIM_SetDriveOPParameters = lib.KIM_SetDriveOPParameters
KIM_SetDriveOPParameters.restype = c_short
KIM_SetDriveOPParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int16, c_int32, c_int32]
# *serialNumber, channel, maxVoltage, stepRate, stepAcceleration

KIM_SetDriveOPParametersStruct = lib.KIM_SetDriveOPParametersStruct
KIM_SetDriveOPParametersStruct.restype = c_short
KIM_SetDriveOPParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_DriveOPParameters]
# *serialNumber, channel, &driveOPParameters

KIM_SetDualChannelMode = lib.KIM_SetDualChannelMode
KIM_SetDualChannelMode.restype = c_short
KIM_SetDualChannelMode.argtypes = [POINTER(c_char), c_bool]
# *serialNumber, enableDualChannel

KIM_SetFeedbackSigParameters = lib.KIM_SetFeedbackSigParameters
KIM_SetFeedbackSigParameters.restype = c_short
KIM_SetFeedbackSigParameters.argtypes = [POINTER(c_char), KIM_Channels, KIM_FBSignalMode, c_int32]
# *serialNumber, channel, feedbackSignalMode, encoderConst

KIM_SetFeedbackSigParametersStruct = lib.KIM_SetFeedbackSigParametersStruct
KIM_SetFeedbackSigParametersStruct.restype = c_short
KIM_SetFeedbackSigParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_FeedbackSigParams]
# *serialNumber, channel, &fbSigParameters

KIM_SetFrontPanelLock = lib.KIM_SetFrontPanelLock
KIM_SetFrontPanelLock.restype = c_short
KIM_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
# *serialNumber, locked

KIM_SetHomeParameters = lib.KIM_SetHomeParameters
KIM_SetHomeParameters.restype = c_short
KIM_SetHomeParameters.argtypes = [
    POINTER(c_char),
    KIM_Channels,
    KIM_TravelDirection,
    KIM_TravelDirection,
    c_int32,
    c_int32]
# *serialNumber, channel, homeDirection, homeLimitSwitch, homeStepRate, homeOffset

KIM_SetHomeParametersStruct = lib.KIM_SetHomeParametersStruct
KIM_SetHomeParametersStruct.restype = c_short
KIM_SetHomeParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_HomeParameters]
# *serialNumber, channel, &homeParameters

KIM_SetJogParameters = lib.KIM_SetJogParameters
KIM_SetJogParameters.restype = c_short
KIM_SetJogParameters.argtypes = [POINTER(c_char), KIM_Channels, KIM_JogMode, c_int32, c_int32, c_int32, c_int32]
# *serialNumber, channel, jogMode, jogStepSizeFwd, jogStepSizeRev, jogStepRate, jogStepAcceleration

KIM_SetJogParametersStruct = lib.KIM_SetJogParametersStruct
KIM_SetJogParametersStruct.restype = c_short
KIM_SetJogParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_JogParameters]
# *serialNumber, channel, &jogParameters

KIM_SetLimitSwitchParameters = lib.KIM_SetLimitSwitchParameters
KIM_SetLimitSwitchParameters.restype = c_short
KIM_SetLimitSwitchParameters.argtypes = [
    POINTER(c_char),
    KIM_Channels,
    KIM_LimitSwitchModes,
    KIM_LimitSwitchModes,
    c_int16]
# *serialNumber, channel, forwardLimit, reverseLimit, stageID

KIM_SetLimitSwitchParametersStruct = lib.KIM_SetLimitSwitchParametersStruct
KIM_SetLimitSwitchParametersStruct.restype = c_short
KIM_SetLimitSwitchParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_LimitSwitchParameters]
# *serialNumber, channel, &limitSwitchParameters

KIM_SetMMIChannelParameters = lib.KIM_SetMMIChannelParameters
KIM_SetMMIChannelParameters.restype = c_short
KIM_SetMMIChannelParameters.argtypes = [POINTER(c_char), KIM_Channels, c_int32, c_int32]
# *serialNumber, channel, presetPos1, presetPos2

KIM_SetMMIChannelParametersStruct = lib.KIM_SetMMIChannelParametersStruct
KIM_SetMMIChannelParametersStruct.restype = c_short
KIM_SetMMIChannelParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_MMIChannelParameters]
# *serialNumber, channel, &mmiParameters

KIM_SetMMIDeviceParameters = lib.KIM_SetMMIDeviceParameters
KIM_SetMMIDeviceParameters.restype = c_short
KIM_SetMMIDeviceParameters.argtypes = [POINTER(c_char), KIM_JoysticModes, c_int32, KIM_DirectionSense, c_int16]
# *serialNumber, joystickMode, maxStepRate, directionSense, displayIntensity

KIM_SetMMIDeviceParametersStruct = lib.KIM_SetMMIDeviceParametersStruct
KIM_SetMMIDeviceParametersStruct.restype = c_short
KIM_SetMMIDeviceParametersStruct.argtypes = [POINTER(c_char), KIM_MMIParameters]
# *serialNumber, &mmiParameters

KIM_SetPosition = lib.KIM_SetPosition
KIM_SetPosition.restype = c_short
KIM_SetPosition.argtypes = [POINTER(c_char), KIM_Channels, c_long]
# *serialNumber, channel, position

KIM_SetRelativeMoveParameter = lib.KIM_SetRelativeMoveParameter
KIM_SetRelativeMoveParameter.restype = c_short
KIM_SetRelativeMoveParameter.argtypes = [POINTER(c_char), KIM_Channels, c_int32]
# *serialNumber, channel, &relativeMove

KIM_SetStageType = lib.KIM_SetStageType
KIM_SetStageType.restype = c_short
KIM_SetStageType.argtypes = [POINTER(c_char), KIM_Stages]
# *serialNumber, stageType

KIM_SetTrigIOParameters = lib.KIM_SetTrigIOParameters
KIM_SetTrigIOParameters.restype = c_short
KIM_SetTrigIOParameters.argtypes = [
    POINTER(c_char),
    KIM_TrigModes,
    KIM_TrigPolarities,
    KIM_Channels,
    KIM_TrigModes,
    KIM_TrigPolarities,
    KIM_Channels]
# *serialNumber, trig1Mode, trig1Polarity, trigChannel1, trig2Mode, trig2Polarity, trigChannel2

KIM_SetTrigIOParametersStruct = lib.KIM_SetTrigIOParametersStruct
KIM_SetTrigIOParametersStruct.restype = c_short
KIM_SetTrigIOParametersStruct.argtypes = [POINTER(c_char), KIM_TrigIOConfig]
# *serialNumber, &trigIOParameters

KIM_SetTrigParamsParameters = lib.KIM_SetTrigParamsParameters
KIM_SetTrigParamsParameters.restype = c_short
KIM_SetTrigParamsParameters.argtypes = [
    POINTER(c_char),
    KIM_Channels,
    KIM_TrigParamsParameters,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]
# *serialNumber, channel, &trigParameters, startPosFwd, intervalFwd, numberOfPulsesFwd, startPosRev, intervalRev, numberOfPulsesRev, pulseWidth, numberOfCycles

KIM_SetTrigParamsParametersStruct = lib.KIM_SetTrigParamsParametersStruct
KIM_SetTrigParamsParametersStruct.restype = c_short
KIM_SetTrigParamsParametersStruct.argtypes = [POINTER(c_char), KIM_Channels, KIM_TrigParamsParameters]
# *serialNumber, channel, &trigParameters

KIM_StartPolling = lib.KIM_StartPolling
KIM_StartPolling.restype = c_bool
KIM_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNumber, milliseconds

KIM_StopPolling = lib.KIM_StopPolling
KIM_StopPolling.restype = c_void_p
KIM_StopPolling.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_SupportsDualChannelMode = lib.KIM_SupportsDualChannelMode
KIM_SupportsDualChannelMode.restype = c_bool
KIM_SupportsDualChannelMode.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_SupportsStageType = lib.KIM_SupportsStageType
KIM_SupportsStageType.restype = c_bool
KIM_SupportsStageType.argtypes = [POINTER(c_char)]
# *serialNumber

KIM_TimeSinceLastMsgReceived = lib.KIM_TimeSinceLastMsgReceived
KIM_TimeSinceLastMsgReceived.restype = c_bool
KIM_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]
# *serialNumber, &lastUpdateTimeMS

KIM_WaitForMessage = lib.KIM_WaitForMessage
KIM_WaitForMessage.restype = c_bool
KIM_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]
# *serialNumber, *messageType, *messageID, *messageData

KIM_ZeroPosition = lib.KIM_ZeroPosition
KIM_ZeroPosition.restype = c_short
KIM_ZeroPosition.argtypes = [POINTER(c_char), KIM_Channels]
# *serialNumber, channel

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
