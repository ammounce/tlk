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
    c_uint,
    c_ulong,
    cdll)
from .safearray import SafeArray
from .definitions.enumerations import (
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    MOT_JogModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes)
from .definitions.structures import (
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_BrushlessTrackSettleParameters,
    MOT_DC_PIDParameters,
    MOT_EncoderResolutionParams,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class KCubeDCServo(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.KCube.DCServo.dll")

        self.KVS_CanDeviceLockFrontPanel = self.lib.KVS_CanDeviceLockFrontPanel
        self.KVS_CanDeviceLockFrontPanel.restype = c_bool
        self.KVS_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_CanHome = self.lib.KVS_CanHome
        self.KVS_CanHome.restype = c_bool
        self.KVS_CanHome.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_CanMoveWithoutHomingFirst = self.lib.KVS_CanMoveWithoutHomingFirst
        self.KVS_CanMoveWithoutHomingFirst.restype = c_bool
        self.KVS_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_CheckConnection = self.lib.KVS_CheckConnection
        self.KVS_CheckConnection.restype = c_bool
        self.KVS_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_ClearMessageQueue = self.lib.KVS_ClearMessageQueue
        self.KVS_ClearMessageQueue.restype = None
        self.KVS_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_Close = self.lib.KVS_Close
        self.KVS_Close.restype = None
        self.KVS_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_DisableChannel = self.lib.KVS_DisableChannel
        self.KVS_DisableChannel.restype = c_short
        self.KVS_DisableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_EnableChannel = self.lib.KVS_EnableChannel
        self.KVS_EnableChannel.restype = c_short
        self.KVS_EnableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_EnableLastMsgTimer = self.lib.KVS_EnableLastMsgTimer
        self.KVS_EnableLastMsgTimer.restype = None
        self.KVS_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.KVS_GetBacklash = self.lib.KVS_GetBacklash
        self.KVS_GetBacklash.restype = c_long
        self.KVS_GetBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetDCPIDParams = self.lib.KVS_GetDCPIDParams
        self.KVS_GetDCPIDParams.restype = c_short
        self.KVS_GetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
        # *DCproportionalIntegralDerivativeParams, *serialNo

        self.KVS_GetDeviceUnitFromRealValue = self.lib.KVS_GetDeviceUnitFromRealValue
        self.KVS_GetDeviceUnitFromRealValue.restype = c_short
        self.KVS_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
        # *device_unit, *serialNo, real_unit, unitType

        self.KVS_GetDigitalOutputs = self.lib.KVS_GetDigitalOutputs
        self.KVS_GetDigitalOutputs.restype = c_byte
        self.KVS_GetDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetEncoderCounter = self.lib.KVS_GetEncoderCounter
        self.KVS_GetEncoderCounter.restype = c_long
        self.KVS_GetEncoderCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetEncoderResolutionParams = self.lib.KVS_GetEncoderResolutionParams
        self.KVS_GetEncoderResolutionParams.restype = c_short
        self.KVS_GetEncoderResolutionParams.argtypes = [MOT_EncoderResolutionParams, POINTER(c_char)]
        # *resolutionParams, *serialNo

        self.KVS_GetFrontPanelLocked = self.lib.KVS_GetFrontPanelLocked
        self.KVS_GetFrontPanelLocked.restype = c_bool
        self.KVS_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetHardwareInfo = self.lib.KVS_GetHardwareInfo
        self.KVS_GetHardwareInfo.restype = c_short
        self.KVS_GetHardwareInfo.argtypes = [
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

        self.KVS_GetHardwareInfoBlock = self.lib.KVS_GetHardwareInfoBlock
        self.KVS_GetHardwareInfoBlock.restype = c_short
        self.KVS_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.KVS_GetHomingParamsBlock = self.lib.KVS_GetHomingParamsBlock
        self.KVS_GetHomingParamsBlock.restype = c_short
        self.KVS_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.KVS_GetHomingVelocity = self.lib.KVS_GetHomingVelocity
        self.KVS_GetHomingVelocity.restype = c_uint
        self.KVS_GetHomingVelocity.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetHubBay = self.lib.KVS_GetHubBay
        self.KVS_GetHubBay.restype = POINTER(c_char)
        self.KVS_GetHubBay.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetJogMode = self.lib.KVS_GetJogMode
        self.KVS_GetJogMode.restype = c_short
        self.KVS_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
        # *mode, *serialNo, *stopMode

        self.KVS_GetJogParamsBlock = self.lib.KVS_GetJogParamsBlock
        self.KVS_GetJogParamsBlock.restype = c_short
        self.KVS_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.KVS_GetJogStepSize = self.lib.KVS_GetJogStepSize
        self.KVS_GetJogStepSize.restype = c_uint
        self.KVS_GetJogStepSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetJogVelParams = self.lib.KVS_GetJogVelParams
        self.KVS_GetJogVelParams.restype = c_short
        self.KVS_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.KVS_GetLEDswitches = self.lib.KVS_GetLEDswitches
        self.KVS_GetLEDswitches.restype = c_long
        self.KVS_GetLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetMotorParams = self.lib.KVS_GetMotorParams
        self.KVS_GetMotorParams.restype = c_short
        self.KVS_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.KVS_GetMotorParamsExt = self.lib.KVS_GetMotorParamsExt
        self.KVS_GetMotorParamsExt.restype = c_short
        self.KVS_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.KVS_GetMotorTravelLimits = self.lib.KVS_GetMotorTravelLimits
        self.KVS_GetMotorTravelLimits.restype = c_short
        self.KVS_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxPosition, *minPosition, *serialNo

        self.KVS_GetMotorTravelMode = self.lib.KVS_GetMotorTravelMode
        self.KVS_GetMotorTravelMode.restype = MOT_TravelModes
        self.KVS_GetMotorTravelMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetMotorVelocityLimits = self.lib.KVS_GetMotorVelocityLimits
        self.KVS_GetMotorVelocityLimits.restype = c_short
        self.KVS_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxAcceleration, *maxVelocity, *serialNo

        self.KVS_GetMoveAbsolutePosition = self.lib.KVS_GetMoveAbsolutePosition
        self.KVS_GetMoveAbsolutePosition.restype = c_int
        self.KVS_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetMoveRelativeDistance = self.lib.KVS_GetMoveRelativeDistance
        self.KVS_GetMoveRelativeDistance.restype = c_int
        self.KVS_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetNextMessage = self.lib.KVS_GetNextMessage
        self.KVS_GetNextMessage.restype = c_bool
        self.KVS_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.KVS_GetNumberPositions = self.lib.KVS_GetNumberPositions
        self.KVS_GetNumberPositions.restype = c_int
        self.KVS_GetNumberPositions.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetPosition = self.lib.KVS_GetPosition
        self.KVS_GetPosition.restype = c_int
        self.KVS_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetPositionCounter = self.lib.KVS_GetPositionCounter
        self.KVS_GetPositionCounter.restype = c_long
        self.KVS_GetPositionCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetRealValueFromDeviceUnit = self.lib.KVS_GetRealValueFromDeviceUnit
        self.KVS_GetRealValueFromDeviceUnit.restype = c_short
        self.KVS_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
        # *real_unit, *serialNo, device_unit, unitType

        self.KVS_GetSoftLimitMode = self.lib.KVS_GetSoftLimitMode
        self.KVS_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
        self.KVS_GetSoftLimitMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetSoftwareVersion = self.lib.KVS_GetSoftwareVersion
        self.KVS_GetSoftwareVersion.restype = c_ulong
        self.KVS_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetStageAxisMaxPos = self.lib.KVS_GetStageAxisMaxPos
        self.KVS_GetStageAxisMaxPos.restype = c_int
        self.KVS_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetStageAxisMinPos = self.lib.KVS_GetStageAxisMinPos
        self.KVS_GetStageAxisMinPos.restype = c_int
        self.KVS_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetStatusBits = self.lib.KVS_GetStatusBits
        self.KVS_GetStatusBits.restype = c_ulong
        self.KVS_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_GetTrackSettleParams = self.lib.KVS_GetTrackSettleParams
        self.KVS_GetTrackSettleParams.restype = c_short
        self.KVS_GetTrackSettleParams.argtypes = [POINTER(c_char), MOT_BrushlessTrackSettleParameters]
        # *serialNo, *settleParams

        self.KVS_GetTriggerConfigParams = self.lib.KVS_GetTriggerConfigParams
        self.KVS_GetTriggerConfigParams.restype = c_short
        self.KVS_GetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity]
        # *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity

        self.KVS_GetTriggerConfigParamsBlock = self.lib.KVS_GetTriggerConfigParamsBlock
        self.KVS_GetTriggerConfigParamsBlock.restype = c_short
        self.KVS_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.KVS_GetTriggerParamsParams = self.lib.KVS_GetTriggerParamsParams
        self.KVS_GetTriggerParamsParams.restype = c_short
        self.KVS_GetTriggerParamsParams.argtypes = [
            c_int32,
            POINTER(c_char),
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32]
        # *cycleCount, *serialNo, *triggerIntervalFwd, *triggerIntervalRev, *triggerPulseCountFwd, *triggerPulseCountRev, *triggerPulseWidth, *triggerStartPositionFwd, *triggerStartPositionRev

        self.KVS_GetTriggerParamsParamsBlock = self.lib.KVS_GetTriggerParamsParamsBlock
        self.KVS_GetTriggerParamsParamsBlock.restype = c_short
        self.KVS_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
        # *serialNo, *triggerParamsParams

        self.KVS_GetVelParams = self.lib.KVS_GetVelParams
        self.KVS_GetVelParams.restype = c_short
        self.KVS_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.KVS_GetVelParamsBlock = self.lib.KVS_GetVelParamsBlock
        self.KVS_GetVelParamsBlock.restype = c_short
        self.KVS_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.KVS_HasLastMsgTimerOverrun = self.lib.KVS_HasLastMsgTimerOverrun
        self.KVS_HasLastMsgTimerOverrun.restype = c_bool
        self.KVS_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_Home = self.lib.KVS_Home
        self.KVS_Home.restype = c_short
        self.KVS_Home.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_Identify = self.lib.KVS_Identify
        self.KVS_Identify.restype = None
        self.KVS_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_LoadNamedSettings = self.lib.KVS_LoadNamedSettings
        self.KVS_LoadNamedSettings.restype = c_bool
        self.KVS_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.KVS_LoadSettings = self.lib.KVS_LoadSettings
        self.KVS_LoadSettings.restype = c_bool
        self.KVS_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_MessageQueueSize = self.lib.KVS_MessageQueueSize
        self.KVS_MessageQueueSize.restype = c_int
        self.KVS_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_MoveAbsolute = self.lib.KVS_MoveAbsolute
        self.KVS_MoveAbsolute.restype = c_short
        self.KVS_MoveAbsolute.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_MoveAtVelocity = self.lib.KVS_MoveAtVelocity
        self.KVS_MoveAtVelocity.restype = c_short
        self.KVS_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, direction

        self.KVS_MoveJog = self.lib.KVS_MoveJog
        self.KVS_MoveJog.restype = c_short
        self.KVS_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, jogDirection

        self.KVS_MoveRelative = self.lib.KVS_MoveRelative
        self.KVS_MoveRelative.restype = c_short
        self.KVS_MoveRelative.argtypes = [POINTER(c_char), c_int]
        # *serialNo, displacement

        self.KVS_MoveRelativeDistance = self.lib.KVS_MoveRelativeDistance
        self.KVS_MoveRelativeDistance.restype = c_short
        self.KVS_MoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_MoveToPosition = self.lib.KVS_MoveToPosition
        self.KVS_MoveToPosition.restype = c_short
        self.KVS_MoveToPosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, index

        self.KVS_NeedsHoming = self.lib.KVS_NeedsHoming
        self.KVS_NeedsHoming.restype = c_bool
        self.KVS_NeedsHoming.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_Open = self.lib.KVS_Open
        self.KVS_Open.restype = c_short
        self.KVS_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_PersistSettings = self.lib.KVS_PersistSettings
        self.KVS_PersistSettings.restype = c_bool
        self.KVS_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_PollingDuration = self.lib.KVS_PollingDuration
        self.KVS_PollingDuration.restype = c_long
        self.KVS_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RegisterMessageCallback = self.lib.KVS_RegisterMessageCallback
        self.KVS_RegisterMessageCallback.restype = None
        self.KVS_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.KVS_RequestBacklash = self.lib.KVS_RequestBacklash
        self.KVS_RequestBacklash.restype = c_short
        self.KVS_RequestBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestDCPIDParams = self.lib.KVS_RequestDCPIDParams
        self.KVS_RequestDCPIDParams.restype = c_short
        self.KVS_RequestDCPIDParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestDigitalOutputs = self.lib.KVS_RequestDigitalOutputs
        self.KVS_RequestDigitalOutputs.restype = c_short
        self.KVS_RequestDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestEncoderCounter = self.lib.KVS_RequestEncoderCounter
        self.KVS_RequestEncoderCounter.restype = c_short
        self.KVS_RequestEncoderCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestEncoderResolutionParams = self.lib.KVS_RequestEncoderResolutionParams
        self.KVS_RequestEncoderResolutionParams.restype = c_short
        self.KVS_RequestEncoderResolutionParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestFrontPanelLocked = self.lib.KVS_RequestFrontPanelLocked
        self.KVS_RequestFrontPanelLocked.restype = c_short
        self.KVS_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestHomingParams = self.lib.KVS_RequestHomingParams
        self.KVS_RequestHomingParams.restype = c_short
        self.KVS_RequestHomingParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestJogParams = self.lib.KVS_RequestJogParams
        self.KVS_RequestJogParams.restype = c_short
        self.KVS_RequestJogParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestLEDswitches = self.lib.KVS_RequestLEDswitches
        self.KVS_RequestLEDswitches.restype = c_short
        self.KVS_RequestLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestMoveAbsolutePosition = self.lib.KVS_RequestMoveAbsolutePosition
        self.KVS_RequestMoveAbsolutePosition.restype = c_short
        self.KVS_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestMoveRelativeDistance = self.lib.KVS_RequestMoveRelativeDistance
        self.KVS_RequestMoveRelativeDistance.restype = c_short
        self.KVS_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestPosTriggerParams = self.lib.KVS_RequestPosTriggerParams
        self.KVS_RequestPosTriggerParams.restype = c_short
        self.KVS_RequestPosTriggerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestPosition = self.lib.KVS_RequestPosition
        self.KVS_RequestPosition.restype = c_short
        self.KVS_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestSettings = self.lib.KVS_RequestSettings
        self.KVS_RequestSettings.restype = c_short
        self.KVS_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestStatusBits = self.lib.KVS_RequestStatusBits
        self.KVS_RequestStatusBits.restype = c_short
        self.KVS_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestTrackSettleParams = self.lib.KVS_RequestTrackSettleParams
        self.KVS_RequestTrackSettleParams.restype = c_short
        self.KVS_RequestTrackSettleParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestTriggerConfigParams = self.lib.KVS_RequestTriggerConfigParams
        self.KVS_RequestTriggerConfigParams.restype = c_short
        self.KVS_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_RequestVelParams = self.lib.KVS_RequestVelParams
        self.KVS_RequestVelParams.restype = c_short
        self.KVS_RequestVelParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_ResetStageToDefaults = self.lib.KVS_ResetStageToDefaults
        self.KVS_ResetStageToDefaults.restype = c_short
        self.KVS_ResetStageToDefaults.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_ResumeMoveMessages = self.lib.KVS_ResumeMoveMessages
        self.KVS_ResumeMoveMessages.restype = c_short
        self.KVS_ResumeMoveMessages.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_SetBacklash = self.lib.KVS_SetBacklash
        self.KVS_SetBacklash.restype = c_short
        self.KVS_SetBacklash.argtypes = [POINTER(c_char), c_long]
        # *serialNo, distance

        self.KVS_SetDCPIDParams = self.lib.KVS_SetDCPIDParams
        self.KVS_SetDCPIDParams.restype = c_short
        self.KVS_SetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
        # *DCproportionalIntegralDerivativeParams, *serialNo

        self.KVS_SetDigitalOutputs = self.lib.KVS_SetDigitalOutputs
        self.KVS_SetDigitalOutputs.restype = c_short
        self.KVS_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.KVS_SetDirection = self.lib.KVS_SetDirection
        self.KVS_SetDirection.restype = None
        self.KVS_SetDirection.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, reverse

        self.KVS_SetEncoderCounter = self.lib.KVS_SetEncoderCounter
        self.KVS_SetEncoderCounter.restype = c_short
        self.KVS_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.KVS_SetFrontPanelLock = self.lib.KVS_SetFrontPanelLock
        self.KVS_SetFrontPanelLock.restype = c_short
        self.KVS_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, locked

        self.KVS_SetHomingParamsBlock = self.lib.KVS_SetHomingParamsBlock
        self.KVS_SetHomingParamsBlock.restype = c_short
        self.KVS_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.KVS_SetHomingVelocity = self.lib.KVS_SetHomingVelocity
        self.KVS_SetHomingVelocity.restype = c_short
        self.KVS_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, velocity

        self.KVS_SetJogMode = self.lib.KVS_SetJogMode
        self.KVS_SetJogMode.restype = c_short
        self.KVS_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
        # *serialNo, mode, stopMode

        self.KVS_SetJogParamsBlock = self.lib.KVS_SetJogParamsBlock
        self.KVS_SetJogParamsBlock.restype = c_short
        self.KVS_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.KVS_SetJogStepSize = self.lib.KVS_SetJogStepSize
        self.KVS_SetJogStepSize.restype = c_short
        self.KVS_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, stepSize

        self.KVS_SetJogVelParams = self.lib.KVS_SetJogVelParams
        self.KVS_SetJogVelParams.restype = c_short
        self.KVS_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.KVS_SetLEDswitches = self.lib.KVS_SetLEDswitches
        self.KVS_SetLEDswitches.restype = c_short
        self.KVS_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
        # *serialNo, LEDswitches

        self.KVS_SetLimitsSoftwareApproachPolicy = self.lib.KVS_SetLimitsSoftwareApproachPolicy
        self.KVS_SetLimitsSoftwareApproachPolicy.restype = None
        self.KVS_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
        # *serialNo, limitsSoftwareApproachPolicy

        self.KVS_SetMotorParams = self.lib.KVS_SetMotorParams
        self.KVS_SetMotorParams.restype = c_short
        self.KVS_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.KVS_SetMotorParamsExt = self.lib.KVS_SetMotorParamsExt
        self.KVS_SetMotorParamsExt.restype = c_short
        self.KVS_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.KVS_SetMotorTravelLimits = self.lib.KVS_SetMotorTravelLimits
        self.KVS_SetMotorTravelLimits.restype = c_short
        self.KVS_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxPosition, minPosition

        self.KVS_SetMotorTravelMode = self.lib.KVS_SetMotorTravelMode
        self.KVS_SetMotorTravelMode.restype = c_short
        self.KVS_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
        # *serialNo, travelMode

        self.KVS_SetMotorVelocityLimits = self.lib.KVS_SetMotorVelocityLimits
        self.KVS_SetMotorVelocityLimits.restype = c_short
        self.KVS_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxAcceleration, maxVelocity

        self.KVS_SetMoveAbsolutePosition = self.lib.KVS_SetMoveAbsolutePosition
        self.KVS_SetMoveAbsolutePosition.restype = c_short
        self.KVS_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, position

        self.KVS_SetMoveRelativeDistance = self.lib.KVS_SetMoveRelativeDistance
        self.KVS_SetMoveRelativeDistance.restype = c_short
        self.KVS_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
        # *serialNo, distance

        self.KVS_SetPositionCounter = self.lib.KVS_SetPositionCounter
        self.KVS_SetPositionCounter.restype = c_short
        self.KVS_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.KVS_SetStageAxisLimits = self.lib.KVS_SetStageAxisLimits
        self.KVS_SetStageAxisLimits.restype = c_short
        self.KVS_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, maxPosition, minPosition

        self.KVS_SetTrackSettleParams = self.lib.KVS_SetTrackSettleParams
        self.KVS_SetTrackSettleParams.restype = c_short
        self.KVS_SetTrackSettleParams.argtypes = [POINTER(c_char), MOT_BrushlessTrackSettleParameters]
        # *serialNo, *settleParams

        self.KVS_SetTriggerConfigParams = self.lib.KVS_SetTriggerConfigParams
        self.KVS_SetTriggerConfigParams.restype = c_short
        self.KVS_SetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity]
        # *serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

        self.KVS_SetTriggerConfigParamsBlock = self.lib.KVS_SetTriggerConfigParamsBlock
        self.KVS_SetTriggerConfigParamsBlock.restype = c_short
        self.KVS_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.KVS_SetTriggerParamsParams = self.lib.KVS_SetTriggerParamsParams
        self.KVS_SetTriggerParamsParams.restype = c_short
        self.KVS_SetTriggerParamsParams.argtypes = [
            POINTER(c_char),
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            c_int32]
        # *serialNo, cycleCount, triggerIntervalFwd, triggerIntervalRev, triggerPulseCountFwd, triggerPulseCountRev, triggerPulseWidth, triggerStartPositionFwd, triggerStartPositionRev

        self.KVS_SetTriggerParamsParamsBlock = self.lib.KVS_SetTriggerParamsParamsBlock
        self.KVS_SetTriggerParamsParamsBlock.restype = c_short
        self.KVS_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
        # *serialNo, *triggerParamsParams

        self.KVS_SetVelParams = self.lib.KVS_SetVelParams
        self.KVS_SetVelParams.restype = c_short
        self.KVS_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.KVS_SetVelParamsBlock = self.lib.KVS_SetVelParamsBlock
        self.KVS_SetVelParamsBlock.restype = c_short
        self.KVS_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.KVS_StartPolling = self.lib.KVS_StartPolling
        self.KVS_StartPolling.restype = c_bool
        self.KVS_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.KVS_StopImmediate = self.lib.KVS_StopImmediate
        self.KVS_StopImmediate.restype = c_short
        self.KVS_StopImmediate.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_StopPolling = self.lib.KVS_StopPolling
        self.KVS_StopPolling.restype = None
        self.KVS_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_StopProfiled = self.lib.KVS_StopProfiled
        self.KVS_StopProfiled.restype = c_short
        self.KVS_StopProfiled.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_SuspendMoveMessages = self.lib.KVS_SuspendMoveMessages
        self.KVS_SuspendMoveMessages.restype = c_short
        self.KVS_SuspendMoveMessages.argtypes = [POINTER(c_char)]
        # *serialNo

        self.KVS_TimeSinceLastMsgReceived = self.lib.KVS_TimeSinceLastMsgReceived
        self.KVS_TimeSinceLastMsgReceived.restype = c_bool
        self.KVS_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.KVS_WaitForMessage = self.lib.KVS_WaitForMessage
        self.KVS_WaitForMessage.restype = c_bool
        self.KVS_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
