from c_types import (
    Structure,
    c_bool,
    c_byte,
    c_float,
    c_int,
    c_int15,
    c_int16,
    c_int32,
    c_int32,
    c_long,
    c_short,
    c_uint,
    c_uint16,
    c_uint32,
    c_uint8,
    c_ulong,
     c_ushort)
from .enumerations import BNT_BNCTriggerModes, BNT_CurrentLimit, BNT_FeedbackSignalSelection, BNT_OutputLowPassFilter, FF_IOModes, FF_SignalModes, KIM_Channels, KIM_DirectionSense, KIM_FBSignalMode, KIM_JogMode, KIM_LimitSwitchModes, KIM_TravelDirection, KIM_TrigModes, KIM_TrigPolarities, KLD_TrigPolarity, KMOT_TriggerPortMode, KMOT_TriggerPortPolarity, KMOT_WheelMode, KNA_HighOutputVoltageRoute, KNA_HighVoltageRange, KNA_TIARange, KNA_TriggerPortMode, KNA_WheelAdjustRate, KPC_TriggerPortMode, KPC_TriggerPortPolarity, KPZ_TriggerPortMode, KPZ_TriggerPortPolarity, KPZ_WheelChangeRate, KPZ_WheelDirectionSense, KPZ_WheelMode, KSC_TriggerPortMode, MOD_IOPortMode, MOD_IOPortSource, MOT_ButtonModes, MOT_JogModes, MOT_LimitSwitchModes, MOT_LimitSwitchSWModes, MOT_StopModes, MOT_TravelDirection, MOT_TriggerInputConfigModes, MOT_TriggerInputSource, MOT_TriggerOutputConfigModes, MOT_TriggerPolarity, MPC_IOModes, MPC_SignalModes, NT_OddOrEven, NT_OutputVoltageRoute, NT_TIARangeMode, NT_VoltageRange, PPC_IOControlMode, QD_FilterEnable, QD_KPA_TrigModes, QD_KPA_TrigPolarities, QD_LowVoltageRoute, QD_OpenLoopHoldValues)

class BNT_IO_Settings(Structure):
    _fields_=[
        ("BNCtriggerOrLowVoltageOut", BNT_BNCTriggerModes)
        ("amplifierCurrentLimit", BNT_CurrentLimit)
        ("amplifierLowPassFilter", BNT_OutputLowPassFilter)
        ("channel", c_long)
        ("feedbackSignal", BNT_FeedbackSignalSelection)
        ]

class FF_IOSettings(Structure):
    _fields_ = [
        ("ADCspeedValue", c_uint)
        ("digIO1OperMode", FF_IOModes)
        ("digIO1PulseWidth", c_uint)
        ("digIO1SignalMode", FF_SignalModes)
        ("digIO2OperMode", FF_IOModes)
        ("digIO2PulseWidth", c_uint)
        ("digIO2SignalMode", FF_SignalModes)
        ("reserved", c_uint)
        ("reserved1", c_int)
        ("transitTime", c_uint)
        ]

class KIM_DriveOPParameters(Structure):
    _fields_ = [
        ("maxVoltage", c_int16)
        ("stepAcceleration", c_int32)
        ("stepRate", c_int32)
        ]

class KIM_FeedbackSigParams(Structure):
    _fields_ = [
        ("encoderConst", c_int32)
        ("feedbackSignalMode", KIM_FBSignalMode)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ]

class KIM_HomeParameters(Structure):
    _fields_ = [
        ("homeDirection", KIM_TravelDirection)
        ("homeLimitSwitch", KIM_TravelDirection)
        ("homeOffset", c_int32)
        ("homeStepRate", c_int32)
        ]

class KIM_JogParameters(Structure):
    _fields_ = [
        ("jogMode", KIM_JogMode)
        ("jogStepAcceleration", c_int32)
        ("jogStepRate", c_int32)
        ("jogStepSizeFwd", c_int32)
        ("jogStepSizeRev", c_int32)
        ]

class KIM_LimitSwitchParameters(Structure):
    _fields_ = [
        ("forwardLimit", KIM_LimitSwitchModes)
        ("reverseLimit", KIM_LimitSwitchModes)
        ("stageID", c_int16)
        ]

class KIM_MMIChannelParameters(Structure):
    _fields_ = [
        ("presentPos1", c_int32)
        ("presentPos2", c_int32)
        ]

