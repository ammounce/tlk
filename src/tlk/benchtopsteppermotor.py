from ctypes import (
    POINTER,
    c_bool,
    c_byte,
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
    c_void_p,
    cdll)
from .definitions.safearray import SafeArray
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
    MOT_PIDLoopEncoderParams,
    MOT_PowerParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Benchtop.StepperMotor.dll")

SBC_CanHome = lib.SBC_CanHome
SBC_CanHome.restype = c_bool
SBC_CanHome.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_CanMoveWithoutHomingFirst = lib.SBC_CanMoveWithoutHomingFirst
SBC_CanMoveWithoutHomingFirst.restype = c_bool
SBC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_CheckConnection = lib.SBC_CheckConnection
SBC_CheckConnection.restype = c_bool
SBC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

SBC_ClearMessageQueue = lib.SBC_ClearMessageQueue
SBC_ClearMessageQueue.restype = c_short
SBC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_Close = lib.SBC_Close
SBC_Close.restype = c_short
SBC_Close.argtypes = [POINTER(c_char)]
# *serialNo

SBC_DisableChannel = lib.SBC_DisableChannel
SBC_DisableChannel.restype = c_short
SBC_DisableChannel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_EnableChannel = lib.SBC_EnableChannel
SBC_EnableChannel.restype = c_short
SBC_EnableChannel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_EnableLastMsgTimer = lib.SBC_EnableLastMsgTimer
SBC_EnableLastMsgTimer.restype = c_void_p
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
SBC_GetCalibrationFile.argtypes = [POINTER(c_char), c_short, POINTER(c_char), c_short]
# *serialNo, channel, *filename, sizeOfBuffer

SBC_GetDeviceUnitFromRealValue = lib.SBC_GetDeviceUnitFromRealValue
SBC_GetDeviceUnitFromRealValue.restype = c_short
SBC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_short, c_double, c_int, c_int]
# *serialNo, channel, real_unit, *device_unit, unitType

SBC_GetDigitalOutputs = lib.SBC_GetDigitalOutputs
SBC_GetDigitalOutputs.restype = c_byte
SBC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetEncoderCounter = lib.SBC_GetEncoderCounter
SBC_GetEncoderCounter.restype = c_long
SBC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetFirmwareVersion = lib.SBC_GetFirmwareVersion
SBC_GetFirmwareVersion.restype = c_ulong
SBC_GetFirmwareVersion.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetHardwareInfo = lib.SBC_GetHardwareInfo
SBC_GetHardwareInfo.restype = c_short
SBC_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    c_short,
    POINTER(c_char),
    c_ulong,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]
# *serialNo, channel, *modelNo, sizeOfModelNo, *type, *numChannels, *notes, sizeOfNotes, *firmwareVersion, *hardwareVersion, *modificationState

SBC_GetHardwareInfoBlock = lib.SBC_GetHardwareInfoBlock
SBC_GetHardwareInfoBlock.restype = c_short
SBC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), c_short, TLI_HardwareInformation]
# *serialNo, channel, *hardwareInfo

SBC_GetHomingParamsBlock = lib.SBC_GetHomingParamsBlock
SBC_GetHomingParamsBlock.restype = c_short
SBC_GetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]
# *serialNo, channel, *homingParams

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
SBC_GetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]
# *serialNo, channel, *mode, *stopMode

SBC_GetJogParamsBlock = lib.SBC_GetJogParamsBlock
SBC_GetJogParamsBlock.restype = c_short
SBC_GetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters, MOT_JogParameters]
# *serialNo, channel, *jogParams, *jogParameters

SBC_GetJogStepSize = lib.SBC_GetJogStepSize
SBC_GetJogStepSize.restype = c_uint
SBC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetJogVelParams = lib.SBC_GetJogVelParams
SBC_GetJogVelParams.restype = c_short
SBC_GetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]
# *serialNo, channel, *acceleration, *maxVelocity

SBC_GetJoystickParams = lib.SBC_GetJoystickParams
SBC_GetJoystickParams.restype = c_short
SBC_GetJoystickParams.argtypes = [POINTER(c_char), c_short, MOT_JoystickParameters]
# *serialNo, channel, *joystickParams

