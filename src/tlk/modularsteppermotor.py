from ctypes import (POINTER, c_bool, c_byte, c_char, c_double, c_float, c_int, c_int32, c_long, c_short, c_uint, cdll)
from .definitions.enumerations import (
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
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_JoystickParameters,
    MOT_LimitSwitchParameters,
    MOT_PowerParameters,
    MOT_VelocityParameters)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.Modular.DLL")
SBC_CanHome = lib.SBC_CanHome
SBC_CanHome.restype = c_bool
SBC_CanHome.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_CanMoveWithoutHomingFirst = lib.SBC_CanMoveWithoutHomingFirst
SBC_CanMoveWithoutHomingFirst.restype = c_bool
SBC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_DisableChannel = lib.SBC_DisableChannel
SBC_DisableChannel.restype = c_short
SBC_DisableChannel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_EnableChannel = lib.SBC_EnableChannel
SBC_EnableChannel.restype = c_short
SBC_EnableChannel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_EnableLastMsgTimer = lib.SBC_EnableLastMsgTimer
SBC_EnableLastMsgTimer.restype = None
SBC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]
# *serialNo, channel, enable, lastMsgTimeout

SBC_GetBacklash = lib.SBC_GetBacklash
SBC_GetBacklash.restype = c_long
SBC_GetBacklash.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetBowIndex = lib.SBC_GetBowIndex
SBC_GetBowIndex.restype = c_short
SBC_GetBowIndex.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetCalibrationFile = lib.SBC_GetCalibrationFile
SBC_GetCalibrationFile.restype = c_bool
SBC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short, c_short]
# *filename, *serialNo, channel, sizeOfBuffer

SBC_GetDeviceUnitFromRealValue = lib.SBC_GetDeviceUnitFromRealValue
SBC_GetDeviceUnitFromRealValue.restype = c_short
SBC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_short, c_double, c_int]
# *device_unit, *serialNo, channel, real_unit, unitType

SBC_GetDigitalOutputs = lib.SBC_GetDigitalOutputs
SBC_GetDigitalOutputs.restype = c_byte
SBC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetEncoderCounter = lib.SBC_GetEncoderCounter
SBC_GetEncoderCounter.restype = c_long
SBC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetHomingParamsBlock = lib.SBC_GetHomingParamsBlock
SBC_GetHomingParamsBlock.restype = c_short
SBC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), c_short]
# *homingParams, *serialNo, channel

SBC_GetHomingVelocity = lib.SBC_GetHomingVelocity
SBC_GetHomingVelocity.restype = c_uint
SBC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetInputVoltage = lib.SBC_GetInputVoltage
SBC_GetInputVoltage.restype = c_long
SBC_GetInputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetJogMode = lib.SBC_GetJogMode
SBC_GetJogMode.restype = c_short
SBC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes, c_short]
# *mode, *serialNo, *stopMode, channel

SBC_GetJogParamsBlock = lib.SBC_GetJogParamsBlock
SBC_GetJogParamsBlock.restype = c_short
SBC_GetJogParamsBlock.argtypes = [MOT_JogParameters, MOT_JogParameters, POINTER(c_char), c_short]
# *jogParameters, *jogParams, *serialNo, channel

SBC_GetJogStepSize = lib.SBC_GetJogStepSize
SBC_GetJogStepSize.restype = c_uint
SBC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetJogVelParams = lib.SBC_GetJogVelParams
SBC_GetJogVelParams.restype = c_short
SBC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
# *acceleration, *maxVelocity, *serialNo, channel

SBC_GetJoystickParams = lib.SBC_GetJoystickParams
SBC_GetJoystickParams.restype = c_short
SBC_GetJoystickParams.argtypes = [MOT_JoystickParameters, POINTER(c_char), c_short]
# *joystickParams, *serialNo, channel

SBC_GetLimitSwitchParams = lib.SBC_GetLimitSwitchParams
SBC_GetLimitSwitchParams.restype = c_short
SBC_GetLimitSwitchParams.argtypes = [
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    POINTER(c_char),
    MOT_LimitSwitchSWModes,
    c_short]
# *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode, channel

SBC_GetLimitSwitchParamsBlock = lib.SBC_GetLimitSwitchParamsBlock
SBC_GetLimitSwitchParamsBlock.restype = c_short
SBC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char), c_short]
# *limitSwitchParams, *serialNo, channel

