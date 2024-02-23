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
    c_void_p,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KST_Stages,
    MOT_ButtonModes,
    MOT_JogModes,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchSWModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_MovementDirections,
    MOT_MovementModes,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes,
    TST_Stages)
from .definitions.structures import (
    MOT_ButtonParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_PotentiometerSteps,
    MOT_PowerParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.StepperMotor.DLL")

SCC_CanHome = lib.SCC_CanHome
SCC_CanHome.restype = c_bool
SCC_CanHome.argtypes = [POINTER(c_char)]
# *serialNo

SCC_CanMoveWithoutHomingFirst = lib.SCC_CanMoveWithoutHomingFirst
SCC_CanMoveWithoutHomingFirst.restype = c_bool
SCC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
# *serialNo

SCC_CheckConnection = lib.SCC_CheckConnection
SCC_CheckConnection.restype = c_bool
SCC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

SCC_ClearMessageQueue = lib.SCC_ClearMessageQueue
SCC_ClearMessageQueue.restype = c_void_p
SCC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

SCC_Close = lib.SCC_Close
SCC_Close.restype = c_void_p
SCC_Close.argtypes = [POINTER(c_char)]
# *serialNo

SCC_DisableChannel = lib.SCC_DisableChannel
SCC_DisableChannel.restype = c_short
SCC_DisableChannel.argtypes = [POINTER(c_char)]
# *serialNo

SCC_EnableChannel = lib.SCC_EnableChannel
SCC_EnableChannel.restype = c_short
SCC_EnableChannel.argtypes = [POINTER(c_char)]
# *serialNo

SCC_EnableLastMsgTimer = lib.SCC_EnableLastMsgTimer
SCC_EnableLastMsgTimer.restype = c_void_p
SCC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

SCC_GetBacklash = lib.SCC_GetBacklash
SCC_GetBacklash.restype = c_long
SCC_GetBacklash.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetBowIndex = lib.SCC_GetBowIndex
SCC_GetBowIndex.restype = c_short
SCC_GetBowIndex.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetButtonParams = lib.SCC_GetButtonParams
SCC_GetButtonParams.restype = c_short
SCC_GetButtonParams.argtypes = [MOT_ButtonModes, c_int, c_int, POINTER(c_char), c_short]
# *buttonMode, *leftButtonPosition, *rightButtonPosition, *serialNo, *timeout

SCC_GetButtonParamsBlock = lib.SCC_GetButtonParamsBlock
SCC_GetButtonParamsBlock.restype = c_short
SCC_GetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
# *buttonParams, *serialNo

SCC_GetCalibrationFile = lib.SCC_GetCalibrationFile
SCC_GetCalibrationFile.restype = c_bool
SCC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
# *filename, *serialNo, sizeOfBuffer

SCC_GetDeviceUnitFromRealValue = lib.SCC_GetDeviceUnitFromRealValue
SCC_GetDeviceUnitFromRealValue.restype = c_short
SCC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
# *device_unit, *serialNo, real_unit, unitType

SCC_GetEncoderCounter = lib.SCC_GetEncoderCounter
SCC_GetEncoderCounter.restype = c_long
SCC_GetEncoderCounter.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetHardwareInfo = lib.SCC_GetHardwareInfo
SCC_GetHardwareInfo.restype = c_short
SCC_GetHardwareInfo.argtypes = [
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

SCC_GetHardwareInfoBlock = lib.SCC_GetHardwareInfoBlock
SCC_GetHardwareInfoBlock.restype = c_short
SCC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

SCC_GetHomingParamsBlock = lib.SCC_GetHomingParamsBlock
SCC_GetHomingParamsBlock.restype = c_short
SCC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
# *homingParams, *serialNo

SCC_GetHomingVelocity = lib.SCC_GetHomingVelocity
SCC_GetHomingVelocity.restype = c_uint
SCC_GetHomingVelocity.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetHubBay = lib.SCC_GetHubBay
SCC_GetHubBay.restype = POINTER(c_char)
SCC_GetHubBay.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetJogMode = lib.SCC_GetJogMode
SCC_GetJogMode.restype = c_short
SCC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
# *mode, *serialNo, *stopMode

SCC_GetJogParamsBlock = lib.SCC_GetJogParamsBlock
SCC_GetJogParamsBlock.restype = c_short
SCC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
# *jogParams, *serialNo

SCC_GetJogStepSize = lib.SCC_GetJogStepSize
SCC_GetJogStepSize.restype = c_uint
SCC_GetJogStepSize.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetJogVelParams = lib.SCC_GetJogVelParams
SCC_GetJogVelParams.restype = c_short
SCC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
# *acceleration, *maxVelocity, *serialNo

SCC_GetLEDswitches = lib.SCC_GetLEDswitches
SCC_GetLEDswitches.restype = c_long
SCC_GetLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetLimitSwitchParams = lib.SCC_GetLimitSwitchParams
SCC_GetLimitSwitchParams.restype = c_short
SCC_GetLimitSwitchParams.argtypes = [
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    POINTER(c_char),
    MOT_LimitSwitchSWModes]
# *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode

SCC_GetLimitSwitchParamsBlock = lib.SCC_GetLimitSwitchParamsBlock
SCC_GetLimitSwitchParamsBlock.restype = c_short
SCC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
# *limitSwitchParams, *serialNo

SCC_GetMotorParams = lib.SCC_GetMotorParams
SCC_GetMotorParams.restype = c_short
SCC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

SCC_GetMotorParamsExt = lib.SCC_GetMotorParamsExt
SCC_GetMotorParamsExt.restype = c_short
SCC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

SCC_GetMotorTravelLimits = lib.SCC_GetMotorTravelLimits
SCC_GetMotorTravelLimits.restype = c_short
SCC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
# *maxPosition, *minPosition, *serialNo

SCC_GetMotorTravelMode = lib.SCC_GetMotorTravelMode
SCC_GetMotorTravelMode.restype = MOT_TravelModes
SCC_GetMotorTravelMode.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetMotorVelocityLimits = lib.SCC_GetMotorVelocityLimits
SCC_GetMotorVelocityLimits.restype = c_short
SCC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
# *maxAcceleration, *maxVelocity, *serialNo

SCC_GetMoveAbsolutePosition = lib.SCC_GetMoveAbsolutePosition
SCC_GetMoveAbsolutePosition.restype = c_int
SCC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetMoveRelativeDistance = lib.SCC_GetMoveRelativeDistance
SCC_GetMoveRelativeDistance.restype = c_int
SCC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetNextMessage = lib.SCC_GetNextMessage
SCC_GetNextMessage.restype = c_bool
SCC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

SCC_GetNumberPositions = lib.SCC_GetNumberPositions
SCC_GetNumberPositions.restype = c_int
SCC_GetNumberPositions.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetPosition = lib.SCC_GetPosition
SCC_GetPosition.restype = c_int
SCC_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetPositionCounter = lib.SCC_GetPositionCounter
SCC_GetPositionCounter.restype = c_long
SCC_GetPositionCounter.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetPotentiometerParams = lib.SCC_GetPotentiometerParams
SCC_GetPotentiometerParams.restype = c_short
SCC_GetPotentiometerParams.argtypes = [POINTER(c_char), c_long, c_ulong, c_short]
# *serialNo, *thresholdDeflection, *velocity, index

SCC_GetPotentiometerParamsBlock = lib.SCC_GetPotentiometerParamsBlock
SCC_GetPotentiometerParamsBlock.restype = c_short
SCC_GetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
# *potentiometerSteps, *serialNo

SCC_GetPowerParams = lib.SCC_GetPowerParams
SCC_GetPowerParams.restype = c_short
SCC_GetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char)]
# *powerParams, *serialNo

