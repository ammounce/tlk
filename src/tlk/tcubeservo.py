from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_double,
    c_float,
    c_int,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_uint,
    c_ulong,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    MOT_ButtonModes,
    MOT_JogModes,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchSWModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_MovementDirections,
    MOT_MovementModes,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes)
from .definitions.structures import (
    MOT_ButtonParameters,
    MOT_DC_PIDParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_PotentiometerSteps,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.TCube.DCServo.DLL")
CC_CanHome = lib.CC_CanHome
CC_CanHome.restype = c_bool
CC_CanHome.argtypes = [POINTER(c_char)]
# *serialNo

CC_CanMoveWithoutHomingFirst = lib.CC_CanMoveWithoutHomingFirst
CC_CanMoveWithoutHomingFirst.restype = c_bool
CC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
# *serialNo

CC_CheckConnection = lib.CC_CheckConnection
CC_CheckConnection.restype = c_bool
CC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

CC_ClearMessageQueue = lib.CC_ClearMessageQueue
CC_ClearMessageQueue.restype = None
CC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

CC_Close = lib.CC_Close
CC_Close.restype = None
CC_Close.argtypes = [POINTER(c_char)]
# *serialNo

CC_DisableChannel = lib.CC_DisableChannel
CC_DisableChannel.restype = c_short
CC_DisableChannel.argtypes = [POINTER(c_char)]
# *serialNo

CC_EnableChannel = lib.CC_EnableChannel
CC_EnableChannel.restype = c_short
CC_EnableChannel.argtypes = [POINTER(c_char)]
# *serialNo

CC_EnableLastMsgTimer = lib.CC_EnableLastMsgTimer
CC_EnableLastMsgTimer.restype = None
CC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

CC_GetBacklash = lib.CC_GetBacklash
CC_GetBacklash.restype = c_long
CC_GetBacklash.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetButtonParams = lib.CC_GetButtonParams
CC_GetButtonParams.restype = c_short
CC_GetButtonParams.argtypes = [MOT_ButtonModes, c_int, c_int, POINTER(c_char), c_short]
# *buttonMode, *leftButtonPosition, *rightButtonPosition, *serialNo, *timeout

CC_GetButtonParamsBlock = lib.CC_GetButtonParamsBlock
CC_GetButtonParamsBlock.restype = c_short
CC_GetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
# *buttonParams, *serialNo

CC_GetDCPIDParams = lib.CC_GetDCPIDParams
CC_GetDCPIDParams.restype = c_short
CC_GetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
# *DCproportionalIntegralDerivativeParams, *serialNo

CC_GetDeviceUnitFromRealValue = lib.CC_GetDeviceUnitFromRealValue
CC_GetDeviceUnitFromRealValue.restype = c_short
CC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
# *device_unit, *serialNo, real_unit, unitType

CC_GetEncoderCounter = lib.CC_GetEncoderCounter
CC_GetEncoderCounter.restype = c_long
CC_GetEncoderCounter.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetHardwareInfo = lib.CC_GetHardwareInfo
CC_GetHardwareInfo.restype = c_short
CC_GetHardwareInfo.argtypes = [
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

CC_GetHardwareInfoBlock = lib.CC_GetHardwareInfoBlock
CC_GetHardwareInfoBlock.restype = c_short
CC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

CC_GetHomingParamsBlock = lib.CC_GetHomingParamsBlock
CC_GetHomingParamsBlock.restype = c_short
CC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
# *homingParams, *serialNo

CC_GetHomingVelocity = lib.CC_GetHomingVelocity
CC_GetHomingVelocity.restype = c_uint
CC_GetHomingVelocity.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetHubBay = lib.CC_GetHubBay
CC_GetHubBay.restype = POINTER(c_char)
CC_GetHubBay.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetJogMode = lib.CC_GetJogMode
CC_GetJogMode.restype = c_short
CC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
# *mode, *serialNo, *stopMode

CC_GetJogParamsBlock = lib.CC_GetJogParamsBlock
CC_GetJogParamsBlock.restype = c_short
CC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
# *jogParams, *serialNo

CC_GetJogStepSize = lib.CC_GetJogStepSize
CC_GetJogStepSize.restype = c_uint
CC_GetJogStepSize.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetJogVelParams = lib.CC_GetJogVelParams
CC_GetJogVelParams.restype = c_short
CC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
# *acceleration, *maxVelocity, *serialNo

CC_GetLEDswitches = lib.CC_GetLEDswitches
CC_GetLEDswitches.restype = c_long
CC_GetLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetLimitSwitchParams = lib.CC_GetLimitSwitchParams
CC_GetLimitSwitchParams.restype = c_short
CC_GetLimitSwitchParams.argtypes = [
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    POINTER(c_char),
    MOT_LimitSwitchSWModes]
# *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode

CC_GetLimitSwitchParamsBlock = lib.CC_GetLimitSwitchParamsBlock
CC_GetLimitSwitchParamsBlock.restype = c_short
CC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
# *limitSwitchParams, *serialNo

CC_GetMotorParams = lib.CC_GetMotorParams
CC_GetMotorParams.restype = c_short
CC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

CC_GetMotorParamsExt = lib.CC_GetMotorParamsExt
CC_GetMotorParamsExt.restype = c_short
CC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

CC_GetMotorTravelLimits = lib.CC_GetMotorTravelLimits
CC_GetMotorTravelLimits.restype = c_short
CC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
# *maxPosition, *minPosition, *serialNo

CC_GetMotorTravelMode = lib.CC_GetMotorTravelMode
CC_GetMotorTravelMode.restype = MOT_TravelModes
CC_GetMotorTravelMode.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetMotorVelocityLimits = lib.CC_GetMotorVelocityLimits
CC_GetMotorVelocityLimits.restype = c_short
CC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
# *maxAcceleration, *maxVelocity, *serialNo

CC_GetMoveAbsolutePosition = lib.CC_GetMoveAbsolutePosition
CC_GetMoveAbsolutePosition.restype = c_int
CC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetMoveRelativeDistance = lib.CC_GetMoveRelativeDistance
CC_GetMoveRelativeDistance.restype = c_int
CC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetNextMessage = lib.CC_GetNextMessage
CC_GetNextMessage.restype = c_bool
CC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

CC_GetNumberPositions = lib.CC_GetNumberPositions
CC_GetNumberPositions.restype = c_int
CC_GetNumberPositions.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetPosition = lib.CC_GetPosition
CC_GetPosition.restype = c_int
CC_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetPositionCounter = lib.CC_GetPositionCounter
CC_GetPositionCounter.restype = c_long
CC_GetPositionCounter.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetPotentiometerParams = lib.CC_GetPotentiometerParams
CC_GetPotentiometerParams.restype = c_short
CC_GetPotentiometerParams.argtypes = [POINTER(c_char), c_long, c_ulong, c_short]
# *serialNo, *thresholdDeflection, *velocity, index

CC_GetPotentiometerParamsBlock = lib.CC_GetPotentiometerParamsBlock
CC_GetPotentiometerParamsBlock.restype = c_short
CC_GetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
# *potentiometerSteps, *serialNo

CC_GetRealValueFromDeviceUnit = lib.CC_GetRealValueFromDeviceUnit
CC_GetRealValueFromDeviceUnit.restype = c_short
CC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
# *real_unit, *serialNo, device_unit, unitType

CC_GetSoftLimitMode = lib.CC_GetSoftLimitMode
CC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
CC_GetSoftLimitMode.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetSoftwareVersion = lib.CC_GetSoftwareVersion
CC_GetSoftwareVersion.restype = c_ulong
CC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetStageAxisMaxPos = lib.CC_GetStageAxisMaxPos
CC_GetStageAxisMaxPos.restype = c_int
CC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetStageAxisMinPos = lib.CC_GetStageAxisMinPos
CC_GetStageAxisMinPos.restype = c_int
CC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetStatusBits = lib.CC_GetStatusBits
CC_GetStatusBits.restype = c_ulong
CC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

CC_GetVelParams = lib.CC_GetVelParams
CC_GetVelParams.restype = c_short
CC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
# *acceleration, *maxVelocity, *serialNo

CC_GetVelParamsBlock = lib.CC_GetVelParamsBlock
CC_GetVelParamsBlock.restype = c_short
CC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
# *serialNo, *velocityParams

CC_HasLastMsgTimerOverrun = lib.CC_HasLastMsgTimerOverrun
CC_HasLastMsgTimerOverrun.restype = c_bool
CC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

CC_Home = lib.CC_Home
CC_Home.restype = c_short
CC_Home.argtypes = [POINTER(c_char)]
# *serialNo

CC_Identify = lib.CC_Identify
CC_Identify.restype = None
CC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

CC_LoadNamedSettings = lib.CC_LoadNamedSettings
CC_LoadNamedSettings.restype = c_bool
CC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

CC_LoadSettings = lib.CC_LoadSettings
CC_LoadSettings.restype = c_bool
CC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

CC_MessageQueueSize = lib.CC_MessageQueueSize
CC_MessageQueueSize.restype = c_int
CC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

CC_MoveAbsolute = lib.CC_MoveAbsolute
CC_MoveAbsolute.restype = c_short
CC_MoveAbsolute.argtypes = [POINTER(c_char)]
# *serialNo

CC_MoveAtVelocity = lib.CC_MoveAtVelocity
CC_MoveAtVelocity.restype = c_short
CC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, direction

CC_MoveJog = lib.CC_MoveJog
CC_MoveJog.restype = c_short
CC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, jogDirection

CC_MoveRelative = lib.CC_MoveRelative
CC_MoveRelative.restype = c_short
CC_MoveRelative.argtypes = [POINTER(c_char), c_int]
# *serialNo, displacement

CC_MoveRelativeDistance = lib.CC_MoveRelativeDistance
CC_MoveRelativeDistance.restype = c_short
CC_MoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

CC_MoveToPosition = lib.CC_MoveToPosition
CC_MoveToPosition.restype = c_short
CC_MoveToPosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, index

CC_NeedsHoming = lib.CC_NeedsHoming
CC_NeedsHoming.restype = c_bool
CC_NeedsHoming.argtypes = [POINTER(c_char)]
# *serialNo

CC_Open = lib.CC_Open
CC_Open.restype = c_short
CC_Open.argtypes = [POINTER(c_char)]
# *serialNo

CC_PersistSettings = lib.CC_PersistSettings
CC_PersistSettings.restype = c_bool
CC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

CC_PollingDuration = lib.CC_PollingDuration
CC_PollingDuration.restype = c_long
CC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

CC_RegisterMessageCallback = lib.CC_RegisterMessageCallback
CC_RegisterMessageCallback.restype = None
CC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

CC_RequestBacklash = lib.CC_RequestBacklash
CC_RequestBacklash.restype = c_short
CC_RequestBacklash.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestButtonParams = lib.CC_RequestButtonParams
CC_RequestButtonParams.restype = c_short
CC_RequestButtonParams.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestDCPIDParams = lib.CC_RequestDCPIDParams
CC_RequestDCPIDParams.restype = c_short
CC_RequestDCPIDParams.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestEncoderCounter = lib.CC_RequestEncoderCounter
CC_RequestEncoderCounter.restype = c_short
CC_RequestEncoderCounter.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestHomingParams = lib.CC_RequestHomingParams
CC_RequestHomingParams.restype = c_short
CC_RequestHomingParams.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestJogParams = lib.CC_RequestJogParams
CC_RequestJogParams.restype = c_short
CC_RequestJogParams.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestLEDswitches = lib.CC_RequestLEDswitches
CC_RequestLEDswitches.restype = c_short
CC_RequestLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestLimitSwitchParams = lib.CC_RequestLimitSwitchParams
CC_RequestLimitSwitchParams.restype = c_short
CC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestMoveAbsolutePosition = lib.CC_RequestMoveAbsolutePosition
CC_RequestMoveAbsolutePosition.restype = c_short
CC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestMoveRelativeDistance = lib.CC_RequestMoveRelativeDistance
CC_RequestMoveRelativeDistance.restype = c_short
CC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestPosition = lib.CC_RequestPosition
CC_RequestPosition.restype = c_short
CC_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestPotentiometerParams = lib.CC_RequestPotentiometerParams
CC_RequestPotentiometerParams.restype = c_short
CC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestSettings = lib.CC_RequestSettings
CC_RequestSettings.restype = c_short
CC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestStatusBits = lib.CC_RequestStatusBits
CC_RequestStatusBits.restype = c_short
CC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

CC_RequestVelParams = lib.CC_RequestVelParams
CC_RequestVelParams.restype = c_short
CC_RequestVelParams.argtypes = [POINTER(c_char)]
# *serialNo

CC_ResetRotationModes = lib.CC_ResetRotationModes
CC_ResetRotationModes.restype = c_short
CC_ResetRotationModes.argtypes = [POINTER(c_char)]
# *serialNo

CC_ResumeMoveMessages = lib.CC_ResumeMoveMessages
CC_ResumeMoveMessages.restype = c_short
CC_ResumeMoveMessages.argtypes = [POINTER(c_char)]
# *serialNo

CC_SetBacklash = lib.CC_SetBacklash
CC_SetBacklash.restype = c_short
CC_SetBacklash.argtypes = [POINTER(c_char), c_long]
# *serialNo, distance

CC_SetButtonParams = lib.CC_SetButtonParams
CC_SetButtonParams.restype = c_short
CC_SetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int]
# *serialNo, buttonMode, leftButtonPosition, rightButtonPosition

CC_SetButtonParamsBlock = lib.CC_SetButtonParamsBlock
CC_SetButtonParamsBlock.restype = c_short
CC_SetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
# *buttonParams, *serialNo

CC_SetDCPIDParams = lib.CC_SetDCPIDParams
CC_SetDCPIDParams.restype = c_short
CC_SetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
# *DCproportionalIntegralDerivativeParams, *serialNo

CC_SetDirection = lib.CC_SetDirection
CC_SetDirection.restype = None
CC_SetDirection.argtypes = [POINTER(c_char), c_bool]
# *serialNo, reverse

CC_SetEncoderCounter = lib.CC_SetEncoderCounter
CC_SetEncoderCounter.restype = c_short
CC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]
# *serialNo, count

