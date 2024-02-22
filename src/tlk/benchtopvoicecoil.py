from ctypes import (
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


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.Benchtop.VoiceCoil.dll")
BVC_CanDeviceLockFrontPanel = lib.BVC_CanDeviceLockFrontPanel
BVC_CanDeviceLockFrontPanel.restype = c_bool
BVC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
# *serialNo

BVC_CanHome = lib.BVC_CanHome
BVC_CanHome.restype = c_bool
BVC_CanHome.argtypes = [POINTER(c_char)]
# *serialNo

BVC_CanMoveWithoutHomingFirst = lib.BVC_CanMoveWithoutHomingFirst
BVC_CanMoveWithoutHomingFirst.restype = c_bool
BVC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]
# *serialNo

BVC_CheckConnection = lib.BVC_CheckConnection
BVC_CheckConnection.restype = c_bool
BVC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

BVC_ClearMessageQueue = lib.BVC_ClearMessageQueue
BVC_ClearMessageQueue.restype = None
BVC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

BVC_Close = lib.BVC_Close
BVC_Close.restype = None
BVC_Close.argtypes = [POINTER(c_char)]
# *serialNo

BVC_DisableChannel = lib.BVC_DisableChannel
BVC_DisableChannel.restype = c_short
BVC_DisableChannel.argtypes = [POINTER(c_char)]
# *serialNo

BVC_EnableChannel = lib.BVC_EnableChannel
BVC_EnableChannel.restype = c_short
BVC_EnableChannel.argtypes = [POINTER(c_char)]
# *serialNo

BVC_EnableLastMsgTimer = lib.BVC_EnableLastMsgTimer
BVC_EnableLastMsgTimer.restype = None
BVC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

BVC_GetBacklash = lib.BVC_GetBacklash
BVC_GetBacklash.restype = c_long
BVC_GetBacklash.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetDCPIDParams = lib.BVC_GetDCPIDParams
BVC_GetDCPIDParams.restype = c_short
BVC_GetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
# *DCproportionalIntegralDerivativeParams, *serialNo

BVC_GetDeviceUnitFromRealValue = lib.BVC_GetDeviceUnitFromRealValue
BVC_GetDeviceUnitFromRealValue.restype = c_short
BVC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_double, c_int]
# *device_unit, *serialNo, real_unit, unitType

BVC_GetDigitalOutputs = lib.BVC_GetDigitalOutputs
BVC_GetDigitalOutputs.restype = c_byte
BVC_GetDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetEncoderCounter = lib.BVC_GetEncoderCounter
BVC_GetEncoderCounter.restype = c_long
BVC_GetEncoderCounter.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetFrontPanelLocked = lib.BVC_GetFrontPanelLocked
BVC_GetFrontPanelLocked.restype = c_bool
BVC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetHardwareInfo = lib.BVC_GetHardwareInfo
BVC_GetHardwareInfo.restype = c_short
BVC_GetHardwareInfo.argtypes = [
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

BVC_GetHardwareInfoBlock = lib.BVC_GetHardwareInfoBlock
BVC_GetHardwareInfoBlock.restype = c_short
BVC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

BVC_GetHomingParamsBlock = lib.BVC_GetHomingParamsBlock
BVC_GetHomingParamsBlock.restype = c_short
BVC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
# *homingParams, *serialNo

BVC_GetHomingVelocity = lib.BVC_GetHomingVelocity
BVC_GetHomingVelocity.restype = c_uint
BVC_GetHomingVelocity.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetHubBay = lib.BVC_GetHubBay
BVC_GetHubBay.restype = POINTER(c_char)
BVC_GetHubBay.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetJogMode = lib.BVC_GetJogMode
BVC_GetJogMode.restype = c_short
BVC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes]
# *mode, *serialNo, *stopMode

BVC_GetJogParamsBlock = lib.BVC_GetJogParamsBlock
BVC_GetJogParamsBlock.restype = c_short
BVC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
# *jogParams, *serialNo

BVC_GetJogStepSize = lib.BVC_GetJogStepSize
BVC_GetJogStepSize.restype = c_uint
BVC_GetJogStepSize.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetJogVelParams = lib.BVC_GetJogVelParams
BVC_GetJogVelParams.restype = c_short
BVC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
# *acceleration, *maxVelocity, *serialNo

