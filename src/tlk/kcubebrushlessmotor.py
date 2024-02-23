from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_double,
    c_int,
    c_int16,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_uint,
    c_ulong,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_WheelDirectionSense,
    KMOT_WheelMode,
    MOT_JogModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_MovementDirections,
    MOT_MovementModes,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes)
from .definitions.structures import (
    KMOT_MMIParams,
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_BrushlessCurrentLoopParameters,
    MOT_BrushlessElectricOutputParameters,
    MOT_BrushlessPositionLoopParameters,
    MOT_BrushlessTrackSettleParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_StageAxisParameters,
    MOT_VelocityParameters,
    MOT_VelocityProfileParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.KCube.BrushlessMotor.dll")
BMC_CanDeviceLockFrontPanel = lib.BMC_CanDeviceLockFrontPanel
BMC_CanDeviceLockFrontPanel.restype = c_bool
BMC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
# *serialNo

BMC_CanHome = lib.BMC_CanHome
BMC_CanHome.restype = c_bool
BMC_CanHome.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_CanMoveWithoutHomingFirst = lib.BMC_CanMoveWithoutHomingFirst
BMC_CanMoveWithoutHomingFirst.restype = c_bool
BMC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_CheckConnection = lib.BMC_CheckConnection
BMC_CheckConnection.restype = c_bool
BMC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

BMC_ClearMessageQueue = lib.BMC_ClearMessageQueue
BMC_ClearMessageQueue.restype = c_short
BMC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_Close = lib.BMC_Close
BMC_Close.restype = c_short
BMC_Close.argtypes = [POINTER(c_char)]
# *serialNo

BMC_DisableChannel = lib.BMC_DisableChannel
BMC_DisableChannel.restype = c_short
BMC_DisableChannel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_EnableChannel = lib.BMC_EnableChannel
BMC_EnableChannel.restype = c_short
BMC_EnableChannel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_EnableLastMsgTimer = lib.BMC_EnableLastMsgTimer
BMC_EnableLastMsgTimer.restype = None
BMC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]
# *serialNo, channel, enable, lastMsgTimeout

BMC_GetBacklash = lib.BMC_GetBacklash
BMC_GetBacklash.restype = c_long
BMC_GetBacklash.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetCurrentLoopParams = lib.BMC_GetCurrentLoopParams
BMC_GetCurrentLoopParams.restype = c_short
BMC_GetCurrentLoopParams.argtypes = [MOT_BrushlessCurrentLoopParameters, POINTER(c_char), POINTER(c_char), c_short]
# *currentLoopParams, *serialNo, *serialNo, channel

BMC_GetDeviceUnitFromRealValue = lib.BMC_GetDeviceUnitFromRealValue
BMC_GetDeviceUnitFromRealValue.restype = c_short
BMC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_short, c_double, c_int]
# *device_unit, *serialNo, channel, real_unit, unitType

BMC_GetDigitalOutputs = lib.BMC_GetDigitalOutputs
BMC_GetDigitalOutputs.restype = c_byte
BMC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetElectricOutputParams = lib.BMC_GetElectricOutputParams
BMC_GetElectricOutputParams.restype = c_short
BMC_GetElectricOutputParams.argtypes = [
    MOT_BrushlessElectricOutputParameters,
    POINTER(c_char),
    POINTER(c_char),
    c_short]
# *electricOutputParams, *serialNo, *serialNo, channel

BMC_GetEncoderCounter = lib.BMC_GetEncoderCounter
BMC_GetEncoderCounter.restype = c_long
BMC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetFirmwareVersion = lib.BMC_GetFirmwareVersion
BMC_GetFirmwareVersion.restype = c_ulong
BMC_GetFirmwareVersion.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetFrontPanelLocked = lib.BMC_GetFrontPanelLocked
BMC_GetFrontPanelLocked.restype = c_bool
BMC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

BMC_GetHardwareInfo = lib.BMC_GetHardwareInfo
BMC_GetHardwareInfo.restype = c_short
BMC_GetHardwareInfo.argtypes = [
    c_ulong,
    c_long,
    POINTER(c_char),
    c_long,
    POINTER(c_char),
    c_short,
    POINTER(c_char),
    c_long,
    c_short,
    c_ulong,
    c_ulong]
# *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numChannels, *serialNo, *type, channel, sizeOfModelNo, sizeOfNotes