class KIM_MMIParameters(Structure):
    _fields_ = [
        ("directionSense", KIM_DirectionSense)
        ("displayIntensity", c_int16)
        ("joystickMode", KIM_JoystickModes)
        ("maxStepRate", c_int32)
        ]

class KIM_Status(Structure):
    _fields_ = [
        ("encoderCount", c_int32)
        ("position", c_int32)
        ("statusBits", c_uint32)
        ]

class KIM_TrigIOConfig(Structure):
    _fields_ = [
        ("trig1Mode", KIM_TrigModes)
        ("trig1Polarity", KIM_TrigPolarities)
        ("trig2Mode", KIM_TrigModes)
        ("trig2Polarity", KIM_TrigPolarities)
        ("trigChannel1", KIM_Channels)
        ("trigChannel2", KIM_Channels)
        ]

class KIM_TrigParamsParameters(Structure):
    _fields_ = [
        ("intervalFwd", c_int32)
        ("intervalRev", c_int32)
        ("numberOfCycles", c_int32)
        ("numberOfPulsesFwd", c_int32)
        ("numberOfPulsesRev", c_int32)
        ("pusleWidth", c_int32)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ("reserved5", c_int16)
        ("reserved6", c_int16)
        ("startPosFwd", c_int32)
        ("startPosRev", c_int32)
        ]

class KLD_MMIParams(Structure):
    _fields_ = [
        ("displayIntensity", c_int16)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ]

class KLD_TrigIOParams(Structure):
    _fields_ = [
        ("mode1", KLDTriggerMode)
        ("mode2", KLDTriggerMode)
        ("polarity1", KLD_TrigPolarity)
        ("polarity2", KLD_TrigPolarity)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ]

class KLS_MMIParams(Structure):
    _fields_ = [
        ]

class KLS_TrigIOParams(Structure):
    _fields_ = [
        ]

class KMOT_MMIParams(Structure):
    _fields_ = [
        ("DisplayDimIntensity", c_int16)
        ("DisplayIntensity", c_int16)
        ("DisplayTimeout", c_int16)
        ("PresentPos1", c_int32)
        ("PresentPos2", c_int32)
        ("WheelAcceleration", c_int32)
        ("WheelDirectionSense", MOT_DirectionSense)
        ("WheelMaxVelocity", c_int32)
        ("WheelMode", KMOT_WheelMode)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ]

class KMOT_TriggerConfig(Structure):
    _fields_ = [
        ("Trigger1Mode", KMOT_TriggerPortMode)
        ("Trigger1Polarity", KMOT_TriggerPortPolarity)
        ("Trigger2Mode", KMOT_TriggerPortMode)
        ("Trigger2Polarity", KMOT_TriggerPortPolarity)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ("reserved5", c_int16)
        ("reserved6", c_int16)
        ]

class KMOT_TriggerParams(Structure):
    _fields_ = [
        ("Cyclecount", c_int32)
        ("TriggerIntervalFwd", c_int32)
        ("TriggerIntervalRev", c_int32)
        ("TriggerPulseCountFwd", c_int32)
        ("TriggerPulseCountRev", c_int32)
        ("TriggerPulseWidth", c_int32)
        ("TriggerStartPositionFwd", c_int32)
        ("TriggerStartPositionRev", c_int32)
        ("reserved1", c_int32)
        ("reserved2", c_int32)
        ("reserved3", c_int32)
        ("reserved4", c_int32)
        ("reserved5", c_int32)
        ("reserved6", c_int32)
        ]

class KNA_FeedbackLoopConstants(Structure):
    _fields_ = [
        ("integralTerm", c_short)
        ("proportionalTerm", c_short)
        ]

class KNA_IOSettings(Structure):
    _fields_ = [
        ("highVoltageOutRange", KNA_HighVoltageRange)
        ("highVoltageOutputRoute", KNA_HighOutputVoltageRoute)
        ("lowVoltageOutRange", KNA_LowVoltageRange)
        ("lowVoltageOutputRoute", KNA_LowOutputVoltageRoute)
        ]

class KNA_MMIParams(Structure):
    _fields_ = [
        ("DisplayIntensity", c_uint16)
        ("WheelAdjustRate", KNA_WheelAdjustRate)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ("reserved5", c_int16)
        ("reserved6", c_int16)
        ]

class KNA_TIARangeParameters(Structure):
    _fields_ = [
        ("changeToOddOrEven", NT_OddOrEven)
        ("downLimit", c_long)
        ("mode", NT_TIARangeMode)
        ("newRange", KNA_TIARange)
        ("settleSamples", c_short)
        ("upLimit", c_long)
        ]