BVC_GetLEDswitches = lib.BVC_GetLEDswitches
BVC_GetLEDswitches.restype = c_long
BVC_GetLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetLimitSwitchParams = lib.BVC_GetLimitSwitchParams
BVC_GetLimitSwitchParams.restype = c_short
BVC_GetLimitSwitchParams.argtypes = [
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    POINTER(c_char),
    MOT_LimitSwitchSWModes]
# *anticlockwiseHardwareLimit, *anticlockwisePosition, *clockwiseHardwareLimit, *clockwisePosition, *serialNo, *softLimitMode

BVC_GetLimitSwitchParamsBlock = lib.BVC_GetLimitSwitchParamsBlock
BVC_GetLimitSwitchParamsBlock.restype = c_short
BVC_GetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
# *limitSwitchParams, *serialNo

BVC_GetMMIParams = lib.BVC_GetMMIParams
BVC_GetMMIParams.restype = c_short
BVC_GetMMIParams.argtypes = [
    KMOT_WheelDirectionSense,
    c_int16,
    c_int32,
    c_int32,
    POINTER(c_char),
    c_int32,
    c_int32,
    KMOT_WheelMode]
# *directionSense, *displayIntensity, *presetPosition1, *presetPosition2, *serialNo, *wheelAcceleration, *wheelMaxVelocity, *wheelMode

BVC_GetMMIParamsBlock = lib.BVC_GetMMIParamsBlock
BVC_GetMMIParamsBlock.restype = c_short
BVC_GetMMIParamsBlock.argtypes = [KMOT_MMIParams, POINTER(c_char)]
# *mmiParams, *serialNo

BVC_GetMMIParamsExt = lib.BVC_GetMMIParamsExt
BVC_GetMMIParamsExt.restype = c_short
BVC_GetMMIParamsExt.argtypes = [
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

BVC_GetMotorParams = lib.BVC_GetMotorParams
BVC_GetMotorParams.restype = c_short
BVC_GetMotorParams.argtypes = [c_long, c_float, POINTER(c_char), c_long]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

BVC_GetMotorParamsExt = lib.BVC_GetMotorParamsExt
BVC_GetMotorParamsExt.restype = c_short
BVC_GetMotorParamsExt.argtypes = [c_double, c_double, POINTER(c_char), c_double]
# *gearBoxRatio, *pitch, *serialNo, *stepsPerRev

BVC_GetMotorTravelLimits = lib.BVC_GetMotorTravelLimits
BVC_GetMotorTravelLimits.restype = c_short
BVC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char)]
# *maxPosition, *minPosition, *serialNo

BVC_GetMotorTravelMode = lib.BVC_GetMotorTravelMode
BVC_GetMotorTravelMode.restype = MOT_TravelModes
BVC_GetMotorTravelMode.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetMotorVelocityLimits = lib.BVC_GetMotorVelocityLimits
BVC_GetMotorVelocityLimits.restype = c_short
BVC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char)]
# *maxAcceleration, *maxVelocity, *serialNo

BVC_GetMoveAbsolutePosition = lib.BVC_GetMoveAbsolutePosition
BVC_GetMoveAbsolutePosition.restype = c_int
BVC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetMoveRelativeDistance = lib.BVC_GetMoveRelativeDistance
BVC_GetMoveRelativeDistance.restype = c_int
BVC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetNextMessage = lib.BVC_GetNextMessage
BVC_GetNextMessage.restype = c_bool
BVC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

BVC_GetNumberPositions = lib.BVC_GetNumberPositions
BVC_GetNumberPositions.restype = c_int
BVC_GetNumberPositions.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetPosition = lib.BVC_GetPosition
BVC_GetPosition.restype = c_int
BVC_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetPositionCounter = lib.BVC_GetPositionCounter
BVC_GetPositionCounter.restype = c_long
BVC_GetPositionCounter.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetRealValueFromDeviceUnit = lib.BVC_GetRealValueFromDeviceUnit
BVC_GetRealValueFromDeviceUnit.restype = c_short
BVC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_int, c_int]
# *real_unit, *serialNo, device_unit, unitType

BVC_GetScanParams = lib.BVC_GetScanParams
BVC_GetScanParams.restype = c_short
BVC_GetScanParams.argtypes = [MOT_BVC_ScanParams, POINTER(c_char)]
# *scanParameters, *serialNo