BMC_GetHardwareInfoBlock = lib.BMC_GetHardwareInfoBlock
BMC_GetHardwareInfoBlock.restype = c_short
BMC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char), c_short]
# *hardwareInfo, *serialNo, channel

BMC_GetHomingParamsBlock = lib.BMC_GetHomingParamsBlock
BMC_GetHomingParamsBlock.restype = c_short
BMC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), POINTER(c_char), c_short]
# *homingParams, *serialNo, *serialNo, channel

BMC_GetHomingVelocity = lib.BMC_GetHomingVelocity
BMC_GetHomingVelocity.restype = c_uint
BMC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetJogMode = lib.BMC_GetJogMode
BMC_GetJogMode.restype = c_short
BMC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes, c_short]
# *mode, *serialNo, *stopMode, channel

BMC_GetJogParamsBlock = lib.BMC_GetJogParamsBlock
BMC_GetJogParamsBlock.restype = c_short
BMC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char), POINTER(c_char), c_short]
# *jogParams, *serialNo, *serialNo, channel

BMC_GetJogStepSize = lib.BMC_GetJogStepSize
BMC_GetJogStepSize.restype = c_uint
BMC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetJogVelParams = lib.BMC_GetJogVelParams
BMC_GetJogVelParams.restype = c_short
BMC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
# *acceleration, *maxVelocity, *serialNo, channel

BMC_GetMMIParams = lib.BMC_GetMMIParams
BMC_GetMMIParams.restype = c_short
BMC_GetMMIParams.argtypes = [
    KMOT_WheelDirectionSense,
    c_int16,
    c_int32,
    c_int32,
    POINTER(c_char),
    c_int32,
    c_int32,
    KMOT_WheelMode]
# *directionSense, *displayIntensity, *presetPosition1, *presetPosition2, *serialNo, *wheelAcceleration, *wheelMaxVelocity, *wheelMode

BMC_GetMMIParamsBlock = lib.BMC_GetMMIParamsBlock
BMC_GetMMIParamsBlock.restype = c_short
BMC_GetMMIParamsBlock.argtypes = [KMOT_MMIParams, POINTER(c_char)]
# *mmiParams, *serialNo

BMC_GetMMIParamsExt = lib.BMC_GetMMIParamsExt
BMC_GetMMIParamsExt.restype = c_short
BMC_GetMMIParamsExt.argtypes = [
    KMOT_WheelDirectionSense,
    c_int16,
    c_int16,
    c_int16,
    c_int32,
    c_int32,
    POINTER(c_char),
    c_int32,
    c_int32,
    KMOT_WheelMode]
# *directionSense, *displayDimIntensity, *displayIntensity, *displayTimeout, *presetPosition1, *presetPosition2, *serialNo, *wheelAcceleration, *wheelMaxVelocity, *wheelMode

BMC_GetMotorParams = lib.BMC_GetMotorParams
BMC_GetMotorParams.restype = c_short
BMC_GetMotorParams.argtypes = [c_long, POINTER(c_char), c_short]
# *countsPerUnit, *serialNo, channel

BMC_GetMotorParamsExt = lib.BMC_GetMotorParamsExt
BMC_GetMotorParamsExt.restype = c_short
BMC_GetMotorParamsExt.argtypes = [c_double, POINTER(c_char), c_short]
# *countsPerUnit, *serialNo, channel

BMC_GetMotorTravelLimits = lib.BMC_GetMotorTravelLimits
BMC_GetMotorTravelLimits.restype = c_short
BMC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
# *maxPosition, *minPosition, *serialNo, channel

BMC_GetMotorTravelMode = lib.BMC_GetMotorTravelMode
BMC_GetMotorTravelMode.restype = MOT_TravelModes
BMC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetMotorVelocityLimits = lib.BMC_GetMotorVelocityLimits
BMC_GetMotorVelocityLimits.restype = c_short
BMC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
# *maxAcceleration, *maxVelocity, *serialNo, channel

BMC_GetMoveAbsolutePosition = lib.BMC_GetMoveAbsolutePosition
BMC_GetMoveAbsolutePosition.restype = c_int
BMC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetMoveRelativeDistance = lib.BMC_GetMoveRelativeDistance
BMC_GetMoveRelativeDistance.restype = c_int
BMC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetNextMessage = lib.BMC_GetNextMessage
BMC_GetNextMessage.restype = c_bool
BMC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
# *messageData, *messageID, *messageType, *serialNo, channel