class KNA_TIAReading(Structure):
    _fields_ = [
        ("absoluteReading", c_float)
        ("relativeReading", c_long)
        ("selectRange", KNA_TIARange)
        ("underOrOverRead", NT_UnderOrOver)
        ]

class KNA_TriggerConfig(Structure):
    _fields_ = [
        ("Trigger1Mode", KNA_TriggerPortMode)
        ("Trigger1Polarity", KNA_TriggerPolarity)
        ("Trigger2Mode", KNA_TriggerPortMode)
        ("Trigger2Polarity", KNA_TriggerPolarity)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ("unused1", c_int16)
        ("unused2", c_int16)
        ]

class KPC_MMIParams(Structure):
    _fields_ = [
        ("DisplayDimIntensity", c_int16)
        ("DisplayIntensity", c_int16)
        ("DisplayTimeout", c_int16)
        ("JoystickDirectionSense", KPZ_WheelChangeRate)
        ("JoystickMode", KPZ_WheelMode)
        ("PositionStep", c_int16)
        ("PresentPos1", c_int16)
        ("PresentPos2", c_int16)
        ("PresentVolt1", c_int16)
        ("PresentVolt2", c_int16)
        ("VoltageAdjustRate", KPZ_WheelChangeRate)
        ("VoltageStep", c_int16)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ]

class KPC_TriggerConfig(Structure):
    _fields_ = [
        ("LowerLimit", c_int32)
        ("MonitorFilterFrequency", c_int16)
        ("MonitorOutput", KPC_MonitorOuptutMode)
        ("MonitorOutputSoftwareValue", c_int32)
        ("SmoothingSamples", c_int16)
        ("Trigger1Mode", KPC_TriggerPortMode)
        ("Trigger1Polarity", KPC_TriggerPortPolarity)
        ("Trigger2Mode", KPC_TriggerPortMode)
        ("Trigger2Polarity", KPC_TriggerPortPolarity)
        ("UpperLimit", c_int32)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ]

class KPZ_MMIParams(Structure):
    _fields_ = [
        ("DisplayDimIntensity", c_int16)
        ("DisplayIntensity", c_int16)
        ("DisplayTimeout", c_int16)
        ("JoystickDirectionSense", KPZ_WheelDirectionSense)
        ("JoystickMode", KPZ_WheelMode)
        ("PresentPos1", c_int32)
        ("PresentPos2", c_int32)
        ("VoltageAdjustRate", KPZ_WheelChangeRate)
        ("VoltageStep", c_int32)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ]

class KPZ_TriggerConfig(Structure):
    _fields_ = [
        ("Trigger1Mode", KPZ_TriggerPortMode)
        ("Trigger1Polarity", KPZ_TriggerPortPolarity)
        ("Trigger2Mode", KPZ_TriggerPortMode)
        ("Trigger2Polarity", KPZ_TriggerPortPolarity)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ("reserved5", c_int16)
        ("reserved6", c_int16)
        ]

class KSC_MMIParams(Structure):
    _fields_ = [
        ("DisplayDimIntensity", c_int16)
        ("DisplayIntensity", c_int15)
        ("DisplayTimeout", c_int16)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ("unused1", c_int16)
        ("unused10", c_int16)
        ("unused2", c_int16)
        ("unused3", c_int16)
        ("unused4", c_int16)
        ("unused5", c_int16)
        ("unused6", c_int16)
        ("unused7", c_int16)
        ("unused8", c_int16)
        ("unused9", c_int16)
        ]

class KSC_TriggerConfig(Structure):
    _fields_ = [
        ("Trigger1Mode", KSC_TriggerPortMode)
        ("Trigger1Polarity", KSC_TriggerPolarity)
        ("Trigger2Mode", KSC_TriggerPortMode)
        ("Trigger2Polarity", KSC_TriggerPolarity)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ("reserved5", c_int16)
        ("reserved6", c_int16)
        ]

class KSG_MMIParams(Structure):
    _fields_ = [
        ("DisplayDimIntensity", c_int16)
        ("DisplayIntensity", c_int16)
        ("DisplayTimeout", c_int16)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ]

