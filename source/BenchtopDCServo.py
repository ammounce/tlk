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
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
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
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_DC_PIDParameters,
    MOT_EncoderResolutionParams,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class BenchtopDCServo(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.Benchtop.DCServo.dll")

        self.BDC_CanHome = self.lib.BDC_CanHome
        self.BDC_CanHome.restype = c_bool
        self.BDC_CanHome.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_CanMoveWithoutHomingFirst = self.lib.BDC_CanMoveWithoutHomingFirst
        self.BDC_CanMoveWithoutHomingFirst.restype = c_bool
        self.BDC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_CheckConnection = self.lib.BDC_CheckConnection
        self.BDC_CheckConnection.restype = c_bool
        self.BDC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_ClearMessageQueue = self.lib.BDC_ClearMessageQueue
        self.BDC_ClearMessageQueue.restype = c_short
        self.BDC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_Close = self.lib.BDC_Close
        self.BDC_Close.restype = c_short
        self.BDC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_DisableChannel = self.lib.BDC_DisableChannel
        self.BDC_DisableChannel.restype = c_short
        self.BDC_DisableChannel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_EnableChannel = self.lib.BDC_EnableChannel
        self.BDC_EnableChannel.restype = c_short
        self.BDC_EnableChannel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_EnableLastMsgTimer = self.lib.BDC_EnableLastMsgTimer
        self.BDC_EnableLastMsgTimer.restype = None
        self.BDC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]
        # *serialNo, channel, enable, lastMsgTimeout

        self.BDC_GetBacklash = self.lib.BDC_GetBacklash
        self.BDC_GetBacklash.restype = c_long
        self.BDC_GetBacklash.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetCalibrationFile = self.lib.BDC_GetCalibrationFile
        self.BDC_GetCalibrationFile.restype = c_bool
        self.BDC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short, c_short]
        # *filename, *serialNo, channel, sizeOfBuffer

        self.BDC_GetDCPIDParams = self.lib.BDC_GetDCPIDParams
        self.BDC_GetDCPIDParams.restype = c_short
        self.BDC_GetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char), c_short]
        # *DCproportionalIntegralDerivativeParams, *serialNo, channel

        self.BDC_GetDeviceUnitFromRealValue = self.lib.BDC_GetDeviceUnitFromRealValue
        self.BDC_GetDeviceUnitFromRealValue.restype = c_short
        self.BDC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_short, c_double, c_int]
        # *device_unit, *serialNo, channel, real_unit, unitType

        self.BDC_GetDigitalOutputs = self.lib.BDC_GetDigitalOutputs
        self.BDC_GetDigitalOutputs.restype = c_byte
        self.BDC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetEncoderCounter = self.lib.BDC_GetEncoderCounter
        self.BDC_GetEncoderCounter.restype = c_long
        self.BDC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetEncoderResolutionParams = self.lib.BDC_GetEncoderResolutionParams
        self.BDC_GetEncoderResolutionParams.restype = c_short
        self.BDC_GetEncoderResolutionParams.argtypes = [MOT_EncoderResolutionParams, POINTER(c_char), c_short]
        # *resolutionParams, *serialNo, channel

        self.BDC_GetFirmwareVersion = self.lib.BDC_GetFirmwareVersion
        self.BDC_GetFirmwareVersion.restype = c_ulong
        self.BDC_GetFirmwareVersion.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetHardwareInfo = self.lib.BDC_GetHardwareInfo
        self.BDC_GetHardwareInfo.restype = c_short
        self.BDC_GetHardwareInfo.argtypes = [
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

        self.BDC_GetHardwareInfoBlock = self.lib.BDC_GetHardwareInfoBlock
        self.BDC_GetHardwareInfoBlock.restype = c_short
        self.BDC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char), c_short]
        # *hardwareInfo, *serialNo, channel

        self.BDC_GetHomingParamsBlock = self.lib.BDC_GetHomingParamsBlock
        self.BDC_GetHomingParamsBlock.restype = c_short
        self.BDC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), c_short]
        # *homingParams, *serialNo, channel

        self.BDC_GetHomingVelocity = self.lib.BDC_GetHomingVelocity
        self.BDC_GetHomingVelocity.restype = c_uint
        self.BDC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetInputVoltage = self.lib.BDC_GetInputVoltage
        self.BDC_GetInputVoltage.restype = c_long
        self.BDC_GetInputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetJogMode = self.lib.BDC_GetJogMode
        self.BDC_GetJogMode.restype = c_short
        self.BDC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes, c_short]
        # *mode, *serialNo, *stopMode, channel

        self.BDC_GetJogParamsBlock = self.lib.BDC_GetJogParamsBlock
        self.BDC_GetJogParamsBlock.restype = c_short
        self.BDC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char), c_short]
        # *jogParams, *serialNo, channel

        self.BDC_GetJogStepSize = self.lib.BDC_GetJogStepSize
        self.BDC_GetJogStepSize.restype = c_uint
        self.BDC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetJogVelParams = self.lib.BDC_GetJogVelParams
        self.BDC_GetJogVelParams.restype = c_short
        self.BDC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
        # *acceleration, *maxVelocity, *serialNo, channel

        self.BDC_GetLimitSwitchParams = self.lib.BDC_GetLimitSwitchParams
        self.BDC_GetLimitSwitchParams.restype = c_short
        self.BDC_GetLimitSwitchParams.argtypes = [
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchModes,
            c_uint,
            POINTER(c_char),
            MOT_LimitSwitchSWModes,
            c_short]
        # *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode, channel

        self.BDC_GetLimitSwitchParamsBlock = self.lib.BDC_GetLimitSwitchParamsBlock
        self.BDC_GetLimitSwitchParamsBlock.restype = c_short
        self.BDC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char), c_short]
        # *limitSwitchParams, *serialNo, channel

        self.BDC_GetMotorParams = self.lib.BDC_GetMotorParams
        self.BDC_GetMotorParams.restype = c_short
        self.BDC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long, c_short]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev, channel

        self.BDC_GetMotorParamsExt = self.lib.BDC_GetMotorParamsExt
        self.BDC_GetMotorParamsExt.restype = c_short
        self.BDC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double, c_short]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev, channel

        self.BDC_GetMotorTravelLimits = self.lib.BDC_GetMotorTravelLimits
        self.BDC_GetMotorTravelLimits.restype = c_short
        self.BDC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
        # *maxPosition, *minPosition, *serialNo, channel

        self.BDC_GetMotorTravelMode = self.lib.BDC_GetMotorTravelMode
        self.BDC_GetMotorTravelMode.restype = MOT_TravelModes
        self.BDC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetMotorVelocityLimits = self.lib.BDC_GetMotorVelocityLimits
        self.BDC_GetMotorVelocityLimits.restype = c_short
        self.BDC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
        # *maxAcceleration, *maxVelocity, *serialNo, channel

        self.BDC_GetMoveAbsolutePosition = self.lib.BDC_GetMoveAbsolutePosition
        self.BDC_GetMoveAbsolutePosition.restype = c_int
        self.BDC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetMoveRelativeDistance = self.lib.BDC_GetMoveRelativeDistance
        self.BDC_GetMoveRelativeDistance.restype = c_int
        self.BDC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetNextMessage = self.lib.BDC_GetNextMessage
        self.BDC_GetNextMessage.restype = c_bool
        self.BDC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
        # *messageData, *messageID, *messageType, *serialNo, channel

        self.BDC_GetNumChannels = self.lib.BDC_GetNumChannels
        self.BDC_GetNumChannels.restype = c_short
        self.BDC_GetNumChannels.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_GetNumberPositions = self.lib.BDC_GetNumberPositions
        self.BDC_GetNumberPositions.restype = c_int
        self.BDC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetPosition = self.lib.BDC_GetPosition
        self.BDC_GetPosition.restype = c_int
        self.BDC_GetPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetPositionCounter = self.lib.BDC_GetPositionCounter
        self.BDC_GetPositionCounter.restype = c_long
        self.BDC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetRackDigitalOutputs = self.lib.BDC_GetRackDigitalOutputs
        self.BDC_GetRackDigitalOutputs.restype = c_byte
        self.BDC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_GetRackStatusBits = self.lib.BDC_GetRackStatusBits
        self.BDC_GetRackStatusBits.restype = c_ulong
        self.BDC_GetRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_GetRealValueFromDeviceUnit = self.lib.BDC_GetRealValueFromDeviceUnit
        self.BDC_GetRealValueFromDeviceUnit.restype = c_short
        self.BDC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_short, c_int, c_int]
        # *real_unit, *serialNo, channel, device_unit, unitType

        self.BDC_GetSoftLimitMode = self.lib.BDC_GetSoftLimitMode
        self.BDC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
        self.BDC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetSoftwareVersion = self.lib.BDC_GetSoftwareVersion
        self.BDC_GetSoftwareVersion.restype = c_ulong
        self.BDC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_GetStageAxisMaxPos = self.lib.BDC_GetStageAxisMaxPos
        self.BDC_GetStageAxisMaxPos.restype = c_int
        self.BDC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetStageAxisMinPos = self.lib.BDC_GetStageAxisMinPos
        self.BDC_GetStageAxisMinPos.restype = c_int
        self.BDC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetStatusBits = self.lib.BDC_GetStatusBits
        self.BDC_GetStatusBits.restype = c_ulong
        self.BDC_GetStatusBits.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetTriggerConfigParams = self.lib.BDC_GetTriggerConfigParams
        self.BDC_GetTriggerConfigParams.restype = c_short
        self.BDC_GetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            c_short]
        # *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity, channel

        self.BDC_GetTriggerConfigParamsBlock = self.lib.BDC_GetTriggerConfigParamsBlock
        self.BDC_GetTriggerConfigParamsBlock.restype = c_short
        self.BDC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig, c_short]
        # *serialNo, *triggerConfigParams, channel

        self.BDC_GetTriggerParams = self.lib.BDC_GetTriggerParams
        self.BDC_GetTriggerParams.restype = c_short
        self.BDC_GetTriggerParams.argtypes = [
            c_int32,
            POINTER(c_char),
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_short]
        # *cycleCount, *serialNo, *triggerIntervalFwd, *triggerIntervalRev, *triggerPulseCountFwd, *triggerPulseCountRev, *triggerPulseWidth, *triggerStartPositionFwd, *triggerStartPositionRev, channel

        self.BDC_GetTriggerParamsBlock = self.lib.BDC_GetTriggerParamsBlock
        self.BDC_GetTriggerParamsBlock.restype = c_short
        self.BDC_GetTriggerParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams, c_short]
        # *serialNo, *triggerParams, channel

        self.BDC_GetTriggerSwitches = self.lib.BDC_GetTriggerSwitches
        self.BDC_GetTriggerSwitches.restype = c_byte
        self.BDC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_GetVelParams = self.lib.BDC_GetVelParams
        self.BDC_GetVelParams.restype = c_short
        self.BDC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
        # *acceleration, *maxVelocity, *serialNo, channel

        self.BDC_GetVelParamsBlock = self.lib.BDC_GetVelParamsBlock
        self.BDC_GetVelParamsBlock.restype = c_short
        self.BDC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters, c_short]
        # *serialNo, *velocityParams, channel

        self.BDC_HasLastMsgTimerOverrun = self.lib.BDC_HasLastMsgTimerOverrun
        self.BDC_HasLastMsgTimerOverrun.restype = c_bool
        self.BDC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_Home = self.lib.BDC_Home
        self.BDC_Home.restype = c_short
        self.BDC_Home.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_Identify = self.lib.BDC_Identify
        self.BDC_Identify.restype = c_short
        self.BDC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_IsCalibrationActive = self.lib.BDC_IsCalibrationActive
        self.BDC_IsCalibrationActive.restype = c_bool
        self.BDC_IsCalibrationActive.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_IsChannelValid = self.lib.BDC_IsChannelValid
        self.BDC_IsChannelValid.restype = c_bool
        self.BDC_IsChannelValid.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_LoadNamedSettings = self.lib.BDC_LoadNamedSettings
        self.BDC_LoadNamedSettings.restype = c_bool
        self.BDC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *serialNo, *settingsName, channel

        self.BDC_LoadSettings = self.lib.BDC_LoadSettings
        self.BDC_LoadSettings.restype = c_bool
        self.BDC_LoadSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_MaxChannelCount = self.lib.BDC_MaxChannelCount
        self.BDC_MaxChannelCount.restype = c_int
        self.BDC_MaxChannelCount.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_MessageQueueSize = self.lib.BDC_MessageQueueSize
        self.BDC_MessageQueueSize.restype = c_int
        self.BDC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_MoveAbsolute = self.lib.BDC_MoveAbsolute
        self.BDC_MoveAbsolute.restype = c_short
        self.BDC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_MoveAtVelocity = self.lib.BDC_MoveAtVelocity
        self.BDC_MoveAtVelocity.restype = c_short
        self.BDC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
        # *serialNo, channel, direction

        self.BDC_MoveJog = self.lib.BDC_MoveJog
        self.BDC_MoveJog.restype = c_short
        self.BDC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
        # *serialNo, channel, jogDirection

        self.BDC_MoveRelative = self.lib.BDC_MoveRelative
        self.BDC_MoveRelative.restype = c_short
        self.BDC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, displacement

        self.BDC_MoveRelativeDistance = self.lib.BDC_MoveRelativeDistance
        self.BDC_MoveRelativeDistance.restype = c_short
        self.BDC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_MoveToPosition = self.lib.BDC_MoveToPosition
        self.BDC_MoveToPosition.restype = c_short
        self.BDC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, index

        self.BDC_NeedsHoming = self.lib.BDC_NeedsHoming
        self.BDC_NeedsHoming.restype = c_bool
        self.BDC_NeedsHoming.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_Open = self.lib.BDC_Open
        self.BDC_Open.restype = c_short
        self.BDC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_PersistSettings = self.lib.BDC_PersistSettings
        self.BDC_PersistSettings.restype = c_bool
        self.BDC_PersistSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_PollingDuration = self.lib.BDC_PollingDuration
        self.BDC_PollingDuration.restype = c_long
        self.BDC_PollingDuration.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RegisterMessageCallback = self.lib.BDC_RegisterMessageCallback
        self.BDC_RegisterMessageCallback.restype = c_short
        self.BDC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, None]
        # *serialNo, channel, void

        self.BDC_RequestBacklash = self.lib.BDC_RequestBacklash
        self.BDC_RequestBacklash.restype = c_short
        self.BDC_RequestBacklash.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestDCPIDParams = self.lib.BDC_RequestDCPIDParams
        self.BDC_RequestDCPIDParams.restype = c_short
        self.BDC_RequestDCPIDParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestDigitalOutputs = self.lib.BDC_RequestDigitalOutputs
        self.BDC_RequestDigitalOutputs.restype = c_short
        self.BDC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestEncoderCounter = self.lib.BDC_RequestEncoderCounter
        self.BDC_RequestEncoderCounter.restype = c_short
        self.BDC_RequestEncoderCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestEncoderResolutionParams = self.lib.BDC_RequestEncoderResolutionParams
        self.BDC_RequestEncoderResolutionParams.restype = c_short
        self.BDC_RequestEncoderResolutionParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestHomingParams = self.lib.BDC_RequestHomingParams
        self.BDC_RequestHomingParams.restype = c_short
        self.BDC_RequestHomingParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestInputVoltage = self.lib.BDC_RequestInputVoltage
        self.BDC_RequestInputVoltage.restype = c_short
        self.BDC_RequestInputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestJogParams = self.lib.BDC_RequestJogParams
        self.BDC_RequestJogParams.restype = c_short
        self.BDC_RequestJogParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestLimitSwitchParams = self.lib.BDC_RequestLimitSwitchParams
        self.BDC_RequestLimitSwitchParams.restype = c_short
        self.BDC_RequestLimitSwitchParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestMoveAbsolutePosition = self.lib.BDC_RequestMoveAbsolutePosition
        self.BDC_RequestMoveAbsolutePosition.restype = c_short
        self.BDC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestMoveRelativeDistance = self.lib.BDC_RequestMoveRelativeDistance
        self.BDC_RequestMoveRelativeDistance.restype = c_short
        self.BDC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestPosition = self.lib.BDC_RequestPosition
        self.BDC_RequestPosition.restype = c_short
        self.BDC_RequestPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestRackDigitalOutputs = self.lib.BDC_RequestRackDigitalOutputs
        self.BDC_RequestRackDigitalOutputs.restype = c_short
        self.BDC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_RequestRackStatusBits = self.lib.BDC_RequestRackStatusBits
        self.BDC_RequestRackStatusBits.restype = c_short
        self.BDC_RequestRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BDC_RequestSettings = self.lib.BDC_RequestSettings
        self.BDC_RequestSettings.restype = c_short
        self.BDC_RequestSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestStatusBits = self.lib.BDC_RequestStatusBits
        self.BDC_RequestStatusBits.restype = c_short
        self.BDC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestTriggerConfigParams = self.lib.BDC_RequestTriggerConfigParams
        self.BDC_RequestTriggerConfigParams.restype = c_short
        self.BDC_RequestTriggerConfigParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestTriggerParams = self.lib.BDC_RequestTriggerParams
        self.BDC_RequestTriggerParams.restype = c_short
        self.BDC_RequestTriggerParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestTriggerSwitches = self.lib.BDC_RequestTriggerSwitches
        self.BDC_RequestTriggerSwitches.restype = c_short
        self.BDC_RequestTriggerSwitches.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_RequestVelParams = self.lib.BDC_RequestVelParams
        self.BDC_RequestVelParams.restype = c_short
        self.BDC_RequestVelParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_ResetRotationModes = self.lib.BDC_ResetRotationModes
        self.BDC_ResetRotationModes.restype = c_short
        self.BDC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_ResumeMoveMessages = self.lib.BDC_ResumeMoveMessages
        self.BDC_ResumeMoveMessages.restype = c_short
        self.BDC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_SetBacklash = self.lib.BDC_SetBacklash
        self.BDC_SetBacklash.restype = c_short
        self.BDC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, distance

        self.BDC_SetCalibrationFile = self.lib.BDC_SetCalibrationFile
        self.BDC_SetCalibrationFile.restype = None
        self.BDC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short, c_bool]
        # *filename, *serialNo, channel, enabled

        self.BDC_SetDCPIDParams = self.lib.BDC_SetDCPIDParams
        self.BDC_SetDCPIDParams.restype = c_short
        self.BDC_SetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char), c_short]
        # *DCproportionalIntegralDerivativeParams, *serialNo, channel

        self.BDC_SetDigitalOutputs = self.lib.BDC_SetDigitalOutputs
        self.BDC_SetDigitalOutputs.restype = c_short
        self.BDC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]
        # *serialNo, channel, outputsBits

        self.BDC_SetDirection = self.lib.BDC_SetDirection
        self.BDC_SetDirection.restype = c_short
        self.BDC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]
        # *serialNo, channel, reverse

        self.BDC_SetEncoderCounter = self.lib.BDC_SetEncoderCounter
        self.BDC_SetEncoderCounter.restype = c_short
        self.BDC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, count

        self.BDC_SetHomingParamsBlock = self.lib.BDC_SetHomingParamsBlock
        self.BDC_SetHomingParamsBlock.restype = c_short
        self.BDC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), c_short]
        # *homingParams, *serialNo, channel

        self.BDC_SetHomingVelocity = self.lib.BDC_SetHomingVelocity
        self.BDC_SetHomingVelocity.restype = c_short
        self.BDC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]
        # *serialNo, channel, velocity

        self.BDC_SetJogMode = self.lib.BDC_SetJogMode
        self.BDC_SetJogMode.restype = c_short
        self.BDC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]
        # *serialNo, channel, mode, stopMode

        self.BDC_SetJogParamsBlock = self.lib.BDC_SetJogParamsBlock
        self.BDC_SetJogParamsBlock.restype = c_short
        self.BDC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char), c_short]
        # *jogParams, *serialNo, channel

        self.BDC_SetJogStepSize = self.lib.BDC_SetJogStepSize
        self.BDC_SetJogStepSize.restype = c_short
        self.BDC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]
        # *serialNo, channel, stepSize

        self.BDC_SetJogVelParams = self.lib.BDC_SetJogVelParams
        self.BDC_SetJogVelParams.restype = c_short
        self.BDC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
        # *serialNo, acceleration, channel, maxVelocity

        self.BDC_SetLimitSwitchParams = self.lib.BDC_SetLimitSwitchParams
        self.BDC_SetLimitSwitchParams.restype = c_short
        self.BDC_SetLimitSwitchParams.argtypes = [
            POINTER(c_char),
            MOT_LimitSwitchModes,
            c_uint,
            c_short,
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchSWModes]
        # *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, channel, clockwiseHardwareLimit, clockwisePosition, softLimitMode

        self.BDC_SetLimitSwitchParamsBlock = self.lib.BDC_SetLimitSwitchParamsBlock
        self.BDC_SetLimitSwitchParamsBlock.restype = c_short
        self.BDC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char), c_short]
        # *limitSwitchParams, *serialNo, channel

        self.BDC_SetLimitsSoftwareApproachPolicy = self.lib.BDC_SetLimitsSoftwareApproachPolicy
        self.BDC_SetLimitsSoftwareApproachPolicy.restype = None
        self.BDC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]
        # *serialNo, channel, limitsSoftwareApproachPolicy

        self.BDC_SetMotorParams = self.lib.BDC_SetMotorParams
        self.BDC_SetMotorParams.restype = c_short
        self.BDC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_float, c_long]
        # *serialNo, channel, gearBoxRatio, pitch, stepsPerRev

        self.BDC_SetMotorParamsExt = self.lib.BDC_SetMotorParamsExt
        self.BDC_SetMotorParamsExt.restype = c_short
        self.BDC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]
        # *serialNo, channel, gearBoxRatio, pitch, stepsPerRev

        self.BDC_SetMotorTravelLimits = self.lib.BDC_SetMotorTravelLimits
        self.BDC_SetMotorTravelLimits.restype = c_short
        self.BDC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
        # *serialNo, channel, maxPosition, minPosition

        self.BDC_SetMotorTravelMode = self.lib.BDC_SetMotorTravelMode
        self.BDC_SetMotorTravelMode.restype = c_short
        self.BDC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]
        # *serialNo, channel, travelMode

        self.BDC_SetMotorVelocityLimits = self.lib.BDC_SetMotorVelocityLimits
        self.BDC_SetMotorVelocityLimits.restype = c_short
        self.BDC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
        # *serialNo, channel, maxAcceleration, maxVelocity

        self.BDC_SetMoveAbsolutePosition = self.lib.BDC_SetMoveAbsolutePosition
        self.BDC_SetMoveAbsolutePosition.restype = c_short
        self.BDC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, position

        self.BDC_SetMoveRelativeDistance = self.lib.BDC_SetMoveRelativeDistance
        self.BDC_SetMoveRelativeDistance.restype = c_short
        self.BDC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, distance

        self.BDC_SetPositionCounter = self.lib.BDC_SetPositionCounter
        self.BDC_SetPositionCounter.restype = c_short
        self.BDC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, count

        self.BDC_SetRackDigitalOutputs = self.lib.BDC_SetRackDigitalOutputs
        self.BDC_SetRackDigitalOutputs.restype = c_short
        self.BDC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.BDC_SetRotationModes = self.lib.BDC_SetRotationModes
        self.BDC_SetRotationModes.restype = c_short
        self.BDC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementDirections, MOT_MovementModes]
        # *serialNo, channel, direction, mode

        self.BDC_SetStageAxisLimits = self.lib.BDC_SetStageAxisLimits
        self.BDC_SetStageAxisLimits.restype = c_short
        self.BDC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]
        # *serialNo, channel, maxPosition, minPosition

        self.BDC_SetTriggerConfigParams = self.lib.BDC_SetTriggerConfigParams
        self.BDC_SetTriggerConfigParams.restype = c_short
        self.BDC_SetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            c_short,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity]
        # *serialNo, channel, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

        self.BDC_SetTriggerConfigParamsBlock = self.lib.BDC_SetTriggerConfigParamsBlock
        self.BDC_SetTriggerConfigParamsBlock.restype = c_short
        self.BDC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig, c_short]
        # *serialNo, *triggerConfigParams, channel

        self.BDC_SetTriggerParams = self.lib.BDC_SetTriggerParams
        self.BDC_SetTriggerParams.restype = c_short
        self.BDC_SetTriggerParams.argtypes = [
            POINTER(c_char),
            c_short,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32]
        # *serialNo, channel, cycleCount, triggerIntervalFwd, triggerIntervalRev, triggerPulseCountFwd, triggerPulseCountRev, triggerPulseWidth, triggerStartPositionFwd, triggerStartPositionRev

        self.BDC_SetTriggerParamsBlock = self.lib.BDC_SetTriggerParamsBlock
        self.BDC_SetTriggerParamsBlock.restype = c_short
        self.BDC_SetTriggerParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams, c_short]
        # *serialNo, *triggerParams, channel

        self.BDC_SetTriggerSwitches = self.lib.BDC_SetTriggerSwitches
        self.BDC_SetTriggerSwitches.restype = c_short
        self.BDC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]
        # *serialNo, channel, indicatorBits

        self.BDC_SetVelParams = self.lib.BDC_SetVelParams
        self.BDC_SetVelParams.restype = c_short
        self.BDC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
        # *serialNo, acceleration, channel, maxVelocity

        self.BDC_SetVelParamsBlock = self.lib.BDC_SetVelParamsBlock
        self.BDC_SetVelParamsBlock.restype = c_short
        self.BDC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters, c_short]
        # *serialNo, *velocityParams, channel

        self.BDC_StartPolling = self.lib.BDC_StartPolling
        self.BDC_StartPolling.restype = c_bool
        self.BDC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, milliseconds

        self.BDC_StopImmediate = self.lib.BDC_StopImmediate
        self.BDC_StopImmediate.restype = c_short
        self.BDC_StopImmediate.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_StopPolling = self.lib.BDC_StopPolling
        self.BDC_StopPolling.restype = None
        self.BDC_StopPolling.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_StopProfiled = self.lib.BDC_StopProfiled
        self.BDC_StopProfiled.restype = c_short
        self.BDC_StopProfiled.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_SuspendMoveMessages = self.lib.BDC_SuspendMoveMessages
        self.BDC_SuspendMoveMessages.restype = c_short
        self.BDC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BDC_TimeSinceLastMsgReceived = self.lib.BDC_TimeSinceLastMsgReceived
        self.BDC_TimeSinceLastMsgReceived.restype = c_bool
        self.BDC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char), c_short]
        # &lastUpdateTimeMS, *serialNo, channel

        self.BDC_WaitForMessage = self.lib.BDC_WaitForMessage
        self.BDC_WaitForMessage.restype = c_bool
        self.BDC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
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