BVC_GetSoftLimitMode = lib.BVC_GetSoftLimitMode
BVC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
BVC_GetSoftLimitMode.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetSoftwareVersion = lib.BVC_GetSoftwareVersion
BVC_GetSoftwareVersion.restype = c_ulong
BVC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetStageAxisMaxPos = lib.BVC_GetStageAxisMaxPos
BVC_GetStageAxisMaxPos.restype = c_int
BVC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetStageAxisMinPos = lib.BVC_GetStageAxisMinPos
BVC_GetStageAxisMinPos.restype = c_int
BVC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetStatusBits = lib.BVC_GetStatusBits
BVC_GetStatusBits.restype = c_ulong
BVC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

BVC_GetTriggerConfigParams = lib.BVC_GetTriggerConfigParams
BVC_GetTriggerConfigParams.restype = c_short
BVC_GetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]
# *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity

BVC_GetTriggerConfigParamsBlock = lib.BVC_GetTriggerConfigParamsBlock
BVC_GetTriggerConfigParamsBlock.restype = c_short
BVC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
# *serialNo, *triggerConfigParams

BVC_GetTriggerParamsParams = lib.BVC_GetTriggerParamsParams
BVC_GetTriggerParamsParams.restype = c_short
BVC_GetTriggerParamsParams.argtypes = [
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

BVC_GetTriggerParamsParamsBlock = lib.BVC_GetTriggerParamsParamsBlock
BVC_GetTriggerParamsParamsBlock.restype = c_short
BVC_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
# *serialNo, *triggerParamsParams

BVC_GetVelParams = lib.BVC_GetVelParams
BVC_GetVelParams.restype = c_short
BVC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char)]
# *acceleration, *maxVelocity, *serialNo

BVC_GetVelParamsBlock = lib.BVC_GetVelParamsBlock
BVC_GetVelParamsBlock.restype = c_short
BVC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
# *serialNo, *velocityParams

BVC_HasLastMsgTimerOverrun = lib.BVC_HasLastMsgTimerOverrun
BVC_HasLastMsgTimerOverrun.restype = c_bool
BVC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

BVC_Home = lib.BVC_Home
BVC_Home.restype = c_short
BVC_Home.argtypes = [POINTER(c_char)]
# *serialNo

BVC_Identify = lib.BVC_Identify
BVC_Identify.restype = None
BVC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

BVC_IsScanning = lib.BVC_IsScanning
BVC_IsScanning.restype = c_bool
BVC_IsScanning.argtypes = [POINTER(c_char)]
# *serialNo

BVC_IsScanningEnabled = lib.BVC_IsScanningEnabled
BVC_IsScanningEnabled.restype = c_bool
BVC_IsScanningEnabled.argtypes = [POINTER(c_char)]
# *serialNo

BVC_LoadNamedSettings = lib.BVC_LoadNamedSettings
BVC_LoadNamedSettings.restype = c_bool
BVC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

BVC_LoadSettings = lib.BVC_LoadSettings
BVC_LoadSettings.restype = c_bool
BVC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

BVC_MessageQueueSize = lib.BVC_MessageQueueSize
BVC_MessageQueueSize.restype = c_int
BVC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

BVC_MoveAbsolute = lib.BVC_MoveAbsolute
BVC_MoveAbsolute.restype = c_short
BVC_MoveAbsolute.argtypes = [POINTER(c_char)]
# *serialNo

BVC_MoveAtVelocity = lib.BVC_MoveAtVelocity
BVC_MoveAtVelocity.restype = c_short
BVC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, direction

BVC_MoveJog = lib.BVC_MoveJog
BVC_MoveJog.restype = c_short
BVC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]
# *serialNo, jogDirection

BVC_MoveRelative = lib.BVC_MoveRelative
BVC_MoveRelative.restype = c_short
BVC_MoveRelative.argtypes = [POINTER(c_char), c_int]
# *serialNo, displacement

BVC_MoveRelativeDistance = lib.BVC_MoveRelativeDistance
BVC_MoveRelativeDistance.restype = c_short
BVC_MoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

BVC_MoveToPosition = lib.BVC_MoveToPosition
BVC_MoveToPosition.restype = c_short
BVC_MoveToPosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, index

BVC_NeedsHoming = lib.BVC_NeedsHoming
BVC_NeedsHoming.restype = c_bool
BVC_NeedsHoming.argtypes = [POINTER(c_char)]
# *serialNo

BVC_Open = lib.BVC_Open
BVC_Open.restype = c_short
BVC_Open.argtypes = [POINTER(c_char)]
# *serialNo