BMC_GetNumberPositions = lib.BMC_GetNumberPositions
BMC_GetNumberPositions.restype = c_int
BMC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetPosLoopParams = lib.BMC_GetPosLoopParams
BMC_GetPosLoopParams.restype = c_short
BMC_GetPosLoopParams.argtypes = [MOT_BrushlessPositionLoopParameters, POINTER(c_char), POINTER(c_char), c_short]
# *positionLoopParams, *serialNo, *serialNo, channel

BMC_GetPosition = lib.BMC_GetPosition
BMC_GetPosition.restype = c_int
BMC_GetPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetPositionCounter = lib.BMC_GetPositionCounter
BMC_GetPositionCounter.restype = c_long
BMC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetRealValueFromDeviceUnit = lib.BMC_GetRealValueFromDeviceUnit
BMC_GetRealValueFromDeviceUnit.restype = c_short
BMC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_short, c_int, c_int]
# *real_unit, *serialNo, channel, device_unit, unitType

BMC_GetSoftLimitMode = lib.BMC_GetSoftLimitMode
BMC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
BMC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetSoftwareVersion = lib.BMC_GetSoftwareVersion
BMC_GetSoftwareVersion.restype = c_ulong
BMC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

BMC_GetStageAxisMaxPos = lib.BMC_GetStageAxisMaxPos
BMC_GetStageAxisMaxPos.restype = c_int
BMC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetStageAxisMinPos = lib.BMC_GetStageAxisMinPos
BMC_GetStageAxisMinPos.restype = c_int
BMC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetStageAxisParams = lib.BMC_GetStageAxisParams
BMC_GetStageAxisParams.restype = c_short
BMC_GetStageAxisParams.argtypes = [
    c_long,
    c_ulong,
    c_int,
    c_int,
    c_int,
    c_int,
    c_int,
    POINTER(c_char),
    POINTER(c_char),
    POINTER(c_char),
    c_ulong,
    c_long,
    c_short,
    c_ulong]
# *axisID, *countsPerUnit, *maxAcceleration, *maxDecceleration, *maxPosition, *maxVelocity, *minPosition, *partNumber, *serialNo, *serialNo, *serialNumber, *stageID, channel, size

BMC_GetStageAxisParamsBlock = lib.BMC_GetStageAxisParamsBlock
BMC_GetStageAxisParamsBlock.restype = c_short
BMC_GetStageAxisParamsBlock.argtypes = [POINTER(c_char), POINTER(c_char), MOT_StageAxisParameters, c_short]
# *serialNo, *serialNo, *stageAxisParams, channel

BMC_GetStatusBits = lib.BMC_GetStatusBits
BMC_GetStatusBits.restype = c_ulong
BMC_GetStatusBits.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetTrackSettleParams = lib.BMC_GetTrackSettleParams
BMC_GetTrackSettleParams.restype = c_short
BMC_GetTrackSettleParams.argtypes = [POINTER(c_char), POINTER(c_char), MOT_BrushlessTrackSettleParameters, c_short]
# *serialNo, *serialNo, *settleParams, channel

BMC_GetTriggerConfigParams = lib.BMC_GetTriggerConfigParams
BMC_GetTriggerConfigParams.restype = c_short
BMC_GetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]
# *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity

BMC_GetTriggerConfigParamsBlock = lib.BMC_GetTriggerConfigParamsBlock
BMC_GetTriggerConfigParamsBlock.restype = c_short
BMC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
# *serialNo, *triggerConfigParams

BMC_GetTriggerParamsParams = lib.BMC_GetTriggerParamsParams
BMC_GetTriggerParamsParams.restype = c_short
BMC_GetTriggerParamsParams.argtypes = [
    c_int32,
    POINTER(c_char),
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]
# *cycleCount, *serialNo, *triggerIntervalFwd, *triggerIntervalRev, *triggerPulseCountFwd, *triggerPulseCountRev, *triggerPulseWidth, *triggerStartPositionFwd, *triggerStartPositionRev

BMC_GetTriggerParamsParamsBlock = lib.BMC_GetTriggerParamsParamsBlock
BMC_GetTriggerParamsParamsBlock.restype = c_short
BMC_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
# *serialNo, *triggerParamsParams

BMC_GetTriggerSwitches = lib.BMC_GetTriggerSwitches
BMC_GetTriggerSwitches.restype = c_byte
BMC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_GetVelParams = lib.BMC_GetVelParams
BMC_GetVelParams.restype = c_short
BMC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
# *acceleration, *maxVelocity, *serialNo, channel