class KSG_TriggerConfig(Structure):
    _fields_ = [
        ("LowerLimit", c_int32)
        ("Trigger1Mode", KPZ_TriggerPortMode)
        ("Trigger1Polarity", KPZ_TriggerPortPolarity)
        ("Trigger2Mode", KPZ_TriggerPortMode)
        ("Trigger2Polarity", KPZ_TriggerPortPolarity)
        ("UpperLimit", c_int32)
        ("reserved1", c_int16)
        ("reserved2", c_int16)
        ("reserved3", c_int16)
        ("reserved4", c_int16)
        ("reserved5", c_int16)
        ("reserved6", c_int16)
        ]

class MOD_AnalogMonitorConfigurationParameters(Structure):
    _fields_ = [
        ("MonitorNo", c_long)
        ("MonitorVar", MOD_Monitro_Variable)
        ("MotorChannelNo", c_long)
        ("Offset", c_long)
        ("Scale", c_long)
        ]

class MOD_AuxIOPortConfigurationParameters(Structure):
    _fields_ = [
        ("Mode", MODE_AuxIOPortMode)
        ("PortNo", c_long)
        ("SWState", c_long)
        ]

class MOD_AuxIOPortConfigurationSetParameters(Structure):
    _fields_ = [
        ("Mode", MODE_AuxIOPortMode)
        ("PortNo", c_long)
        ("SWState", c_long)
        ]

class MOD_IOPortConfigurationParameters(Structure):
    _fields_ = [
        ("Mode", MOD_IOPortMode)
        ("PortNo", c_long)
        ("Source", MOD_IOPortSource)
        ]

class MOT_BVC_ScanParams(Structure):
    _fields_ = [
        ("enable", c_bool)
        ("scanAmplitude", c_ulong)
        ("scanCenterPosition", c_long)
        ("scanFrequency", c_ulong)
        ]

class MOT_BrushlessCurrentLoopParameters(Structure):
    _fields_ = [
        ("deadErrorBand", c_long)
        ("feedForward", c_long)
        ("integralGain", c_long)
        ("integralLimit", c_long)
        ("lastNotUsed", c_long)
        ("notUsed", c_long)
        ("phase", MOT_CurrentLoopPhases)
        ("proportionalGain", c_long)
        ]

class MOT_BrushlessElectricOutputParameters(Structure):
    _fields_ = [
        ("continuousCurrentLimit", c_long)
        ("excessEnergyLimit", c_long)
        ("lastNotUsed", c_long)
        ("motorSignalBias", c_short)
        ("motorSignalLimit", c_short)
        ("notUsed", c_long)
        ]

class MOT_BrushlessPositionLoopParameters(Structure):
    _fields_ = [
        ("accelerationFeedForward", c_long)
        ("derivativeRecalculationTime", c_long)
        ("differentialGain", c_long)
        ("factorForOutput", c_long)
        ("integralGain", c_long)
        ("integralLimit", c_ulong)
        ("lastNotUsed", c_long)
        ("notUsed", c_long)
        ("positionErrorLimit", c_ulong)
        ("proportionalGain", c_long)
        ("velocityFeedForward", c_long)
        ]

class MOT_BrushlessTrackSettleParameters(Structure):
    _fields_ = [
        ("lastNotUsed", c_long)
        ("maxTrackingError", c_long)
        ("notUsed", c_long)
        ("settledError", c_long)
        ("time", c_long)
        ]

class MOT_ButtonParameters(Structure):
    _fields_ = [
        ("buttonMode", MOT_ButtonModes)
        ("leftButtonPosition", c_int)
        ("rightButtonPosition", c_int)
        ("timeout", c_long)
        ("unused", c_long)
        ]

class MOT_ChannelPosition(Structure):
    _fields_ = [
        ("channelNumber", c_long)
        ("position", c_int)
        ]

class MOT_DC_PIDParameters(Structure):
    _fields_ = [
        ("differentialGain", c_int)
        ("integralGain", c_int)
        ("integralLimit", c_int)
        ("parameterFilter", c_long)
        ("proportionalGain", c_int)
        ]

class MOT_EncoderResolutionParams(Structure):
    _fields_ = [
        ("encoderResolutionWholeNumber", c_ulong)
        ("enconderResolutionFraction", c_long)
        ("unused1", c_long)
        ("unused2", c_long)
        ("unused3", c_long)
        ]

class MOT_HomingParameters(Structure):
    _fields_ = [
        ("direction", MOT_TravelDirection)
        ("limitSwitch", MOT_HomeLimitSwitchDirection)
        ("offsetDistance", c_uint)
        ("velocity", c_uint)
        ]