CC_SetHomingParamsBlock = lib.CC_SetHomingParamsBlock
CC_SetHomingParamsBlock.restype = c_short
CC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
# *homingParams, *serialNo

CC_SetHomingVelocity = lib.CC_SetHomingVelocity
CC_SetHomingVelocity.restype = c_short
CC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
# *serialNo, velocity

CC_SetJogMode = lib.CC_SetJogMode
CC_SetJogMode.restype = c_short
CC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
# *serialNo, mode, stopMode

CC_SetJogParamsBlock = lib.CC_SetJogParamsBlock
CC_SetJogParamsBlock.restype = c_short
CC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
# *jogParams, *serialNo

CC_SetJogStepSize = lib.CC_SetJogStepSize
CC_SetJogStepSize.restype = c_short
CC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
# *serialNo, stepSize

CC_SetJogVelParams = lib.CC_SetJogVelParams
CC_SetJogVelParams.restype = c_short
CC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, acceleration, maxVelocity

CC_SetLEDswitches = lib.CC_SetLEDswitches
CC_SetLEDswitches.restype = c_short
CC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
# *serialNo, LEDswitches

CC_SetLimitSwitchParams = lib.CC_SetLimitSwitchParams
CC_SetLimitSwitchParams.restype = c_short
CC_SetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchSWModes]
# *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, clockwiseHardwareLimit, clockwisePosition, softLimitMode

CC_SetLimitSwitchParamsBlock = lib.CC_SetLimitSwitchParamsBlock
CC_SetLimitSwitchParamsBlock.restype = c_short
CC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
# *limitSwitchParams, *serialNo

CC_SetLimitsSoftwareApproachPolicy = lib.CC_SetLimitsSoftwareApproachPolicy
CC_SetLimitsSoftwareApproachPolicy.restype = None
CC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
# *serialNo, limitsSoftwareApproachPolicy

CC_SetMotorParams = lib.CC_SetMotorParams
CC_SetMotorParams.restype = c_short
CC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
# *serialNo, gearBoxRatio, pitch, stepsPerRev

CC_SetMotorParamsExt = lib.CC_SetMotorParamsExt
CC_SetMotorParamsExt.restype = c_short
CC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
# *serialNo, gearBoxRatio, pitch, stepsPerRev

CC_SetMotorTravelLimits = lib.CC_SetMotorTravelLimits
CC_SetMotorTravelLimits.restype = c_short
CC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
# *serialNo, maxPosition, minPosition

CC_SetMotorTravelMode = lib.CC_SetMotorTravelMode
CC_SetMotorTravelMode.restype = c_short
CC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
# *serialNo, travelMode

CC_SetMotorVelocityLimits = lib.CC_SetMotorVelocityLimits
CC_SetMotorVelocityLimits.restype = c_short
CC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
# *serialNo, maxAcceleration, maxVelocity