SBC_GetMotorParams = lib.SBC_GetMotorParams
SBC_GetMotorParams.restype = c_short
SBC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long, c_short]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev, channel

SBC_GetMotorParamsExt = lib.SBC_GetMotorParamsExt
SBC_GetMotorParamsExt.restype = c_short
SBC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double, c_short]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev, channel

SBC_GetMotorTravelLimits = lib.SBC_GetMotorTravelLimits
SBC_GetMotorTravelLimits.restype = c_short
SBC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
# *maxPosition, *minPosition, *serialNo, channel

SBC_GetMotorTravelMode = lib.SBC_GetMotorTravelMode
SBC_GetMotorTravelMode.restype = MOT_TravelModes
SBC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetMotorVelocityLimits = lib.SBC_GetMotorVelocityLimits
SBC_GetMotorVelocityLimits.restype = c_short
SBC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
# *maxAcceleration, *maxVelocity, *serialNo, channel

SBC_GetMoveAbsolutePosition = lib.SBC_GetMoveAbsolutePosition
SBC_GetMoveAbsolutePosition.restype = c_int
SBC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetMoveRelativeDistance = lib.SBC_GetMoveRelativeDistance
SBC_GetMoveRelativeDistance.restype = c_int
SBC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetNumberPositions = lib.SBC_GetNumberPositions
SBC_GetNumberPositions.restype = c_int
SBC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetPosition = lib.SBC_GetPosition
SBC_GetPosition.restype = c_int
SBC_GetPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetPositionCounter = lib.SBC_GetPositionCounter
SBC_GetPositionCounter.restype = c_long
SBC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetPowerParams = lib.SBC_GetPowerParams
SBC_GetPowerParams.restype = c_short
SBC_GetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char), c_short]
# *powerParams, *serialNo, channel

SBC_GetRealValueFromDeviceUnit = lib.SBC_GetRealValueFromDeviceUnit
SBC_GetRealValueFromDeviceUnit.restype = c_short
SBC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_short, c_int, c_int]
# *real_unit, *serialNo, channel, device_unit, unitType

SBC_GetSoftLimitMode = lib.SBC_GetSoftLimitMode
SBC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
SBC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetStageAxisMaxPos = lib.SBC_GetStageAxisMaxPos
SBC_GetStageAxisMaxPos.restype = c_int
SBC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetStageAxisMinPos = lib.SBC_GetStageAxisMinPos
SBC_GetStageAxisMinPos.restype = c_int
SBC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetStatusBits = lib.SBC_GetStatusBits
SBC_GetStatusBits.restype = c_ulong
SBC_GetStatusBits.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetTriggerSwitches = lib.SBC_GetTriggerSwitches
SBC_GetTriggerSwitches.restype = c_byte
SBC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetVelParams = lib.SBC_GetVelParams
SBC_GetVelParams.restype = c_short
SBC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
# *acceleration, *maxVelocity, *serialNo, channel

SBC_GetVelParamsBlock = lib.SBC_GetVelParamsBlock
SBC_GetVelParamsBlock.restype = c_short
SBC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters, MOT_VelocityParameters, c_short]
# *serialNo, *velocityParameters, *velocityParams, channel

SBC_HasLastMsgTimerOverrun = lib.SBC_HasLastMsgTimerOverrun
SBC_HasLastMsgTimerOverrun.restype = c_bool
SBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_Home = lib.SBC_Home
SBC_Home.restype = c_short
SBC_Home.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_IsCalibrationActive = lib.SBC_IsCalibrationActive
SBC_IsCalibrationActive.restype = c_bool
SBC_IsCalibrationActive.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_MoveAbsolute = lib.SBC_MoveAbsolute
SBC_MoveAbsolute.restype = c_short
SBC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_MoveAtVelocity = lib.SBC_MoveAtVelocity
SBC_MoveAtVelocity.restype = c_short
SBC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
# *serialNo, channel, direction

SBC_MoveJog = lib.SBC_MoveJog
SBC_MoveJog.restype = c_short
SBC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
# *serialNo, channel, jogDirection

SBC_MoveRelative = lib.SBC_MoveRelative
SBC_MoveRelative.restype = c_short
SBC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, displacement

