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
from pathlib import Path


class TCubeStepperMotor(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.TCube.StepperMotor.DLL")

        self.SCC_CanHome = self.lib.SCC_CanHome
        self.SCC_CanHome.restype = c_bool
        self.SCC_CanHome.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_CanMoveWithoutHomingFirst = self.lib.SCC_CanMoveWithoutHomingFirst
        self.SCC_CanMoveWithoutHomingFirst.restype = c_bool
        self.SCC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_CheckConnection = self.lib.SCC_CheckConnection
        self.SCC_CheckConnection.restype = c_bool
        self.SCC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_ClearMessageQueue = self.lib.SCC_ClearMessageQueue
        self.SCC_ClearMessageQueue.restype = None
        self.SCC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_Close = self.lib.SCC_Close
        self.SCC_Close.restype = None
        self.SCC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_DisableChannel = self.lib.SCC_DisableChannel
        self.SCC_DisableChannel.restype = c_short
        self.SCC_DisableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_EnableChannel = self.lib.SCC_EnableChannel
        self.SCC_EnableChannel.restype = c_short
        self.SCC_EnableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_EnableLastMsgTimer = self.lib.SCC_EnableLastMsgTimer
        self.SCC_EnableLastMsgTimer.restype = None
        self.SCC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.SCC_GetBacklash = self.lib.SCC_GetBacklash
        self.SCC_GetBacklash.restype = c_long
        self.SCC_GetBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetBowIndex = self.lib.SCC_GetBowIndex
        self.SCC_GetBowIndex.restype = c_short
        self.SCC_GetBowIndex.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetButtonParams = self.lib.SCC_GetButtonParams
        self.SCC_GetButtonParams.restype = c_short
        self.SCC_GetButtonParams.argtypes = [MOT_ButtonModes, c_int, c_int, POINTER(c_char), c_short]
        # *buttonMode, *leftButtonPosition, *rightButtonPosition, *serialNo, *timeout

        self.SCC_GetButtonParamsBlock = self.lib.SCC_GetButtonParamsBlock
        self.SCC_GetButtonParamsBlock.restype = c_short
        self.SCC_GetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
        # *buttonParams, *serialNo

        self.SCC_GetCalibrationFile = self.lib.SCC_GetCalibrationFile
        self.SCC_GetCalibrationFile.restype = c_bool
        self.SCC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *filename, *serialNo, sizeOfBuffer

        self.SCC_GetDeviceUnitFromRealValue = self.lib.SCC_GetDeviceUnitFromRealValue
        self.SCC_GetDeviceUnitFromRealValue.restype = c_short
        self.SCC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
        # *device_unit, *serialNo, real_unit, unitType

        self.SCC_GetEncoderCounter = self.lib.SCC_GetEncoderCounter
        self.SCC_GetEncoderCounter.restype = c_long
        self.SCC_GetEncoderCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetHardwareInfo = self.lib.SCC_GetHardwareInfo
        self.SCC_GetHardwareInfo.restype = c_short
        self.SCC_GetHardwareInfo.argtypes = [
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

        self.SCC_GetHardwareInfoBlock = self.lib.SCC_GetHardwareInfoBlock
        self.SCC_GetHardwareInfoBlock.restype = c_short
        self.SCC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.SCC_GetHomingParamsBlock = self.lib.SCC_GetHomingParamsBlock
        self.SCC_GetHomingParamsBlock.restype = c_short
        self.SCC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.SCC_GetHomingVelocity = self.lib.SCC_GetHomingVelocity
        self.SCC_GetHomingVelocity.restype = c_uint
        self.SCC_GetHomingVelocity.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetHubBay = self.lib.SCC_GetHubBay
        self.SCC_GetHubBay.restype = POINTER(c_char)
        self.SCC_GetHubBay.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetJogMode = self.lib.SCC_GetJogMode
        self.SCC_GetJogMode.restype = c_short
        self.SCC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
        # *mode, *serialNo, *stopMode

        self.SCC_GetJogParamsBlock = self.lib.SCC_GetJogParamsBlock
        self.SCC_GetJogParamsBlock.restype = c_short
        self.SCC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.SCC_GetJogStepSize = self.lib.SCC_GetJogStepSize
        self.SCC_GetJogStepSize.restype = c_uint
        self.SCC_GetJogStepSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetJogVelParams = self.lib.SCC_GetJogVelParams
        self.SCC_GetJogVelParams.restype = c_short
        self.SCC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.SCC_GetLEDswitches = self.lib.SCC_GetLEDswitches
        self.SCC_GetLEDswitches.restype = c_long
        self.SCC_GetLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetLimitSwitchParams = self.lib.SCC_GetLimitSwitchParams
        self.SCC_GetLimitSwitchParams.restype = c_short
        self.SCC_GetLimitSwitchParams.argtypes = [MOT_LimitSwitchModes, c_uint,
                                                  MOT_LimitSwitchModes, c_uint, POINTER(c_char), MOT_LimitSwitchSWModes]
        # *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode

        self.SCC_GetLimitSwitchParamsBlock = self.lib.SCC_GetLimitSwitchParamsBlock
        self.SCC_GetLimitSwitchParamsBlock.restype = c_short
        self.SCC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
        # *limitSwitchParams, *serialNo

        self.SCC_GetMotorParams = self.lib.SCC_GetMotorParams
        self.SCC_GetMotorParams.restype = c_short
        self.SCC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.SCC_GetMotorParamsExt = self.lib.SCC_GetMotorParamsExt
        self.SCC_GetMotorParamsExt.restype = c_short
        self.SCC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.SCC_GetMotorTravelLimits = self.lib.SCC_GetMotorTravelLimits
        self.SCC_GetMotorTravelLimits.restype = c_short
        self.SCC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxPosition, *minPosition, *serialNo

        self.SCC_GetMotorTravelMode = self.lib.SCC_GetMotorTravelMode
        self.SCC_GetMotorTravelMode.restype = MOT_TravelModes
        self.SCC_GetMotorTravelMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetMotorVelocityLimits = self.lib.SCC_GetMotorVelocityLimits
        self.SCC_GetMotorVelocityLimits.restype = c_short
        self.SCC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxAcceleration, *maxVelocity, *serialNo

        self.SCC_GetMoveAbsolutePosition = self.lib.SCC_GetMoveAbsolutePosition
        self.SCC_GetMoveAbsolutePosition.restype = c_int
        self.SCC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetMoveRelativeDistance = self.lib.SCC_GetMoveRelativeDistance
        self.SCC_GetMoveRelativeDistance.restype = c_int
        self.SCC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetNextMessage = self.lib.SCC_GetNextMessage
        self.SCC_GetNextMessage.restype = c_bool
        self.SCC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.SCC_GetNumberPositions = self.lib.SCC_GetNumberPositions
        self.SCC_GetNumberPositions.restype = c_int
        self.SCC_GetNumberPositions.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetPosition = self.lib.SCC_GetPosition
        self.SCC_GetPosition.restype = c_int
        self.SCC_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetPositionCounter = self.lib.SCC_GetPositionCounter
        self.SCC_GetPositionCounter.restype = c_long
        self.SCC_GetPositionCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetPotentiometerParams = self.lib.SCC_GetPotentiometerParams
        self.SCC_GetPotentiometerParams.restype = c_short
        self.SCC_GetPotentiometerParams.argtypes = [POINTER(c_char), c_long, c_ulong, c_short]
        # *serialNo, *thresholdDeflection, *velocity, index

        self.SCC_GetPotentiometerParamsBlock = self.lib.SCC_GetPotentiometerParamsBlock
        self.SCC_GetPotentiometerParamsBlock.restype = c_short
        self.SCC_GetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
        # *potentiometerSteps, *serialNo

        self.SCC_GetPowerParams = self.lib.SCC_GetPowerParams
        self.SCC_GetPowerParams.restype = c_short
        self.SCC_GetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char)]
        # *powerParams, *serialNo

        self.SCC_GetRealValueFromDeviceUnit = self.lib.SCC_GetRealValueFromDeviceUnit
        self.SCC_GetRealValueFromDeviceUnit.restype = c_short
        self.SCC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
        # *real_unit, *serialNo, device_unit, unitType

        self.SCC_GetSoftLimitMode = self.lib.SCC_GetSoftLimitMode
        self.SCC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
        self.SCC_GetSoftLimitMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetSoftwareVersion = self.lib.SCC_GetSoftwareVersion
        self.SCC_GetSoftwareVersion.restype = c_ulong
        self.SCC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetStageAxisMaxPos = self.lib.SCC_GetStageAxisMaxPos
        self.SCC_GetStageAxisMaxPos.restype = c_int
        self.SCC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetStageAxisMinPos = self.lib.SCC_GetStageAxisMinPos
        self.SCC_GetStageAxisMinPos.restype = c_int
        self.SCC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetStatusBits = self.lib.SCC_GetStatusBits
        self.SCC_GetStatusBits.restype = c_ulong
        self.SCC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_GetVelParams = self.lib.SCC_GetVelParams
        self.SCC_GetVelParams.restype = c_short
        self.SCC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.SCC_GetVelParamsBlock = self.lib.SCC_GetVelParamsBlock
        self.SCC_GetVelParamsBlock.restype = c_short
        self.SCC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.SCC_HasLastMsgTimerOverrun = self.lib.SCC_HasLastMsgTimerOverrun
        self.SCC_HasLastMsgTimerOverrun.restype = c_bool
        self.SCC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_Home = self.lib.SCC_Home
        self.SCC_Home.restype = c_short
        self.SCC_Home.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_Identify = self.lib.SCC_Identify
        self.SCC_Identify.restype = None
        self.SCC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_IsCalibrationActive = self.lib.SCC_IsCalibrationActive
        self.SCC_IsCalibrationActive.restype = c_bool
        self.SCC_IsCalibrationActive.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_LoadNamedSettings = self.lib.SCC_LoadNamedSettings
        self.SCC_LoadNamedSettings.restype = c_bool
        self.SCC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.SCC_LoadSettings = self.lib.SCC_LoadSettings
        self.SCC_LoadSettings.restype = c_bool
        self.SCC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_MessageQueueSize = self.lib.SCC_MessageQueueSize
        self.SCC_MessageQueueSize.restype = c_int
        self.SCC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_MoveAbsolute = self.lib.SCC_MoveAbsolute
        self.SCC_MoveAbsolute.restype = c_short
        self.SCC_MoveAbsolute.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_MoveAtVelocity = self.lib.SCC_MoveAtVelocity
        self.SCC_MoveAtVelocity.restype = c_short
        self.SCC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, direction

        self.SCC_MoveJog = self.lib.SCC_MoveJog
        self.SCC_MoveJog.restype = c_short
        self.SCC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, jogDirection

        self.SCC_MoveRelative = self.lib.SCC_MoveRelative
        self.SCC_MoveRelative.restype = c_short
        self.SCC_MoveRelative.argtypes = [POINTER(c_char), c_int]
        # *serialNo, displacement

        self.SCC_MoveRelativeDistance = self.lib.SCC_MoveRelativeDistance
        self.SCC_MoveRelativeDistance.restype = c_short
        self.SCC_MoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_MoveToPosition = self.lib.SCC_MoveToPosition
        self.SCC_MoveToPosition.restype = c_short
        self.SCC_MoveToPosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, index

        self.SCC_NeedsHoming = self.lib.SCC_NeedsHoming
        self.SCC_NeedsHoming.restype = c_bool
        self.SCC_NeedsHoming.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_Open = self.lib.SCC_Open
        self.SCC_Open.restype = c_short
        self.SCC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_PersistSettings = self.lib.SCC_PersistSettings
        self.SCC_PersistSettings.restype = c_bool
        self.SCC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_PollingDuration = self.lib.SCC_PollingDuration
        self.SCC_PollingDuration.restype = c_long
        self.SCC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RegisterMessageCallback = self.lib.SCC_RegisterMessageCallback
        self.SCC_RegisterMessageCallback.restype = None
        self.SCC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.SCC_RequestBacklash = self.lib.SCC_RequestBacklash
        self.SCC_RequestBacklash.restype = c_short
        self.SCC_RequestBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestBowIndex = self.lib.SCC_RequestBowIndex
        self.SCC_RequestBowIndex.restype = c_short
        self.SCC_RequestBowIndex.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestButtonParams = self.lib.SCC_RequestButtonParams
        self.SCC_RequestButtonParams.restype = c_short
        self.SCC_RequestButtonParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestEncoderCounter = self.lib.SCC_RequestEncoderCounter
        self.SCC_RequestEncoderCounter.restype = c_short
        self.SCC_RequestEncoderCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestHomingParams = self.lib.SCC_RequestHomingParams
        self.SCC_RequestHomingParams.restype = c_short
        self.SCC_RequestHomingParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestJogParams = self.lib.SCC_RequestJogParams
        self.SCC_RequestJogParams.restype = c_short
        self.SCC_RequestJogParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestLEDswitches = self.lib.SCC_RequestLEDswitches
        self.SCC_RequestLEDswitches.restype = c_short
        self.SCC_RequestLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestLimitSwitchParams = self.lib.SCC_RequestLimitSwitchParams
        self.SCC_RequestLimitSwitchParams.restype = c_short
        self.SCC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestMoveAbsolutePosition = self.lib.SCC_RequestMoveAbsolutePosition
        self.SCC_RequestMoveAbsolutePosition.restype = c_short
        self.SCC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestMoveRelativeDistance = self.lib.SCC_RequestMoveRelativeDistance
        self.SCC_RequestMoveRelativeDistance.restype = c_short
        self.SCC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestPosition = self.lib.SCC_RequestPosition
        self.SCC_RequestPosition.restype = c_short
        self.SCC_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestPotentiometerParams = self.lib.SCC_RequestPotentiometerParams
        self.SCC_RequestPotentiometerParams.restype = c_short
        self.SCC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestPowerParams = self.lib.SCC_RequestPowerParams
        self.SCC_RequestPowerParams.restype = c_short
        self.SCC_RequestPowerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestSettings = self.lib.SCC_RequestSettings
        self.SCC_RequestSettings.restype = c_short
        self.SCC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestStatusBits = self.lib.SCC_RequestStatusBits
        self.SCC_RequestStatusBits.restype = c_short
        self.SCC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_RequestVelParams = self.lib.SCC_RequestVelParams
        self.SCC_RequestVelParams.restype = c_short
        self.SCC_RequestVelParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_ResetRotationModes = self.lib.SCC_ResetRotationModes
        self.SCC_ResetRotationModes.restype = c_short
        self.SCC_ResetRotationModes.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_ResumeMoveMessages = self.lib.SCC_ResumeMoveMessages
        self.SCC_ResumeMoveMessages.restype = c_short
        self.SCC_ResumeMoveMessages.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_SetBacklash = self.lib.SCC_SetBacklash
        self.SCC_SetBacklash.restype = c_short
        self.SCC_SetBacklash.argtypes = [POINTER(c_char), c_long]
        # *serialNo, distance

        self.SCC_SetBowIndex = self.lib.SCC_SetBowIndex
        self.SCC_SetBowIndex.restype = c_short
        self.SCC_SetBowIndex.argtypes = [POINTER(c_char), c_short]
        # *serialNo, bowIndex

        self.SCC_SetButtonParams = self.lib.SCC_SetButtonParams
        self.SCC_SetButtonParams.restype = c_short
        self.SCC_SetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int]
        # *serialNo, buttonMode, leftButtonPosition, rightButtonPosition

        self.SCC_SetButtonParamsBlock = self.lib.SCC_SetButtonParamsBlock
        self.SCC_SetButtonParamsBlock.restype = c_short
        self.SCC_SetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
        # *buttonParams, *serialNo

        self.SCC_SetCalibrationFile = self.lib.SCC_SetCalibrationFile
        self.SCC_SetCalibrationFile.restype = None
        self.SCC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_bool]
        # *filename, *serialNo, enabled

        self.SCC_SetDirection = self.lib.SCC_SetDirection
        self.SCC_SetDirection.restype = None
        self.SCC_SetDirection.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, reverse

        self.SCC_SetEncoderCounter = self.lib.SCC_SetEncoderCounter
        self.SCC_SetEncoderCounter.restype = c_short
        self.SCC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.SCC_SetHomingParamsBlock = self.lib.SCC_SetHomingParamsBlock
        self.SCC_SetHomingParamsBlock.restype = c_short
        self.SCC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.SCC_SetHomingVelocity = self.lib.SCC_SetHomingVelocity
        self.SCC_SetHomingVelocity.restype = c_short
        self.SCC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, velocity

        self.SCC_SetJogMode = self.lib.SCC_SetJogMode
        self.SCC_SetJogMode.restype = c_short
        self.SCC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
        # *serialNo, mode, stopMode

        self.SCC_SetJogParamsBlock = self.lib.SCC_SetJogParamsBlock
        self.SCC_SetJogParamsBlock.restype = c_short
        self.SCC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.SCC_SetJogStepSize = self.lib.SCC_SetJogStepSize
        self.SCC_SetJogStepSize.restype = c_short
        self.SCC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, stepSize

        self.SCC_SetJogVelParams = self.lib.SCC_SetJogVelParams
        self.SCC_SetJogVelParams.restype = c_short
        self.SCC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.SCC_SetLEDswitches = self.lib.SCC_SetLEDswitches
        self.SCC_SetLEDswitches.restype = c_short
        self.SCC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
        # *serialNo, LEDswitches

        self.SCC_SetLimitSwitchParams = self.lib.SCC_SetLimitSwitchParams
        self.SCC_SetLimitSwitchParams.restype = c_short
        self.SCC_SetLimitSwitchParams.argtypes = [
            POINTER(c_char),
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchSWModes]
        # *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, clockwiseHardwareLimit, clockwisePosition, softLimitMode

        self.SCC_SetLimitSwitchParamsBlock = self.lib.SCC_SetLimitSwitchParamsBlock
        self.SCC_SetLimitSwitchParamsBlock.restype = c_short
        self.SCC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
        # *limitSwitchParams, *serialNo

        self.SCC_SetLimitsSoftwareApproachPolicy = self.lib.SCC_SetLimitsSoftwareApproachPolicy
        self.SCC_SetLimitsSoftwareApproachPolicy.restype = None
        self.SCC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
        # *serialNo, limitsSoftwareApproachPolicy

        self.SCC_SetMotorParams = self.lib.SCC_SetMotorParams
        self.SCC_SetMotorParams.restype = c_short
        self.SCC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.SCC_SetMotorParamsExt = self.lib.SCC_SetMotorParamsExt
        self.SCC_SetMotorParamsExt.restype = c_short
        self.SCC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.SCC_SetMotorTravelLimits = self.lib.SCC_SetMotorTravelLimits
        self.SCC_SetMotorTravelLimits.restype = c_short
        self.SCC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxPosition, minPosition

        self.SCC_SetMotorTravelMode = self.lib.SCC_SetMotorTravelMode
        self.SCC_SetMotorTravelMode.restype = c_short
        self.SCC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
        # *serialNo, travelMode

        self.SCC_SetMotorVelocityLimits = self.lib.SCC_SetMotorVelocityLimits
        self.SCC_SetMotorVelocityLimits.restype = c_short
        self.SCC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxAcceleration, maxVelocity

        self.SCC_SetMoveAbsolutePosition = self.lib.SCC_SetMoveAbsolutePosition
        self.SCC_SetMoveAbsolutePosition.restype = c_short
        self.SCC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, position

        self.SCC_SetMoveRelativeDistance = self.lib.SCC_SetMoveRelativeDistance
        self.SCC_SetMoveRelativeDistance.restype = c_short
        self.SCC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
        # *serialNo, distance

        self.SCC_SetPositionCounter = self.lib.SCC_SetPositionCounter
        self.SCC_SetPositionCounter.restype = c_short
        self.SCC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.SCC_SetPotentiometerParams = self.lib.SCC_SetPotentiometerParams
        self.SCC_SetPotentiometerParams.restype = c_short
        self.SCC_SetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]
        # *serialNo, index, thresholdDeflection, velocity

        self.SCC_SetPotentiometerParamsBlock = self.lib.SCC_SetPotentiometerParamsBlock
        self.SCC_SetPotentiometerParamsBlock.restype = c_short
        self.SCC_SetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
        # *potentiometerSteps, *serialNo

        self.SCC_SetPowerParams = self.lib.SCC_SetPowerParams
        self.SCC_SetPowerParams.restype = c_short
        self.SCC_SetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char)]
        # *powerParams, *serialNo

        self.SCC_SetRotationModes = self.lib.SCC_SetRotationModes
        self.SCC_SetRotationModes.restype = c_short
        self.SCC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementDirections, MOT_MovementModes]
        # *serialNo, direction, mode

        self.SCC_SetStageAxisLimits = self.lib.SCC_SetStageAxisLimits
        self.SCC_SetStageAxisLimits.restype = c_short
        self.SCC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, maxPosition, minPosition

        self.SCC_SetStageType = self.lib.SCC_SetStageType
        self.SCC_SetStageType.restype = c_short
        self.SCC_SetStageType.argtypes = [POINTER(c_char), KST_Stages, TST_Stages]
        # *serialNo, stageId, stageId

        self.SCC_SetVelParams = self.lib.SCC_SetVelParams
        self.SCC_SetVelParams.restype = c_short
        self.SCC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.SCC_SetVelParamsBlock = self.lib.SCC_SetVelParamsBlock
        self.SCC_SetVelParamsBlock.restype = c_short
        self.SCC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.SCC_StartPolling = self.lib.SCC_StartPolling
        self.SCC_StartPolling.restype = c_bool
        self.SCC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.SCC_StopImmediate = self.lib.SCC_StopImmediate
        self.SCC_StopImmediate.restype = c_short
        self.SCC_StopImmediate.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_StopPolling = self.lib.SCC_StopPolling
        self.SCC_StopPolling.restype = None
        self.SCC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_StopProfiled = self.lib.SCC_StopProfiled
        self.SCC_StopProfiled.restype = c_short
        self.SCC_StopProfiled.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_SuspendMoveMessages = self.lib.SCC_SuspendMoveMessages
        self.SCC_SuspendMoveMessages.restype = c_short
        self.SCC_SuspendMoveMessages.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SCC_TimeSinceLastMsgReceived = self.lib.SCC_TimeSinceLastMsgReceived
        self.SCC_TimeSinceLastMsgReceived.restype = c_bool
        self.SCC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.SCC_WaitForMessage = self.lib.SCC_WaitForMessage
        self.SCC_WaitForMessage.restype = c_bool
        self.SCC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