SBC_GetLimitSwitchParams = lib.SBC_GetLimitSwitchParams
SBC_GetLimitSwitchParams.restype = c_short
SBC_GetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    c_short,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchModes,
    c_uint,
    c_uint,
    MOT_LimitSwitchSWModes]
# *serialNo, channel, *clockwiseHardwareLimit, *anticlockwiseHardwareLimit, *clockwisePosition, *anticlockwisePosition, *softLimitMode

SBC_GetLimitSwitchParamsBlock = lib.SBC_GetLimitSwitchParamsBlock
SBC_GetLimitSwitchParamsBlock.restype = c_short
SBC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_LimitSwitchParameters]
# *serialNo, channel, *limitSwitchParams

SBC_GetMotorParams = lib.SBC_GetMotorParams
SBC_GetMotorParams.restype = c_short
SBC_GetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_float]
# *serialNo, channel, *stepsPerRev, *gearBoxRatio, *pitch

SBC_GetMotorParamsExt = lib.SBC_GetMotorParamsExt
SBC_GetMotorParamsExt.restype = c_short
SBC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]
# *serialNo, channel, *stepsPerRev, *gearBoxRatio, *pitch

SBC_GetMotorTravelLimits = lib.SBC_GetMotorTravelLimits
SBC_GetMotorTravelLimits.restype = c_short
SBC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
# *serialNo, channel, *minPosition, *maxPosition

SBC_GetMotorTravelMode = lib.SBC_GetMotorTravelMode
SBC_GetMotorTravelMode.restype = MOT_TravelModes
SBC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetMotorVelocityLimits = lib.SBC_GetMotorVelocityLimits
SBC_GetMotorVelocityLimits.restype = c_short
SBC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
# *serialNo, channel, *maxVelocity, *maxAcceleration

SBC_GetMoveAbsolutePosition = lib.SBC_GetMoveAbsolutePosition
SBC_GetMoveAbsolutePosition.restype = c_int
SBC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetMoveRelativeDistance = lib.SBC_GetMoveRelativeDistance
SBC_GetMoveRelativeDistance.restype = c_int
SBC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetNextMessage = lib.SBC_GetNextMessage
SBC_GetNextMessage.restype = c_bool
SBC_GetNextMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]
# *serialNo, channel, *messageType, *messageID, *messageData

SBC_GetNumChannels = lib.SBC_GetNumChannels
SBC_GetNumChannels.restype = c_short
SBC_GetNumChannels.argtypes = [POINTER(c_char)]
# *serialNo

SBC_GetNumberPositions = lib.SBC_GetNumberPositions
SBC_GetNumberPositions.restype = c_int
SBC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetPIDLoopEncoderCoeff = lib.SBC_GetPIDLoopEncoderCoeff
SBC_GetPIDLoopEncoderCoeff.restype = c_double
SBC_GetPIDLoopEncoderCoeff.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetPIDLoopEncoderParams = lib.SBC_GetPIDLoopEncoderParams
SBC_GetPIDLoopEncoderParams.restype = c_short
SBC_GetPIDLoopEncoderParams.argtypes = [POINTER(c_char), c_short, MOT_PIDLoopEncoderParams]
# *serialNo, channel, *params

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
SBC_GetPowerParams.argtypes = [POINTER(c_char), c_short, MOT_PowerParameters]
# *serialNo, channel, *powerParams

SBC_GetRackDigitalOutputs = lib.SBC_GetRackDigitalOutputs
SBC_GetRackDigitalOutputs.restype = c_byte
SBC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

SBC_GetRackStatusBits = lib.SBC_GetRackStatusBits
SBC_GetRackStatusBits.restype = c_ulong
SBC_GetRackStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

SBC_GetRealValueFromDeviceUnit = lib.SBC_GetRealValueFromDeviceUnit
SBC_GetRealValueFromDeviceUnit.restype = c_short
SBC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_short, c_int, c_double, c_int]
# *serialNo, channel, device_unit, *real_unit, unitType

SBC_GetSoftLimitMode = lib.SBC_GetSoftLimitMode
SBC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
SBC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_GetSoftwareVersion = lib.SBC_GetSoftwareVersion
SBC_GetSoftwareVersion.restype = c_ulong
SBC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

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
SBC_GetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]
# *serialNo, channel, *acceleration, *maxVelocity

