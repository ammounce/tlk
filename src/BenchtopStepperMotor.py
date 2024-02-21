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
from pathlib import Path


class BenchtopStepperMotor(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.Benchtop.StepperMotor.dll")

        self.SBC_CanHome = self.lib.SBC_CanHome
        self.SBC_CanHome.restype = c_bool
        self.SBC_CanHome.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_CanMoveWithoutHomingFirst = self.lib.SBC_CanMoveWithoutHomingFirst
        self.SBC_CanMoveWithoutHomingFirst.restype = c_bool
        self.SBC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_CheckConnection = self.lib.SBC_CheckConnection
        self.SBC_CheckConnection.restype = c_bool
        self.SBC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_ClearMessageQueue = self.lib.SBC_ClearMessageQueue
        self.SBC_ClearMessageQueue.restype = c_short
        self.SBC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_Close = self.lib.SBC_Close
        self.SBC_Close.restype = c_short
        self.SBC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_DisableChannel = self.lib.SBC_DisableChannel
        self.SBC_DisableChannel.restype = c_short
        self.SBC_DisableChannel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_EnableChannel = self.lib.SBC_EnableChannel
        self.SBC_EnableChannel.restype = c_short
        self.SBC_EnableChannel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_EnableLastMsgTimer = self.lib.SBC_EnableLastMsgTimer
        self.SBC_EnableLastMsgTimer.restype = None
        self.SBC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]
        # *serialNo, channel, enable, lastMsgTimeout

        self.SBC_GetBacklash = self.lib.SBC_GetBacklash
        self.SBC_GetBacklash.restype = c_long
        self.SBC_GetBacklash.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetBowIndex = self.lib.SBC_GetBowIndex
        self.SBC_GetBowIndex.restype = c_short
        self.SBC_GetBowIndex.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetCalibrationFile = self.lib.SBC_GetCalibrationFile
        self.SBC_GetCalibrationFile.restype = c_bool
        self.SBC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short, c_short]
        # *filename, *serialNo, channel, sizeOfBuffer

        self.SBC_GetDeviceUnitFromRealValue = self.lib.SBC_GetDeviceUnitFromRealValue
        self.SBC_GetDeviceUnitFromRealValue.restype = c_short
        self.SBC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_short, c_double, c_int]
        # *device_unit, *serialNo, channel, real_unit, unitType

        self.SBC_GetDigitalOutputs = self.lib.SBC_GetDigitalOutputs
        self.SBC_GetDigitalOutputs.restype = c_byte
        self.SBC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetEncoderCounter = self.lib.SBC_GetEncoderCounter
        self.SBC_GetEncoderCounter.restype = c_long
        self.SBC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetFirmwareVersion = self.lib.SBC_GetFirmwareVersion
        self.SBC_GetFirmwareVersion.restype = c_ulong
        self.SBC_GetFirmwareVersion.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetHardwareInfo = self.lib.SBC_GetHardwareInfo
        self.SBC_GetHardwareInfo.restype = c_short
        self.SBC_GetHardwareInfo.argtypes = [
            c_ulong,
            c_long,
            POINTER(c_char),
            c_long,
            POINTER(c_char),
            c_long,
            POINTER(c_char),
            c_long,
            c_short,
            c_ulong,
            c_ulong]
        # *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numChannels, *serialNo, *type, channel, sizeOfModelNo, sizeOfNotes

        self.SBC_GetHardwareInfoBlock = self.lib.SBC_GetHardwareInfoBlock
        self.SBC_GetHardwareInfoBlock.restype = c_short
        self.SBC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char), c_short]
        # *hardwareInfo, *serialNo, channel

        self.SBC_GetHomingParamsBlock = self.lib.SBC_GetHomingParamsBlock
        self.SBC_GetHomingParamsBlock.restype = c_short
        self.SBC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), c_short]
        # *homingParams, *serialNo, channel

        self.SBC_GetHomingVelocity = self.lib.SBC_GetHomingVelocity
        self.SBC_GetHomingVelocity.restype = c_uint
        self.SBC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetInputVoltage = self.lib.SBC_GetInputVoltage
        self.SBC_GetInputVoltage.restype = c_long
        self.SBC_GetInputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetJogMode = self.lib.SBC_GetJogMode
        self.SBC_GetJogMode.restype = c_short
        self.SBC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes, c_short]
        # *mode, *serialNo, *stopMode, channel

        self.SBC_GetJogParamsBlock = self.lib.SBC_GetJogParamsBlock
        self.SBC_GetJogParamsBlock.restype = c_short
        self.SBC_GetJogParamsBlock.argtypes = [MOT_JogParameters, MOT_JogParameters, POINTER(c_char), c_short]
        # *jogParameters, *jogParams, *serialNo, channel

        self.SBC_GetJogStepSize = self.lib.SBC_GetJogStepSize
        self.SBC_GetJogStepSize.restype = c_uint
        self.SBC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetJogVelParams = self.lib.SBC_GetJogVelParams
        self.SBC_GetJogVelParams.restype = c_short
        self.SBC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
        # *acceleration, *maxVelocity, *serialNo, channel

        self.SBC_GetJoystickParams = self.lib.SBC_GetJoystickParams
        self.SBC_GetJoystickParams.restype = c_short
        self.SBC_GetJoystickParams.argtypes = [MOT_JoystickParameters, POINTER(c_char), c_short]
        # *joystickParams, *serialNo, channel

        self.SBC_GetLimitSwitchParams = self.lib.SBC_GetLimitSwitchParams
        self.SBC_GetLimitSwitchParams.restype = c_short
        self.SBC_GetLimitSwitchParams.argtypes = [
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchModes,
            c_uint,
            POINTER(c_char),
            MOT_LimitSwitchSWModes,
            c_short]
        # *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode, channel

        self.SBC_GetLimitSwitchParamsBlock = self.lib.SBC_GetLimitSwitchParamsBlock
        self.SBC_GetLimitSwitchParamsBlock.restype = c_short
        self.SBC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char), c_short]
        # *limitSwitchParams, *serialNo, channel

        self.SBC_GetMotorParams = self.lib.SBC_GetMotorParams
        self.SBC_GetMotorParams.restype = c_short
        self.SBC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long, c_short]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev, channel

        self.SBC_GetMotorParamsExt = self.lib.SBC_GetMotorParamsExt
        self.SBC_GetMotorParamsExt.restype = c_short
        self.SBC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double, c_short]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev, channel

        self.SBC_GetMotorTravelLimits = self.lib.SBC_GetMotorTravelLimits
        self.SBC_GetMotorTravelLimits.restype = c_short
        self.SBC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
        # *maxPosition, *minPosition, *serialNo, channel

        self.SBC_GetMotorTravelMode = self.lib.SBC_GetMotorTravelMode
        self.SBC_GetMotorTravelMode.restype = MOT_TravelModes
        self.SBC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetMotorVelocityLimits = self.lib.SBC_GetMotorVelocityLimits
        self.SBC_GetMotorVelocityLimits.restype = c_short
        self.SBC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
        # *maxAcceleration, *maxVelocity, *serialNo, channel

        self.SBC_GetMoveAbsolutePosition = self.lib.SBC_GetMoveAbsolutePosition
        self.SBC_GetMoveAbsolutePosition.restype = c_int
        self.SBC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetMoveRelativeDistance = self.lib.SBC_GetMoveRelativeDistance
        self.SBC_GetMoveRelativeDistance.restype = c_int
        self.SBC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetNextMessage = self.lib.SBC_GetNextMessage
        self.SBC_GetNextMessage.restype = c_bool
        self.SBC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
        # *messageData, *messageID, *messageType, *serialNo, channel

        self.SBC_GetNumChannels = self.lib.SBC_GetNumChannels
        self.SBC_GetNumChannels.restype = c_short
        self.SBC_GetNumChannels.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_GetNumberPositions = self.lib.SBC_GetNumberPositions
        self.SBC_GetNumberPositions.restype = c_int
        self.SBC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetPIDLoopEncoderCoeff = self.lib.SBC_GetPIDLoopEncoderCoeff
        self.SBC_GetPIDLoopEncoderCoeff.restype = c_double
        self.SBC_GetPIDLoopEncoderCoeff.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetPIDLoopEncoderParams = self.lib.SBC_GetPIDLoopEncoderParams
        self.SBC_GetPIDLoopEncoderParams.restype = c_short
        self.SBC_GetPIDLoopEncoderParams.argtypes = [MOT_PIDLoopEncoderParams, POINTER(c_char), c_short]
        # *params, *serialNo, channel

        self.SBC_GetPosition = self.lib.SBC_GetPosition
        self.SBC_GetPosition.restype = c_int
        self.SBC_GetPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetPositionCounter = self.lib.SBC_GetPositionCounter
        self.SBC_GetPositionCounter.restype = c_long
        self.SBC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetPowerParams = self.lib.SBC_GetPowerParams
        self.SBC_GetPowerParams.restype = c_short
        self.SBC_GetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char), c_short]
        # *powerParams, *serialNo, channel

        self.SBC_GetRackDigitalOutputs = self.lib.SBC_GetRackDigitalOutputs
        self.SBC_GetRackDigitalOutputs.restype = c_byte
        self.SBC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_GetRackStatusBits = self.lib.SBC_GetRackStatusBits
        self.SBC_GetRackStatusBits.restype = c_ulong
        self.SBC_GetRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_GetRealValueFromDeviceUnit = self.lib.SBC_GetRealValueFromDeviceUnit
        self.SBC_GetRealValueFromDeviceUnit.restype = c_short
        self.SBC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_short, c_int, c_int]
        # *real_unit, *serialNo, channel, device_unit, unitType

        self.SBC_GetSoftLimitMode = self.lib.SBC_GetSoftLimitMode
        self.SBC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
        self.SBC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetSoftwareVersion = self.lib.SBC_GetSoftwareVersion
        self.SBC_GetSoftwareVersion.restype = c_ulong
        self.SBC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_GetStageAxisMaxPos = self.lib.SBC_GetStageAxisMaxPos
        self.SBC_GetStageAxisMaxPos.restype = c_int
        self.SBC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetStageAxisMinPos = self.lib.SBC_GetStageAxisMinPos
        self.SBC_GetStageAxisMinPos.restype = c_int
        self.SBC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetStatusBits = self.lib.SBC_GetStatusBits
        self.SBC_GetStatusBits.restype = c_ulong
        self.SBC_GetStatusBits.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetTriggerSwitches = self.lib.SBC_GetTriggerSwitches
        self.SBC_GetTriggerSwitches.restype = c_byte
        self.SBC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_GetVelParams = self.lib.SBC_GetVelParams
        self.SBC_GetVelParams.restype = c_short
        self.SBC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
        # *acceleration, *maxVelocity, *serialNo, channel

        self.SBC_GetVelParamsBlock = self.lib.SBC_GetVelParamsBlock
        self.SBC_GetVelParamsBlock.restype = c_short
        self.SBC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters, MOT_VelocityParameters, c_short]
        # *serialNo, *velocityParameters, *velocityParams, channel

        self.SBC_HasLastMsgTimerOverrun = self.lib.SBC_HasLastMsgTimerOverrun
        self.SBC_HasLastMsgTimerOverrun.restype = c_bool
        self.SBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_Home = self.lib.SBC_Home
        self.SBC_Home.restype = c_short
        self.SBC_Home.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_Identify = self.lib.SBC_Identify
        self.SBC_Identify.restype = None
        self.SBC_Identify.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_IsCalibrationActive = self.lib.SBC_IsCalibrationActive
        self.SBC_IsCalibrationActive.restype = c_bool
        self.SBC_IsCalibrationActive.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_IsChannelValid = self.lib.SBC_IsChannelValid
        self.SBC_IsChannelValid.restype = c_bool
        self.SBC_IsChannelValid.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_LoadNamedSettings = self.lib.SBC_LoadNamedSettings
        self.SBC_LoadNamedSettings.restype = c_bool
        self.SBC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *serialNo, *settingsName, channel

        self.SBC_LoadSettings = self.lib.SBC_LoadSettings
        self.SBC_LoadSettings.restype = c_bool
        self.SBC_LoadSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_MaxChannelCount = self.lib.SBC_MaxChannelCount
        self.SBC_MaxChannelCount.restype = c_int
        self.SBC_MaxChannelCount.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_MessageQueueSize = self.lib.SBC_MessageQueueSize
        self.SBC_MessageQueueSize.restype = c_int
        self.SBC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_MoveAbsolute = self.lib.SBC_MoveAbsolute
        self.SBC_MoveAbsolute.restype = c_short
        self.SBC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_MoveAtVelocity = self.lib.SBC_MoveAtVelocity
        self.SBC_MoveAtVelocity.restype = c_short
        self.SBC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
        # *serialNo, channel, direction

        self.SBC_MoveJog = self.lib.SBC_MoveJog
        self.SBC_MoveJog.restype = c_short
        self.SBC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
        # *serialNo, channel, jogDirection

        self.SBC_MoveRelative = self.lib.SBC_MoveRelative
        self.SBC_MoveRelative.restype = c_short
        self.SBC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, displacement

        self.SBC_MoveRelativeDistance = self.lib.SBC_MoveRelativeDistance
        self.SBC_MoveRelativeDistance.restype = c_short
        self.SBC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_MoveToPosition = self.lib.SBC_MoveToPosition
        self.SBC_MoveToPosition.restype = c_short
        self.SBC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, index

        self.SBC_NeedsHoming = self.lib.SBC_NeedsHoming
        self.SBC_NeedsHoming.restype = c_bool
        self.SBC_NeedsHoming.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_Open = self.lib.SBC_Open
        self.SBC_Open.restype = c_short
        self.SBC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_PersistSettings = self.lib.SBC_PersistSettings
        self.SBC_PersistSettings.restype = c_bool
        self.SBC_PersistSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_PollingDuration = self.lib.SBC_PollingDuration
        self.SBC_PollingDuration.restype = c_long
        self.SBC_PollingDuration.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RegisterMessageCallback = self.lib.SBC_RegisterMessageCallback
        self.SBC_RegisterMessageCallback.restype = c_short
        self.SBC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, None]
        # *serialNo, channel, void

        self.SBC_RequestBacklash = self.lib.SBC_RequestBacklash
        self.SBC_RequestBacklash.restype = c_short
        self.SBC_RequestBacklash.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestBowIndex = self.lib.SBC_RequestBowIndex
        self.SBC_RequestBowIndex.restype = c_short
        self.SBC_RequestBowIndex.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestDigitalOutputs = self.lib.SBC_RequestDigitalOutputs
        self.SBC_RequestDigitalOutputs.restype = c_short
        self.SBC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestEncoderCounter = self.lib.SBC_RequestEncoderCounter
        self.SBC_RequestEncoderCounter.restype = c_short
        self.SBC_RequestEncoderCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestHomingParams = self.lib.SBC_RequestHomingParams
        self.SBC_RequestHomingParams.restype = c_short
        self.SBC_RequestHomingParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestInputVoltage = self.lib.SBC_RequestInputVoltage
        self.SBC_RequestInputVoltage.restype = c_short
        self.SBC_RequestInputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestJogParams = self.lib.SBC_RequestJogParams
        self.SBC_RequestJogParams.restype = c_short
        self.SBC_RequestJogParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestJoystickParams = self.lib.SBC_RequestJoystickParams
        self.SBC_RequestJoystickParams.restype = c_short
        self.SBC_RequestJoystickParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestLimitSwitchParams = self.lib.SBC_RequestLimitSwitchParams
        self.SBC_RequestLimitSwitchParams.restype = c_short
        self.SBC_RequestLimitSwitchParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestMoveAbsolutePosition = self.lib.SBC_RequestMoveAbsolutePosition
        self.SBC_RequestMoveAbsolutePosition.restype = c_short
        self.SBC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestMoveRelativeDistance = self.lib.SBC_RequestMoveRelativeDistance
        self.SBC_RequestMoveRelativeDistance.restype = c_short
        self.SBC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestPIDLoopEncoderParams = self.lib.SBC_RequestPIDLoopEncoderParams
        self.SBC_RequestPIDLoopEncoderParams.restype = c_short
        self.SBC_RequestPIDLoopEncoderParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestPosition = self.lib.SBC_RequestPosition
        self.SBC_RequestPosition.restype = c_short
        self.SBC_RequestPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestPowerParams = self.lib.SBC_RequestPowerParams
        self.SBC_RequestPowerParams.restype = c_short
        self.SBC_RequestPowerParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestRackDigitalOutputs = self.lib.SBC_RequestRackDigitalOutputs
        self.SBC_RequestRackDigitalOutputs.restype = c_short
        self.SBC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_RequestRackStatusBits = self.lib.SBC_RequestRackStatusBits
        self.SBC_RequestRackStatusBits.restype = c_short
        self.SBC_RequestRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SBC_RequestSettings = self.lib.SBC_RequestSettings
        self.SBC_RequestSettings.restype = c_short
        self.SBC_RequestSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestStatusBits = self.lib.SBC_RequestStatusBits
        self.SBC_RequestStatusBits.restype = c_short
        self.SBC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestTriggerSwitches = self.lib.SBC_RequestTriggerSwitches
        self.SBC_RequestTriggerSwitches.restype = c_short
        self.SBC_RequestTriggerSwitches.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_RequestVelParams = self.lib.SBC_RequestVelParams
        self.SBC_RequestVelParams.restype = c_short
        self.SBC_RequestVelParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_ResetRotationModes = self.lib.SBC_ResetRotationModes
        self.SBC_ResetRotationModes.restype = c_short
        self.SBC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_ResumeMoveMessages = self.lib.SBC_ResumeMoveMessages
        self.SBC_ResumeMoveMessages.restype = c_short
        self.SBC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_SetBacklash = self.lib.SBC_SetBacklash
        self.SBC_SetBacklash.restype = c_short
        self.SBC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, distance

        self.SBC_SetBowIndex = self.lib.SBC_SetBowIndex
        self.SBC_SetBowIndex.restype = c_short
        self.SBC_SetBowIndex.argtypes = [POINTER(c_char), c_short, c_short]
        # *serialNo, bowIndex, channel

        self.SBC_SetCalibrationFile = self.lib.SBC_SetCalibrationFile
        self.SBC_SetCalibrationFile.restype = None
        self.SBC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short, c_bool]
        # *filename, *serialNo, channel, enabled

        self.SBC_SetDigitalOutputs = self.lib.SBC_SetDigitalOutputs
        self.SBC_SetDigitalOutputs.restype = c_short
        self.SBC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]
        # *serialNo, channel, outputsBits

        self.SBC_SetDirection = self.lib.SBC_SetDirection
        self.SBC_SetDirection.restype = c_short
        self.SBC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]
        # *serialNo, channel, reverse

        self.SBC_SetEncoderCounter = self.lib.SBC_SetEncoderCounter
        self.SBC_SetEncoderCounter.restype = c_short
        self.SBC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, count

        self.SBC_SetHomingParamsBlock = self.lib.SBC_SetHomingParamsBlock
        self.SBC_SetHomingParamsBlock.restype = c_short
        self.SBC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), c_short]
        # *homingParams, *serialNo, channel

        self.SBC_SetHomingVelocity = self.lib.SBC_SetHomingVelocity
        self.SBC_SetHomingVelocity.restype = c_short
        self.SBC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]
        # *serialNo, channel, velocity

        self.SBC_SetJogMode = self.lib.SBC_SetJogMode
        self.SBC_SetJogMode.restype = c_short
        self.SBC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]
        # *serialNo, channel, mode, stopMode

        self.SBC_SetJogParamsBlock = self.lib.SBC_SetJogParamsBlock
        self.SBC_SetJogParamsBlock.restype = c_short
        self.SBC_SetJogParamsBlock.argtypes = [MOT_JogParameters, MOT_JogParameters, POINTER(c_char), c_short]
        # *jogParameters, *jogParams, *serialNo, channel

        self.SBC_SetJogStepSize = self.lib.SBC_SetJogStepSize
        self.SBC_SetJogStepSize.restype = c_short
        self.SBC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]
        # *serialNo, channel, stepSize

        self.SBC_SetJogVelParams = self.lib.SBC_SetJogVelParams
        self.SBC_SetJogVelParams.restype = c_short
        self.SBC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
        # *serialNo, acceleration, channel, maxVelocity

        self.SBC_SetJoystickParams = self.lib.SBC_SetJoystickParams
        self.SBC_SetJoystickParams.restype = c_short
        self.SBC_SetJoystickParams.argtypes = [MOT_JoystickParameters, POINTER(c_char), c_short]
        # *joystickParams, *serialNo, channel

        self.SBC_SetLimitSwitchParams = self.lib.SBC_SetLimitSwitchParams
        self.SBC_SetLimitSwitchParams.restype = c_short
        self.SBC_SetLimitSwitchParams.argtypes = [
            POINTER(c_char),
            MOT_LimitSwitchModes,
            c_uint,
            c_short,
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchSWModes]
        # *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, channel, clockwiseHardwareLimit, clockwisePosition, softLimitMode

        self.SBC_SetLimitSwitchParamsBlock = self.lib.SBC_SetLimitSwitchParamsBlock
        self.SBC_SetLimitSwitchParamsBlock.restype = c_short
        self.SBC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char), c_short]
        # *limitSwitchParams, *serialNo, channel

        self.SBC_SetLimitsSoftwareApproachPolicy = self.lib.SBC_SetLimitsSoftwareApproachPolicy
        self.SBC_SetLimitsSoftwareApproachPolicy.restype = None
        self.SBC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]
        # *serialNo, channel, limitsSoftwareApproachPolicy

        self.SBC_SetMotorParams = self.lib.SBC_SetMotorParams
        self.SBC_SetMotorParams.restype = c_short
        self.SBC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_float, c_long]
        # *serialNo, channel, gearBoxRatio, pitch, stepsPerRev

        self.SBC_SetMotorParamsExt = self.lib.SBC_SetMotorParamsExt
        self.SBC_SetMotorParamsExt.restype = c_short
        self.SBC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]
        # *serialNo, channel, gearBoxRatio, pitch, stepsPerRev

        self.SBC_SetMotorTravelLimits = self.lib.SBC_SetMotorTravelLimits
        self.SBC_SetMotorTravelLimits.restype = c_short
        self.SBC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
        # *serialNo, channel, maxPosition, minPosition

        self.SBC_SetMotorTravelMode = self.lib.SBC_SetMotorTravelMode
        self.SBC_SetMotorTravelMode.restype = c_short
        self.SBC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]
        # *serialNo, channel, travelMode

        self.SBC_SetMotorVelocityLimits = self.lib.SBC_SetMotorVelocityLimits
        self.SBC_SetMotorVelocityLimits.restype = c_short
        self.SBC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
        # *serialNo, channel, maxAcceleration, maxVelocity

        self.SBC_SetMoveAbsolutePosition = self.lib.SBC_SetMoveAbsolutePosition
        self.SBC_SetMoveAbsolutePosition.restype = c_short
        self.SBC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, position

        self.SBC_SetMoveRelativeDistance = self.lib.SBC_SetMoveRelativeDistance
        self.SBC_SetMoveRelativeDistance.restype = c_short
        self.SBC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, distance

        self.SBC_SetPIDLoopEncoderCoeff = self.lib.SBC_SetPIDLoopEncoderCoeff
        self.SBC_SetPIDLoopEncoderCoeff.restype = c_short
        self.SBC_SetPIDLoopEncoderCoeff.argtypes = [POINTER(c_char), c_short, c_double]
        # *serialNo, channel, coeff

        self.SBC_SetPIDLoopEncoderParams = self.lib.SBC_SetPIDLoopEncoderParams
        self.SBC_SetPIDLoopEncoderParams.restype = c_short
        self.SBC_SetPIDLoopEncoderParams.argtypes = [MOT_PIDLoopEncoderParams, POINTER(c_char), c_short]
        # *params, *serialNo, channel

        self.SBC_SetPositionCounter = self.lib.SBC_SetPositionCounter
        self.SBC_SetPositionCounter.restype = c_short
        self.SBC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, count

        self.SBC_SetPowerParams = self.lib.SBC_SetPowerParams
        self.SBC_SetPowerParams.restype = c_short
        self.SBC_SetPowerParams.argtypes = [MOT_PowerParameters, POINTER(c_char), c_short]
        # *powerParams, *serialNo, channel

        self.SBC_SetRackDigitalOutputs = self.lib.SBC_SetRackDigitalOutputs
        self.SBC_SetRackDigitalOutputs.restype = c_short
        self.SBC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.SBC_SetRotationModes = self.lib.SBC_SetRotationModes
        self.SBC_SetRotationModes.restype = c_short
        self.SBC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementDirections, MOT_MovementModes]
        # *serialNo, channel, direction, mode

        self.SBC_SetStageAxisLimits = self.lib.SBC_SetStageAxisLimits
        self.SBC_SetStageAxisLimits.restype = c_short
        self.SBC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]
        # *serialNo, channel, maxPosition, minPosition

        self.SBC_SetTriggerSwitches = self.lib.SBC_SetTriggerSwitches
        self.SBC_SetTriggerSwitches.restype = c_short
        self.SBC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]
        # *serialNo, channel, indicatorBits

        self.SBC_SetVelParams = self.lib.SBC_SetVelParams
        self.SBC_SetVelParams.restype = c_short
        self.SBC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
        # *serialNo, acceleration, channel, maxVelocity

        self.SBC_SetVelParamsBlock = self.lib.SBC_SetVelParamsBlock
        self.SBC_SetVelParamsBlock.restype = c_short
        self.SBC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters, MOT_VelocityParameters, c_short]
        # *serialNo, *velocityParameters, *velocityParams, channel

        self.SBC_StartPolling = self.lib.SBC_StartPolling
        self.SBC_StartPolling.restype = c_bool
        self.SBC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, milliseconds

        self.SBC_StopImmediate = self.lib.SBC_StopImmediate
        self.SBC_StopImmediate.restype = c_short
        self.SBC_StopImmediate.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_StopPolling = self.lib.SBC_StopPolling
        self.SBC_StopPolling.restype = None
        self.SBC_StopPolling.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_StopProfiled = self.lib.SBC_StopProfiled
        self.SBC_StopProfiled.restype = c_short
        self.SBC_StopProfiled.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_SuspendMoveMessages = self.lib.SBC_SuspendMoveMessages
        self.SBC_SuspendMoveMessages.restype = c_short
        self.SBC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_TimeSinceLastMsgReceived = self.lib.SBC_TimeSinceLastMsgReceived
        self.SBC_TimeSinceLastMsgReceived.restype = c_bool
        self.SBC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char), c_short]
        # &lastUpdateTimeMS, *serialNo, channel

        self.SBC_UsesPIDLoopEncoding = self.lib.SBC_UsesPIDLoopEncoding
        self.SBC_UsesPIDLoopEncoding.restype = c_bool
        self.SBC_UsesPIDLoopEncoding.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.SBC_WaitForMessage = self.lib.SBC_WaitForMessage
        self.SBC_WaitForMessage.restype = c_bool
        self.SBC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
        # *messageData, *messageID, *messageType, *serialNo, channel

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