BVC_PersistSettings = lib.BVC_PersistSettings
BVC_PersistSettings.restype = c_bool
BVC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

BVC_PollingDuration = lib.BVC_PollingDuration
BVC_PollingDuration.restype = c_long
BVC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RegisterMessageCallback = lib.BVC_RegisterMessageCallback
BVC_RegisterMessageCallback.restype = None
BVC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

BVC_RequestBacklash = lib.BVC_RequestBacklash
BVC_RequestBacklash.restype = c_short
BVC_RequestBacklash.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestDCPIDParams = lib.BVC_RequestDCPIDParams
BVC_RequestDCPIDParams.restype = c_short
BVC_RequestDCPIDParams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestDigitalOutputs = lib.BVC_RequestDigitalOutputs
BVC_RequestDigitalOutputs.restype = c_short
BVC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestEncoderCounter = lib.BVC_RequestEncoderCounter
BVC_RequestEncoderCounter.restype = c_short
BVC_RequestEncoderCounter.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestFrontPanelLocked = lib.BVC_RequestFrontPanelLocked
BVC_RequestFrontPanelLocked.restype = c_short
BVC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestHomingParams = lib.BVC_RequestHomingParams
BVC_RequestHomingParams.restype = c_short
BVC_RequestHomingParams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestJogParams = lib.BVC_RequestJogParams
BVC_RequestJogParams.restype = c_short
BVC_RequestJogParams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestLEDswitches = lib.BVC_RequestLEDswitches
BVC_RequestLEDswitches.restype = c_short
BVC_RequestLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestLimitSwitchParams = lib.BVC_RequestLimitSwitchParams
BVC_RequestLimitSwitchParams.restype = c_short
BVC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestMMIparams = lib.BVC_RequestMMIparams
BVC_RequestMMIparams.restype = c_short
BVC_RequestMMIparams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestMoveAbsolutePosition = lib.BVC_RequestMoveAbsolutePosition
BVC_RequestMoveAbsolutePosition.restype = c_short
BVC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestMoveRelativeDistance = lib.BVC_RequestMoveRelativeDistance
BVC_RequestMoveRelativeDistance.restype = c_short
BVC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestPosTriggerParams = lib.BVC_RequestPosTriggerParams
BVC_RequestPosTriggerParams.restype = c_short
BVC_RequestPosTriggerParams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestPosition = lib.BVC_RequestPosition
BVC_RequestPosition.restype = c_short
BVC_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestScanParams = lib.BVC_RequestScanParams
BVC_RequestScanParams.restype = c_short
BVC_RequestScanParams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestSettings = lib.BVC_RequestSettings
BVC_RequestSettings.restype = c_short
BVC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestStatusBits = lib.BVC_RequestStatusBits
BVC_RequestStatusBits.restype = c_short
BVC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestTriggerConfigParams = lib.BVC_RequestTriggerConfigParams
BVC_RequestTriggerConfigParams.restype = c_short
BVC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_RequestVelParams = lib.BVC_RequestVelParams
BVC_RequestVelParams.restype = c_short
BVC_RequestVelParams.argtypes = [POINTER(c_char)]
# *serialNo

BVC_ResetRotationModes = lib.BVC_ResetRotationModes
BVC_ResetRotationModes.restype = c_short
BVC_ResetRotationModes.argtypes = [POINTER(c_char)]
# *serialNo

BVC_ResetStageToDefaults = lib.BVC_ResetStageToDefaults
BVC_ResetStageToDefaults.restype = c_short
BVC_ResetStageToDefaults.argtypes = [POINTER(c_char)]
# *serialNo

BVC_ResumeMoveMessages = lib.BVC_ResumeMoveMessages
BVC_ResumeMoveMessages.restype = c_short
BVC_ResumeMoveMessages.argtypes = [POINTER(c_char)]
# *serialNo

BVC_SetBacklash = lib.BVC_SetBacklash
BVC_SetBacklash.restype = c_short
BVC_SetBacklash.argtypes = [POINTER(c_char), c_long]
# *serialNo, distance

BVC_SetDCPIDParams = lib.BVC_SetDCPIDParams
BVC_SetDCPIDParams.restype = c_short
BVC_SetDCPIDParams.argtypes = [MOT_DC_PIDParameters, POINTER(c_char)]
# *DCproportionalIntegralDerivativeParams, *serialNo