SCC_GetRealValueFromDeviceUnit = lib.SCC_GetRealValueFromDeviceUnit
SCC_GetRealValueFromDeviceUnit.restype = c_short
SCC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
# *real_unit, *serialNo, device_unit, unitType

SCC_GetSoftLimitMode = lib.SCC_GetSoftLimitMode
SCC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
SCC_GetSoftLimitMode.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetSoftwareVersion = lib.SCC_GetSoftwareVersion
SCC_GetSoftwareVersion.restype = c_ulong
SCC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetStageAxisMaxPos = lib.SCC_GetStageAxisMaxPos
SCC_GetStageAxisMaxPos.restype = c_int
SCC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetStageAxisMinPos = lib.SCC_GetStageAxisMinPos
SCC_GetStageAxisMinPos.restype = c_int
SCC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetStatusBits = lib.SCC_GetStatusBits
SCC_GetStatusBits.restype = c_ulong
SCC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

SCC_GetVelParams = lib.SCC_GetVelParams
SCC_GetVelParams.restype = c_short
SCC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
# *acceleration, *maxVelocity, *serialNo

SCC_GetVelParamsBlock = lib.SCC_GetVelParamsBlock
SCC_GetVelParamsBlock.restype = c_short
SCC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
# *serialNo, *velocityParams