BMC_GetVelParamsBlock = lib.BMC_GetVelParamsBlock
BMC_GetVelParamsBlock.restype = c_short
BMC_GetVelParamsBlock.argtypes = [POINTER(c_char), POINTER(c_char), MOT_VelocityParameters, c_short]
# *serialNo, *serialNo, *velocityParams, channel

BMC_GetVelocityProfileParams = lib.BMC_GetVelocityProfileParams
BMC_GetVelocityProfileParams.restype = c_short
BMC_GetVelocityProfileParams.argtypes = [POINTER(c_char), POINTER(c_char), MOT_VelocityProfileParameters, c_short]
# *serialNo, *serialNo, *velocityProfileParams, channel

BMC_HasLastMsgTimerOverrun = lib.BMC_HasLastMsgTimerOverrun
BMC_HasLastMsgTimerOverrun.restype = c_bool
BMC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_Home = lib.BMC_Home
BMC_Home.restype = c_short
BMC_Home.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_Identify = lib.BMC_Identify
BMC_Identify.restype = None
BMC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

BMC_LoadNamedSettings = lib.BMC_LoadNamedSettings
BMC_LoadNamedSettings.restype = c_bool
BMC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
# *serialNo, *settingsName, channel

BMC_LoadSettings = lib.BMC_LoadSettings
BMC_LoadSettings.restype = c_bool
BMC_LoadSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_MessageQueueSize = lib.BMC_MessageQueueSize
BMC_MessageQueueSize.restype = c_int
BMC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_MoveAbsolute = lib.BMC_MoveAbsolute
BMC_MoveAbsolute.restype = c_short
BMC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_MoveAtVelocity = lib.BMC_MoveAtVelocity
BMC_MoveAtVelocity.restype = c_short
BMC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
# *serialNo, channel, direction

BMC_MoveJog = lib.BMC_MoveJog
BMC_MoveJog.restype = c_short
BMC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
# *serialNo, channel, jogDirection

BMC_MoveRelative = lib.BMC_MoveRelative
BMC_MoveRelative.restype = c_short
BMC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, displacement

BMC_MoveRelativeDistance = lib.BMC_MoveRelativeDistance
BMC_MoveRelativeDistance.restype = c_short
BMC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_MoveToPosition = lib.BMC_MoveToPosition
BMC_MoveToPosition.restype = c_short
BMC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, index

BMC_NeedsHoming = lib.BMC_NeedsHoming
BMC_NeedsHoming.restype = c_bool
BMC_NeedsHoming.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_Open = lib.BMC_Open
BMC_Open.restype = c_short
BMC_Open.argtypes = [POINTER(c_char)]
# *serialNo

BMC_OverrideHomeRequirement = lib.BMC_OverrideHomeRequirement
BMC_OverrideHomeRequirement.restype = c_short
BMC_OverrideHomeRequirement.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_PersistSettings = lib.BMC_PersistSettings
BMC_PersistSettings.restype = c_bool
BMC_PersistSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_PollingDuration = lib.BMC_PollingDuration
BMC_PollingDuration.restype = c_long
BMC_PollingDuration.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RegisterMessageCallback = lib.BMC_RegisterMessageCallback
BMC_RegisterMessageCallback.restype = c_short
BMC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, None]
# *serialNo, channel, void

BMC_RequestBacklash = lib.BMC_RequestBacklash
BMC_RequestBacklash.restype = c_short
BMC_RequestBacklash.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestCurrentLoopParams = lib.BMC_RequestCurrentLoopParams
BMC_RequestCurrentLoopParams.restype = c_short
BMC_RequestCurrentLoopParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestDigitalOutputs = lib.BMC_RequestDigitalOutputs
BMC_RequestDigitalOutputs.restype = c_short
BMC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestElectricOutputParams = lib.BMC_RequestElectricOutputParams
BMC_RequestElectricOutputParams.restype = c_short
BMC_RequestElectricOutputParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestEncoderCounter = lib.BMC_RequestEncoderCounter
BMC_RequestEncoderCounter.restype = c_short
BMC_RequestEncoderCounter.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestFrontPanelLocked = lib.BMC_RequestFrontPanelLocked
BMC_RequestFrontPanelLocked.restype = c_short
BMC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

