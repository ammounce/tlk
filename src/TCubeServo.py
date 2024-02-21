from c_types import (
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
    MOT_DC_PIDParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_PotentiometerSteps,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class TCubeServo(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.TCube.DCServo.DLL")

        self.CC_CanHome = self.lib.CC_CanHome
        self.CC_CanHome.restype = c_bool
        self.CC_CanHome.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_CanMoveWithoutHomingFirst = self.lib.CC_CanMoveWithoutHomingFirst
        self.CC_CanMoveWithoutHomingFirst.restype = c_bool
        self.CC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_CheckConnection = self.lib.CC_CheckConnection
        self.CC_CheckConnection.restype = c_bool
        self.CC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_ClearMessageQueue = self.lib.CC_ClearMessageQueue
        self.CC_ClearMessageQueue.restype = None
        self.CC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_Close = self.lib.CC_Close
        self.CC_Close.restype = None
        self.CC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_DisableChannel = self.lib.CC_DisableChannel
        self.CC_DisableChannel.restype = c_short
        self.CC_DisableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_EnableChannel = self.lib.CC_EnableChannel
        self.CC_EnableChannel.restype = c_short
        self.CC_EnableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_EnableLastMsgTimer = self.lib.CC_EnableLastMsgTimer
        self.CC_EnableLastMsgTimer.restype = None
        self.CC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.CC_GetBacklash = self.lib.CC_GetBacklash
        self.CC_GetBacklash.restype = c_long
        self.CC_GetBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetButtonParams = self.lib.CC_GetButtonParams
        self.CC_GetButtonParams.restype = c_short
        self.CC_GetButtonParams.argtypes = [MOT_ButtonModes, c_int, c_int, POINTER(c_char), c_short]
        # *buttonMode, *leftButtonPosition, *rightButtonPosition, *serialNo, *timeout

        self.CC_GetButtonParamsBlock = self.lib.CC_GetButtonParamsBlock
        self.CC_GetButtonParamsBlock.restype = c_short
        self.CC_GetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
        # *buttonParams, *serialNo

        self.CC_GetDCPIDParams = self.lib.CC_GetDCPIDParams
        self.CC_GetDCPIDParams.restype = c_short
        self.CC_GetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
        # *DCproportionalIntegralDerivativeParams, *serialNo

        self.CC_GetDeviceUnitFromRealValue = self.lib.CC_GetDeviceUnitFromRealValue
        self.CC_GetDeviceUnitFromRealValue.restype = c_short
        self.CC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
        # *device_unit, *serialNo, real_unit, unitType

        self.CC_GetEncoderCounter = self.lib.CC_GetEncoderCounter
        self.CC_GetEncoderCounter.restype = c_long
        self.CC_GetEncoderCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetHardwareInfo = self.lib.CC_GetHardwareInfo
        self.CC_GetHardwareInfo.restype = c_short
        self.CC_GetHardwareInfo.argtypes = [
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

        self.CC_GetHardwareInfoBlock = self.lib.CC_GetHardwareInfoBlock
        self.CC_GetHardwareInfoBlock.restype = c_short
        self.CC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.CC_GetHomingParamsBlock = self.lib.CC_GetHomingParamsBlock
        self.CC_GetHomingParamsBlock.restype = c_short
        self.CC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.CC_GetHomingVelocity = self.lib.CC_GetHomingVelocity
        self.CC_GetHomingVelocity.restype = c_uint
        self.CC_GetHomingVelocity.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetHubBay = self.lib.CC_GetHubBay
        self.CC_GetHubBay.restype = POINTER(c_char)
        self.CC_GetHubBay.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetJogMode = self.lib.CC_GetJogMode
        self.CC_GetJogMode.restype = c_short
        self.CC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
        # *mode, *serialNo, *stopMode

        self.CC_GetJogParamsBlock = self.lib.CC_GetJogParamsBlock
        self.CC_GetJogParamsBlock.restype = c_short
        self.CC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.CC_GetJogStepSize = self.lib.CC_GetJogStepSize
        self.CC_GetJogStepSize.restype = c_uint
        self.CC_GetJogStepSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetJogVelParams = self.lib.CC_GetJogVelParams
        self.CC_GetJogVelParams.restype = c_short
        self.CC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.CC_GetLEDswitches = self.lib.CC_GetLEDswitches
        self.CC_GetLEDswitches.restype = c_long
        self.CC_GetLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetLimitSwitchParams = self.lib.CC_GetLimitSwitchParams
        self.CC_GetLimitSwitchParams.restype = c_short
        self.CC_GetLimitSwitchParams.argtypes = [MOT_LimitSwitchModes, c_uint,
                                                 MOT_LimitSwitchModes, c_uint, POINTER(c_char), MOT_LimitSwitchSWModes]
        # *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode

        self.CC_GetLimitSwitchParamsBlock = self.lib.CC_GetLimitSwitchParamsBlock
        self.CC_GetLimitSwitchParamsBlock.restype = c_short
        self.CC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
        # *limitSwitchParams, *serialNo

        self.CC_GetMotorParams = self.lib.CC_GetMotorParams
        self.CC_GetMotorParams.restype = c_short
        self.CC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.CC_GetMotorParamsExt = self.lib.CC_GetMotorParamsExt
        self.CC_GetMotorParamsExt.restype = c_short
        self.CC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.CC_GetMotorTravelLimits = self.lib.CC_GetMotorTravelLimits
        self.CC_GetMotorTravelLimits.restype = c_short
        self.CC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxPosition, *minPosition, *serialNo

        self.CC_GetMotorTravelMode = self.lib.CC_GetMotorTravelMode
        self.CC_GetMotorTravelMode.restype = MOT_TravelModes
        self.CC_GetMotorTravelMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetMotorVelocityLimits = self.lib.CC_GetMotorVelocityLimits
        self.CC_GetMotorVelocityLimits.restype = c_short
        self.CC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxAcceleration, *maxVelocity, *serialNo

        self.CC_GetMoveAbsolutePosition = self.lib.CC_GetMoveAbsolutePosition
        self.CC_GetMoveAbsolutePosition.restype = c_int
        self.CC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetMoveRelativeDistance = self.lib.CC_GetMoveRelativeDistance
        self.CC_GetMoveRelativeDistance.restype = c_int
        self.CC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetNextMessage = self.lib.CC_GetNextMessage
        self.CC_GetNextMessage.restype = c_bool
        self.CC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.CC_GetNumberPositions = self.lib.CC_GetNumberPositions
        self.CC_GetNumberPositions.restype = c_int
        self.CC_GetNumberPositions.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetPosition = self.lib.CC_GetPosition
        self.CC_GetPosition.restype = c_int
        self.CC_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetPositionCounter = self.lib.CC_GetPositionCounter
        self.CC_GetPositionCounter.restype = c_long
        self.CC_GetPositionCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetPotentiometerParams = self.lib.CC_GetPotentiometerParams
        self.CC_GetPotentiometerParams.restype = c_short
        self.CC_GetPotentiometerParams.argtypes = [POINTER(c_char), c_long, c_ulong, c_short]
        # *serialNo, *thresholdDeflection, *velocity, index

        self.CC_GetPotentiometerParamsBlock = self.lib.CC_GetPotentiometerParamsBlock
        self.CC_GetPotentiometerParamsBlock.restype = c_short
        self.CC_GetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
        # *potentiometerSteps, *serialNo

        self.CC_GetRealValueFromDeviceUnit = self.lib.CC_GetRealValueFromDeviceUnit
        self.CC_GetRealValueFromDeviceUnit.restype = c_short
        self.CC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
        # *real_unit, *serialNo, device_unit, unitType

        self.CC_GetSoftLimitMode = self.lib.CC_GetSoftLimitMode
        self.CC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
        self.CC_GetSoftLimitMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetSoftwareVersion = self.lib.CC_GetSoftwareVersion
        self.CC_GetSoftwareVersion.restype = c_ulong
        self.CC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetStageAxisMaxPos = self.lib.CC_GetStageAxisMaxPos
        self.CC_GetStageAxisMaxPos.restype = c_int
        self.CC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetStageAxisMinPos = self.lib.CC_GetStageAxisMinPos
        self.CC_GetStageAxisMinPos.restype = c_int
        self.CC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetStatusBits = self.lib.CC_GetStatusBits
        self.CC_GetStatusBits.restype = c_ulong
        self.CC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_GetVelParams = self.lib.CC_GetVelParams
        self.CC_GetVelParams.restype = c_short
        self.CC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.CC_GetVelParamsBlock = self.lib.CC_GetVelParamsBlock
        self.CC_GetVelParamsBlock.restype = c_short
        self.CC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.CC_HasLastMsgTimerOverrun = self.lib.CC_HasLastMsgTimerOverrun
        self.CC_HasLastMsgTimerOverrun.restype = c_bool
        self.CC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_Home = self.lib.CC_Home
        self.CC_Home.restype = c_short
        self.CC_Home.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_Identify = self.lib.CC_Identify
        self.CC_Identify.restype = None
        self.CC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_LoadNamedSettings = self.lib.CC_LoadNamedSettings
        self.CC_LoadNamedSettings.restype = c_bool
        self.CC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.CC_LoadSettings = self.lib.CC_LoadSettings
        self.CC_LoadSettings.restype = c_bool
        self.CC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_MessageQueueSize = self.lib.CC_MessageQueueSize
        self.CC_MessageQueueSize.restype = c_int
        self.CC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_MoveAbsolute = self.lib.CC_MoveAbsolute
        self.CC_MoveAbsolute.restype = c_short
        self.CC_MoveAbsolute.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_MoveAtVelocity = self.lib.CC_MoveAtVelocity
        self.CC_MoveAtVelocity.restype = c_short
        self.CC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, direction

        self.CC_MoveJog = self.lib.CC_MoveJog
        self.CC_MoveJog.restype = c_short
        self.CC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, jogDirection

        self.CC_MoveRelative = self.lib.CC_MoveRelative
        self.CC_MoveRelative.restype = c_short
        self.CC_MoveRelative.argtypes = [POINTER(c_char), c_int]
        # *serialNo, displacement

        self.CC_MoveRelativeDistance = self.lib.CC_MoveRelativeDistance
        self.CC_MoveRelativeDistance.restype = c_short
        self.CC_MoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_MoveToPosition = self.lib.CC_MoveToPosition
        self.CC_MoveToPosition.restype = c_short
        self.CC_MoveToPosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, index

        self.CC_NeedsHoming = self.lib.CC_NeedsHoming
        self.CC_NeedsHoming.restype = c_bool
        self.CC_NeedsHoming.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_Open = self.lib.CC_Open
        self.CC_Open.restype = c_short
        self.CC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_PersistSettings = self.lib.CC_PersistSettings
        self.CC_PersistSettings.restype = c_bool
        self.CC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_PollingDuration = self.lib.CC_PollingDuration
        self.CC_PollingDuration.restype = c_long
        self.CC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RegisterMessageCallback = self.lib.CC_RegisterMessageCallback
        self.CC_RegisterMessageCallback.restype = None
        self.CC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.CC_RequestBacklash = self.lib.CC_RequestBacklash
        self.CC_RequestBacklash.restype = c_short
        self.CC_RequestBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestButtonParams = self.lib.CC_RequestButtonParams
        self.CC_RequestButtonParams.restype = c_short
        self.CC_RequestButtonParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestDCPIDParams = self.lib.CC_RequestDCPIDParams
        self.CC_RequestDCPIDParams.restype = c_short
        self.CC_RequestDCPIDParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestEncoderCounter = self.lib.CC_RequestEncoderCounter
        self.CC_RequestEncoderCounter.restype = c_short
        self.CC_RequestEncoderCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestHomingParams = self.lib.CC_RequestHomingParams
        self.CC_RequestHomingParams.restype = c_short
        self.CC_RequestHomingParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestJogParams = self.lib.CC_RequestJogParams
        self.CC_RequestJogParams.restype = c_short
        self.CC_RequestJogParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestLEDswitches = self.lib.CC_RequestLEDswitches
        self.CC_RequestLEDswitches.restype = c_short
        self.CC_RequestLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestLimitSwitchParams = self.lib.CC_RequestLimitSwitchParams
        self.CC_RequestLimitSwitchParams.restype = c_short
        self.CC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestMoveAbsolutePosition = self.lib.CC_RequestMoveAbsolutePosition
        self.CC_RequestMoveAbsolutePosition.restype = c_short
        self.CC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestMoveRelativeDistance = self.lib.CC_RequestMoveRelativeDistance
        self.CC_RequestMoveRelativeDistance.restype = c_short
        self.CC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestPosition = self.lib.CC_RequestPosition
        self.CC_RequestPosition.restype = c_short
        self.CC_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestPotentiometerParams = self.lib.CC_RequestPotentiometerParams
        self.CC_RequestPotentiometerParams.restype = c_short
        self.CC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestSettings = self.lib.CC_RequestSettings
        self.CC_RequestSettings.restype = c_short
        self.CC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestStatusBits = self.lib.CC_RequestStatusBits
        self.CC_RequestStatusBits.restype = c_short
        self.CC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_RequestVelParams = self.lib.CC_RequestVelParams
        self.CC_RequestVelParams.restype = c_short
        self.CC_RequestVelParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_ResetRotationModes = self.lib.CC_ResetRotationModes
        self.CC_ResetRotationModes.restype = c_short
        self.CC_ResetRotationModes.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_ResumeMoveMessages = self.lib.CC_ResumeMoveMessages
        self.CC_ResumeMoveMessages.restype = c_short
        self.CC_ResumeMoveMessages.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_SetBacklash = self.lib.CC_SetBacklash
        self.CC_SetBacklash.restype = c_short
        self.CC_SetBacklash.argtypes = [POINTER(c_char), c_long]
        # *serialNo, distance

        self.CC_SetButtonParams = self.lib.CC_SetButtonParams
        self.CC_SetButtonParams.restype = c_short
        self.CC_SetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int]
        # *serialNo, buttonMode, leftButtonPosition, rightButtonPosition

        self.CC_SetButtonParamsBlock = self.lib.CC_SetButtonParamsBlock
        self.CC_SetButtonParamsBlock.restype = c_short
        self.CC_SetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
        # *buttonParams, *serialNo

        self.CC_SetDCPIDParams = self.lib.CC_SetDCPIDParams
        self.CC_SetDCPIDParams.restype = c_short
        self.CC_SetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
        # *DCproportionalIntegralDerivativeParams, *serialNo

        self.CC_SetDirection = self.lib.CC_SetDirection
        self.CC_SetDirection.restype = None
        self.CC_SetDirection.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, reverse

        self.CC_SetEncoderCounter = self.lib.CC_SetEncoderCounter
        self.CC_SetEncoderCounter.restype = c_short
        self.CC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.CC_SetHomingParamsBlock = self.lib.CC_SetHomingParamsBlock
        self.CC_SetHomingParamsBlock.restype = c_short
        self.CC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.CC_SetHomingVelocity = self.lib.CC_SetHomingVelocity
        self.CC_SetHomingVelocity.restype = c_short
        self.CC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, velocity

        self.CC_SetJogMode = self.lib.CC_SetJogMode
        self.CC_SetJogMode.restype = c_short
        self.CC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
        # *serialNo, mode, stopMode

        self.CC_SetJogParamsBlock = self.lib.CC_SetJogParamsBlock
        self.CC_SetJogParamsBlock.restype = c_short
        self.CC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.CC_SetJogStepSize = self.lib.CC_SetJogStepSize
        self.CC_SetJogStepSize.restype = c_short
        self.CC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, stepSize

        self.CC_SetJogVelParams = self.lib.CC_SetJogVelParams
        self.CC_SetJogVelParams.restype = c_short
        self.CC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.CC_SetLEDswitches = self.lib.CC_SetLEDswitches
        self.CC_SetLEDswitches.restype = c_short
        self.CC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
        # *serialNo, LEDswitches

        self.CC_SetLimitSwitchParams = self.lib.CC_SetLimitSwitchParams
        self.CC_SetLimitSwitchParams.restype = c_short
        self.CC_SetLimitSwitchParams.argtypes = [
            POINTER(c_char),
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchSWModes]
        # *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, clockwiseHardwareLimit, clockwisePosition, softLimitMode

        self.CC_SetLimitSwitchParamsBlock = self.lib.CC_SetLimitSwitchParamsBlock
        self.CC_SetLimitSwitchParamsBlock.restype = c_short
        self.CC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
        # *limitSwitchParams, *serialNo

        self.CC_SetLimitsSoftwareApproachPolicy = self.lib.CC_SetLimitsSoftwareApproachPolicy
        self.CC_SetLimitsSoftwareApproachPolicy.restype = None
        self.CC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
        # *serialNo, limitsSoftwareApproachPolicy

        self.CC_SetMotorParams = self.lib.CC_SetMotorParams
        self.CC_SetMotorParams.restype = c_short
        self.CC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.CC_SetMotorParamsExt = self.lib.CC_SetMotorParamsExt
        self.CC_SetMotorParamsExt.restype = c_short
        self.CC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.CC_SetMotorTravelLimits = self.lib.CC_SetMotorTravelLimits
        self.CC_SetMotorTravelLimits.restype = c_short
        self.CC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxPosition, minPosition

        self.CC_SetMotorTravelMode = self.lib.CC_SetMotorTravelMode
        self.CC_SetMotorTravelMode.restype = c_short
        self.CC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
        # *serialNo, travelMode

        self.CC_SetMotorVelocityLimits = self.lib.CC_SetMotorVelocityLimits
        self.CC_SetMotorVelocityLimits.restype = c_short
        self.CC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxAcceleration, maxVelocity

        self.CC_SetMoveAbsolutePosition = self.lib.CC_SetMoveAbsolutePosition
        self.CC_SetMoveAbsolutePosition.restype = c_short
        self.CC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, position

        self.CC_SetMoveRelativeDistance = self.lib.CC_SetMoveRelativeDistance
        self.CC_SetMoveRelativeDistance.restype = c_short
        self.CC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
        # *serialNo, distance

        self.CC_SetPositionCounter = self.lib.CC_SetPositionCounter
        self.CC_SetPositionCounter.restype = c_short
        self.CC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.CC_SetPotentiometerParams = self.lib.CC_SetPotentiometerParams
        self.CC_SetPotentiometerParams.restype = c_short
        self.CC_SetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]
        # *serialNo, index, thresholdDeflection, velocity

        self.CC_SetPotentiometerParamsBlock = self.lib.CC_SetPotentiometerParamsBlock
        self.CC_SetPotentiometerParamsBlock.restype = c_short
        self.CC_SetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
        # *potentiometerSteps, *serialNo

        self.CC_SetRotationModes = self.lib.CC_SetRotationModes
        self.CC_SetRotationModes.restype = c_short
        self.CC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementDirections, MOT_MovementModes]
        # *serialNo, direction, mode

        self.CC_SetStageAxisLimits = self.lib.CC_SetStageAxisLimits
        self.CC_SetStageAxisLimits.restype = c_short
        self.CC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, maxPosition, minPosition

        self.CC_SetVelParams = self.lib.CC_SetVelParams
        self.CC_SetVelParams.restype = c_short
        self.CC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.CC_SetVelParamsBlock = self.lib.CC_SetVelParamsBlock
        self.CC_SetVelParamsBlock.restype = c_short
        self.CC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.CC_StartPolling = self.lib.CC_StartPolling
        self.CC_StartPolling.restype = c_bool
        self.CC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.CC_StopImmediate = self.lib.CC_StopImmediate
        self.CC_StopImmediate.restype = c_short
        self.CC_StopImmediate.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_StopPolling = self.lib.CC_StopPolling
        self.CC_StopPolling.restype = None
        self.CC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_StopProfiled = self.lib.CC_StopProfiled
        self.CC_StopProfiled.restype = c_short
        self.CC_StopProfiled.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_SuspendMoveMessages = self.lib.CC_SuspendMoveMessages
        self.CC_SuspendMoveMessages.restype = c_short
        self.CC_SuspendMoveMessages.argtypes = [POINTER(c_char)]
        # *serialNo

        self.CC_TimeSinceLastMsgReceived = self.lib.CC_TimeSinceLastMsgReceived
        self.CC_TimeSinceLastMsgReceived.restype = c_bool
        self.CC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.CC_WaitForMessage = self.lib.CC_WaitForMessage
        self.CC_WaitForMessage.restype = c_bool
        self.CC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