SBC_GetVelParamsBlock = lib.SBC_GetVelParamsBlock
SBC_GetVelParamsBlock.restype = c_short
SBC_GetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters, MOT_VelocityParameters]
# *serialNo, channel, *velocityParams, *velocityParameters

SBC_HasLastMsgTimerOverrun = lib.SBC_HasLastMsgTimerOverrun
SBC_HasLastMsgTimerOverrun.restype = c_bool
SBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_Home = lib.SBC_Home
SBC_Home.restype = c_short
SBC_Home.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_Identify = lib.SBC_Identify
SBC_Identify.restype = c_void_p
SBC_Identify.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_IsCalibrationActive = lib.SBC_IsCalibrationActive
SBC_IsCalibrationActive.restype = c_bool
SBC_IsCalibrationActive.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_IsChannelValid = lib.SBC_IsChannelValid
SBC_IsChannelValid.restype = c_bool
SBC_IsChannelValid.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_LoadNamedSettings = lib.SBC_LoadNamedSettings
SBC_LoadNamedSettings.restype = c_bool
SBC_LoadNamedSettings.argtypes = [POINTER(c_char), c_short, POINTER(c_char)]
# *serialNo, channel, *settingsName

SBC_LoadSettings = lib.SBC_LoadSettings
SBC_LoadSettings.restype = c_bool
SBC_LoadSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_MaxChannelCount = lib.SBC_MaxChannelCount
SBC_MaxChannelCount.restype = c_int
SBC_MaxChannelCount.argtypes = [POINTER(c_char)]
# *serialNo

SBC_MessageQueueSize = lib.SBC_MessageQueueSize
SBC_MessageQueueSize.restype = c_int
SBC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]
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

SBC_Open = lib.SBC_Open
SBC_Open.restype = c_short
SBC_Open.argtypes = [POINTER(c_char)]
# *serialNo

SBC_PersistSettings = lib.SBC_PersistSettings
SBC_PersistSettings.restype = c_bool
SBC_PersistSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_PollingDuration = lib.SBC_PollingDuration
SBC_PollingDuration.restype = c_long
SBC_PollingDuration.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RegisterMessageCallback = lib.SBC_RegisterMessageCallback
SBC_RegisterMessageCallback.restype = c_short
SBC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, c_void_p]
# *serialNo, channel, void

SBC_RequestBacklash = lib.SBC_RequestBacklash
SBC_RequestBacklash.restype = c_short
SBC_RequestBacklash.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestBowIndex = lib.SBC_RequestBowIndex
SBC_RequestBowIndex.restype = c_short
SBC_RequestBowIndex.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestDigitalOutputs = lib.SBC_RequestDigitalOutputs
SBC_RequestDigitalOutputs.restype = c_short
SBC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestEncoderCounter = lib.SBC_RequestEncoderCounter
SBC_RequestEncoderCounter.restype = c_short
SBC_RequestEncoderCounter.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestHomingParams = lib.SBC_RequestHomingParams
SBC_RequestHomingParams.restype = c_short
SBC_RequestHomingParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestInputVoltage = lib.SBC_RequestInputVoltage
SBC_RequestInputVoltage.restype = c_short
SBC_RequestInputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestJogParams = lib.SBC_RequestJogParams
SBC_RequestJogParams.restype = c_short
SBC_RequestJogParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestJoystickParams = lib.SBC_RequestJoystickParams
SBC_RequestJoystickParams.restype = c_short
SBC_RequestJoystickParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestLimitSwitchParams = lib.SBC_RequestLimitSwitchParams
SBC_RequestLimitSwitchParams.restype = c_short
SBC_RequestLimitSwitchParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestMoveAbsolutePosition = lib.SBC_RequestMoveAbsolutePosition
SBC_RequestMoveAbsolutePosition.restype = c_short
SBC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestMoveRelativeDistance = lib.SBC_RequestMoveRelativeDistance
SBC_RequestMoveRelativeDistance.restype = c_short
SBC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestPIDLoopEncoderParams = lib.SBC_RequestPIDLoopEncoderParams
SBC_RequestPIDLoopEncoderParams.restype = c_short
SBC_RequestPIDLoopEncoderParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestPosition = lib.SBC_RequestPosition
SBC_RequestPosition.restype = c_short
SBC_RequestPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestPowerParams = lib.SBC_RequestPowerParams
SBC_RequestPowerParams.restype = c_short
SBC_RequestPowerParams.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestRackDigitalOutputs = lib.SBC_RequestRackDigitalOutputs
SBC_RequestRackDigitalOutputs.restype = c_short
SBC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