BMC_RequestHomingParams = lib.BMC_RequestHomingParams
BMC_RequestHomingParams.restype = c_short
BMC_RequestHomingParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestJogParams = lib.BMC_RequestJogParams
BMC_RequestJogParams.restype = c_short
BMC_RequestJogParams.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
# *serialNo, *serialNo, channel

BMC_RequestMMIparams = lib.BMC_RequestMMIparams
BMC_RequestMMIparams.restype = c_short
BMC_RequestMMIparams.argtypes = [POINTER(c_char)]
# *serialNo

BMC_RequestMoveAbsolutePosition = lib.BMC_RequestMoveAbsolutePosition
BMC_RequestMoveAbsolutePosition.restype = c_short
BMC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestMoveRelativeDistance = lib.BMC_RequestMoveRelativeDistance
BMC_RequestMoveRelativeDistance.restype = c_short
BMC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestPosLoopParams = lib.BMC_RequestPosLoopParams
BMC_RequestPosLoopParams.restype = c_short
BMC_RequestPosLoopParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestPosTriggerParams = lib.BMC_RequestPosTriggerParams
BMC_RequestPosTriggerParams.restype = c_short
BMC_RequestPosTriggerParams.argtypes = [POINTER(c_char)]
# *serialNo

BMC_RequestPosition = lib.BMC_RequestPosition
BMC_RequestPosition.restype = c_short
BMC_RequestPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestSettings = lib.BMC_RequestSettings
BMC_RequestSettings.restype = c_short
BMC_RequestSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestStageAxisParams = lib.BMC_RequestStageAxisParams
BMC_RequestStageAxisParams.restype = c_short
BMC_RequestStageAxisParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestStatusBits = lib.BMC_RequestStatusBits
BMC_RequestStatusBits.restype = c_short
BMC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestTrackSettleParams = lib.BMC_RequestTrackSettleParams
BMC_RequestTrackSettleParams.restype = c_short
BMC_RequestTrackSettleParams.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
# *serialNo, *serialNo, channel

BMC_RequestTriggerConfigParams = lib.BMC_RequestTriggerConfigParams
BMC_RequestTriggerConfigParams.restype = c_short
BMC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
# *serialNo

BMC_RequestTriggerSwitches = lib.BMC_RequestTriggerSwitches
BMC_RequestTriggerSwitches.restype = c_short
BMC_RequestTriggerSwitches.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestVelParams = lib.BMC_RequestVelParams
BMC_RequestVelParams.restype = c_short
BMC_RequestVelParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_RequestVelocityProfileParams = lib.BMC_RequestVelocityProfileParams
BMC_RequestVelocityProfileParams.restype = c_short
BMC_RequestVelocityProfileParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_ResetRotationModes = lib.BMC_ResetRotationModes
BMC_ResetRotationModes.restype = c_short
BMC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_ResetStageToDefaults = lib.BMC_ResetStageToDefaults
BMC_ResetStageToDefaults.restype = c_short
BMC_ResetStageToDefaults.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_ResumeMoveMessages = lib.BMC_ResumeMoveMessages
BMC_ResumeMoveMessages.restype = c_short
BMC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_SetBacklash = lib.BMC_SetBacklash
BMC_SetBacklash.restype = c_short
BMC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, channel, distance

BMC_SetCurrentLoopParams = lib.BMC_SetCurrentLoopParams
BMC_SetCurrentLoopParams.restype = c_short
BMC_SetCurrentLoopParams.argtypes = [MOT_BrushlessCurrentLoopParameters, POINTER(c_char), POINTER(c_char), c_short]
# *currentLoopParams, *serialNo, *serialNo, channel

BMC_SetDigitalOutputs = lib.BMC_SetDigitalOutputs
BMC_SetDigitalOutputs.restype = c_short
BMC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]
# *serialNo, channel, outputsBits

BMC_SetDirection = lib.BMC_SetDirection
BMC_SetDirection.restype = c_short
BMC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]
# *serialNo, channel, reverse

BMC_SetElectricOutputParams = lib.BMC_SetElectricOutputParams
BMC_SetElectricOutputParams.restype = c_short
BMC_SetElectricOutputParams.argtypes = [
    MOT_BrushlessElectricOutputParameters,
    POINTER(c_char),
    POINTER(c_char),
    c_short]
# *electricOutputParams, *serialNo, *serialNo, channel

BMC_SetEncoderCounter = lib.BMC_SetEncoderCounter
BMC_SetEncoderCounter.restype = c_short
BMC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, channel, count