BVC_SetDigitalOutputs = lib.BVC_SetDigitalOutputs
BVC_SetDigitalOutputs.restype = c_short
BVC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
# *serialNo, outputsBits

BVC_SetDirection = lib.BVC_SetDirection
BVC_SetDirection.restype = None
BVC_SetDirection.argtypes = [POINTER(c_char), c_bool]
# *serialNo, reverse

BVC_SetEncoderCounter = lib.BVC_SetEncoderCounter
BVC_SetEncoderCounter.restype = c_short
BVC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]
# *serialNo, count

BVC_SetFrontPanelLock = lib.BVC_SetFrontPanelLock
BVC_SetFrontPanelLock.restype = c_short
BVC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
# *serialNo, locked

BVC_SetHomingParamsBlock = lib.BVC_SetHomingParamsBlock
BVC_SetHomingParamsBlock.restype = c_short
BVC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char)]
# *homingParams, *serialNo

BVC_SetHomingVelocity = lib.BVC_SetHomingVelocity
BVC_SetHomingVelocity.restype = c_short
BVC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]
# *serialNo, velocity

BVC_SetJogMode = lib.BVC_SetJogMode
BVC_SetJogMode.restype = c_short
BVC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]
# *serialNo, mode, stopMode

BVC_SetJogParamsBlock = lib.BVC_SetJogParamsBlock
BVC_SetJogParamsBlock.restype = c_short
BVC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char)]
# *jogParams, *serialNo

BVC_SetJogStepSize = lib.BVC_SetJogStepSize
BVC_SetJogStepSize.restype = c_short
BVC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]
# *serialNo, stepSize

BVC_SetJogVelParams = lib.BVC_SetJogVelParams
BVC_SetJogVelParams.restype = c_short
BVC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, acceleration, maxVelocity

BVC_SetLEDswitches = lib.BVC_SetLEDswitches
BVC_SetLEDswitches.restype = c_short
BVC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
# *serialNo, LEDswitches

BVC_SetLimitSwitchParams = lib.BVC_SetLimitSwitchParams
BVC_SetLimitSwitchParams.restype = c_short
BVC_SetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchModes,
    c_uint,
    MOT_LimitSwitchSWModes]
# *serialNo, anticlockwiseHardwareLimit, anticlockwisePosition, clockwiseHardwareLimit, clockwisePosition, softLimitMode

BVC_SetLimitSwitchParamsBlock = lib.BVC_SetLimitSwitchParamsBlock
BVC_SetLimitSwitchParamsBlock.restype = c_short
BVC_SetLimitSwitchParamsBlock.argtypes = [MOT_LimitSwitchParameters, POINTER(c_char)]
# *limitSwitchParams, *serialNo

BVC_SetLimitsSoftwareApproachPolicy = lib.BVC_SetLimitsSoftwareApproachPolicy
BVC_SetLimitsSoftwareApproachPolicy.restype = None
BVC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]
# *serialNo, limitsSoftwareApproachPolicy

BVC_SetMMIParams = lib.BVC_SetMMIParams
BVC_SetMMIParams.restype = c_short
BVC_SetMMIParams.argtypes = [
    POINTER(c_char),
    KMOT_WheelDirectionSense,
    c_int16,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    KMOT_WheelMode]
# *serialNo, directionSense, displayIntensity, presetPosition1, presetPosition2, wheelAcceleration, wheelMaxVelocity, wheelMode

BVC_SetMMIParamsBlock = lib.BVC_SetMMIParamsBlock
BVC_SetMMIParamsBlock.restype = c_short
BVC_SetMMIParamsBlock.argtypes = [KMOT_MMIParams, POINTER(c_char)]
# *mmiParams, *serialNo

BVC_SetMMIParamsExt = lib.BVC_SetMMIParamsExt
BVC_SetMMIParamsExt.restype = c_short
BVC_SetMMIParamsExt.argtypes = [
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

BVC_SetMotorParams = lib.BVC_SetMotorParams
BVC_SetMotorParams.restype = c_short
BVC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_float, c_long]
# *serialNo, gearBoxRatio, pitch, stepsPerRev

BVC_SetMotorParamsExt = lib.BVC_SetMotorParamsExt
BVC_SetMotorParamsExt.restype = c_short
BVC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]
# *serialNo, gearBoxRatio, pitch, stepsPerRev

BVC_SetMotorTravelLimits = lib.BVC_SetMotorTravelLimits
BVC_SetMotorTravelLimits.restype = c_short
BVC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]
# *serialNo, maxPosition, minPosition