SBC_RequestRackStatusBits = lib.SBC_RequestRackStatusBits
SBC_RequestRackStatusBits.restype = c_short
SBC_RequestRackStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

SBC_RequestSettings = lib.SBC_RequestSettings
SBC_RequestSettings.restype = c_short
SBC_RequestSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestStatusBits = lib.SBC_RequestStatusBits
SBC_RequestStatusBits.restype = c_short
SBC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestTriggerSwitches = lib.SBC_RequestTriggerSwitches
SBC_RequestTriggerSwitches.restype = c_short
SBC_RequestTriggerSwitches.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_RequestVelParams = lib.SBC_RequestVelParams
SBC_RequestVelParams.restype = c_short
SBC_RequestVelParams.argtypes = [POINTER(c_char), c_short]
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
# *serialNo, channel, bowIndex

SBC_SetCalibrationFile = lib.SBC_SetCalibrationFile
SBC_SetCalibrationFile.restype = c_void_p
SBC_SetCalibrationFile.argtypes = [POINTER(c_char), c_short, POINTER(c_char), c_bool]
# *serialNo, channel, *filename, enabled

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
SBC_SetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]
# *serialNo, channel, *homingParams

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
SBC_SetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters, MOT_JogParameters]
# *serialNo, channel, *jogParams, *jogParameters

SBC_SetJogStepSize = lib.SBC_SetJogStepSize
SBC_SetJogStepSize.restype = c_short
SBC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]
# *serialNo, channel, stepSize

SBC_SetJogVelParams = lib.SBC_SetJogVelParams
SBC_SetJogVelParams.restype = c_short
SBC_SetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]
# *serialNo, channel, acceleration, maxVelocity

SBC_SetJoystickParams = lib.SBC_SetJoystickParams
SBC_SetJoystickParams.restype = c_short
SBC_SetJoystickParams.argtypes = [POINTER(c_char), c_short, MOT_JoystickParameters]
# *serialNo, channel, *joystickParams

SBC_SetLimitSwitchParams = lib.SBC_SetLimitSwitchParams
SBC_SetLimitSwitchParams.restype = c_short
SBC_SetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    c_short,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchModes,
    c_uint,
    c_uint,
    MOT_LimitSwitchSWModes]
# *serialNo, channel, clockwiseHardwareLimit, anticlockwiseHardwareLimit, clockwisePosition, anticlockwisePosition, softLimitMode

SBC_SetLimitSwitchParamsBlock = lib.SBC_SetLimitSwitchParamsBlock
SBC_SetLimitSwitchParamsBlock.restype = c_short
SBC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_LimitSwitchParameters]
# *serialNo, channel, *limitSwitchParams

SBC_SetLimitsSoftwareApproachPolicy = lib.SBC_SetLimitsSoftwareApproachPolicy
SBC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
SBC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]
# *serialNo, channel, limitsSoftwareApproachPolicy

SBC_SetMotorParams = lib.SBC_SetMotorParams
SBC_SetMotorParams.restype = c_short
SBC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_float]
# *serialNo, channel, stepsPerRev, gearBoxRatio, pitch

SBC_SetMotorParamsExt = lib.SBC_SetMotorParamsExt
SBC_SetMotorParamsExt.restype = c_short
SBC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]
# *serialNo, channel, stepsPerRev, gearBoxRatio, pitch

SBC_SetMotorTravelLimits = lib.SBC_SetMotorTravelLimits
SBC_SetMotorTravelLimits.restype = c_short
SBC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
# *serialNo, channel, minPosition, maxPosition