SCC_HasLastMsgTimerOverrun = lib.SCC_HasLastMsgTimerOverrun
SCC_HasLastMsgTimerOverrun.restype = c_bool
SCC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

SCC_Home = lib.SCC_Home
SCC_Home.restype = c_short
SCC_Home.argtypes = [POINTER(c_char)]
# *serialNo

SCC_Identify = lib.SCC_Identify
SCC_Identify.restype = c_void_p
SCC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

SCC_IsCalibrationActive = lib.SCC_IsCalibrationActive
SCC_IsCalibrationActive.restype = c_bool
SCC_IsCalibrationActive.argtypes = [POINTER(c_char)]
# *serialNo

SCC_LoadNamedSettings = lib.SCC_LoadNamedSettings
SCC_LoadNamedSettings.restype = c_bool
SCC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

SCC_LoadSettings = lib.SCC_LoadSettings
SCC_LoadSettings.restype = c_bool
SCC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

SCC_MessageQueueSize = lib.SCC_MessageQueueSize
SCC_MessageQueueSize.restype = c_int
SCC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

SCC_MoveAbsolute = lib.SCC_MoveAbsolute
SCC_MoveAbsolute.restype = c_short
SCC_MoveAbsolute.argtypes = [POINTER(c_char)]
# *serialNo

SCC_MoveAtVelocity = lib.SCC_MoveAtVelocity
SCC_MoveAtVelocity.restype = c_short
SCC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, direction

SCC_MoveJog = lib.SCC_MoveJog
SCC_MoveJog.restype = c_short
SCC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, jogDirection

SCC_MoveRelative = lib.SCC_MoveRelative
SCC_MoveRelative.restype = c_short
SCC_MoveRelative.argtypes = [POINTER(c_char), c_int]
# *serialNo, displacement

SCC_MoveRelativeDistance = lib.SCC_MoveRelativeDistance
SCC_MoveRelativeDistance.restype = c_short
SCC_MoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

SCC_MoveToPosition = lib.SCC_MoveToPosition
SCC_MoveToPosition.restype = c_short
SCC_MoveToPosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, index

SCC_NeedsHoming = lib.SCC_NeedsHoming
SCC_NeedsHoming.restype = c_bool
SCC_NeedsHoming.argtypes = [POINTER(c_char)]
# *serialNo

SCC_Open = lib.SCC_Open
SCC_Open.restype = c_short
SCC_Open.argtypes = [POINTER(c_char)]
# *serialNo

SCC_PersistSettings = lib.SCC_PersistSettings
SCC_PersistSettings.restype = c_bool
SCC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

SCC_PollingDuration = lib.SCC_PollingDuration
SCC_PollingDuration.restype = c_long
SCC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RegisterMessageCallback = lib.SCC_RegisterMessageCallback
SCC_RegisterMessageCallback.restype = c_void_p
SCC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNo, void

SCC_RequestBacklash = lib.SCC_RequestBacklash
SCC_RequestBacklash.restype = c_short
SCC_RequestBacklash.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestBowIndex = lib.SCC_RequestBowIndex
SCC_RequestBowIndex.restype = c_short
SCC_RequestBowIndex.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestButtonParams = lib.SCC_RequestButtonParams
SCC_RequestButtonParams.restype = c_short
SCC_RequestButtonParams.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestEncoderCounter = lib.SCC_RequestEncoderCounter
SCC_RequestEncoderCounter.restype = c_short
SCC_RequestEncoderCounter.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestHomingParams = lib.SCC_RequestHomingParams
SCC_RequestHomingParams.restype = c_short
SCC_RequestHomingParams.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestJogParams = lib.SCC_RequestJogParams
SCC_RequestJogParams.restype = c_short
SCC_RequestJogParams.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestLEDswitches = lib.SCC_RequestLEDswitches
SCC_RequestLEDswitches.restype = c_short
SCC_RequestLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestLimitSwitchParams = lib.SCC_RequestLimitSwitchParams
SCC_RequestLimitSwitchParams.restype = c_short
SCC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestMoveAbsolutePosition = lib.SCC_RequestMoveAbsolutePosition
SCC_RequestMoveAbsolutePosition.restype = c_short
SCC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestMoveRelativeDistance = lib.SCC_RequestMoveRelativeDistance
SCC_RequestMoveRelativeDistance.restype = c_short
SCC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestPosition = lib.SCC_RequestPosition
SCC_RequestPosition.restype = c_short
SCC_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestPotentiometerParams = lib.SCC_RequestPotentiometerParams
SCC_RequestPotentiometerParams.restype = c_short
SCC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestPowerParams = lib.SCC_RequestPowerParams
SCC_RequestPowerParams.restype = c_short
SCC_RequestPowerParams.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestSettings = lib.SCC_RequestSettings
SCC_RequestSettings.restype = c_short
SCC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestStatusBits = lib.SCC_RequestStatusBits
SCC_RequestStatusBits.restype = c_short
SCC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

SCC_RequestVelParams = lib.SCC_RequestVelParams
SCC_RequestVelParams.restype = c_short
SCC_RequestVelParams.argtypes = [POINTER(c_char)]
# *serialNo

SCC_ResetRotationModes = lib.SCC_ResetRotationModes
SCC_ResetRotationModes.restype = c_short
SCC_ResetRotationModes.argtypes = [POINTER(c_char)]
# *serialNo

SCC_ResumeMoveMessages = lib.SCC_ResumeMoveMessages
SCC_ResumeMoveMessages.restype = c_short
SCC_ResumeMoveMessages.argtypes = [POINTER(c_char)]
# *serialNo

SCC_SetBacklash = lib.SCC_SetBacklash
SCC_SetBacklash.restype = c_short
SCC_SetBacklash.argtypes = [POINTER(c_char), c_long]
# *serialNo, distance

SCC_SetBowIndex = lib.SCC_SetBowIndex
SCC_SetBowIndex.restype = c_short
SCC_SetBowIndex.argtypes = [POINTER(c_char), c_short]
# *serialNo, bowIndex

SCC_SetButtonParams = lib.SCC_SetButtonParams
SCC_SetButtonParams.restype = c_short
SCC_SetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int]
# *serialNo, buttonMode, leftButtonPosition, rightButtonPosition

SCC_SetButtonParamsBlock = lib.SCC_SetButtonParamsBlock
SCC_SetButtonParamsBlock.restype = c_short
SCC_SetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
# *buttonParams, *serialNo

SCC_SetCalibrationFile = lib.SCC_SetCalibrationFile
SCC_SetCalibrationFile.restype = c_void_p
SCC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_bool]
# *filename, *serialNo, enabled

SCC_SetDirection = lib.SCC_SetDirection
SCC_SetDirection.restype = c_void_p
SCC_SetDirection.argtypes = [POINTER(c_char), c_bool]
# *serialNo, reverse

SCC_SetEncoderCounter = lib.SCC_SetEncoderCounter
SCC_SetEncoderCounter.restype = c_short
SCC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]
# *serialNo, count

SCC_SetHomingParamsBlock = lib.SCC_SetHomingParamsBlock
SCC_SetHomingParamsBlock.restype = c_short
SCC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
# *homingParams, *serialNo

SCC_SetHomingVelocity = lib.SCC_SetHomingVelocity
SCC_SetHomingVelocity.restype = c_short
SCC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
# *serialNo, velocity

SCC_SetJogMode = lib.SCC_SetJogMode
SCC_SetJogMode.restype = c_short
SCC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
# *serialNo, mode, stopMode

SCC_SetJogParamsBlock = lib.SCC_SetJogParamsBlock
SCC_SetJogParamsBlock.restype = c_short
SCC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
# *jogParams, *serialNo

SCC_SetJogStepSize = lib.SCC_SetJogStepSize
SCC_SetJogStepSize.restype = c_short
SCC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
# *serialNo, stepSize

SCC_SetJogVelParams = lib.SCC_SetJogVelParams
SCC_SetJogVelParams.restype = c_short
SCC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, acceleration, maxVelocity

SCC_SetLEDswitches = lib.SCC_SetLEDswitches
SCC_SetLEDswitches.restype = c_short
SCC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
# *serialNo, LEDswitches

SCC_SetLimitSwitchParams = lib.SCC_SetLimitSwitchParams
SCC_SetLimitSwitchParams.restype = c_short
SCC_SetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchSWModes]
# *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, clockwiseHardwareLimit, clockwisePosition, softLimitMode

SCC_SetLimitSwitchParamsBlock = lib.SCC_SetLimitSwitchParamsBlock
SCC_SetLimitSwitchParamsBlock.restype = c_short
SCC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
# *limitSwitchParams, *serialNo