class MOT_JogParameters(Structure):
    _fields_ = [
        ("mode", MOT_JogModes)
        ("stepSize", c_uint)
        ("stopMode", MOT_StopModes)
        ("velParams", MOT_VelocityParameters)
        ]

class MOT_JoystickParameters(Structure):
    _fields_ = [
        ("directionSense", MOT_TravelDirection)
        ("highGearAcceleration", c_ulong)
        ("highGearMaxVelocity", c_ulong)
        ("lowGearAcceleration", c_ulong)
        ("lowGearMaxVelocity", c_ulong)
        ]

class MOT_LCDMoveParams(Structure):
    _fields_ = [
        ("JogAccn", c_int)
        ("JogMaxVel", c_int)
        ("JogMode", MOT_JogModes)
        ("PresentPosition1", c_int)
        ("PresentPosition2", c_int)
        ("PresentPosition3", c_int)
        ("StepSize", c_uint)
        ("StopMode", MOT_StopModes)
        ("reserved1", c_long)
        ("reserved10", c_long)
        ("reserved2", c_long)
        ("reserved3", c_long)
        ("reserved4", c_long)
        ("reserved5", c_long)
        ("reserved6", c_long)
        ("reserved7", c_long)
        ("reserved8", c_long)
        ("reserved9", c_long)
        ]

class MOT_LCDParams(Structure):
    _fields_ = [
        ("DisplayDimIntensity", c_long)
        ("DisplayIntensity", c_long)
        ("DisplayTimeout", c_long)
        ("JSSensitivity", c_long)
        ("reserved1", c_long)
        ("reserved10", c_long)
        ("reserved2", c_long)
        ("reserved3", c_long)
        ("reserved4", c_long)
        ("reserved5", c_long)
        ("reserved6", c_long)
        ("reserved7", c_long)
        ("reserved8", c_long)
        ("reserved9", c_long)
        ]

class MOT_LimitSwitchParameters(Structure):
    _fields_ = [
        ("anticlockwiseHardwareLimit", MOT_LimitSwitchModes)
        ("anticlockwisePosition", c_ulong)
        ("clockwiseHardwareLimit", MOTLimitSwitchModes)
        ("clockwisePosition", MOT_LimitSwitchSWModes)
        ]

class MOT_PIDLoopEncoderParams(Structure):
    _fields_ = [
        ("PIDOutputLimit", c_int)
        ("PIDTolerance", c_int)
        ("differentialGain", c_int)
        ("integralGain", c_int)
        ("loopMode", MOT_PID_LoopMode)
        ("proportionalGain", c_int)
        ]

class MOT_PotentiometerStep(Structure):
    _fields_ = [
        ("thresholdDeflection", c_long)
        ("velocity", c_ulong)
        ]

class MOT_PotentiometerSteps(Structure):
    _fields_ = [
        ("potentionmeterStepParameters1", MOT_PotentiometerStep)
        ("potentionmeterStepParameters2", MOT_PotentiometerStep)
        ("potentionmeterStepParameters3", MOT_PotentiometerStep)
        ("potentionmeterStepParameters4", MOT_PotentiometerStep)
        ]

class MOT_PowerParameters(Structure):
    _fields_ = [
        ("movePercentage", c_long)
        ("restPercentage", c_long)
        ]

class MOT_RasterScanMoveAxisParams(Structure):
    _fields_ = [
        ("AxisMovement1", MOT_RasterScanMoveAxisParams)
        ("AxisMovement2", MOT_RasterScanMoveAxisParams)
        ("ChannelNo", c_long)
        ("CycleCount", c_long)
        ("DwellTime", c_long)
        ("RelativeDistance", c_long)
        ("ScanPattern", MOT_RasterScanMovePattern)
        ("StartPos", c_long)
        ("TriggerInPolarity", MOT_TriggerPolarity)
        ("TriggerMode", MOT_RasterScanMoveTriggerMode)
        ("TriggerSource", MOT_TriggerInputSource)
        ]

class MOT_RasterScanMoveParams(Structure):
    _fields_ = [
        ]

class MOT_StageAxisParameters(Structure):
    _fields_ = [
        ("axisID", c_long)
        ("countsPerUnit", c_ulong)
        ("maxAcceleration", c_int)
        ("maxDecceleration", c_int)
        ("maxPosition", c_int)
        ("maxVelocity", c_int)
        ("minPosition", c_int)
        ("partNumber", 16 * c_char)
        ("reserved1", c_long)
        ("reserved2", c_long)
        ("reserved3", c_long)
        ("reserved4", c_long)
        ("reserved5", c_ulong)
        ("reserved6", c_ulong)
        ("reserved7", c_ulong)
        ("reserved8", c_ulong)
        ("serialNumber", c_ulong)
        ("stageID", c_long)
        ]