BMC_SetFrontPanelLock = lib.BMC_SetFrontPanelLock
BMC_SetFrontPanelLock.restype = c_short
BMC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
# *serialNo, locked

BMC_SetHomingParamsBlock = lib.BMC_SetHomingParamsBlock
BMC_SetHomingParamsBlock.restype = c_short
BMC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), POINTER(c_char), c_short]
# *homingParams, *serialNo, *serialNo, channel

BMC_SetHomingVelocity = lib.BMC_SetHomingVelocity
BMC_SetHomingVelocity.restype = c_short
BMC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]
# *serialNo, channel, velocity

BMC_SetJogMode = lib.BMC_SetJogMode
BMC_SetJogMode.restype = c_short
BMC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]
# *serialNo, channel, mode, stopMode

BMC_SetJogParamsBlock = lib.BMC_SetJogParamsBlock
BMC_SetJogParamsBlock.restype = c_short
BMC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char), POINTER(c_char), c_short]
# *jogParams, *serialNo, *serialNo, channel

BMC_SetJogStepSize = lib.BMC_SetJogStepSize
BMC_SetJogStepSize.restype = c_short
BMC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]
# *serialNo, channel, stepSize

BMC_SetJogVelParams = lib.BMC_SetJogVelParams
BMC_SetJogVelParams.restype = c_short
BMC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
# *serialNo, acceleration, channel, maxVelocity

BMC_SetLimitsSoftwareApproachPolicy = lib.BMC_SetLimitsSoftwareApproachPolicy
BMC_SetLimitsSoftwareApproachPolicy.restype = None
BMC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]
# *serialNo, channel, limitsSoftwareApproachPolicy

BMC_SetMMIParams = lib.BMC_SetMMIParams
BMC_SetMMIParams.restype = c_short
BMC_SetMMIParams.argtypes = [
    POINTER(c_char),
    KMOT_WheelDirectionSense,
    c_int16,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    KMOT_WheelMode]
# *serialNo, directionSense, displayIntensity, presetPosition1, presetPosition2, wheelAcceleration, wheelMaxVelocity, wheelMode

BMC_SetMMIParamsBlock = lib.BMC_SetMMIParamsBlock
BMC_SetMMIParamsBlock.restype = c_short
BMC_SetMMIParamsBlock.argtypes = [KMOT_MMIParams, POINTER(c_char)]
# *mmiParams, *serialNo

BMC_SetMMIParamsExt = lib.BMC_SetMMIParamsExt
BMC_SetMMIParamsExt.restype = c_short
BMC_SetMMIParamsExt.argtypes = [
    POINTER(c_char),
    KMOT_WheelDirectionSense,
    c_int16,
    c_int16,
    c_int16,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    KMOT_WheelMode]
# *serialNo, directionSense, displayDimIntensity, displayIntensity, displayTimeout, presetPosition1, presetPosition2, wheelAcceleration, wheelMaxVelocity, wheelMode

BMC_SetMotorParams = lib.BMC_SetMotorParams
BMC_SetMotorParams.restype = c_short
BMC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, channel, countsPerUnit

BMC_SetMotorParamsExt = lib.BMC_SetMotorParamsExt
BMC_SetMotorParamsExt.restype = c_short
BMC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double]
# *serialNo, channel, countsPerUnit

BMC_SetMotorTravelLimits = lib.BMC_SetMotorTravelLimits
BMC_SetMotorTravelLimits.restype = c_short
BMC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
# *serialNo, channel, maxPosition, minPosition

BMC_SetMotorTravelMode = lib.BMC_SetMotorTravelMode
BMC_SetMotorTravelMode.restype = c_short
BMC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]
# *serialNo, channel, travelMode

BMC_SetMotorVelocityLimits = lib.BMC_SetMotorVelocityLimits
BMC_SetMotorVelocityLimits.restype = c_short
BMC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
# *serialNo, channel, maxAcceleration, maxVelocity

BMC_SetMoveAbsolutePosition = lib.BMC_SetMoveAbsolutePosition
BMC_SetMoveAbsolutePosition.restype = c_short
BMC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, position

BMC_SetMoveRelativeDistance = lib.BMC_SetMoveRelativeDistance
BMC_SetMoveRelativeDistance.restype = c_short
BMC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, distance

