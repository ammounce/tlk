from c_types import (
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


class IntegratedStepperMotor(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.IntegratedStepperMotors.DLL")

        self.ISC_CanHome = self.lib.ISC_CanHome
        self.ISC_CanHome.restype = c_bool
        self.ISC_CanHome.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_CanMoveWithoutHomingFirst = self.lib.ISC_CanMoveWithoutHomingFirst
        self.ISC_CanMoveWithoutHomingFirst.restype = c_bool
        self.ISC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_CheckConnection = self.lib.ISC_CheckConnection
        self.ISC_CheckConnection.restype = c_bool
        self.ISC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_ClearMessageQueue = self.lib.ISC_ClearMessageQueue
        self.ISC_ClearMessageQueue.restype = None
        self.ISC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_Close = self.lib.ISC_Close
        self.ISC_Close.restype = None
        self.ISC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_DisableChannel = self.lib.ISC_DisableChannel
        self.ISC_DisableChannel.restype = c_short
        self.ISC_DisableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_EnableChannel = self.lib.ISC_EnableChannel
        self.ISC_EnableChannel.restype = c_short
        self.ISC_EnableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_EnableLastMsgTimer = self.lib.ISC_EnableLastMsgTimer
        self.ISC_EnableLastMsgTimer.restype = None
        self.ISC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.ISC_GetBacklash = self.lib.ISC_GetBacklash
        self.ISC_GetBacklash.restype = c_long
        self.ISC_GetBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetBowIndex = self.lib.ISC_GetBowIndex
        self.ISC_GetBowIndex.restype = c_short
        self.ISC_GetBowIndex.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetButtonParams = self.lib.ISC_GetButtonParams
        self.ISC_GetButtonParams.restype = c_short
        self.ISC_GetButtonParams.argtypes = [MOT_ButtonModes, c_int, c_int, POINTER(c_char), c_short]
        # *buttonMode, *leftButtonPosition, *rightButtonPosition, *serialNo, *timeout

        self.ISC_GetButtonParamsBlock = self.lib.ISC_GetButtonParamsBlock
        self.ISC_GetButtonParamsBlock.restype = c_short
        self.ISC_GetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
        # *buttonParams, *serialNo

        self.ISC_GetCalibrationFile = self.lib.ISC_GetCalibrationFile
        self.ISC_GetCalibrationFile.restype = c_bool
        self.ISC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *filename, *serialNo, sizeOfBuffer

        self.ISC_GetDeviceUnitFromRealValue = self.lib.ISC_GetDeviceUnitFromRealValue
        self.ISC_GetDeviceUnitFromRealValue.restype = c_short
        self.ISC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
        # *device_unit, *serialNo, real_unit, unitType

        self.ISC_GetFirmwareVersion = self.lib.ISC_GetFirmwareVersion
        self.ISC_GetFirmwareVersion.restype = c_ulong
        self.ISC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetHardwareInfo = self.lib.ISC_GetHardwareInfo
        self.ISC_GetHardwareInfo.restype = c_short
        self.ISC_GetHardwareInfo.argtypes = [
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

        self.ISC_GetHardwareInfoBlock = self.lib.ISC_GetHardwareInfoBlock
        self.ISC_GetHardwareInfoBlock.restype = c_short
        self.ISC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.ISC_GetHomingParamsBlock = self.lib.ISC_GetHomingParamsBlock
        self.ISC_GetHomingParamsBlock.restype = c_short
        self.ISC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.ISC_GetHomingVelocity = self.lib.ISC_GetHomingVelocity
        self.ISC_GetHomingVelocity.restype = c_uint
        self.ISC_GetHomingVelocity.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetJogMode = self.lib.ISC_GetJogMode
        self.ISC_GetJogMode.restype = c_short
        self.ISC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
        # *mode, *serialNo, *stopMode

        self.ISC_GetJogParamsBlock = self.lib.ISC_GetJogParamsBlock
        self.ISC_GetJogParamsBlock.restype = c_short
        self.ISC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.ISC_GetJogStepSize = self.lib.ISC_GetJogStepSize
        self.ISC_GetJogStepSize.restype = c_uint
        self.ISC_GetJogStepSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetJogVelParams = self.lib.ISC_GetJogVelParams
        self.ISC_GetJogVelParams.restype = c_short
        self.ISC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.ISC_GetLEDswitches = self.lib.ISC_GetLEDswitches
        self.ISC_GetLEDswitches.restype = c_long
        self.ISC_GetLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetLimitSwitchParams = self.lib.ISC_GetLimitSwitchParams
        self.ISC_GetLimitSwitchParams.restype = c_short
        self.ISC_GetLimitSwitchParams.argtypes = [MOT_LimitSwitchModes, c_uint,
                                                  MOT_LimitSwitchModes, c_uint, POINTER(c_char), MOT_LimitSwitchSWModes]
        # *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode

        self.ISC_GetLimitSwitchParamsBlock = self.lib.ISC_GetLimitSwitchParamsBlock
        self.ISC_GetLimitSwitchParamsBlock.restype = c_short
        self.ISC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
        # *limitSwitchParams, *serialNo

        self.ISC_GetMotorParams = self.lib.ISC_GetMotorParams
        self.ISC_GetMotorParams.restype = c_short
        self.ISC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.ISC_GetMotorParamsExt = self.lib.ISC_GetMotorParamsExt
        self.ISC_GetMotorParamsExt.restype = c_short
        self.ISC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.ISC_GetMotorTravelLimits = self.lib.ISC_GetMotorTravelLimits
        self.ISC_GetMotorTravelLimits.restype = c_short
        self.ISC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxPosition, *minPosition, *serialNo

        self.ISC_GetMotorTravelMode = self.lib.ISC_GetMotorTravelMode
        self.ISC_GetMotorTravelMode.restype = MOT_TravelModes
        self.ISC_GetMotorTravelMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetMotorVelocityLimits = self.lib.ISC_GetMotorVelocityLimits
        self.ISC_GetMotorVelocityLimits.restype = c_short
        self.ISC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxAcceleration, *maxVelocity, *serialNo

        self.ISC_GetMoveAbsolutePosition = self.lib.ISC_GetMoveAbsolutePosition
        self.ISC_GetMoveAbsolutePosition.restype = c_int
        self.ISC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetMoveRelativeDistance = self.lib.ISC_GetMoveRelativeDistance
        self.ISC_GetMoveRelativeDistance.restype = c_int
        self.ISC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetNextMessage = self.lib.ISC_GetNextMessage
        self.ISC_GetNextMessage.restype = c_bool
        self.ISC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.ISC_GetNumberPositions = self.lib.ISC_GetNumberPositions
        self.ISC_GetNumberPositions.restype = c_int
        self.ISC_GetNumberPositions.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetPosition = self.lib.ISC_GetPosition
        self.ISC_GetPosition.restype = c_int
        self.ISC_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetPositionCounter = self.lib.ISC_GetPositionCounter
        self.ISC_GetPositionCounter.restype = c_long
        self.ISC_GetPositionCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetPotentiometerParams = self.lib.ISC_GetPotentiometerParams
        self.ISC_GetPotentiometerParams.restype = c_short
        self.ISC_GetPotentiometerParams.argtypes = [POINTER(c_char), c_long, c_ulong, c_short]
        # *serialNo, *thresholdDeflection, *velocity, index

        self.ISC_GetPotentiometerParamsBlock = self.lib.ISC_GetPotentiometerParamsBlock
        self.ISC_GetPotentiometerParamsBlock.restype = c_short
        self.ISC_GetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
        # *potentiometerSteps, *serialNo

        self.ISC_GetPowerParams = self.lib.ISC_GetPowerParams
        self.ISC_GetPowerParams.restype = c_short
        self.ISC_GetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char)]
        # *powerParams, *serialNo

        self.ISC_GetRealValueFromDeviceUnit = self.lib.ISC_GetRealValueFromDeviceUnit
        self.ISC_GetRealValueFromDeviceUnit.restype = c_short
        self.ISC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
        # *real_unit, *serialNo, device_unit, unitType

        self.ISC_GetSoftLimitMode = self.lib.ISC_GetSoftLimitMode
        self.ISC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
        self.ISC_GetSoftLimitMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetSoftwareVersion = self.lib.ISC_GetSoftwareVersion
        self.ISC_GetSoftwareVersion.restype = c_ulong
        self.ISC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetStageAxisMaxPos = self.lib.ISC_GetStageAxisMaxPos
        self.ISC_GetStageAxisMaxPos.restype = c_int
        self.ISC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetStageAxisMinPos = self.lib.ISC_GetStageAxisMinPos
        self.ISC_GetStageAxisMinPos.restype = c_int
        self.ISC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetStatusBits = self.lib.ISC_GetStatusBits
        self.ISC_GetStatusBits.restype = c_ulong
        self.ISC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetTriggerSwitches = self.lib.ISC_GetTriggerSwitches
        self.ISC_GetTriggerSwitches.restype = c_byte
        self.ISC_GetTriggerSwitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_GetVelParams = self.lib.ISC_GetVelParams
        self.ISC_GetVelParams.restype = c_short
        self.ISC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.ISC_GetVelParamsBlock = self.lib.ISC_GetVelParamsBlock
        self.ISC_GetVelParamsBlock.restype = c_short
        self.ISC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.ISC_HasLastMsgTimerOverrun = self.lib.ISC_HasLastMsgTimerOverrun
        self.ISC_HasLastMsgTimerOverrun.restype = c_bool
        self.ISC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_Home = self.lib.ISC_Home
        self.ISC_Home.restype = c_short
        self.ISC_Home.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_Identify = self.lib.ISC_Identify
        self.ISC_Identify.restype = None
        self.ISC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_IsCalibrationActive = self.lib.ISC_IsCalibrationActive
        self.ISC_IsCalibrationActive.restype = c_bool
        self.ISC_IsCalibrationActive.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_LoadNamedSettings = self.lib.ISC_LoadNamedSettings
        self.ISC_LoadNamedSettings.restype = c_bool
        self.ISC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.ISC_LoadSettings = self.lib.ISC_LoadSettings
        self.ISC_LoadSettings.restype = c_bool
        self.ISC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_MessageQueueSize = self.lib.ISC_MessageQueueSize
        self.ISC_MessageQueueSize.restype = c_int
        self.ISC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_MoveAbsolute = self.lib.ISC_MoveAbsolute
        self.ISC_MoveAbsolute.restype = c_short
        self.ISC_MoveAbsolute.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_MoveAtVelocity = self.lib.ISC_MoveAtVelocity
        self.ISC_MoveAtVelocity.restype = c_short
        self.ISC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, direction

        self.ISC_MoveJog = self.lib.ISC_MoveJog
        self.ISC_MoveJog.restype = c_short
        self.ISC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, jogDirection

        self.ISC_MoveRelative = self.lib.ISC_MoveRelative
        self.ISC_MoveRelative.restype = c_short
        self.ISC_MoveRelative.argtypes = [POINTER(c_char), c_int]
        # *serialNo, displacement

        self.ISC_MoveRelativeDistance = self.lib.ISC_MoveRelativeDistance
        self.ISC_MoveRelativeDistance.restype = c_short
        self.ISC_MoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_MoveToPosition = self.lib.ISC_MoveToPosition
        self.ISC_MoveToPosition.restype = c_short
        self.ISC_MoveToPosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, index

        self.ISC_NeedsHoming = self.lib.ISC_NeedsHoming
        self.ISC_NeedsHoming.restype = c_bool
        self.ISC_NeedsHoming.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_Open = self.lib.ISC_Open
        self.ISC_Open.restype = c_short
        self.ISC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_PersistSettings = self.lib.ISC_PersistSettings
        self.ISC_PersistSettings.restype = c_bool
        self.ISC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_PollingDuration = self.lib.ISC_PollingDuration
        self.ISC_PollingDuration.restype = c_long
        self.ISC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RegisterMessageCallback = self.lib.ISC_RegisterMessageCallback
        self.ISC_RegisterMessageCallback.restype = None
        self.ISC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.ISC_RequestBacklash = self.lib.ISC_RequestBacklash
        self.ISC_RequestBacklash.restype = c_short
        self.ISC_RequestBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestBowIndex = self.lib.ISC_RequestBowIndex
        self.ISC_RequestBowIndex.restype = c_short
        self.ISC_RequestBowIndex.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestButtonParams = self.lib.ISC_RequestButtonParams
        self.ISC_RequestButtonParams.restype = c_short
        self.ISC_RequestButtonParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestHomingParams = self.lib.ISC_RequestHomingParams
        self.ISC_RequestHomingParams.restype = c_short
        self.ISC_RequestHomingParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestJogParams = self.lib.ISC_RequestJogParams
        self.ISC_RequestJogParams.restype = c_short
        self.ISC_RequestJogParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestLimitSwitchParams = self.lib.ISC_RequestLimitSwitchParams
        self.ISC_RequestLimitSwitchParams.restype = c_short
        self.ISC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestMoveAbsolutePosition = self.lib.ISC_RequestMoveAbsolutePosition
        self.ISC_RequestMoveAbsolutePosition.restype = c_short
        self.ISC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestMoveRelativeDistance = self.lib.ISC_RequestMoveRelativeDistance
        self.ISC_RequestMoveRelativeDistance.restype = c_short
        self.ISC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestPosition = self.lib.ISC_RequestPosition
        self.ISC_RequestPosition.restype = c_short
        self.ISC_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestPotentiometerParams = self.lib.ISC_RequestPotentiometerParams
        self.ISC_RequestPotentiometerParams.restype = c_short
        self.ISC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestPowerParams = self.lib.ISC_RequestPowerParams
        self.ISC_RequestPowerParams.restype = c_short
        self.ISC_RequestPowerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestSettings = self.lib.ISC_RequestSettings
        self.ISC_RequestSettings.restype = c_short
        self.ISC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestStatus = self.lib.ISC_RequestStatus
        self.ISC_RequestStatus.restype = c_short
        self.ISC_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestStatusBits = self.lib.ISC_RequestStatusBits
        self.ISC_RequestStatusBits.restype = c_short
        self.ISC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestTriggerSwitches = self.lib.ISC_RequestTriggerSwitches
        self.ISC_RequestTriggerSwitches.restype = c_short
        self.ISC_RequestTriggerSwitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_RequestVelParams = self.lib.ISC_RequestVelParams
        self.ISC_RequestVelParams.restype = c_short
        self.ISC_RequestVelParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_ResetRotationModes = self.lib.ISC_ResetRotationModes
        self.ISC_ResetRotationModes.restype = c_short
        self.ISC_ResetRotationModes.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_ResetStageToDefaults = self.lib.ISC_ResetStageToDefaults
        self.ISC_ResetStageToDefaults.restype = c_short
        self.ISC_ResetStageToDefaults.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_SetBacklash = self.lib.ISC_SetBacklash
        self.ISC_SetBacklash.restype = c_short
        self.ISC_SetBacklash.argtypes = [POINTER(c_char), c_long]
        # *serialNo, distance

        self.ISC_SetBowIndex = self.lib.ISC_SetBowIndex
        self.ISC_SetBowIndex.restype = c_short
        self.ISC_SetBowIndex.argtypes = [POINTER(c_char), c_short]
        # *serialNo, bowIndex

        self.ISC_SetButtonParams = self.lib.ISC_SetButtonParams
        self.ISC_SetButtonParams.restype = c_short
        self.ISC_SetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int]
        # *serialNo, buttonMode, leftButtonPosition, rightButtonPosition

        self.ISC_SetButtonParamsBlock = self.lib.ISC_SetButtonParamsBlock
        self.ISC_SetButtonParamsBlock.restype = c_short
        self.ISC_SetButtonParamsBlock.argtypes = [MOT_ButtonParameters, POINTER(c_char)]
        # *buttonParams, *serialNo

        self.ISC_SetCalibrationFile = self.lib.ISC_SetCalibrationFile
        self.ISC_SetCalibrationFile.restype = None
        self.ISC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_bool]
        # *filename, *serialNo, enabled

        self.ISC_SetDirection = self.lib.ISC_SetDirection
        self.ISC_SetDirection.restype = None
        self.ISC_SetDirection.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, reverse

        self.ISC_SetHomingParamsBlock = self.lib.ISC_SetHomingParamsBlock
        self.ISC_SetHomingParamsBlock.restype = c_short
        self.ISC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.ISC_SetHomingVelocity = self.lib.ISC_SetHomingVelocity
        self.ISC_SetHomingVelocity.restype = c_short
        self.ISC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, velocity

        self.ISC_SetJogMode = self.lib.ISC_SetJogMode
        self.ISC_SetJogMode.restype = c_short
        self.ISC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
        # *serialNo, mode, stopMode

        self.ISC_SetJogParamsBlock = self.lib.ISC_SetJogParamsBlock
        self.ISC_SetJogParamsBlock.restype = c_short
        self.ISC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.ISC_SetJogStepSize = self.lib.ISC_SetJogStepSize
        self.ISC_SetJogStepSize.restype = c_short
        self.ISC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, stepSize

        self.ISC_SetJogVelParams = self.lib.ISC_SetJogVelParams
        self.ISC_SetJogVelParams.restype = c_short
        self.ISC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.ISC_SetLEDswitches = self.lib.ISC_SetLEDswitches
        self.ISC_SetLEDswitches.restype = c_short
        self.ISC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
        # *serialNo, LEDswitches

        self.ISC_SetLimitSwitchParams = self.lib.ISC_SetLimitSwitchParams
        self.ISC_SetLimitSwitchParams.restype = c_short
        self.ISC_SetLimitSwitchParams.argtypes = [
            POINTER(c_char),
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchSWModes]
        # *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, clockwiseHardwareLimit, clockwisePosition, softLimitMode

        self.ISC_SetLimitSwitchParamsBlock = self.lib.ISC_SetLimitSwitchParamsBlock
        self.ISC_SetLimitSwitchParamsBlock.restype = c_short
        self.ISC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
        # *limitSwitchParams, *serialNo

        self.ISC_SetLimitsSoftwareApproachPolicy = self.lib.ISC_SetLimitsSoftwareApproachPolicy
        self.ISC_SetLimitsSoftwareApproachPolicy.restype = None
        self.ISC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
        # *serialNo, limitsSoftwareApproachPolicy

        self.ISC_SetMotorParams = self.lib.ISC_SetMotorParams
        self.ISC_SetMotorParams.restype = c_short
        self.ISC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.ISC_SetMotorParamsExt = self.lib.ISC_SetMotorParamsExt
        self.ISC_SetMotorParamsExt.restype = c_short
        self.ISC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.ISC_SetMotorTravelLimits = self.lib.ISC_SetMotorTravelLimits
        self.ISC_SetMotorTravelLimits.restype = c_short
        self.ISC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxPosition, minPosition

        self.ISC_SetMotorTravelMode = self.lib.ISC_SetMotorTravelMode
        self.ISC_SetMotorTravelMode.restype = c_short
        self.ISC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
        # *serialNo, travelMode

        self.ISC_SetMotorVelocityLimits = self.lib.ISC_SetMotorVelocityLimits
        self.ISC_SetMotorVelocityLimits.restype = c_short
        self.ISC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxAcceleration, maxVelocity

        self.ISC_SetMoveAbsolutePosition = self.lib.ISC_SetMoveAbsolutePosition
        self.ISC_SetMoveAbsolutePosition.restype = c_short
        self.ISC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, position

        self.ISC_SetMoveRelativeDistance = self.lib.ISC_SetMoveRelativeDistance
        self.ISC_SetMoveRelativeDistance.restype = c_short
        self.ISC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
        # *serialNo, distance

        self.ISC_SetPositionCounter = self.lib.ISC_SetPositionCounter
        self.ISC_SetPositionCounter.restype = c_short
        self.ISC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.ISC_SetPotentiometerParams = self.lib.ISC_SetPotentiometerParams
        self.ISC_SetPotentiometerParams.restype = c_short
        self.ISC_SetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]
        # *serialNo, index, thresholdDeflection, velocity

        self.ISC_SetPotentiometerParamsBlock = self.lib.ISC_SetPotentiometerParamsBlock
        self.ISC_SetPotentiometerParamsBlock.restype = c_short
        self.ISC_SetPotentiometerParamsBlock.argtypes = [MOT_PotentiometerSteps, POINTER(c_char)]
        # *potentiometerSteps, *serialNo

        self.ISC_SetPowerParams = self.lib.ISC_SetPowerParams
        self.ISC_SetPowerParams.restype = c_short
        self.ISC_SetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char)]
        # *powerParams, *serialNo

        self.ISC_SetRotationModes = self.lib.ISC_SetRotationModes
        self.ISC_SetRotationModes.restype = c_short
        self.ISC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementDirections, MOT_MovementModes]
        # *serialNo, direction, mode

        self.ISC_SetStageAxisLimits = self.lib.ISC_SetStageAxisLimits
        self.ISC_SetStageAxisLimits.restype = c_short
        self.ISC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, maxPosition, minPosition

        self.ISC_SetTriggerSwitches = self.lib.ISC_SetTriggerSwitches
        self.ISC_SetTriggerSwitches.restype = c_short
        self.ISC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, indicatorBits

        self.ISC_SetVelParams = self.lib.ISC_SetVelParams
        self.ISC_SetVelParams.restype = c_short
        self.ISC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.ISC_SetVelParamsBlock = self.lib.ISC_SetVelParamsBlock
        self.ISC_SetVelParamsBlock.restype = c_short
        self.ISC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.ISC_StartPolling = self.lib.ISC_StartPolling
        self.ISC_StartPolling.restype = c_bool
        self.ISC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.ISC_StopImmediate = self.lib.ISC_StopImmediate
        self.ISC_StopImmediate.restype = c_short
        self.ISC_StopImmediate.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_StopPolling = self.lib.ISC_StopPolling
        self.ISC_StopPolling.restype = None
        self.ISC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_StopProfiled = self.lib.ISC_StopProfiled
        self.ISC_StopProfiled.restype = c_short
        self.ISC_StopProfiled.argtypes = [POINTER(c_char)]
        # *serialNo

        self.ISC_TimeSinceLastMsgReceived = self.lib.ISC_TimeSinceLastMsgReceived
        self.ISC_TimeSinceLastMsgReceived.restype = c_bool
        self.ISC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.ISC_WaitForMessage = self.lib.ISC_WaitForMessage
        self.ISC_WaitForMessage.restype = c_bool
        self.ISC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