class MOT_TriggerIOConfigParameters(Structure):
    _fields_ = [
        ("CycleCount", c_long)
        ("InputSource", MOT_TriggerInputSource)
        ("IntervalFwd", c_long)
        ("IntervalRev", c_long)
        ("PulseCountFwd", c_long)
        ("PulseCountRev", c_long)
        ("PulseWidth", c_long)
        ("StartPositionFwd", c_long)
        ("StartPositionRev", c_long)
        ("TriggerInMode", MOT_TriggerInputConfigModes)
        ("TriggerInPolarity", MOT_TriggerPolarity)
        ("TriggerOUtPolarity", MOT_TriggerPolarity)
        ("TriggerOutMode", MOT_TriggerOutputConfigModes)
        ("reserved1", c_long)
        ("reserved2", c_long)
        ("reserved3", c_long)
        ("reserved4", c_long)
        ]

class MOT_VelocityParameters(Structure):
    _fields_ = [
        ("acceleration", c_int)
        ("maxVelocity", c_int)
        ("minVelocity", c_int)
        ]

class MOT_VelocityProfileParameters(Structure):
    _fields_ = [
        ("jerk", c_ulong)
        ("lastNotUsed", c_long)
        ("mode", MOT_VelocityProfileModes)
        ("notUsed", c_long)
        ]

class MPC_IOSettings(Structure):
    _fields_ = [
        ("ADCSpeedValue", c_uint)
        ("digIO1OperMode", MPC_IOModes)
        ("digIO1PulseWdith", c_uint)
        ("digIO1SignalMode", MPC_SignalModes)
        ("digIO2OperMode", MPC_IOModes)
        ("digIO2PulseWdith", c_uint)
        ("digIO2SignalMode", MPC_SignalModes)
        ("reserved1", c_int)
        ("reserved2", c_uint)
        ("transitTime", c_uint)
        ]

class Macros(Structure):
    _fields_ = [
        ]

class NT_CircleDiameterLUT(Structure):
    _fields_ = [
        ("LUT_Diameter1", c_long)
        ("LUT_Diameter10", c_long)
        ("LUT_Diameter11", c_long)
        ("LUT_Diameter12", c_long)
        ("LUT_Diameter13", c_long)
        ("LUT_Diameter14", c_long)
        ("LUT_Diameter15", c_long)
        ("LUT_Diameter16", c_long)
        ("LUT_Diameter2", c_long)
        ("LUT_Diameter3", c_long)
        ("LUT_Diameter4", c_long)
        ("LUT_Diameter5", c_long)
        ("LUT_Diameter6", c_long)
        ("LUT_Diameter7", c_long)
        ("LUT_Diameter8", c_long)
        ("LUT_Diameter9", c_long)
        ]

class NT_CircleParameters(Structure):
    _fields_ = [
        ("algorithmAdjustment", NT_CircleAdjustment)
        ("diameter", c_long)
        ("maxDiameter", c_long)
        ("minDiameter", c_long)
        ("mode", NT_circleDiameterMode)
        ("samplesPerRevolution", c_long)
        ]

class NT_GainParameters(Structure):
    _fields_ = [
        ("controlMode", c_long)
        ("gain", c_short)
        ]

class NT_HVComponent(Structure):
    _fields_ = [
        ("horizontalComponent", c_long)
        ("verticalComponent", c_long)
        ]

class NT_IOSettings(Structure):
    _fields_ = [
        ("lowVoltageOutputRange", NT_VoltageRange)
        ("lowVoltageOutputRoute", NT_OutputVoltageRoute)
        ("notYetInUse", c_long)
        ("unused", c_long)
        ]

class NT_LowPassFilterParameters(Structure):
    _fields_ = [
        ("notUsed1", NT_LowPassFrequency)
        ("notUsed2", NT_LowPassFrequency)
        ("notUsed3", NT_LowPassFrequency)
        ("notUsed4", NT_LowPassFrequency)
        ("param1", NT_LowPassFrequency)
        ]