BMC_SetPosLoopParams = lib.BMC_SetPosLoopParams
BMC_SetPosLoopParams.restype = c_short
BMC_SetPosLoopParams.argtypes = [MOT_BrushlessPositionLoopParameters, POINTER(c_char), POINTER(c_char), c_short]
# *positionLoopParams, *serialNo, *serialNo, channel

BMC_SetPositionCounter = lib.BMC_SetPositionCounter
BMC_SetPositionCounter.restype = c_short
BMC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, channel, count

BMC_SetRotationModes = lib.BMC_SetRotationModes
BMC_SetRotationModes.restype = c_short
BMC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementDirections, MOT_MovementModes]
# *serialNo, channel, direction, mode

BMC_SetStageAxisLimits = lib.BMC_SetStageAxisLimits
BMC_SetStageAxisLimits.restype = c_short
BMC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]
# *serialNo, channel, maxPosition, minPosition

BMC_SetTrackSettleParams = lib.BMC_SetTrackSettleParams
BMC_SetTrackSettleParams.restype = c_short
BMC_SetTrackSettleParams.argtypes = [POINTER(c_char), POINTER(c_char), MOT_BrushlessTrackSettleParameters, c_short]
# *serialNo, *serialNo, *settleParams, channel

BMC_SetTriggerConfigParams = lib.BMC_SetTriggerConfigParams
BMC_SetTriggerConfigParams.restype = c_short
BMC_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]
# *serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

BMC_SetTriggerConfigParamsBlock = lib.BMC_SetTriggerConfigParamsBlock
BMC_SetTriggerConfigParamsBlock.restype = c_short
BMC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
# *serialNo, *triggerConfigParams

BMC_SetTriggerParamsParams = lib.BMC_SetTriggerParamsParams
BMC_SetTriggerParamsParams.restype = c_short
BMC_SetTriggerParamsParams.argtypes = [
    POINTER(c_char),
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]
# *serialNo, cycleCount, triggerIntervalFwd, triggerIntervalRev, triggerPulseCountFwd, triggerPulseCountRev, triggerPulseWidth, triggerStartPositionFwd, triggerStartPositionRev

BMC_SetTriggerParamsParamsBlock = lib.BMC_SetTriggerParamsParamsBlock
BMC_SetTriggerParamsParamsBlock.restype = c_short
BMC_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
# *serialNo, *triggerParamsParams

BMC_SetTriggerSwitches = lib.BMC_SetTriggerSwitches
BMC_SetTriggerSwitches.restype = c_short
BMC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]
# *serialNo, channel, indicatorBits

BMC_SetVelParams = lib.BMC_SetVelParams
BMC_SetVelParams.restype = c_short
BMC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
# *serialNo, acceleration, channel, maxVelocity

BMC_SetVelParamsBlock = lib.BMC_SetVelParamsBlock
BMC_SetVelParamsBlock.restype = c_short
BMC_SetVelParamsBlock.argtypes = [POINTER(c_char), POINTER(c_char), MOT_VelocityParameters, c_short]
# *serialNo, *serialNo, *velocityParams, channel

BMC_SetVelocityProfileParams = lib.BMC_SetVelocityProfileParams
BMC_SetVelocityProfileParams.restype = c_short
BMC_SetVelocityProfileParams.argtypes = [POINTER(c_char), POINTER(c_char), MOT_VelocityProfileParameters, c_short]
# *serialNo, *serialNo, *velocityProfileParams, channel

BMC_StartPolling = lib.BMC_StartPolling
BMC_StartPolling.restype = c_bool
BMC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, milliseconds

BMC_StopImmediate = lib.BMC_StopImmediate
BMC_StopImmediate.restype = c_short
BMC_StopImmediate.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_StopPolling = lib.BMC_StopPolling
BMC_StopPolling.restype = None
BMC_StopPolling.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_StopProfiled = lib.BMC_StopProfiled
BMC_StopProfiled.restype = c_short
BMC_StopProfiled.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_SuspendMoveMessages = lib.BMC_SuspendMoveMessages
BMC_SuspendMoveMessages.restype = c_short
BMC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

BMC_TimeSinceLastMsgReceived = lib.BMC_TimeSinceLastMsgReceived
BMC_TimeSinceLastMsgReceived.restype = c_bool
BMC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char), c_short]
# &lastUpdateTimeMS, *serialNo, channel

BMC_WaitForMessage = lib.BMC_WaitForMessage
BMC_WaitForMessage.restype = c_bool
BMC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
# *messageData, *messageID, *messageType, *serialNo, channel

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
