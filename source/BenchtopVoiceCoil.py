from c_types import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_double,
    c_float,
    c_int,
    c_int16,
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
    KMOT_WheelDirectionSense,
    KMOT_WheelMode,
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
    KMOT_MMIParams,
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_BVC_ScanParams,
    MOT_DC_PIDParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class BenchtopVoiceCoil(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.Benchtop.VoiceCoil.dll")

        self.BVC_CanDeviceLockFrontPanel = self.lib.BVC_CanDeviceLockFrontPanel
        self.BVC_CanDeviceLockFrontPanel.restype = c_bool
        self.BVC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_CanHome = self.lib.BVC_CanHome
        self.BVC_CanHome.restype = c_bool
        self.BVC_CanHome.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_CanMoveWithoutHomingFirst = self.lib.BVC_CanMoveWithoutHomingFirst
        self.BVC_CanMoveWithoutHomingFirst.restype = c_bool
        self.BVC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_CheckConnection = self.lib.BVC_CheckConnection
        self.BVC_CheckConnection.restype = c_bool
        self.BVC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_ClearMessageQueue = self.lib.BVC_ClearMessageQueue
        self.BVC_ClearMessageQueue.restype = None
        self.BVC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_Close = self.lib.BVC_Close
        self.BVC_Close.restype = None
        self.BVC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_DisableChannel = self.lib.BVC_DisableChannel
        self.BVC_DisableChannel.restype = c_short
        self.BVC_DisableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_EnableChannel = self.lib.BVC_EnableChannel
        self.BVC_EnableChannel.restype = c_short
        self.BVC_EnableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_EnableLastMsgTimer = self.lib.BVC_EnableLastMsgTimer
        self.BVC_EnableLastMsgTimer.restype = None
        self.BVC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.BVC_GetBacklash = self.lib.BVC_GetBacklash
        self.BVC_GetBacklash.restype = c_long
        self.BVC_GetBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetDCPIDParams = self.lib.BVC_GetDCPIDParams
        self.BVC_GetDCPIDParams.restype = c_short
        self.BVC_GetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
        # *DCproportionalIntegralDerivativeParams, *serialNo

        self.BVC_GetDeviceUnitFromRealValue = self.lib.BVC_GetDeviceUnitFromRealValue
        self.BVC_GetDeviceUnitFromRealValue.restype = c_short
        self.BVC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
        # *device_unit, *serialNo, real_unit, unitType

        self.BVC_GetDigitalOutputs = self.lib.BVC_GetDigitalOutputs
        self.BVC_GetDigitalOutputs.restype = c_byte
        self.BVC_GetDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetEncoderCounter = self.lib.BVC_GetEncoderCounter
        self.BVC_GetEncoderCounter.restype = c_long
        self.BVC_GetEncoderCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetFrontPanelLocked = self.lib.BVC_GetFrontPanelLocked
        self.BVC_GetFrontPanelLocked.restype = c_bool
        self.BVC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetHardwareInfo = self.lib.BVC_GetHardwareInfo
        self.BVC_GetHardwareInfo.restype = c_short
        self.BVC_GetHardwareInfo.argtypes = [
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

        self.BVC_GetHardwareInfoBlock = self.lib.BVC_GetHardwareInfoBlock
        self.BVC_GetHardwareInfoBlock.restype = c_short
        self.BVC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.BVC_GetHomingParamsBlock = self.lib.BVC_GetHomingParamsBlock
        self.BVC_GetHomingParamsBlock.restype = c_short
        self.BVC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.BVC_GetHomingVelocity = self.lib.BVC_GetHomingVelocity
        self.BVC_GetHomingVelocity.restype = c_uint
        self.BVC_GetHomingVelocity.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetHubBay = self.lib.BVC_GetHubBay
        self.BVC_GetHubBay.restype = POINTER(c_char)
        self.BVC_GetHubBay.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetJogMode = self.lib.BVC_GetJogMode
        self.BVC_GetJogMode.restype = c_short
        self.BVC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
        # *mode, *serialNo, *stopMode

        self.BVC_GetJogParamsBlock = self.lib.BVC_GetJogParamsBlock
        self.BVC_GetJogParamsBlock.restype = c_short
        self.BVC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.BVC_GetJogStepSize = self.lib.BVC_GetJogStepSize
        self.BVC_GetJogStepSize.restype = c_uint
        self.BVC_GetJogStepSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetJogVelParams = self.lib.BVC_GetJogVelParams
        self.BVC_GetJogVelParams.restype = c_short
        self.BVC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.BVC_GetLEDswitches = self.lib.BVC_GetLEDswitches
        self.BVC_GetLEDswitches.restype = c_long
        self.BVC_GetLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetLimitSwitchParams = self.lib.BVC_GetLimitSwitchParams
        self.BVC_GetLimitSwitchParams.restype = c_short
        self.BVC_GetLimitSwitchParams.argtypes = [MOT_LimitSwitchModes, c_uint,
                                                  MOT_LimitSwitchModes, c_uint, POINTER(c_char), MOT_LimitSwitchSWModes]
        # *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode

        self.BVC_GetLimitSwitchParamsBlock = self.lib.BVC_GetLimitSwitchParamsBlock
        self.BVC_GetLimitSwitchParamsBlock.restype = c_short
        self.BVC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
        # *limitSwitchParams, *serialNo

        self.BVC_GetMMIParams = self.lib.BVC_GetMMIParams
        self.BVC_GetMMIParams.restype = c_short
        self.BVC_GetMMIParams.argtypes = [KMOT_WheelDirectionSense, c_int16,
                                          c_int32, c_int32, POINTER(c_char), c_int32, c_int32, KMOT_WheelMode]
        # *directionSense, *displayIntensity, *presetPosition1, *presetPosition2, *serialNo, *wheelAcceleration, *wheelMaxVelocity, *wheelMode

        self.BVC_GetMMIParamsBlock = self.lib.BVC_GetMMIParamsBlock
        self.BVC_GetMMIParamsBlock.restype = c_short
        self.BVC_GetMMIParamsBlock.argtypes = [KMOT_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.BVC_GetMMIParamsExt = self.lib.BVC_GetMMIParamsExt
        self.BVC_GetMMIParamsExt.restype = c_short
        self.BVC_GetMMIParamsExt.argtypes = [
            KMOT_WheelDirectionSense,
            c_int16,
            c_int16,
            c_int16,
            c_int32,
            c_int32,
            POINTER(c_char),
            c_int32,
            c_int32,
            KMOT_WheelMode]
        # *directionSense, *displayDimIntensity, *displayIntensity, *displayTimeout, *presetPosition1, *presetPosition2, *serialNo, *wheelAcceleration, *wheelMaxVelocity, *wheelMode

        self.BVC_GetMotorParams = self.lib.BVC_GetMotorParams
        self.BVC_GetMotorParams.restype = c_short
        self.BVC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.BVC_GetMotorParamsExt = self.lib.BVC_GetMotorParamsExt
        self.BVC_GetMotorParamsExt.restype = c_short
        self.BVC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
        # *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

        self.BVC_GetMotorTravelLimits = self.lib.BVC_GetMotorTravelLimits
        self.BVC_GetMotorTravelLimits.restype = c_short
        self.BVC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxPosition, *minPosition, *serialNo

        self.BVC_GetMotorTravelMode = self.lib.BVC_GetMotorTravelMode
        self.BVC_GetMotorTravelMode.restype = MOT_TravelModes
        self.BVC_GetMotorTravelMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetMotorVelocityLimits = self.lib.BVC_GetMotorVelocityLimits
        self.BVC_GetMotorVelocityLimits.restype = c_short
        self.BVC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
        # *maxAcceleration, *maxVelocity, *serialNo

        self.BVC_GetMoveAbsolutePosition = self.lib.BVC_GetMoveAbsolutePosition
        self.BVC_GetMoveAbsolutePosition.restype = c_int
        self.BVC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetMoveRelativeDistance = self.lib.BVC_GetMoveRelativeDistance
        self.BVC_GetMoveRelativeDistance.restype = c_int
        self.BVC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetNextMessage = self.lib.BVC_GetNextMessage
        self.BVC_GetNextMessage.restype = c_bool
        self.BVC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.BVC_GetNumberPositions = self.lib.BVC_GetNumberPositions
        self.BVC_GetNumberPositions.restype = c_int
        self.BVC_GetNumberPositions.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetPosition = self.lib.BVC_GetPosition
        self.BVC_GetPosition.restype = c_int
        self.BVC_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetPositionCounter = self.lib.BVC_GetPositionCounter
        self.BVC_GetPositionCounter.restype = c_long
        self.BVC_GetPositionCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetRealValueFromDeviceUnit = self.lib.BVC_GetRealValueFromDeviceUnit
        self.BVC_GetRealValueFromDeviceUnit.restype = c_short
        self.BVC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
        # *real_unit, *serialNo, device_unit, unitType

        self.BVC_GetScanParams = self.lib.BVC_GetScanParams
        self.BVC_GetScanParams.restype = c_short
        self.BVC_GetScanParams.argtypes = [MOT_BVC_ScanParams, POINTER(c_char)]
        # *scanParameters, *serialNo

        self.BVC_GetSoftLimitMode = self.lib.BVC_GetSoftLimitMode
        self.BVC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
        self.BVC_GetSoftLimitMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetSoftwareVersion = self.lib.BVC_GetSoftwareVersion
        self.BVC_GetSoftwareVersion.restype = c_ulong
        self.BVC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetStageAxisMaxPos = self.lib.BVC_GetStageAxisMaxPos
        self.BVC_GetStageAxisMaxPos.restype = c_int
        self.BVC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetStageAxisMinPos = self.lib.BVC_GetStageAxisMinPos
        self.BVC_GetStageAxisMinPos.restype = c_int
        self.BVC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetStatusBits = self.lib.BVC_GetStatusBits
        self.BVC_GetStatusBits.restype = c_ulong
        self.BVC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_GetTriggerConfigParams = self.lib.BVC_GetTriggerConfigParams
        self.BVC_GetTriggerConfigParams.restype = c_short
        self.BVC_GetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity]
        # *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity

        self.BVC_GetTriggerConfigParamsBlock = self.lib.BVC_GetTriggerConfigParamsBlock
        self.BVC_GetTriggerConfigParamsBlock.restype = c_short
        self.BVC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.BVC_GetTriggerParamsParams = self.lib.BVC_GetTriggerParamsParams
        self.BVC_GetTriggerParamsParams.restype = c_short
        self.BVC_GetTriggerParamsParams.argtypes = [
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

        self.BVC_GetTriggerParamsParamsBlock = self.lib.BVC_GetTriggerParamsParamsBlock
        self.BVC_GetTriggerParamsParamsBlock.restype = c_short
        self.BVC_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
        # *serialNo, *triggerParamsParams

        self.BVC_GetVelParams = self.lib.BVC_GetVelParams
        self.BVC_GetVelParams.restype = c_short
        self.BVC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
        # *acceleration, *maxVelocity, *serialNo

        self.BVC_GetVelParamsBlock = self.lib.BVC_GetVelParamsBlock
        self.BVC_GetVelParamsBlock.restype = c_short
        self.BVC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.BVC_HasLastMsgTimerOverrun = self.lib.BVC_HasLastMsgTimerOverrun
        self.BVC_HasLastMsgTimerOverrun.restype = c_bool
        self.BVC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_Home = self.lib.BVC_Home
        self.BVC_Home.restype = c_short
        self.BVC_Home.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_Identify = self.lib.BVC_Identify
        self.BVC_Identify.restype = None
        self.BVC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_IsScanning = self.lib.BVC_IsScanning
        self.BVC_IsScanning.restype = c_bool
        self.BVC_IsScanning.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_IsScanningEnabled = self.lib.BVC_IsScanningEnabled
        self.BVC_IsScanningEnabled.restype = c_bool
        self.BVC_IsScanningEnabled.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_LoadNamedSettings = self.lib.BVC_LoadNamedSettings
        self.BVC_LoadNamedSettings.restype = c_bool
        self.BVC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.BVC_LoadSettings = self.lib.BVC_LoadSettings
        self.BVC_LoadSettings.restype = c_bool
        self.BVC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_MessageQueueSize = self.lib.BVC_MessageQueueSize
        self.BVC_MessageQueueSize.restype = c_int
        self.BVC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_MoveAbsolute = self.lib.BVC_MoveAbsolute
        self.BVC_MoveAbsolute.restype = c_short
        self.BVC_MoveAbsolute.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_MoveAtVelocity = self.lib.BVC_MoveAtVelocity
        self.BVC_MoveAtVelocity.restype = c_short
        self.BVC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, direction

        self.BVC_MoveJog = self.lib.BVC_MoveJog
        self.BVC_MoveJog.restype = c_short
        self.BVC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
        # *serialNo, jogDirection

        self.BVC_MoveRelative = self.lib.BVC_MoveRelative
        self.BVC_MoveRelative.restype = c_short
        self.BVC_MoveRelative.argtypes = [POINTER(c_char), c_int]
        # *serialNo, displacement

        self.BVC_MoveRelativeDistance = self.lib.BVC_MoveRelativeDistance
        self.BVC_MoveRelativeDistance.restype = c_short
        self.BVC_MoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_MoveToPosition = self.lib.BVC_MoveToPosition
        self.BVC_MoveToPosition.restype = c_short
        self.BVC_MoveToPosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, index

        self.BVC_NeedsHoming = self.lib.BVC_NeedsHoming
        self.BVC_NeedsHoming.restype = c_bool
        self.BVC_NeedsHoming.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_Open = self.lib.BVC_Open
        self.BVC_Open.restype = c_short
        self.BVC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_PersistSettings = self.lib.BVC_PersistSettings
        self.BVC_PersistSettings.restype = c_bool
        self.BVC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_PollingDuration = self.lib.BVC_PollingDuration
        self.BVC_PollingDuration.restype = c_long
        self.BVC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RegisterMessageCallback = self.lib.BVC_RegisterMessageCallback
        self.BVC_RegisterMessageCallback.restype = None
        self.BVC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.BVC_RequestBacklash = self.lib.BVC_RequestBacklash
        self.BVC_RequestBacklash.restype = c_short
        self.BVC_RequestBacklash.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestDCPIDParams = self.lib.BVC_RequestDCPIDParams
        self.BVC_RequestDCPIDParams.restype = c_short
        self.BVC_RequestDCPIDParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestDigitalOutputs = self.lib.BVC_RequestDigitalOutputs
        self.BVC_RequestDigitalOutputs.restype = c_short
        self.BVC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestEncoderCounter = self.lib.BVC_RequestEncoderCounter
        self.BVC_RequestEncoderCounter.restype = c_short
        self.BVC_RequestEncoderCounter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestFrontPanelLocked = self.lib.BVC_RequestFrontPanelLocked
        self.BVC_RequestFrontPanelLocked.restype = c_short
        self.BVC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestHomingParams = self.lib.BVC_RequestHomingParams
        self.BVC_RequestHomingParams.restype = c_short
        self.BVC_RequestHomingParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestJogParams = self.lib.BVC_RequestJogParams
        self.BVC_RequestJogParams.restype = c_short
        self.BVC_RequestJogParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestLEDswitches = self.lib.BVC_RequestLEDswitches
        self.BVC_RequestLEDswitches.restype = c_short
        self.BVC_RequestLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestLimitSwitchParams = self.lib.BVC_RequestLimitSwitchParams
        self.BVC_RequestLimitSwitchParams.restype = c_short
        self.BVC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestMMIparams = self.lib.BVC_RequestMMIparams
        self.BVC_RequestMMIparams.restype = c_short
        self.BVC_RequestMMIparams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestMoveAbsolutePosition = self.lib.BVC_RequestMoveAbsolutePosition
        self.BVC_RequestMoveAbsolutePosition.restype = c_short
        self.BVC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestMoveRelativeDistance = self.lib.BVC_RequestMoveRelativeDistance
        self.BVC_RequestMoveRelativeDistance.restype = c_short
        self.BVC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestPosTriggerParams = self.lib.BVC_RequestPosTriggerParams
        self.BVC_RequestPosTriggerParams.restype = c_short
        self.BVC_RequestPosTriggerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestPosition = self.lib.BVC_RequestPosition
        self.BVC_RequestPosition.restype = c_short
        self.BVC_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestScanParams = self.lib.BVC_RequestScanParams
        self.BVC_RequestScanParams.restype = c_short
        self.BVC_RequestScanParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestSettings = self.lib.BVC_RequestSettings
        self.BVC_RequestSettings.restype = c_short
        self.BVC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestStatusBits = self.lib.BVC_RequestStatusBits
        self.BVC_RequestStatusBits.restype = c_short
        self.BVC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestTriggerConfigParams = self.lib.BVC_RequestTriggerConfigParams
        self.BVC_RequestTriggerConfigParams.restype = c_short
        self.BVC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_RequestVelParams = self.lib.BVC_RequestVelParams
        self.BVC_RequestVelParams.restype = c_short
        self.BVC_RequestVelParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_ResetRotationModes = self.lib.BVC_ResetRotationModes
        self.BVC_ResetRotationModes.restype = c_short
        self.BVC_ResetRotationModes.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_ResetStageToDefaults = self.lib.BVC_ResetStageToDefaults
        self.BVC_ResetStageToDefaults.restype = c_short
        self.BVC_ResetStageToDefaults.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_ResumeMoveMessages = self.lib.BVC_ResumeMoveMessages
        self.BVC_ResumeMoveMessages.restype = c_short
        self.BVC_ResumeMoveMessages.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_SetBacklash = self.lib.BVC_SetBacklash
        self.BVC_SetBacklash.restype = c_short
        self.BVC_SetBacklash.argtypes = [POINTER(c_char), c_long]
        # *serialNo, distance

        self.BVC_SetDCPIDParams = self.lib.BVC_SetDCPIDParams
        self.BVC_SetDCPIDParams.restype = c_short
        self.BVC_SetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
        # *DCproportionalIntegralDerivativeParams, *serialNo

        self.BVC_SetDigitalOutputs = self.lib.BVC_SetDigitalOutputs
        self.BVC_SetDigitalOutputs.restype = c_short
        self.BVC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.BVC_SetDirection = self.lib.BVC_SetDirection
        self.BVC_SetDirection.restype = None
        self.BVC_SetDirection.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, reverse

        self.BVC_SetEncoderCounter = self.lib.BVC_SetEncoderCounter
        self.BVC_SetEncoderCounter.restype = c_short
        self.BVC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.BVC_SetFrontPanelLock = self.lib.BVC_SetFrontPanelLock
        self.BVC_SetFrontPanelLock.restype = c_short
        self.BVC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, locked

        self.BVC_SetHomingParamsBlock = self.lib.BVC_SetHomingParamsBlock
        self.BVC_SetHomingParamsBlock.restype = c_short
        self.BVC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
        # *homingParams, *serialNo

        self.BVC_SetHomingVelocity = self.lib.BVC_SetHomingVelocity
        self.BVC_SetHomingVelocity.restype = c_short
        self.BVC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, velocity

        self.BVC_SetJogMode = self.lib.BVC_SetJogMode
        self.BVC_SetJogMode.restype = c_short
        self.BVC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
        # *serialNo, mode, stopMode

        self.BVC_SetJogParamsBlock = self.lib.BVC_SetJogParamsBlock
        self.BVC_SetJogParamsBlock.restype = c_short
        self.BVC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
        # *jogParams, *serialNo

        self.BVC_SetJogStepSize = self.lib.BVC_SetJogStepSize
        self.BVC_SetJogStepSize.restype = c_short
        self.BVC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, stepSize

        self.BVC_SetJogVelParams = self.lib.BVC_SetJogVelParams
        self.BVC_SetJogVelParams.restype = c_short
        self.BVC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.BVC_SetLEDswitches = self.lib.BVC_SetLEDswitches
        self.BVC_SetLEDswitches.restype = c_short
        self.BVC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
        # *serialNo, LEDswitches

        self.BVC_SetLimitSwitchParams = self.lib.BVC_SetLimitSwitchParams
        self.BVC_SetLimitSwitchParams.restype = c_short
        self.BVC_SetLimitSwitchParams.argtypes = [
            POINTER(c_char),
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchModes,
            c_uint,
            MOT_LimitSwitchSWModes]
        # *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, clockwiseHardwareLimit, clockwisePosition, softLimitMode

        self.BVC_SetLimitSwitchParamsBlock = self.lib.BVC_SetLimitSwitchParamsBlock
        self.BVC_SetLimitSwitchParamsBlock.restype = c_short
        self.BVC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
        # *limitSwitchParams, *serialNo

        self.BVC_SetLimitsSoftwareApproachPolicy = self.lib.BVC_SetLimitsSoftwareApproachPolicy
        self.BVC_SetLimitsSoftwareApproachPolicy.restype = None
        self.BVC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
        # *serialNo, limitsSoftwareApproachPolicy

        self.BVC_SetMMIParams = self.lib.BVC_SetMMIParams
        self.BVC_SetMMIParams.restype = c_short
        self.BVC_SetMMIParams.argtypes = [
            POINTER(c_char),
            KMOT_WheelDirectionSense,
            c_int16,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            KMOT_WheelMode]
        # *serialNo, directionSense, displayIntensity, presetPosition1, presetPosition2, wheelAcceleration, wheelMaxVelocity, wheelMode

        self.BVC_SetMMIParamsBlock = self.lib.BVC_SetMMIParamsBlock
        self.BVC_SetMMIParamsBlock.restype = c_short
        self.BVC_SetMMIParamsBlock.argtypes = [KMOT_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.BVC_SetMMIParamsExt = self.lib.BVC_SetMMIParamsExt
        self.BVC_SetMMIParamsExt.restype = c_short
        self.BVC_SetMMIParamsExt.argtypes = [
            POINTER(c_char),
            KMOT_WheelDirectionSense,
            c_int16,
            c_int16,
            c_int16,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            KMOT_WheelMode]
        # *serialNo, directionSense, displayDimIntensity, displayIntensity, displayTimeout, presetPosition1, presetPosition2, wheelAcceleration, wheelMaxVelocity, wheelMode

        self.BVC_SetMotorParams = self.lib.BVC_SetMotorParams
        self.BVC_SetMotorParams.restype = c_short
        self.BVC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.BVC_SetMotorParamsExt = self.lib.BVC_SetMotorParamsExt
        self.BVC_SetMotorParamsExt.restype = c_short
        self.BVC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
        # *serialNo, gearBoxRatio, pitch, stepsPerRev

        self.BVC_SetMotorTravelLimits = self.lib.BVC_SetMotorTravelLimits
        self.BVC_SetMotorTravelLimits.restype = c_short
        self.BVC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxPosition, minPosition

        self.BVC_SetMotorTravelMode = self.lib.BVC_SetMotorTravelMode
        self.BVC_SetMotorTravelMode.restype = c_short
        self.BVC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
        # *serialNo, travelMode

        self.BVC_SetMotorVelocityLimits = self.lib.BVC_SetMotorVelocityLimits
        self.BVC_SetMotorVelocityLimits.restype = c_short
        self.BVC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
        # *serialNo, maxAcceleration, maxVelocity

        self.BVC_SetMoveAbsolutePosition = self.lib.BVC_SetMoveAbsolutePosition
        self.BVC_SetMoveAbsolutePosition.restype = c_short
        self.BVC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, position

        self.BVC_SetMoveRelativeDistance = self.lib.BVC_SetMoveRelativeDistance
        self.BVC_SetMoveRelativeDistance.restype = c_short
        self.BVC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
        # *serialNo, distance

        self.BVC_SetPositionCounter = self.lib.BVC_SetPositionCounter
        self.BVC_SetPositionCounter.restype = c_short
        self.BVC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, count

        self.BVC_SetRotationModes = self.lib.BVC_SetRotationModes
        self.BVC_SetRotationModes.restype = c_short
        self.BVC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementDirections, MOT_MovementModes]
        # *serialNo, direction, mode

        self.BVC_SetScanParams = self.lib.BVC_SetScanParams
        self.BVC_SetScanParams.restype = c_short
        self.BVC_SetScanParams.argtypes = [MOT_BVC_ScanParams, POINTER(c_char)]
        # *scanParameters, *serialNo

        self.BVC_SetStageAxisLimits = self.lib.BVC_SetStageAxisLimits
        self.BVC_SetStageAxisLimits.restype = c_short
        self.BVC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, maxPosition, minPosition

        self.BVC_SetTriggerConfigParams = self.lib.BVC_SetTriggerConfigParams
        self.BVC_SetTriggerConfigParams.restype = c_short
        self.BVC_SetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity]
        # *serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

        self.BVC_SetTriggerConfigParamsBlock = self.lib.BVC_SetTriggerConfigParamsBlock
        self.BVC_SetTriggerConfigParamsBlock.restype = c_short
        self.BVC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.BVC_SetTriggerParamsParams = self.lib.BVC_SetTriggerParamsParams
        self.BVC_SetTriggerParamsParams.restype = c_short
        self.BVC_SetTriggerParamsParams.argtypes = [
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

        self.BVC_SetTriggerParamsParamsBlock = self.lib.BVC_SetTriggerParamsParamsBlock
        self.BVC_SetTriggerParamsParamsBlock.restype = c_short
        self.BVC_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
        # *serialNo, *triggerParamsParams

        self.BVC_SetVelParams = self.lib.BVC_SetVelParams
        self.BVC_SetVelParams.restype = c_short
        self.BVC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, acceleration, maxVelocity

        self.BVC_SetVelParamsBlock = self.lib.BVC_SetVelParamsBlock
        self.BVC_SetVelParamsBlock.restype = c_short
        self.BVC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
        # *serialNo, *velocityParams

        self.BVC_StartPolling = self.lib.BVC_StartPolling
        self.BVC_StartPolling.restype = c_bool
        self.BVC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.BVC_StartScanning = self.lib.BVC_StartScanning
        self.BVC_StartScanning.restype = c_short
        self.BVC_StartScanning.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_StopImmediate = self.lib.BVC_StopImmediate
        self.BVC_StopImmediate.restype = c_short
        self.BVC_StopImmediate.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_StopPolling = self.lib.BVC_StopPolling
        self.BVC_StopPolling.restype = None
        self.BVC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_StopProfiled = self.lib.BVC_StopProfiled
        self.BVC_StopProfiled.restype = c_short
        self.BVC_StopProfiled.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_StopScanning = self.lib.BVC_StopScanning
        self.BVC_StopScanning.restype = c_short
        self.BVC_StopScanning.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_SuspendMoveMessages = self.lib.BVC_SuspendMoveMessages
        self.BVC_SuspendMoveMessages.restype = c_short
        self.BVC_SuspendMoveMessages.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BVC_TimeSinceLastMsgReceived = self.lib.BVC_TimeSinceLastMsgReceived
        self.BVC_TimeSinceLastMsgReceived.restype = c_bool
        self.BVC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.BVC_WaitForMessage = self.lib.BVC_WaitForMessage
        self.BVC_WaitForMessage.restype = c_bool
        self.BVC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