class NT_TIARangeParameters(Structure):
    _fields_ = [
        ("changeToOddOrEven", NT_OddOrEven)
        ("downLimit", c_long)
        ("mode", NT_TIARangeMode)
        ("newRange", NT_TIARangeMode)
        ("settleSamples", c_short)
        ("upLimit", c_long)
        ]

class NT_TIAReading(Structure):
    _fields_ = [
        ("absoluteReading", c_float)
        ("relativeReading", c_long)
        ("selectedRange", NT_TIARangeMode)
        ("underOrOverRead", NT_UnderOrOver)
        ]

class PDXC2_ClosedLoopParameters(Structure):
    _fields_ = [
        ("Acceleration", c_uint32)
        ("Differential", c_uint32)
        ("Integral", c_uint32)
        ("Proportional", c_uint32)
        ("RefSpeed", c_uint32)
        ]

class PDXC2_JogParameters(Structure):
    _fields_ = [
        ("CloseLoopSpeed", c_int32)
        ("CloseLoopStepSize", c_int32)
        ("ClosedLoopAcceleration", c_int32)
        ("JogMode", PZ_JogModes)
        ("OpenLoopAcceleration", c_int32)
        ("OpenLoopStepRate", c_int32)
        ("OpenLoopStepSize", c_int32)
        ]

class PDXC2_OpenLoopMoveParameters(Structure):
    _fields_ = [
        ("StepSize", c_int32)
        ]

class PDXC2_Status(Structure):
    _fields_ = [
        ("Position", c_int32)
        ("StatusBit", c_int32)
        ("Unused", c_int32)
        ]

class PDXC2_TriggerParams(Structure):
    _fields_ = [
        ("AnalogGain", c_float)
        ("AnalogInOffset", c_float)
        ("AnalogOutGain", c_float)
        ("AnalogOutOffset", c_float)
        ("FallFixedStep", c_int32)
        ("FallPosition1", c_int32)
        ("FallPosition2", c_int32)
        ("RiseFixedStep", c_int32)
        ("RisePosition1", c_int32)
        ("RisePosition2", c_int32)
        ]

class PPC_IOSettings(Structure):
    _fields_ = [
        ("FPBrightness", PCC_DisplayIntensity)
        ("controlSrc", PPC_IOControlMode)
        ("feedbackPolarity", PCC_FeedbackPolarity)
        ("feedbackSrc", PCC_IOFeedbackSourceDefinition)
        ("monitorOPBandwidth", PCC_IOOutputBandwidth)
        ("monitorOPSig", PCC_IOOutputMode)
        ]

class PPC_NotchParams(Structure):
    _fields_ = [
        ("filter1Fc", c_float)
        ("filter1Q", c_float)
        ("filter2Fc", c_float)
        ("filter2Q", c_float)
        ("filterNo", PCC_NotchFilterChannel)
        ("notchFilter1On", PCCNotchFilterState)
        ("notchFilter2On", PCCNotchFilterState)
        ]

class PPC_PIDConsts(Structure):
    _fields_ = [
        ("PIDConstsD", c_float)
        ("PIDConstsDFc", c_float)
        ("PIDConstsI", c_float)
        ("PIDConstsP", c_float)
        ("PIDDerivFilterOn", PCC_DerivFilterState)
        ("PIDIndex", c_byte)
        ]

class PPC_PIDCriteria(Structure):
    _fields_ = [
        ("PIDConstIndex", c_uint16)
        ("criterialD", c_uint8)
        ("priority", c_uint16)
        ("targetErrorWindow", c_uint16)
        ("unusedByte", c_uint8)
        ("wReservedPart1", c_long)
        ("wReservedPart2", c_long)
        ("wReservedPart3", c_long)
        ]

class PZ_FeedbackLoopConstants(Structure):
    _fields_ = [
        ("integratTerm", c_short)
        ("proportionalTerm", c_short)
        ]

class PZ_LUTWaveParameters(Structure):
    _fields_ = [
        ("LUTValueDelay", c_uint)
        ("cycleLength", c_short)
        ("mode", PZ_OutputLUTModes)
        ("numCycles", c_uint)
        ("numOutTriggerRepeat", c_short)
        ("outTriggerDuration", c_uint)
        ("outTriggerStart", c_short)
        ("postCycleDelay", c_uint)
        ("preCycleDelay", c_uint)
        ]

class QD_ClosedLoopPosition(Structure):
    _fields_ = [
        ("x", c_int16)
        ("y", c_int16)
        ]