SBC_MoveRelativeDistance = lib.SBC_MoveRelativeDistance
SBC_MoveRelativeDistance.restype = c_short
SBC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_MoveToPosition = lib.SBC_MoveToPosition
SBC_MoveToPosition.restype = c_short
SBC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, index

SBC_NeedsHoming = lib.SBC_NeedsHoming
SBC_NeedsHoming.restype = c_bool
SBC_NeedsHoming.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_PollingDuration = lib.SBC_PollingDuration
SBC_PollingDuration.restype = c_long
SBC_PollingDuration.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestDigitalOutputs = lib.SBC_RequestDigitalOutputs
SBC_RequestDigitalOutputs.restype = c_short
SBC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestInputVoltage = lib.SBC_RequestInputVoltage
SBC_RequestInputVoltage.restype = c_short
SBC_RequestInputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestPosition = lib.SBC_RequestPosition
SBC_RequestPosition.restype = c_short
SBC_RequestPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestSettings = lib.SBC_RequestSettings
SBC_RequestSettings.restype = c_short
SBC_RequestSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestStatusBits = lib.SBC_RequestStatusBits
SBC_RequestStatusBits.restype = c_short
SBC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_ResetRotationModes = lib.SBC_ResetRotationModes
SBC_ResetRotationModes.restype = c_short
SBC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_ResumeMoveMessages = lib.SBC_ResumeMoveMessages
SBC_ResumeMoveMessages.restype = c_short
SBC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_SetBacklash = lib.SBC_SetBacklash
SBC_SetBacklash.restype = c_short
SBC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, channel, distance

SBC_SetBowIndex = lib.SBC_SetBowIndex
SBC_SetBowIndex.restype = c_short
SBC_SetBowIndex.argtypes = [POINTER(c_char), c_short, c_short]
# *serialNo, bowIndex, channel

SBC_SetCalibrationFile = lib.SBC_SetCalibrationFile
SBC_SetCalibrationFile.restype = None
SBC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short, c_bool]
# *filename, *serialNo, channel, enabled

SBC_SetDigitalOutputs = lib.SBC_SetDigitalOutputs
SBC_SetDigitalOutputs.restype = c_short
SBC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]
# *serialNo, channel, outputsBits

SBC_SetDirection = lib.SBC_SetDirection
SBC_SetDirection.restype = c_short
SBC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]
# *serialNo, channel, reverse

SBC_SetEncoderCounter = lib.SBC_SetEncoderCounter
SBC_SetEncoderCounter.restype = c_short
SBC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, channel, count

SBC_SetHomingParamsBlock = lib.SBC_SetHomingParamsBlock
SBC_SetHomingParamsBlock.restype = c_short
SBC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), c_short]
# *homingParams, *serialNo, channel

SBC_SetHomingVelocity = lib.SBC_SetHomingVelocity
SBC_SetHomingVelocity.restype = c_short
SBC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]
# *serialNo, channel, velocity

SBC_SetJogMode = lib.SBC_SetJogMode
SBC_SetJogMode.restype = c_short
SBC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]
# *serialNo, channel, mode, stopMode

SBC_SetJogParamsBlock = lib.SBC_SetJogParamsBlock
SBC_SetJogParamsBlock.restype = c_short
SBC_SetJogParamsBlock.argtypes = [MOT_JogParameters, MOT_JogParameters, POINTER(c_char), c_short]
# *jogParameters, *jogParams, *serialNo, channel

SBC_SetJogStepSize = lib.SBC_SetJogStepSize
SBC_SetJogStepSize.restype = c_short
SBC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]
# *serialNo, channel, stepSize

SBC_SetJogVelParams = lib.SBC_SetJogVelParams
SBC_SetJogVelParams.restype = c_short
SBC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
# *serialNo, acceleration, channel, maxVelocity

SBC_SetJoystickParams = lib.SBC_SetJoystickParams
SBC_SetJoystickParams.restype = c_short
SBC_SetJoystickParams.argtypes = [MOT_JoystickParameters, POINTER(c_char), c_short]
# *joystickParams, *serialNo, channel