CC_SetMoveAbsolutePosition = lib.CC_SetMoveAbsolutePosition
CC_SetMoveAbsolutePosition.restype = c_short
CC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, position

CC_SetMoveRelativeDistance = lib.CC_SetMoveRelativeDistance
CC_SetMoveRelativeDistance.restype = c_short
CC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
# *serialNo, distance

CC_SetPositionCounter = lib.CC_SetPositionCounter
CC_SetPositionCounter.restype = c_short
CC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
# *serialNo, count

CC_SetPotentiometerParams = lib.CC_SetPotentiometerParams
CC_SetPotentiometerParams.restype = c_short
CC_SetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]
# *serialNo, index, thresholdDeflection, velocity

CC_SetPotentiometerParamsBlock = lib.CC_SetPotentiometerParamsBlock
CC_SetPotentiometerParamsBlock.restype = c_short
CC_SetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
# *potentiometerSteps, *serialNo

CC_SetRotationModes = lib.CC_SetRotationModes
CC_SetRotationModes.restype = c_short
CC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementDirections, MOT_MovementModes]
# *serialNo, direction, mode

CC_SetStageAxisLimits = lib.CC_SetStageAxisLimits
CC_SetStageAxisLimits.restype = c_short
CC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, maxPosition, minPosition

CC_SetVelParams = lib.CC_SetVelParams
CC_SetVelParams.restype = c_short
CC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, acceleration, maxVelocity

CC_SetVelParamsBlock = lib.CC_SetVelParamsBlock
CC_SetVelParamsBlock.restype = c_short
CC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
# *serialNo, *velocityParams

CC_StartPolling = lib.CC_StartPolling
CC_StartPolling.restype = c_bool
CC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

CC_StopImmediate = lib.CC_StopImmediate
CC_StopImmediate.restype = c_short
CC_StopImmediate.argtypes = [POINTER(c_char)]
# *serialNo

CC_StopPolling = lib.CC_StopPolling
CC_StopPolling.restype = None
CC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

CC_StopProfiled = lib.CC_StopProfiled
CC_StopProfiled.restype = c_short
CC_StopProfiled.argtypes = [POINTER(c_char)]
# *serialNo

CC_SuspendMoveMessages = lib.CC_SuspendMoveMessages
CC_SuspendMoveMessages.restype = c_short
CC_SuspendMoveMessages.argtypes = [POINTER(c_char)]
# *serialNo

CC_TimeSinceLastMsgReceived = lib.CC_TimeSinceLastMsgReceived
CC_TimeSinceLastMsgReceived.restype = c_bool
CC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

CC_WaitForMessage = lib.CC_WaitForMessage
CC_WaitForMessage.restype = c_bool
CC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