class QD_KPA_DigitalIO(Structure):
    _fields_ = [
        ("wDigOPs", c_long)
        ("wReservedPart1", c_long)
        ("wReservedPart2", c_long)
        ("wReservedPart3", c_long)
        ("wReservedPart4", c_long)
        ("wReservedPart5", c_long)
        ("wReservedPart6", c_long)
        ]

class QD_KPA_TrigIOConfig(Structure):
    _fields_ = [
        ("trig1DiffThreshold", c_long)
        ("trig1Mode", QD_KPA_TrigModes)
        ("trig1Polarity", QD_KPA_TrigPolarities)
        ("trig1SumMax", c_long)
        ("trig1SumMin", c_long)
        ("trig2DiffThreshold", c_long)
        ("trig2Mode", QD_KPA_TrigModes)
        ("trig2Polarity", QD_KPA_TrigPolarities)
        ("trig2SumMax", c_long)
        ("trig2SumMin", c_long)
        ("wReservedPart1", c_long)
        ("wReservedPart2", c_long)
        ("wReservedPart3", c_long)
        ("wReservedPart4", c_long)
        ("wReservedPart5", c_long)
        ("wReservedPart6", c_long)
        ]

class QD_LoopParameters(Structure):
    _fields_ = [
        ("differentialGain", c_float)
        ("integralGain", c_float)
        ("lowPassFilerEnabled", QD_FilterEnable)
        ("lowPassfilterCutOffFreq", c_float)
        ("notchFilterCenterFrequency", c_float)
        ("notchFilterEnabled", QD_FilterEnable)
        ("notchFilterQ", c_float)
        ("proportionalGain", c_float)
        ]

class QD_LowPassFilterParameters(Structure):
    _fields_ = [
        ("lowPassFilterCutOffFreq", c_float)
        ("lowPassFilterEnabled", QD_FilterEnable)
        ]

class QD_NotchFilterParameters(Structure):
    _fields_ = [
        ("notchFilterCenterFrequency", c_float)
        ("notchFilterEnable", QD_FilterEnable)
        ("notchFilterQ", c_float)
        ]

class QD_PIDParameters(Structure):
    _fields_ = [
        ("differentialGain", c_float)
        ("integralGain", c_float)
        ("proportionalGain", c_float)
        ]

class QD_Position(Structure):
    _fields_ = [
        ("x", c_int16)
        ("y", c_int16)
        ]

class QD_PositionDemandParameters(Structure):
    _fields_ = [
        ("lowVoltageOutputRoute", QD_LowVoltageRoute)
        ("maxXdemand", c_int16)
        ("maxYdemand", c_int16)
        ("minXdemand", c_int16)
        ("minYdemand", c_int16)
        ("openLoopOptions", QD_OpenLoopHoldValues)
        ("xFeedBackSignedGain", c_int16)
        ("yFeedBackSignedGain", c_int16)
        ]

class QD_Readings(Structure):
    _fields_ = [
        ("demandPos", QD_Position)
        ("posDifference", QD_Position)
        ("sum", c_long)
        ]

class SC_CycleParameters(Structure):
    _fields_ = [
        ("closeTime", c_uint)
        ("numCycles", c_uint)
        ("opeTime", c_uint)
        ]

class TC_LoopParameters(Structure):
    _fields_ = [
        ("differentialGain", c_ushort)
        ("integralGain", c_ushort)
        ("proportionalGain", c_ushort)
        ]

class TLI_DeviceInfo(Structure):
    _fields_ = [
        ("PID", c_ulong)
        ("description", 65 * c_char)
        ("isCustomType", c_bool)
        ("isKnownType", c_bool)
        ("isLaser", c_bool)
        ("isPiezoDevice", c_bool)
        ("isRack", c_bool)
        ("maxChannels", c_short)
        ("motorType", MOT_MotorTypes)
        ("serialNo", 9 * c_char)
        ("typeID", c_ulong)
        ]

class TLI_HardwareInformation(Structure):
    _fields_ = [
        ("deviceDependantData", 12 * c_byte)
        ("firmwareVersion", c_ulong)
        ("hardwareVersion", c_long)
        ("modelNumber", 8 * c_char)
        ("modificationState", c_long)
        ("notes", 48 * c_char)
        ("numChannels", c_short)
        ("serialNumber", c_ulong)
        ("type", c_long)
        ]

class TPZ_IOSettings(Structure):
    _fields_ = [
        ]

class TSG_IOSettings(Structure):
    _fields_ = [
        ]