BVC_SetMotorTravelMode = lib.BVC_SetMotorTravelMode
BVC_SetMotorTravelMode.restype = c_short
BVC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]
# *serialNo, travelMode

BVC_SetMotorVelocityLimits = lib.BVC_SetMotorVelocityLimits
BVC_SetMotorVelocityLimits.restype = c_short
BVC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]
# *serialNo, maxAcceleration, maxVelocity

BVC_SetMoveAbsolutePosition = lib.BVC_SetMoveAbsolutePosition
BVC_SetMoveAbsolutePosition.restype = c_short
BVC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, position

BVC_SetMoveRelativeDistance = lib.BVC_SetMoveRelativeDistance
BVC_SetMoveRelativeDistance.restype = c_short
BVC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]
# *serialNo, distance

BVC_SetPositionCounter = lib.BVC_SetPositionCounter
BVC_SetPositionCounter.restype = c_short
BVC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]
# *serialNo, count

BVC_SetRotationModes = lib.BVC_SetRotationModes
BVC_SetRotationModes.restype = c_short
BVC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementDirections, MOT_MovementModes]
# *serialNo, direction, mode

BVC_SetScanParams = lib.BVC_SetScanParams
BVC_SetScanParams.restype = c_short
BVC_SetScanParams.argtypes = [MOT_BVC_ScanParams, POINTER(c_char)]
# *scanParameters, *serialNo

BVC_SetStageAxisLimits = lib.BVC_SetStageAxisLimits
BVC_SetStageAxisLimits.restype = c_short
BVC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, maxPosition, minPosition

BVC_SetTriggerConfigParams = lib.BVC_SetTriggerConfigParams
BVC_SetTriggerConfigParams.restype = c_short
BVC_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]
# *serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

BVC_SetTriggerConfigParamsBlock = lib.BVC_SetTriggerConfigParamsBlock
BVC_SetTriggerConfigParamsBlock.restype = c_short
BVC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
# *serialNo, *triggerConfigParams

BVC_SetTriggerParamsParams = lib.BVC_SetTriggerParamsParams
BVC_SetTriggerParamsParams.restype = c_short
BVC_SetTriggerParamsParams.argtypes = [
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

BVC_SetTriggerParamsParamsBlock = lib.BVC_SetTriggerParamsParamsBlock
BVC_SetTriggerParamsParamsBlock.restype = c_short
BVC_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
# *serialNo, *triggerParamsParams

BVC_SetVelParams = lib.BVC_SetVelParams
BVC_SetVelParams.restype = c_short
BVC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, acceleration, maxVelocity

BVC_SetVelParamsBlock = lib.BVC_SetVelParamsBlock
BVC_SetVelParamsBlock.restype = c_short
BVC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]
# *serialNo, *velocityParams

BVC_StartPolling = lib.BVC_StartPolling
BVC_StartPolling.restype = c_bool
BVC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

BVC_StartScanning = lib.BVC_StartScanning
BVC_StartScanning.restype = c_short
BVC_StartScanning.argtypes = [POINTER(c_char)]
# *serialNo

BVC_StopImmediate = lib.BVC_StopImmediate
BVC_StopImmediate.restype = c_short
BVC_StopImmediate.argtypes = [POINTER(c_char)]
# *serialNo

BVC_StopPolling = lib.BVC_StopPolling
BVC_StopPolling.restype = None
BVC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

BVC_StopProfiled = lib.BVC_StopProfiled
BVC_StopProfiled.restype = c_short
BVC_StopProfiled.argtypes = [POINTER(c_char)]
# *serialNo

BVC_StopScanning = lib.BVC_StopScanning
BVC_StopScanning.restype = c_short
BVC_StopScanning.argtypes = [POINTER(c_char)]
# *serialNo

BVC_SuspendMoveMessages = lib.BVC_SuspendMoveMessages
BVC_SuspendMoveMessages.restype = c_short
BVC_SuspendMoveMessages.argtypes = [POINTER(c_char)]
# *serialNo

BVC_TimeSinceLastMsgReceived = lib.BVC_TimeSinceLastMsgReceived
BVC_TimeSinceLastMsgReceived.restype = c_bool
BVC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

BVC_WaitForMessage = lib.BVC_WaitForMessage
BVC_WaitForMessage.restype = c_bool
BVC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