SBC_SetMotorTravelMode = lib.SBC_SetMotorTravelMode
SBC_SetMotorTravelMode.restype = c_short
SBC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]
# *serialNo, channel, travelMode

SBC_SetMotorVelocityLimits = lib.SBC_SetMotorVelocityLimits
SBC_SetMotorVelocityLimits.restype = c_short
SBC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
# *serialNo, channel, maxVelocity, maxAcceleration

SBC_SetMoveAbsolutePosition = lib.SBC_SetMoveAbsolutePosition
SBC_SetMoveAbsolutePosition.restype = c_short
SBC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, position

SBC_SetMoveRelativeDistance = lib.SBC_SetMoveRelativeDistance
SBC_SetMoveRelativeDistance.restype = c_short
SBC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, distance

SBC_SetPIDLoopEncoderCoeff = lib.SBC_SetPIDLoopEncoderCoeff
SBC_SetPIDLoopEncoderCoeff.restype = c_short
SBC_SetPIDLoopEncoderCoeff.argtypes = [POINTER(c_char), c_short, c_double]
# *serialNo, channel, coeff

SBC_SetPIDLoopEncoderParams = lib.SBC_SetPIDLoopEncoderParams
SBC_SetPIDLoopEncoderParams.restype = c_short
SBC_SetPIDLoopEncoderParams.argtypes = [POINTER(c_char), c_short, MOT_PIDLoopEncoderParams]
# *serialNo, channel, *params

SBC_SetPositionCounter = lib.SBC_SetPositionCounter
SBC_SetPositionCounter.restype = c_short
SBC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]
# *serialNo, channel, count

SBC_SetPowerParams = lib.SBC_SetPowerParams
SBC_SetPowerParams.restype = c_short
SBC_SetPowerParams.argtypes = [POINTER(c_char), c_short, MOT_PowerParameters]
# *serialNo, channel, *powerParams

SBC_SetRackDigitalOutputs = lib.SBC_SetRackDigitalOutputs
SBC_SetRackDigitalOutputs.restype = c_short
SBC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
# *serialNo, outputsBits

SBC_SetRotationModes = lib.SBC_SetRotationModes
SBC_SetRotationModes.restype = c_short
SBC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementModes, MOT_MovementDirections]
# *serialNo, channel, mode, direction

SBC_SetStageAxisLimits = lib.SBC_SetStageAxisLimits
SBC_SetStageAxisLimits.restype = c_short
SBC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]
# *serialNo, channel, minPosition, maxPosition

SBC_SetTriggerSwitches = lib.SBC_SetTriggerSwitches
SBC_SetTriggerSwitches.restype = c_short
SBC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]
# *serialNo, channel, indicatorBits

SBC_SetVelParams = lib.SBC_SetVelParams
SBC_SetVelParams.restype = c_short
SBC_SetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]
# *serialNo, channel, acceleration, maxVelocity

SBC_SetVelParamsBlock = lib.SBC_SetVelParamsBlock
SBC_SetVelParamsBlock.restype = c_short
SBC_SetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters, MOT_VelocityParameters]
# *serialNo, channel, *velocityParams, *velocityParameters

SBC_StartPolling = lib.SBC_StartPolling
SBC_StartPolling.restype = c_bool
SBC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, milliseconds

SBC_StopImmediate = lib.SBC_StopImmediate
SBC_StopImmediate.restype = c_short
SBC_StopImmediate.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_StopPolling = lib.SBC_StopPolling
SBC_StopPolling.restype = c_void_p
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

SBC_TimeSinceLastMsgReceived = lib.SBC_TimeSinceLastMsgReceived
SBC_TimeSinceLastMsgReceived.restype = c_bool
SBC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_short, c_int64]
# *serialNo, channel, &lastUpdateTimeMS

SBC_UsesPIDLoopEncoding = lib.SBC_UsesPIDLoopEncoding
SBC_UsesPIDLoopEncoding.restype = c_bool
SBC_UsesPIDLoopEncoding.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

SBC_WaitForMessage = lib.SBC_WaitForMessage
SBC_WaitForMessage.restype = c_bool
SBC_WaitForMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]
# *serialNo, channel, *messageType, *messageID, *messageData

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