SBC_SetLimitSwitchParams = lib.SBC_SetLimitSwitchParams
SBC_SetLimitSwitchParams.restype = c_short
SBC_SetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    MOT_LimitSwitchModes,
    c_uint,
    c_short,
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchSWModes]
# *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, channel, clockwiseHardwareLimit, clockwisePosition, softLimitMode

SBC_SetLimitSwitchParamsBlock = lib.SBC_SetLimitSwitchParamsBlock
SBC_SetLimitSwitchParamsBlock.restype = c_short
SBC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char), c_short]
# *limitSwitchParams, *serialNo, channel

SBC_SetLimitsSoftwareApproachPolicy = lib.SBC_SetLimitsSoftwareApproachPolicy
SBC_SetLimitsSoftwareApproachPolicy.restype = None
SBC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]
# *serialNo, channel, limitsSoftwareApproachPolicy

SBC_SetMotorParams = lib.SBC_SetMotorParams
SBC_SetMotorParams.restype = c_short
SBC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_float, c_long]
# *serialNo, channel, gearBoxRatio, pitch, stepsPerRev

SBC_SetMotorParamsExt = lib.SBC_SetMotorParamsExt
SBC_SetMotorParamsExt.restype = c_short
SBC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]
# *serialNo, channel, gearBoxRatio, pitch, stepsPerRev

SBC_SetMotorTravelLimits = lib.SBC_SetMotorTravelLimits
SBC_SetMotorTravelLimits.restype = c_short
SBC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
# *serialNo, channel, maxPosition, minPosition

SBC_SetMotorTravelMode = lib.SBC_SetMotorTravelMode
SBC_SetMotorTravelMode.restype = c_short
SBC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]
# *serialNo, channel, travelMode

SBC_SetMotorVelocityLimits = lib.SBC_SetMotorVelocityLimits
SBC_SetMotorVelocityLimits.restype = c_short
SBC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
# *serialNo, channel, maxAcceleration, maxVelocity

SBC_SetMoveAbsolutePosition = lib.SBC_SetMoveAbsolutePosition
SBC_SetMoveAbsolutePosition.restype = c_short
SBC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, position

SBC_SetMoveRelativeDistance = lib.SBC_SetMoveRelativeDistance
SBC_SetMoveRelativeDistance.restype = c_short
SBC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, distance

SBC_SetPositionCounter = lib.SBC_SetPositionCounter
SBC_SetPositionCounter.restype = c_short
SBC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, channel, count

SBC_SetPowerParams = lib.SBC_SetPowerParams
SBC_SetPowerParams.restype = c_short
SBC_SetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char), c_short]
# *powerParams, *serialNo, channel

SBC_SetRotationModes = lib.SBC_SetRotationModes
SBC_SetRotationModes.restype = c_short
SBC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementDirections, MOT_MovementModes]
# *serialNo, channel, direction, mode

SBC_SetStageAxisLimits = lib.SBC_SetStageAxisLimits
SBC_SetStageAxisLimits.restype = c_short
SBC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]
# *serialNo, channel, maxPosition, minPosition

SBC_SetTriggerSwitches = lib.SBC_SetTriggerSwitches
SBC_SetTriggerSwitches.restype = c_short
SBC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]
# *serialNo, channel, indicatorBits

SBC_SetVelParams = lib.SBC_SetVelParams
SBC_SetVelParams.restype = c_short
SBC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
# *serialNo, acceleration, channel, maxVelocity

SBC_SetVelParamsBlock = lib.SBC_SetVelParamsBlock
SBC_SetVelParamsBlock.restype = c_short
SBC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters, MOT_VelocityParameters, c_short]
# *serialNo, *velocityParameters, *velocityParams, channel

SBC_StartPolling = lib.SBC_StartPolling
SBC_StartPolling.restype = c_bool
SBC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, milliseconds

SBC_StopImmediate = lib.SBC_StopImmediate
SBC_StopImmediate.restype = c_short
SBC_StopImmediate.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_StopPolling = lib.SBC_StopPolling
SBC_StopPolling.restype = None
SBC_StopPolling.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_StopProfiled = lib.SBC_StopProfiled
SBC_StopProfiled.restype = c_short
SBC_StopProfiled.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_SuspendMoveMessages = lib.SBC_SuspendMoveMessages
SBC_SuspendMoveMessages.restype = c_short
SBC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel
