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
    cdll)
from .safearray import SafeArray
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
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_PotentiometerSteps,
    MOT_PowerParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.IntegratedStepperMotors.DLL")
ISC_CanHome = lib.ISC_CanHome
ISC_CanHome.restype = c_bool
ISC_CanHome.argtypes = [POINTER(c_char)]
# *serialNo

ISC_CanMoveWithoutHomingFirst = lib.ISC_CanMoveWithoutHomingFirst
ISC_CanMoveWithoutHomingFirst.restype = c_bool
ISC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
# *serialNo

ISC_CheckConnection = lib.ISC_CheckConnection
ISC_CheckConnection.restype = c_bool
ISC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

ISC_ClearMessageQueue = lib.ISC_ClearMessageQueue
ISC_ClearMessageQueue.restype = None
ISC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

ISC_Close = lib.ISC_Close
ISC_Close.restype = None
ISC_Close.argtypes = [POINTER(c_char)]
# *serialNo

ISC_DisableChannel = lib.ISC_DisableChannel
ISC_DisableChannel.restype = c_short
ISC_DisableChannel.argtypes = [POINTER(c_char)]
# *serialNo

ISC_EnableChannel = lib.ISC_EnableChannel
ISC_EnableChannel.restype = c_short
ISC_EnableChannel.argtypes = [POINTER(c_char)]
# *serialNo

ISC_EnableLastMsgTimer = lib.ISC_EnableLastMsgTimer
ISC_EnableLastMsgTimer.restype = None
ISC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

ISC_GetBacklash = lib.ISC_GetBacklash
ISC_GetBacklash.restype = c_long
ISC_GetBacklash.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetBowIndex = lib.ISC_GetBowIndex
ISC_GetBowIndex.restype = c_short
ISC_GetBowIndex.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetButtonParams = lib.ISC_GetButtonParams
ISC_GetButtonParams.restype = c_short
ISC_GetButtonParams.argtypes = [MOT_ButtonModes, c_int, c_int, POINTER(c_char), c_short]
# *buttonMode, *leftButtonPosition, *rightButtonPosition, *serialNo, *timeout

ISC_GetButtonParamsBlock = lib.ISC_GetButtonParamsBlock
ISC_GetButtonParamsBlock.restype = c_short
ISC_GetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
# *buttonParams, *serialNo

ISC_GetCalibrationFile = lib.ISC_GetCalibrationFile
ISC_GetCalibrationFile.restype = c_bool
ISC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
# *filename, *serialNo, sizeOfBuffer

ISC_GetDeviceUnitFromRealValue = lib.ISC_GetDeviceUnitFromRealValue
ISC_GetDeviceUnitFromRealValue.restype = c_short
ISC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
# *device_unit, *serialNo, real_unit, unitType

ISC_GetFirmwareVersion = lib.ISC_GetFirmwareVersion
ISC_GetFirmwareVersion.restype = c_ulong
ISC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetHardwareInfo = lib.ISC_GetHardwareInfo
ISC_GetHardwareInfo.restype = c_short
ISC_GetHardwareInfo.argtypes = [
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

ISC_GetHardwareInfoBlock = lib.ISC_GetHardwareInfoBlock
ISC_GetHardwareInfoBlock.restype = c_short
ISC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

ISC_GetHomingParamsBlock = lib.ISC_GetHomingParamsBlock
ISC_GetHomingParamsBlock.restype = c_short
ISC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
# *homingParams, *serialNo

ISC_GetHomingVelocity = lib.ISC_GetHomingVelocity
ISC_GetHomingVelocity.restype = c_uint
ISC_GetHomingVelocity.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetJogMode = lib.ISC_GetJogMode
ISC_GetJogMode.restype = c_short
ISC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
# *mode, *serialNo, *stopMode

ISC_GetJogParamsBlock = lib.ISC_GetJogParamsBlock
ISC_GetJogParamsBlock.restype = c_short
ISC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
# *jogParams, *serialNo

ISC_GetJogStepSize = lib.ISC_GetJogStepSize
ISC_GetJogStepSize.restype = c_uint
ISC_GetJogStepSize.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetJogVelParams = lib.ISC_GetJogVelParams
ISC_GetJogVelParams.restype = c_short
ISC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
# *acceleration, *maxVelocity, *serialNo

ISC_GetLEDswitches = lib.ISC_GetLEDswitches
ISC_GetLEDswitches.restype = c_long
ISC_GetLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetLimitSwitchParams = lib.ISC_GetLimitSwitchParams
ISC_GetLimitSwitchParams.restype = c_short
ISC_GetLimitSwitchParams.argtypes = [
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    POINTER(c_char),
    MOT_LimitSwitchSWModes]
# *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode

ISC_GetLimitSwitchParamsBlock = lib.ISC_GetLimitSwitchParamsBlock
ISC_GetLimitSwitchParamsBlock.restype = c_short
ISC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
# *limitSwitchParams, *serialNo

ISC_GetMotorParams = lib.ISC_GetMotorParams
ISC_GetMotorParams.restype = c_short
ISC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

ISC_GetMotorParamsExt = lib.ISC_GetMotorParamsExt
ISC_GetMotorParamsExt.restype = c_short
ISC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

ISC_GetMotorTravelLimits = lib.ISC_GetMotorTravelLimits
ISC_GetMotorTravelLimits.restype = c_short
ISC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
# *maxPosition, *minPosition, *serialNo

ISC_GetMotorTravelMode = lib.ISC_GetMotorTravelMode
ISC_GetMotorTravelMode.restype = MOT_TravelModes
ISC_GetMotorTravelMode.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetMotorVelocityLimits = lib.ISC_GetMotorVelocityLimits
ISC_GetMotorVelocityLimits.restype = c_short
ISC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
# *maxAcceleration, *maxVelocity, *serialNo

ISC_GetMoveAbsolutePosition = lib.ISC_GetMoveAbsolutePosition
ISC_GetMoveAbsolutePosition.restype = c_int
ISC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetMoveRelativeDistance = lib.ISC_GetMoveRelativeDistance
ISC_GetMoveRelativeDistance.restype = c_int
ISC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetNextMessage = lib.ISC_GetNextMessage
ISC_GetNextMessage.restype = c_bool
ISC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

ISC_GetNumberPositions = lib.ISC_GetNumberPositions
ISC_GetNumberPositions.restype = c_int
ISC_GetNumberPositions.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetPosition = lib.ISC_GetPosition
ISC_GetPosition.restype = c_int
ISC_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetPositionCounter = lib.ISC_GetPositionCounter
ISC_GetPositionCounter.restype = c_long
ISC_GetPositionCounter.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetPotentiometerParams = lib.ISC_GetPotentiometerParams
ISC_GetPotentiometerParams.restype = c_short
ISC_GetPotentiometerParams.argtypes = [POINTER(c_char), c_long, c_ulong, c_short]
# *serialNo, *thresholdDeflection, *velocity, index

ISC_GetPotentiometerParamsBlock = lib.ISC_GetPotentiometerParamsBlock
ISC_GetPotentiometerParamsBlock.restype = c_short
ISC_GetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
# *potentiometerSteps, *serialNo

ISC_GetPowerParams = lib.ISC_GetPowerParams
ISC_GetPowerParams.restype = c_short
ISC_GetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char)]
# *powerParams, *serialNo

ISC_GetRealValueFromDeviceUnit = lib.ISC_GetRealValueFromDeviceUnit
ISC_GetRealValueFromDeviceUnit.restype = c_short
ISC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
# *real_unit, *serialNo, device_unit, unitType

ISC_GetSoftLimitMode = lib.ISC_GetSoftLimitMode
ISC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
ISC_GetSoftLimitMode.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetSoftwareVersion = lib.ISC_GetSoftwareVersion
ISC_GetSoftwareVersion.restype = c_ulong
ISC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetStageAxisMaxPos = lib.ISC_GetStageAxisMaxPos
ISC_GetStageAxisMaxPos.restype = c_int
ISC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetStageAxisMinPos = lib.ISC_GetStageAxisMinPos
ISC_GetStageAxisMinPos.restype = c_int
ISC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetStatusBits = lib.ISC_GetStatusBits
ISC_GetStatusBits.restype = c_ulong
ISC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetTriggerSwitches = lib.ISC_GetTriggerSwitches
ISC_GetTriggerSwitches.restype = c_byte
ISC_GetTriggerSwitches.argtypes = [POINTER(c_char)]
# *serialNo

ISC_GetVelParams = lib.ISC_GetVelParams
ISC_GetVelParams.restype = c_short
ISC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
# *acceleration, *maxVelocity, *serialNo

ISC_GetVelParamsBlock = lib.ISC_GetVelParamsBlock
ISC_GetVelParamsBlock.restype = c_short
ISC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
# *serialNo, *velocityParams

ISC_HasLastMsgTimerOverrun = lib.ISC_HasLastMsgTimerOverrun
ISC_HasLastMsgTimerOverrun.restype = c_bool
ISC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

ISC_Home = lib.ISC_Home
ISC_Home.restype = c_short
ISC_Home.argtypes = [POINTER(c_char)]
# *serialNo

ISC_Identify = lib.ISC_Identify
ISC_Identify.restype = None
ISC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

ISC_IsCalibrationActive = lib.ISC_IsCalibrationActive
ISC_IsCalibrationActive.restype = c_bool
ISC_IsCalibrationActive.argtypes = [POINTER(c_char)]
# *serialNo

ISC_LoadNamedSettings = lib.ISC_LoadNamedSettings
ISC_LoadNamedSettings.restype = c_bool
ISC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

ISC_LoadSettings = lib.ISC_LoadSettings
ISC_LoadSettings.restype = c_bool
ISC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

ISC_MessageQueueSize = lib.ISC_MessageQueueSize
ISC_MessageQueueSize.restype = c_int
ISC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

ISC_MoveAbsolute = lib.ISC_MoveAbsolute
ISC_MoveAbsolute.restype = c_short
ISC_MoveAbsolute.argtypes = [POINTER(c_char)]
# *serialNo

ISC_MoveAtVelocity = lib.ISC_MoveAtVelocity
ISC_MoveAtVelocity.restype = c_short
ISC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, direction

ISC_MoveJog = lib.ISC_MoveJog
ISC_MoveJog.restype = c_short
ISC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, jogDirection

ISC_MoveRelative = lib.ISC_MoveRelative
ISC_MoveRelative.restype = c_short
ISC_MoveRelative.argtypes = [POINTER(c_char), c_int]
# *serialNo, displacement

ISC_MoveRelativeDistance = lib.ISC_MoveRelativeDistance
ISC_MoveRelativeDistance.restype = c_short
ISC_MoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

ISC_MoveToPosition = lib.ISC_MoveToPosition
ISC_MoveToPosition.restype = c_short
ISC_MoveToPosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, index

ISC_NeedsHoming = lib.ISC_NeedsHoming
ISC_NeedsHoming.restype = c_bool
ISC_NeedsHoming.argtypes = [POINTER(c_char)]
# *serialNo

ISC_Open = lib.ISC_Open
ISC_Open.restype = c_short
ISC_Open.argtypes = [POINTER(c_char)]
# *serialNo

ISC_PersistSettings = lib.ISC_PersistSettings
ISC_PersistSettings.restype = c_bool
ISC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

ISC_PollingDuration = lib.ISC_PollingDuration
ISC_PollingDuration.restype = c_long
ISC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RegisterMessageCallback = lib.ISC_RegisterMessageCallback
ISC_RegisterMessageCallback.restype = None
ISC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

ISC_RequestBacklash = lib.ISC_RequestBacklash
ISC_RequestBacklash.restype = c_short
ISC_RequestBacklash.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestBowIndex = lib.ISC_RequestBowIndex
ISC_RequestBowIndex.restype = c_short
ISC_RequestBowIndex.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestButtonParams = lib.ISC_RequestButtonParams
ISC_RequestButtonParams.restype = c_short
ISC_RequestButtonParams.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestHomingParams = lib.ISC_RequestHomingParams
ISC_RequestHomingParams.restype = c_short
ISC_RequestHomingParams.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestJogParams = lib.ISC_RequestJogParams
ISC_RequestJogParams.restype = c_short
ISC_RequestJogParams.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestLimitSwitchParams = lib.ISC_RequestLimitSwitchParams
ISC_RequestLimitSwitchParams.restype = c_short
ISC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestMoveAbsolutePosition = lib.ISC_RequestMoveAbsolutePosition
ISC_RequestMoveAbsolutePosition.restype = c_short
ISC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestMoveRelativeDistance = lib.ISC_RequestMoveRelativeDistance
ISC_RequestMoveRelativeDistance.restype = c_short
ISC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestPosition = lib.ISC_RequestPosition
ISC_RequestPosition.restype = c_short
ISC_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestPotentiometerParams = lib.ISC_RequestPotentiometerParams
ISC_RequestPotentiometerParams.restype = c_short
ISC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestPowerParams = lib.ISC_RequestPowerParams
ISC_RequestPowerParams.restype = c_short
ISC_RequestPowerParams.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestSettings = lib.ISC_RequestSettings
ISC_RequestSettings.restype = c_short
ISC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestStatus = lib.ISC_RequestStatus
ISC_RequestStatus.restype = c_short
ISC_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestStatusBits = lib.ISC_RequestStatusBits
ISC_RequestStatusBits.restype = c_short
ISC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestTriggerSwitches = lib.ISC_RequestTriggerSwitches
ISC_RequestTriggerSwitches.restype = c_short
ISC_RequestTriggerSwitches.argtypes = [POINTER(c_char)]
# *serialNo

ISC_RequestVelParams = lib.ISC_RequestVelParams
ISC_RequestVelParams.restype = c_short
ISC_RequestVelParams.argtypes = [POINTER(c_char)]
# *serialNo

ISC_ResetRotationModes = lib.ISC_ResetRotationModes
ISC_ResetRotationModes.restype = c_short
ISC_ResetRotationModes.argtypes = [POINTER(c_char)]
# *serialNo

ISC_ResetStageToDefaults = lib.ISC_ResetStageToDefaults
ISC_ResetStageToDefaults.restype = c_short
ISC_ResetStageToDefaults.argtypes = [POINTER(c_char)]
# *serialNo

ISC_SetBacklash = lib.ISC_SetBacklash
ISC_SetBacklash.restype = c_short
ISC_SetBacklash.argtypes = [POINTER(c_char), c_long]
# *serialNo, distance

ISC_SetBowIndex = lib.ISC_SetBowIndex
ISC_SetBowIndex.restype = c_short
ISC_SetBowIndex.argtypes = [POINTER(c_char), c_short]
# *serialNo, bowIndex

ISC_SetButtonParams = lib.ISC_SetButtonParams
ISC_SetButtonParams.restype = c_short
ISC_SetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int]
# *serialNo, buttonMode, leftButtonPosition, rightButtonPosition

ISC_SetButtonParamsBlock = lib.ISC_SetButtonParamsBlock
ISC_SetButtonParamsBlock.restype = c_short
ISC_SetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
# *buttonParams, *serialNo

ISC_SetCalibrationFile = lib.ISC_SetCalibrationFile
ISC_SetCalibrationFile.restype = None
ISC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_bool]
# *filename, *serialNo, enabled

ISC_SetDirection = lib.ISC_SetDirection
ISC_SetDirection.restype = None
ISC_SetDirection.argtypes = [POINTER(c_char), c_bool]
# *serialNo, reverse

ISC_SetHomingParamsBlock = lib.ISC_SetHomingParamsBlock
ISC_SetHomingParamsBlock.restype = c_short
ISC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
# *homingParams, *serialNo

ISC_SetHomingVelocity = lib.ISC_SetHomingVelocity
ISC_SetHomingVelocity.restype = c_short
ISC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
# *serialNo, velocity

ISC_SetJogMode = lib.ISC_SetJogMode
ISC_SetJogMode.restype = c_short
ISC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
# *serialNo, mode, stopMode

ISC_SetJogParamsBlock = lib.ISC_SetJogParamsBlock
ISC_SetJogParamsBlock.restype = c_short
ISC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
# *jogParams, *serialNo

ISC_SetJogStepSize = lib.ISC_SetJogStepSize
ISC_SetJogStepSize.restype = c_short
ISC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
# *serialNo, stepSize

ISC_SetJogVelParams = lib.ISC_SetJogVelParams
ISC_SetJogVelParams.restype = c_short
ISC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, acceleration, maxVelocity

ISC_SetLEDswitches = lib.ISC_SetLEDswitches
ISC_SetLEDswitches.restype = c_short
ISC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
# *serialNo, LEDswitches

ISC_SetLimitSwitchParams = lib.ISC_SetLimitSwitchParams
ISC_SetLimitSwitchParams.restype = c_short
ISC_SetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchSWModes]
# *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, clockwiseHardwareLimit, clockwisePosition, softLimitMode

ISC_SetLimitSwitchParamsBlock = lib.ISC_SetLimitSwitchParamsBlock
ISC_SetLimitSwitchParamsBlock.restype = c_short
ISC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
# *limitSwitchParams, *serialNo

ISC_SetLimitsSoftwareApproachPolicy = lib.ISC_SetLimitsSoftwareApproachPolicy
ISC_SetLimitsSoftwareApproachPolicy.restype = None
ISC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
# *serialNo, limitsSoftwareApproachPolicy

ISC_SetMotorParams = lib.ISC_SetMotorParams
ISC_SetMotorParams.restype = c_short
ISC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
# *serialNo, gearBoxRatio, pitch, stepsPerRev

ISC_SetMotorParamsExt = lib.ISC_SetMotorParamsExt
ISC_SetMotorParamsExt.restype = c_short
ISC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
# *serialNo, gearBoxRatio, pitch, stepsPerRev

ISC_SetMotorTravelLimits = lib.ISC_SetMotorTravelLimits
ISC_SetMotorTravelLimits.restype = c_short
ISC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
# *serialNo, maxPosition, minPosition

ISC_SetMotorTravelMode = lib.ISC_SetMotorTravelMode
ISC_SetMotorTravelMode.restype = c_short
ISC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
# *serialNo, travelMode

ISC_SetMotorVelocityLimits = lib.ISC_SetMotorVelocityLimits
ISC_SetMotorVelocityLimits.restype = c_short
ISC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
# *serialNo, maxAcceleration, maxVelocity

ISC_SetMoveAbsolutePosition = lib.ISC_SetMoveAbsolutePosition
ISC_SetMoveAbsolutePosition.restype = c_short
ISC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, position

ISC_SetMoveRelativeDistance = lib.ISC_SetMoveRelativeDistance
ISC_SetMoveRelativeDistance.restype = c_short
ISC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
# *serialNo, distance

ISC_SetPositionCounter = lib.ISC_SetPositionCounter
ISC_SetPositionCounter.restype = c_short
ISC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
# *serialNo, count

ISC_SetPotentiometerParams = lib.ISC_SetPotentiometerParams
ISC_SetPotentiometerParams.restype = c_short
ISC_SetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]
# *serialNo, index, thresholdDeflection, velocity

ISC_SetPotentiometerParamsBlock = lib.ISC_SetPotentiometerParamsBlock
ISC_SetPotentiometerParamsBlock.restype = c_short
ISC_SetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
# *potentiometerSteps, *serialNo

ISC_SetPowerParams = lib.ISC_SetPowerParams
ISC_SetPowerParams.restype = c_short
ISC_SetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char)]
# *powerParams, *serialNo

ISC_SetRotationModes = lib.ISC_SetRotationModes
ISC_SetRotationModes.restype = c_short
ISC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementDirections, MOT_MovementModes]
# *serialNo, direction, mode

ISC_SetStageAxisLimits = lib.ISC_SetStageAxisLimits
ISC_SetStageAxisLimits.restype = c_short
ISC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, maxPosition, minPosition

ISC_SetTriggerSwitches = lib.ISC_SetTriggerSwitches
ISC_SetTriggerSwitches.restype = c_short
ISC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_byte]
# *serialNo, indicatorBits

ISC_SetVelParams = lib.ISC_SetVelParams
ISC_SetVelParams.restype = c_short
ISC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, acceleration, maxVelocity

ISC_SetVelParamsBlock = lib.ISC_SetVelParamsBlock
ISC_SetVelParamsBlock.restype = c_short
ISC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
# *serialNo, *velocityParams

ISC_StartPolling = lib.ISC_StartPolling
ISC_StartPolling.restype = c_bool
ISC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

ISC_StopImmediate = lib.ISC_StopImmediate
ISC_StopImmediate.restype = c_short
ISC_StopImmediate.argtypes = [POINTER(c_char)]
# *serialNo

ISC_StopPolling = lib.ISC_StopPolling
ISC_StopPolling.restype = None
ISC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

ISC_StopProfiled = lib.ISC_StopProfiled
ISC_StopProfiled.restype = c_short
ISC_StopProfiled.argtypes = [POINTER(c_char)]
# *serialNo

ISC_TimeSinceLastMsgReceived = lib.ISC_TimeSinceLastMsgReceived
ISC_TimeSinceLastMsgReceived.restype = c_bool
ISC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

ISC_WaitForMessage = lib.ISC_WaitForMessage
ISC_WaitForMessage.restype = c_bool
ISC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