SCC_SetLimitsSoftwareApproachPolicy = lib.SCC_SetLimitsSoftwareApproachPolicy
SCC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
SCC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
# *serialNo, limitsSoftwareApproachPolicy

SCC_SetMotorParams = lib.SCC_SetMotorParams
SCC_SetMotorParams.restype = c_short
SCC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
# *serialNo, gearBoxRatio, pitch, stepsPerRev

SCC_SetMotorParamsExt = lib.SCC_SetMotorParamsExt
SCC_SetMotorParamsExt.restype = c_short
SCC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
# *serialNo, gearBoxRatio, pitch, stepsPerRev

SCC_SetMotorTravelLimits = lib.SCC_SetMotorTravelLimits
SCC_SetMotorTravelLimits.restype = c_short
SCC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
# *serialNo, maxPosition, minPosition

SCC_SetMotorTravelMode = lib.SCC_SetMotorTravelMode
SCC_SetMotorTravelMode.restype = c_short
SCC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
# *serialNo, travelMode

SCC_SetMotorVelocityLimits = lib.SCC_SetMotorVelocityLimits
SCC_SetMotorVelocityLimits.restype = c_short
SCC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
# *serialNo, maxAcceleration, maxVelocity

SCC_SetMoveAbsolutePosition = lib.SCC_SetMoveAbsolutePosition
SCC_SetMoveAbsolutePosition.restype = c_short
SCC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, position

SCC_SetMoveRelativeDistance = lib.SCC_SetMoveRelativeDistance
SCC_SetMoveRelativeDistance.restype = c_short
SCC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
# *serialNo, distance

SCC_SetPositionCounter = lib.SCC_SetPositionCounter
SCC_SetPositionCounter.restype = c_short
SCC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
# *serialNo, count

SCC_SetPotentiometerParams = lib.SCC_SetPotentiometerParams
SCC_SetPotentiometerParams.restype = c_short
SCC_SetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]
# *serialNo, index, thresholdDeflection, velocity

SCC_SetPotentiometerParamsBlock = lib.SCC_SetPotentiometerParamsBlock
SCC_SetPotentiometerParamsBlock.restype = c_short
SCC_SetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
# *potentiometerSteps, *serialNo

SCC_SetPowerParams = lib.SCC_SetPowerParams
SCC_SetPowerParams.restype = c_short
SCC_SetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char)]
# *powerParams, *serialNo

SCC_SetRotationModes = lib.SCC_SetRotationModes
SCC_SetRotationModes.restype = c_short
SCC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementDirections, MOT_MovementModes]
# *serialNo, direction, mode

SCC_SetStageAxisLimits = lib.SCC_SetStageAxisLimits
SCC_SetStageAxisLimits.restype = c_short
SCC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, maxPosition, minPosition

SCC_SetStageType = lib.SCC_SetStageType
SCC_SetStageType.restype = c_short
SCC_SetStageType.argtypes = [POINTER(c_char), KST_Stages, TST_Stages]
# *serialNo, stageId, stageId

SCC_SetVelParams = lib.SCC_SetVelParams
SCC_SetVelParams.restype = c_short
SCC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, acceleration, maxVelocity

SCC_SetVelParamsBlock = lib.SCC_SetVelParamsBlock
SCC_SetVelParamsBlock.restype = c_short
SCC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
# *serialNo, *velocityParams

SCC_StartPolling = lib.SCC_StartPolling
SCC_StartPolling.restype = c_bool
SCC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

SCC_StopImmediate = lib.SCC_StopImmediate
SCC_StopImmediate.restype = c_short
SCC_StopImmediate.argtypes = [POINTER(c_char)]
# *serialNo

SCC_StopPolling = lib.SCC_StopPolling
SCC_StopPolling.restype = c_void_p
SCC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

SCC_StopProfiled = lib.SCC_StopProfiled
SCC_StopProfiled.restype = c_short
SCC_StopProfiled.argtypes = [POINTER(c_char)]
# *serialNo

SCC_SuspendMoveMessages = lib.SCC_SuspendMoveMessages
SCC_SuspendMoveMessages.restype = c_short
SCC_SuspendMoveMessages.argtypes = [POINTER(c_char)]
# *serialNo

SCC_TimeSinceLastMsgReceived = lib.SCC_TimeSinceLastMsgReceived
SCC_TimeSinceLastMsgReceived.restype = c_bool
SCC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

SCC_WaitForMessage = lib.SCC_WaitForMessage
SCC_WaitForMessage.restype = c_bool
SCC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
#

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
#

TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p
#
