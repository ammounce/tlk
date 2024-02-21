from c_types import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_double,
    c_int,
    c_int16,
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
    KMOT_WheelDirectionSense,
    KMOT_WheelMode,
    MOT_JogModes,
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
    MOT_BrushlessCurrentLoopParameters,
    MOT_BrushlessElectricOutputParameters,
    MOT_BrushlessPositionLoopParameters,
    MOT_BrushlessTrackSettleParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_StageAxisParameters,
    MOT_VelocityParameters,
    MOT_VelocityProfileParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class KCubeBrushlessMotor(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.KCube.BrushlessMotor.dll")

        self.BMC_CanDeviceLockFrontPanel = self.lib.BMC_CanDeviceLockFrontPanel
        self.BMC_CanDeviceLockFrontPanel.restype = c_bool
        self.BMC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_CanHome = self.lib.BMC_CanHome
        self.BMC_CanHome.restype = c_bool
        self.BMC_CanHome.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_CanMoveWithoutHomingFirst = self.lib.BMC_CanMoveWithoutHomingFirst
        self.BMC_CanMoveWithoutHomingFirst.restype = c_bool
        self.BMC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_CheckConnection = self.lib.BMC_CheckConnection
        self.BMC_CheckConnection.restype = c_bool
        self.BMC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_ClearMessageQueue = self.lib.BMC_ClearMessageQueue
        self.BMC_ClearMessageQueue.restype = c_short
        self.BMC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_Close = self.lib.BMC_Close
        self.BMC_Close.restype = c_short
        self.BMC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_DisableChannel = self.lib.BMC_DisableChannel
        self.BMC_DisableChannel.restype = c_short
        self.BMC_DisableChannel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_EnableChannel = self.lib.BMC_EnableChannel
        self.BMC_EnableChannel.restype = c_short
        self.BMC_EnableChannel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_EnableLastMsgTimer = self.lib.BMC_EnableLastMsgTimer
        self.BMC_EnableLastMsgTimer.restype = None
        self.BMC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]
        # *serialNo, channel, enable, lastMsgTimeout

        self.BMC_GetBacklash = self.lib.BMC_GetBacklash
        self.BMC_GetBacklash.restype = c_long
        self.BMC_GetBacklash.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetCurrentLoopParams = self.lib.BMC_GetCurrentLoopParams
        self.BMC_GetCurrentLoopParams.restype = c_short
        self.BMC_GetCurrentLoopParams.argtypes = [
            MOT_BrushlessCurrentLoopParameters,
            POINTER(c_char),
            POINTER(c_char),
            c_short]
        # *currentLoopParams, *serialNo, *serialNo, channel

        self.BMC_GetDeviceUnitFromRealValue = self.lib.BMC_GetDeviceUnitFromRealValue
        self.BMC_GetDeviceUnitFromRealValue.restype = c_short
        self.BMC_GetDeviceUnitFromRealValue.argtypes = [c_int, POINTER(c_char), c_short, c_double, c_int]
        # *device_unit, *serialNo, channel, real_unit, unitType

        self.BMC_GetDigitalOutputs = self.lib.BMC_GetDigitalOutputs
        self.BMC_GetDigitalOutputs.restype = c_byte
        self.BMC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetElectricOutputParams = self.lib.BMC_GetElectricOutputParams
        self.BMC_GetElectricOutputParams.restype = c_short
        self.BMC_GetElectricOutputParams.argtypes = [
            MOT_BrushlessElectricOutputParameters, POINTER(c_char), POINTER(c_char), c_short]
        # *electricOutputParams, *serialNo, *serialNo, channel

        self.BMC_GetEncoderCounter = self.lib.BMC_GetEncoderCounter
        self.BMC_GetEncoderCounter.restype = c_long
        self.BMC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetFirmwareVersion = self.lib.BMC_GetFirmwareVersion
        self.BMC_GetFirmwareVersion.restype = c_ulong
        self.BMC_GetFirmwareVersion.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetFrontPanelLocked = self.lib.BMC_GetFrontPanelLocked
        self.BMC_GetFrontPanelLocked.restype = c_bool
        self.BMC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_GetHardwareInfo = self.lib.BMC_GetHardwareInfo
        self.BMC_GetHardwareInfo.restype = c_short
        self.BMC_GetHardwareInfo.argtypes = [
            c_ulong,
            c_long,
            POINTER(c_char),
            c_long,
            POINTER(c_char),
            c_short,
            POINTER(c_char),
            c_long,
            c_short,
            c_ulong,
            c_ulong]
        # *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numChannels, *serialNo, *type, channel, sizeOfModelNo, sizeOfNotes

        self.BMC_GetHardwareInfoBlock = self.lib.BMC_GetHardwareInfoBlock
        self.BMC_GetHardwareInfoBlock.restype = c_short
        self.BMC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char), c_short]
        # *hardwareInfo, *serialNo, channel

        self.BMC_GetHomingParamsBlock = self.lib.BMC_GetHomingParamsBlock
        self.BMC_GetHomingParamsBlock.restype = c_short
        self.BMC_GetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), POINTER(c_char), c_short]
        # *homingParams, *serialNo, *serialNo, channel

        self.BMC_GetHomingVelocity = self.lib.BMC_GetHomingVelocity
        self.BMC_GetHomingVelocity.restype = c_uint
        self.BMC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetJogMode = self.lib.BMC_GetJogMode
        self.BMC_GetJogMode.restype = c_short
        self.BMC_GetJogMode.argtypes = [MOT_JogModes, POINTER(c_char), MOT_StopModes, c_short]
        # *mode, *serialNo, *stopMode, channel

        self.BMC_GetJogParamsBlock = self.lib.BMC_GetJogParamsBlock
        self.BMC_GetJogParamsBlock.restype = c_short
        self.BMC_GetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char), POINTER(c_char), c_short]
        # *jogParams, *serialNo, *serialNo, channel

        self.BMC_GetJogStepSize = self.lib.BMC_GetJogStepSize
        self.BMC_GetJogStepSize.restype = c_uint
        self.BMC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetJogVelParams = self.lib.BMC_GetJogVelParams
        self.BMC_GetJogVelParams.restype = c_short
        self.BMC_GetJogVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
        # *acceleration, *maxVelocity, *serialNo, channel

        self.BMC_GetMMIParams = self.lib.BMC_GetMMIParams
        self.BMC_GetMMIParams.restype = c_short
        self.BMC_GetMMIParams.argtypes = [KMOT_WheelDirectionSense, c_int16,
                                          c_int32, c_int32, POINTER(c_char), c_int32, c_int32, KMOT_WheelMode]
        # *directionSense, *displayIntensity, *presetPosition1, *presetPosition2, *serialNo, *wheelAcceleration, *wheelMaxVelocity, *wheelMode

        self.BMC_GetMMIParamsBlock = self.lib.BMC_GetMMIParamsBlock
        self.BMC_GetMMIParamsBlock.restype = c_short
        self.BMC_GetMMIParamsBlock.argtypes = [KMOT_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.BMC_GetMMIParamsExt = self.lib.BMC_GetMMIParamsExt
        self.BMC_GetMMIParamsExt.restype = c_short
        self.BMC_GetMMIParamsExt.argtypes = [
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

        self.BMC_GetMotorParams = self.lib.BMC_GetMotorParams
        self.BMC_GetMotorParams.restype = c_short
        self.BMC_GetMotorParams.argtypes = [c_long, POINTER(c_char), c_short]
        # *countsPerUnit, *serialNo, channel

        self.BMC_GetMotorParamsExt = self.lib.BMC_GetMotorParamsExt
        self.BMC_GetMotorParamsExt.restype = c_short
        self.BMC_GetMotorParamsExt.argtypes = [c_double, POINTER(c_char), c_short]
        # *countsPerUnit, *serialNo, channel

        self.BMC_GetMotorTravelLimits = self.lib.BMC_GetMotorTravelLimits
        self.BMC_GetMotorTravelLimits.restype = c_short
        self.BMC_GetMotorTravelLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
        # *maxPosition, *minPosition, *serialNo, channel

        self.BMC_GetMotorTravelMode = self.lib.BMC_GetMotorTravelMode
        self.BMC_GetMotorTravelMode.restype = MOT_TravelModes
        self.BMC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetMotorVelocityLimits = self.lib.BMC_GetMotorVelocityLimits
        self.BMC_GetMotorVelocityLimits.restype = c_short
        self.BMC_GetMotorVelocityLimits.argtypes = [c_double, c_double, POINTER(c_char), c_short]
        # *maxAcceleration, *maxVelocity, *serialNo, channel

        self.BMC_GetMoveAbsolutePosition = self.lib.BMC_GetMoveAbsolutePosition
        self.BMC_GetMoveAbsolutePosition.restype = c_int
        self.BMC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetMoveRelativeDistance = self.lib.BMC_GetMoveRelativeDistance
        self.BMC_GetMoveRelativeDistance.restype = c_int
        self.BMC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetNextMessage = self.lib.BMC_GetNextMessage
        self.BMC_GetNextMessage.restype = c_bool
        self.BMC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
        # *messageData, *messageID, *messageType, *serialNo, channel

        self.BMC_GetNumberPositions = self.lib.BMC_GetNumberPositions
        self.BMC_GetNumberPositions.restype = c_int
        self.BMC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetPosLoopParams = self.lib.BMC_GetPosLoopParams
        self.BMC_GetPosLoopParams.restype = c_short
        self.BMC_GetPosLoopParams.argtypes = [
            MOT_BrushlessPositionLoopParameters,
            POINTER(c_char),
            POINTER(c_char),
            c_short]
        # *positionLoopParams, *serialNo, *serialNo, channel

        self.BMC_GetPosition = self.lib.BMC_GetPosition
        self.BMC_GetPosition.restype = c_int
        self.BMC_GetPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetPositionCounter = self.lib.BMC_GetPositionCounter
        self.BMC_GetPositionCounter.restype = c_long
        self.BMC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetRealValueFromDeviceUnit = self.lib.BMC_GetRealValueFromDeviceUnit
        self.BMC_GetRealValueFromDeviceUnit.restype = c_short
        self.BMC_GetRealValueFromDeviceUnit.argtypes = [c_double, POINTER(c_char), c_short, c_int, c_int]
        # *real_unit, *serialNo, channel, device_unit, unitType

        self.BMC_GetSoftLimitMode = self.lib.BMC_GetSoftLimitMode
        self.BMC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
        self.BMC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetSoftwareVersion = self.lib.BMC_GetSoftwareVersion
        self.BMC_GetSoftwareVersion.restype = c_ulong
        self.BMC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_GetStageAxisMaxPos = self.lib.BMC_GetStageAxisMaxPos
        self.BMC_GetStageAxisMaxPos.restype = c_int
        self.BMC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetStageAxisMinPos = self.lib.BMC_GetStageAxisMinPos
        self.BMC_GetStageAxisMinPos.restype = c_int
        self.BMC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetStageAxisParams = self.lib.BMC_GetStageAxisParams
        self.BMC_GetStageAxisParams.restype = c_short
        self.BMC_GetStageAxisParams.argtypes = [
            c_long,
            c_ulong,
            c_int,
            c_int,
            c_int,
            c_int,
            c_int,
            POINTER(c_char),
            POINTER(c_char),
            POINTER(c_char),
            c_ulong,
            c_long,
            c_short,
            c_ulong]
        # *axisID, *countsPerUnit, *maxAcceleration, *maxDecceleration, *maxPosition, *maxVelocity, *minPosition, *partNumber, *serialNo, *serialNo, *serialNumber, *stageID, channel, size

        self.BMC_GetStageAxisParamsBlock = self.lib.BMC_GetStageAxisParamsBlock
        self.BMC_GetStageAxisParamsBlock.restype = c_short
        self.BMC_GetStageAxisParamsBlock.argtypes = [POINTER(c_char), POINTER(c_char), MOT_StageAxisParameters, c_short]
        # *serialNo, *serialNo, *stageAxisParams, channel

        self.BMC_GetStatusBits = self.lib.BMC_GetStatusBits
        self.BMC_GetStatusBits.restype = c_ulong
        self.BMC_GetStatusBits.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetTrackSettleParams = self.lib.BMC_GetTrackSettleParams
        self.BMC_GetTrackSettleParams.restype = c_short
        self.BMC_GetTrackSettleParams.argtypes = [POINTER(c_char), POINTER(
            c_char), MOT_BrushlessTrackSettleParameters, c_short]
        # *serialNo, *serialNo, *settleParams, channel

        self.BMC_GetTriggerConfigParams = self.lib.BMC_GetTriggerConfigParams
        self.BMC_GetTriggerConfigParams.restype = c_short
        self.BMC_GetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity]
        # *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity

        self.BMC_GetTriggerConfigParamsBlock = self.lib.BMC_GetTriggerConfigParamsBlock
        self.BMC_GetTriggerConfigParamsBlock.restype = c_short
        self.BMC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.BMC_GetTriggerParamsParams = self.lib.BMC_GetTriggerParamsParams
        self.BMC_GetTriggerParamsParams.restype = c_short
        self.BMC_GetTriggerParamsParams.argtypes = [
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

        self.BMC_GetTriggerParamsParamsBlock = self.lib.BMC_GetTriggerParamsParamsBlock
        self.BMC_GetTriggerParamsParamsBlock.restype = c_short
        self.BMC_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
        # *serialNo, *triggerParamsParams

        self.BMC_GetTriggerSwitches = self.lib.BMC_GetTriggerSwitches
        self.BMC_GetTriggerSwitches.restype = c_byte
        self.BMC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_GetVelParams = self.lib.BMC_GetVelParams
        self.BMC_GetVelParams.restype = c_short
        self.BMC_GetVelParams.argtypes = [c_int, c_int, POINTER(c_char), c_short]
        # *acceleration, *maxVelocity, *serialNo, channel

        self.BMC_GetVelParamsBlock = self.lib.BMC_GetVelParamsBlock
        self.BMC_GetVelParamsBlock.restype = c_short
        self.BMC_GetVelParamsBlock.argtypes = [POINTER(c_char), POINTER(c_char), MOT_VelocityParameters, c_short]
        # *serialNo, *serialNo, *velocityParams, channel

        self.BMC_GetVelocityProfileParams = self.lib.BMC_GetVelocityProfileParams
        self.BMC_GetVelocityProfileParams.restype = c_short
        self.BMC_GetVelocityProfileParams.argtypes = [
            POINTER(c_char), POINTER(c_char), MOT_VelocityProfileParameters, c_short]
        # *serialNo, *serialNo, *velocityProfileParams, channel

        self.BMC_HasLastMsgTimerOverrun = self.lib.BMC_HasLastMsgTimerOverrun
        self.BMC_HasLastMsgTimerOverrun.restype = c_bool
        self.BMC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_Home = self.lib.BMC_Home
        self.BMC_Home.restype = c_short
        self.BMC_Home.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_Identify = self.lib.BMC_Identify
        self.BMC_Identify.restype = None
        self.BMC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_LoadNamedSettings = self.lib.BMC_LoadNamedSettings
        self.BMC_LoadNamedSettings.restype = c_bool
        self.BMC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *serialNo, *settingsName, channel

        self.BMC_LoadSettings = self.lib.BMC_LoadSettings
        self.BMC_LoadSettings.restype = c_bool
        self.BMC_LoadSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_MessageQueueSize = self.lib.BMC_MessageQueueSize
        self.BMC_MessageQueueSize.restype = c_int
        self.BMC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_MoveAbsolute = self.lib.BMC_MoveAbsolute
        self.BMC_MoveAbsolute.restype = c_short
        self.BMC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_MoveAtVelocity = self.lib.BMC_MoveAtVelocity
        self.BMC_MoveAtVelocity.restype = c_short
        self.BMC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
        # *serialNo, channel, direction

        self.BMC_MoveJog = self.lib.BMC_MoveJog
        self.BMC_MoveJog.restype = c_short
        self.BMC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]
        # *serialNo, channel, jogDirection

        self.BMC_MoveRelative = self.lib.BMC_MoveRelative
        self.BMC_MoveRelative.restype = c_short
        self.BMC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, displacement

        self.BMC_MoveRelativeDistance = self.lib.BMC_MoveRelativeDistance
        self.BMC_MoveRelativeDistance.restype = c_short
        self.BMC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_MoveToPosition = self.lib.BMC_MoveToPosition
        self.BMC_MoveToPosition.restype = c_short
        self.BMC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, index

        self.BMC_NeedsHoming = self.lib.BMC_NeedsHoming
        self.BMC_NeedsHoming.restype = c_bool
        self.BMC_NeedsHoming.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_Open = self.lib.BMC_Open
        self.BMC_Open.restype = c_short
        self.BMC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_OverrideHomeRequirement = self.lib.BMC_OverrideHomeRequirement
        self.BMC_OverrideHomeRequirement.restype = c_short
        self.BMC_OverrideHomeRequirement.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_PersistSettings = self.lib.BMC_PersistSettings
        self.BMC_PersistSettings.restype = c_bool
        self.BMC_PersistSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_PollingDuration = self.lib.BMC_PollingDuration
        self.BMC_PollingDuration.restype = c_long
        self.BMC_PollingDuration.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RegisterMessageCallback = self.lib.BMC_RegisterMessageCallback
        self.BMC_RegisterMessageCallback.restype = c_short
        self.BMC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, None]
        # *serialNo, channel, void

        self.BMC_RequestBacklash = self.lib.BMC_RequestBacklash
        self.BMC_RequestBacklash.restype = c_short
        self.BMC_RequestBacklash.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestCurrentLoopParams = self.lib.BMC_RequestCurrentLoopParams
        self.BMC_RequestCurrentLoopParams.restype = c_short
        self.BMC_RequestCurrentLoopParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestDigitalOutputs = self.lib.BMC_RequestDigitalOutputs
        self.BMC_RequestDigitalOutputs.restype = c_short
        self.BMC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestElectricOutputParams = self.lib.BMC_RequestElectricOutputParams
        self.BMC_RequestElectricOutputParams.restype = c_short
        self.BMC_RequestElectricOutputParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestEncoderCounter = self.lib.BMC_RequestEncoderCounter
        self.BMC_RequestEncoderCounter.restype = c_short
        self.BMC_RequestEncoderCounter.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestFrontPanelLocked = self.lib.BMC_RequestFrontPanelLocked
        self.BMC_RequestFrontPanelLocked.restype = c_short
        self.BMC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_RequestHomingParams = self.lib.BMC_RequestHomingParams
        self.BMC_RequestHomingParams.restype = c_short
        self.BMC_RequestHomingParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestJogParams = self.lib.BMC_RequestJogParams
        self.BMC_RequestJogParams.restype = c_short
        self.BMC_RequestJogParams.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *serialNo, *serialNo, channel

        self.BMC_RequestMMIparams = self.lib.BMC_RequestMMIparams
        self.BMC_RequestMMIparams.restype = c_short
        self.BMC_RequestMMIparams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_RequestMoveAbsolutePosition = self.lib.BMC_RequestMoveAbsolutePosition
        self.BMC_RequestMoveAbsolutePosition.restype = c_short
        self.BMC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestMoveRelativeDistance = self.lib.BMC_RequestMoveRelativeDistance
        self.BMC_RequestMoveRelativeDistance.restype = c_short
        self.BMC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestPosLoopParams = self.lib.BMC_RequestPosLoopParams
        self.BMC_RequestPosLoopParams.restype = c_short
        self.BMC_RequestPosLoopParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestPosTriggerParams = self.lib.BMC_RequestPosTriggerParams
        self.BMC_RequestPosTriggerParams.restype = c_short
        self.BMC_RequestPosTriggerParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_RequestPosition = self.lib.BMC_RequestPosition
        self.BMC_RequestPosition.restype = c_short
        self.BMC_RequestPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestSettings = self.lib.BMC_RequestSettings
        self.BMC_RequestSettings.restype = c_short
        self.BMC_RequestSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestStageAxisParams = self.lib.BMC_RequestStageAxisParams
        self.BMC_RequestStageAxisParams.restype = c_short
        self.BMC_RequestStageAxisParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestStatusBits = self.lib.BMC_RequestStatusBits
        self.BMC_RequestStatusBits.restype = c_short
        self.BMC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestTrackSettleParams = self.lib.BMC_RequestTrackSettleParams
        self.BMC_RequestTrackSettleParams.restype = c_short
        self.BMC_RequestTrackSettleParams.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *serialNo, *serialNo, channel

        self.BMC_RequestTriggerConfigParams = self.lib.BMC_RequestTriggerConfigParams
        self.BMC_RequestTriggerConfigParams.restype = c_short
        self.BMC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.BMC_RequestTriggerSwitches = self.lib.BMC_RequestTriggerSwitches
        self.BMC_RequestTriggerSwitches.restype = c_short
        self.BMC_RequestTriggerSwitches.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestVelParams = self.lib.BMC_RequestVelParams
        self.BMC_RequestVelParams.restype = c_short
        self.BMC_RequestVelParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_RequestVelocityProfileParams = self.lib.BMC_RequestVelocityProfileParams
        self.BMC_RequestVelocityProfileParams.restype = c_short
        self.BMC_RequestVelocityProfileParams.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_ResetRotationModes = self.lib.BMC_ResetRotationModes
        self.BMC_ResetRotationModes.restype = c_short
        self.BMC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_ResetStageToDefaults = self.lib.BMC_ResetStageToDefaults
        self.BMC_ResetStageToDefaults.restype = c_short
        self.BMC_ResetStageToDefaults.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_ResumeMoveMessages = self.lib.BMC_ResumeMoveMessages
        self.BMC_ResumeMoveMessages.restype = c_short
        self.BMC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_SetBacklash = self.lib.BMC_SetBacklash
        self.BMC_SetBacklash.restype = c_short
        self.BMC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, distance

        self.BMC_SetCurrentLoopParams = self.lib.BMC_SetCurrentLoopParams
        self.BMC_SetCurrentLoopParams.restype = c_short
        self.BMC_SetCurrentLoopParams.argtypes = [
            MOT_BrushlessCurrentLoopParameters,
            POINTER(c_char),
            POINTER(c_char),
            c_short]
        # *currentLoopParams, *serialNo, *serialNo, channel

        self.BMC_SetDigitalOutputs = self.lib.BMC_SetDigitalOutputs
        self.BMC_SetDigitalOutputs.restype = c_short
        self.BMC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]
        # *serialNo, channel, outputsBits

        self.BMC_SetDirection = self.lib.BMC_SetDirection
        self.BMC_SetDirection.restype = c_short
        self.BMC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]
        # *serialNo, channel, reverse

        self.BMC_SetElectricOutputParams = self.lib.BMC_SetElectricOutputParams
        self.BMC_SetElectricOutputParams.restype = c_short
        self.BMC_SetElectricOutputParams.argtypes = [
            MOT_BrushlessElectricOutputParameters, POINTER(c_char), POINTER(c_char), c_short]
        # *electricOutputParams, *serialNo, *serialNo, channel

        self.BMC_SetEncoderCounter = self.lib.BMC_SetEncoderCounter
        self.BMC_SetEncoderCounter.restype = c_short
        self.BMC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, count

        self.BMC_SetFrontPanelLock = self.lib.BMC_SetFrontPanelLock
        self.BMC_SetFrontPanelLock.restype = c_short
        self.BMC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, locked

        self.BMC_SetHomingParamsBlock = self.lib.BMC_SetHomingParamsBlock
        self.BMC_SetHomingParamsBlock.restype = c_short
        self.BMC_SetHomingParamsBlock.argtypes = [MOT_HomingParameters, POINTER(c_char), POINTER(c_char), c_short]
        # *homingParams, *serialNo, *serialNo, channel

        self.BMC_SetHomingVelocity = self.lib.BMC_SetHomingVelocity
        self.BMC_SetHomingVelocity.restype = c_short
        self.BMC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]
        # *serialNo, channel, velocity

        self.BMC_SetJogMode = self.lib.BMC_SetJogMode
        self.BMC_SetJogMode.restype = c_short
        self.BMC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]
        # *serialNo, channel, mode, stopMode

        self.BMC_SetJogParamsBlock = self.lib.BMC_SetJogParamsBlock
        self.BMC_SetJogParamsBlock.restype = c_short
        self.BMC_SetJogParamsBlock.argtypes = [MOT_JogParameters, POINTER(c_char), POINTER(c_char), c_short]
        # *jogParams, *serialNo, *serialNo, channel

        self.BMC_SetJogStepSize = self.lib.BMC_SetJogStepSize
        self.BMC_SetJogStepSize.restype = c_short
        self.BMC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]
        # *serialNo, channel, stepSize

        self.BMC_SetJogVelParams = self.lib.BMC_SetJogVelParams
        self.BMC_SetJogVelParams.restype = c_short
        self.BMC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
        # *serialNo, acceleration, channel, maxVelocity

        self.BMC_SetLimitsSoftwareApproachPolicy = self.lib.BMC_SetLimitsSoftwareApproachPolicy
        self.BMC_SetLimitsSoftwareApproachPolicy.restype = None
        self.BMC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]
        # *serialNo, channel, limitsSoftwareApproachPolicy

        self.BMC_SetMMIParams = self.lib.BMC_SetMMIParams
        self.BMC_SetMMIParams.restype = c_short
        self.BMC_SetMMIParams.argtypes = [
            POINTER(c_char),
            KMOT_WheelDirectionSense,
            c_int16,
            c_int32,
            c_int32,
            c_int32,
            c_int32,
            KMOT_WheelMode]
        # *serialNo, directionSense, displayIntensity, presetPosition1, presetPosition2, wheelAcceleration, wheelMaxVelocity, wheelMode

        self.BMC_SetMMIParamsBlock = self.lib.BMC_SetMMIParamsBlock
        self.BMC_SetMMIParamsBlock.restype = c_short
        self.BMC_SetMMIParamsBlock.argtypes = [KMOT_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.BMC_SetMMIParamsExt = self.lib.BMC_SetMMIParamsExt
        self.BMC_SetMMIParamsExt.restype = c_short
        self.BMC_SetMMIParamsExt.argtypes = [
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

        self.BMC_SetMotorParams = self.lib.BMC_SetMotorParams
        self.BMC_SetMotorParams.restype = c_short
        self.BMC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, countsPerUnit

        self.BMC_SetMotorParamsExt = self.lib.BMC_SetMotorParamsExt
        self.BMC_SetMotorParamsExt.restype = c_short
        self.BMC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double]
        # *serialNo, channel, countsPerUnit

        self.BMC_SetMotorTravelLimits = self.lib.BMC_SetMotorTravelLimits
        self.BMC_SetMotorTravelLimits.restype = c_short
        self.BMC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
        # *serialNo, channel, maxPosition, minPosition

        self.BMC_SetMotorTravelMode = self.lib.BMC_SetMotorTravelMode
        self.BMC_SetMotorTravelMode.restype = c_short
        self.BMC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]
        # *serialNo, channel, travelMode

        self.BMC_SetMotorVelocityLimits = self.lib.BMC_SetMotorVelocityLimits
        self.BMC_SetMotorVelocityLimits.restype = c_short
        self.BMC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]
        # *serialNo, channel, maxAcceleration, maxVelocity

        self.BMC_SetMoveAbsolutePosition = self.lib.BMC_SetMoveAbsolutePosition
        self.BMC_SetMoveAbsolutePosition.restype = c_short
        self.BMC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, position

        self.BMC_SetMoveRelativeDistance = self.lib.BMC_SetMoveRelativeDistance
        self.BMC_SetMoveRelativeDistance.restype = c_short
        self.BMC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, distance

        self.BMC_SetPosLoopParams = self.lib.BMC_SetPosLoopParams
        self.BMC_SetPosLoopParams.restype = c_short
        self.BMC_SetPosLoopParams.argtypes = [
            MOT_BrushlessPositionLoopParameters,
            POINTER(c_char),
            POINTER(c_char),
            c_short]
        # *positionLoopParams, *serialNo, *serialNo, channel

        self.BMC_SetPositionCounter = self.lib.BMC_SetPositionCounter
        self.BMC_SetPositionCounter.restype = c_short
        self.BMC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]
        # *serialNo, channel, count

        self.BMC_SetRotationModes = self.lib.BMC_SetRotationModes
        self.BMC_SetRotationModes.restype = c_short
        self.BMC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementDirections, MOT_MovementModes]
        # *serialNo, channel, direction, mode

        self.BMC_SetStageAxisLimits = self.lib.BMC_SetStageAxisLimits
        self.BMC_SetStageAxisLimits.restype = c_short
        self.BMC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]
        # *serialNo, channel, maxPosition, minPosition

        self.BMC_SetTrackSettleParams = self.lib.BMC_SetTrackSettleParams
        self.BMC_SetTrackSettleParams.restype = c_short
        self.BMC_SetTrackSettleParams.argtypes = [POINTER(c_char), POINTER(
            c_char), MOT_BrushlessTrackSettleParameters, c_short]
        # *serialNo, *serialNo, *settleParams, channel

        self.BMC_SetTriggerConfigParams = self.lib.BMC_SetTriggerConfigParams
        self.BMC_SetTriggerConfigParams.restype = c_short
        self.BMC_SetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity,
            KMOT_TriggerPortMode,
            KMOT_TriggerPortPolarity]
        # *serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

        self.BMC_SetTriggerConfigParamsBlock = self.lib.BMC_SetTriggerConfigParamsBlock
        self.BMC_SetTriggerConfigParamsBlock.restype = c_short
        self.BMC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.BMC_SetTriggerParamsParams = self.lib.BMC_SetTriggerParamsParams
        self.BMC_SetTriggerParamsParams.restype = c_short
        self.BMC_SetTriggerParamsParams.argtypes = [
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

        self.BMC_SetTriggerParamsParamsBlock = self.lib.BMC_SetTriggerParamsParamsBlock
        self.BMC_SetTriggerParamsParamsBlock.restype = c_short
        self.BMC_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]
        # *serialNo, *triggerParamsParams

        self.BMC_SetTriggerSwitches = self.lib.BMC_SetTriggerSwitches
        self.BMC_SetTriggerSwitches.restype = c_short
        self.BMC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]
        # *serialNo, channel, indicatorBits

        self.BMC_SetVelParams = self.lib.BMC_SetVelParams
        self.BMC_SetVelParams.restype = c_short
        self.BMC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_short, c_int]
        # *serialNo, acceleration, channel, maxVelocity

        self.BMC_SetVelParamsBlock = self.lib.BMC_SetVelParamsBlock
        self.BMC_SetVelParamsBlock.restype = c_short
        self.BMC_SetVelParamsBlock.argtypes = [POINTER(c_char), POINTER(c_char), MOT_VelocityParameters, c_short]
        # *serialNo, *serialNo, *velocityParams, channel

        self.BMC_SetVelocityProfileParams = self.lib.BMC_SetVelocityProfileParams
        self.BMC_SetVelocityProfileParams.restype = c_short
        self.BMC_SetVelocityProfileParams.argtypes = [
            POINTER(c_char), POINTER(c_char), MOT_VelocityProfileParameters, c_short]
        # *serialNo, *serialNo, *velocityProfileParams, channel

        self.BMC_StartPolling = self.lib.BMC_StartPolling
        self.BMC_StartPolling.restype = c_bool
        self.BMC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, milliseconds

        self.BMC_StopImmediate = self.lib.BMC_StopImmediate
        self.BMC_StopImmediate.restype = c_short
        self.BMC_StopImmediate.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_StopPolling = self.lib.BMC_StopPolling
        self.BMC_StopPolling.restype = None
        self.BMC_StopPolling.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_StopProfiled = self.lib.BMC_StopProfiled
        self.BMC_StopProfiled.restype = c_short
        self.BMC_StopProfiled.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_SuspendMoveMessages = self.lib.BMC_SuspendMoveMessages
        self.BMC_SuspendMoveMessages.restype = c_short
        self.BMC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.BMC_TimeSinceLastMsgReceived = self.lib.BMC_TimeSinceLastMsgReceived
        self.BMC_TimeSinceLastMsgReceived.restype = c_bool
        self.BMC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char), c_short]
        # &lastUpdateTimeMS, *serialNo, channel

        self.BMC_WaitForMessage = self.lib.BMC_WaitForMessage
        self.BMC_WaitForMessage.restype = c_bool
        self.BMC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
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
