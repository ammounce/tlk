from c_types import, c_byte, c_int16, c_long, c_short, c_uin16, c_ushort

= None

BNT_BNCTriggerModes = c_long
NT_BNCModeTrigger = c_long(0x0000)
NT_BNCModeLVOut = c_long(0xFFFF)

BNT_CurrentLimit = c_long
NT_CurrentLimit_100mA = c_long(0x00)
NT_CurrentLimit_250mA = c_long(0x01)
NT_CurrentLimit_500mA = c_long(0x02)

BNT_FeedbackSignalSelection = c_long
NT_FeedbackSignalDC = c_long(0x0000)
NT_FeedbackSignalAC = c_long(0xFFFF)

BNT_OutputLowPassFilter = c_long
NT_OutputFilter_10Hz = c_long(0x0)
NT_OutputFilter_100Hz = c_long(0x1)
NT_OutputFilter_5kHz = c_long(0x2)
NT_OutputFilter_None = c_long(0x3)

ChannelEnableModes = c_int16
ChannelNone = c_int16(0x00)
Channel1Only = c_int16(0x01)
Channel2Only = c_int16(0x02)
Channel3Only = c_int16(0x03)
Channel4Only = c_int16(0x04)
Channels1and2 = c_int16(0x05)
Channels3and4 = c_int16(0x06)

FF_IOModes = c_long
FF_ToggleOnPositiveEdge = c_long(0x01)
FF_SetPositionOnPositiveEdge = c_long(0x02)
FF_OutputHighAtSetPosition = c_long(0x04)
FF_OutputHighWhemMoving = c_long(0x08)

FF_Positions = None

FF_SignalModes = c_long
FF_InputButton = c_long(0x01)
FF_InputLogic = c_long(0x02)
FF_InputSwap = c_long(0x04)
FF_OutputLevel = c_long(0x10)
FF_OutputPulse = c_long(0x20)
FF_OutputSwap = c_long(0x40)

HubAnalogueModes = None

KIM_Channels = c_uin16
Channel1 = c_uin16(1)
Channel2 = c_uin16(2)
Channel3 = c_uin16(2)
Channel4 = c_uin16(4)

KIM_DirectionSense = c_int16
Dir_Disabled = c_int16(0x0)
Dir_Forward = c_int16(0x01)
Dir_Reverse = c_int16(0x02)

KIM_FBSignalMode = c_int16
FB_LimitSwitch = c_int16(0x01)
FB_Encoder = c_int16(0x02)

KIM_JogMode = c_uin16
JogContinuous = c_uin16(0x01)
JogStep = c_uin16(0x02)

KIM_JoysticModes = c_int16
JS_Velocity = c_int16(0x01)
JS_Jog = c_int16(0x02)
JS_GotoPosition = c_int16(0x03)

KIM_LimitSwitchModes = c_int16
Ignore = c_int16(0x01)
SwitchMakes = c_int16(0x02)
SwitchBreaks = c_int16(0x03)
SwitchMakes_HomeOnly = c_int16(0x04)
SwitchBreaks_HomeOnly = c_int16(0x05)

KIM_Stages = c_ushort
Undefined_stage = c_ushort(0)
PIA_stage = c_ushort(1)
PDR_Stage = c_ushort(2)

KIM_TravelDirection = c_byte
Forward = c_byte(0x01)
Reverse = c_byte(0x02)

KIM_TrigModes = c_int16
Trig_Disabled = c_int16(0x00)
Trig_In_GPI = c_int16(0x01)
Trig_InRelativeMove = c_int16(0x02)
Trig_InAbsoluteMove = c_int16(0x03)
Trig_InResetCount = c_int16(0x04)
Trig_Out_GP0 = c_int16(0x0A)
Trig_Out_InMotion = c_int16(0x0B)
Trig_Out_AtMaxVelocity = c_int16(0x0C)
Trig_Out_PosStepFwd = c_int16(0x0D)
Trig_Out_PosStepRev = c_int16(0x0E)
Trig_Out_PosStepBoth = c_int16(0x0F)
Trig_Out_AtFwdLimit = c_int16(0x10)
Trig_Out_AtRevLimit = c_int16(0x11)
Trig_Out_AtEitherLimit = c_int16(0x12)

KIM_TrigPolarities = c_int16
Trig_High = c_int16(0x01)
Trig_Low = c_int16(0x02)

KLD_RAMPUP = c_int16
KLD_RampUpImmediate = c_int16(0)
KLD_RampUpRamped = c_int16(1)

KLD_TrigPolarity = c_ushort
KLD_TrigPol_High = c_ushort(0x01)
KLD_TrigPol_Low = c_ushort(0x02)

KLD_TriggerMode = c_ushort
KLD_Disabled = c_ushort(0)
KLD_Output = c_ushort(0x0a)
KLD_LaserOn = c_ushort(0x0b)
KLD_InterlockEnabled = c_ushort(0x0c)
KLD_SetPointChange = c_ushort(0x0d)
KLD_HighStability = c_ushort(0x0e)
KLD_LowStability = c_ushort(0x0f)
KLD_Input = c_ushort(1)

KLS_OpMode = c_ushort
KLS_ConstantPower = c_ushort(0)
KLS_ConstantCurrent = c_ushort(1)

KLS_TrigPolarity = c_ushort
KLS_TrigPol_High = c_ushort(0x01)
KLS_TrigPol_Low = c_ushort(0x02)

KLS_TriggerMode = c_ushort
KLS_Disabled = c_ushort(0)
KLS_Output = c_ushort(0x0a)
KLS_LaserOn = c_ushort(0x0b)
KLS_InterlockEnabled = c_ushort(0x0c)
KLS_SetPointChange = c_ushort(0x0d)
KLS_HighStability = c_ushort(0x0e)
KLS_LowStability = c_ushort(0x0f)
KLS_Input = c_ushort(1)

KMOT_TriggerPortMode = None

KMOT_TriggerPortPolarity = None

KMOT_WheelDirectionSense = None

KMOT_WheelMode = None

KNA_Channels = c_long
KNA_ChannelUndefined = c_long(0x00)
KNA_Channel1 = c_long(0x01)
KNA_Channel2 = c_long(0x02)

KNA_FeedbackModeTypes = c_short
PZ_ControlModeUndefined = c_short(0)
PZ_OpenLoop = c_short(1)
PZ_CloseLoop = c_short(2)
PZ_OpenLoopSmooth = c_short(3)
PZ_CloseLoopSmooth = c_short(4)

KNA_FeedbackSource = None

KNA_HighOutputVoltageRoute = None

KNA_HighVoltageRange = None

KNA_TIARange = None

KNA_TriggerPortMode = None

KNA_TriggerPortPolarity = None

KNA_WheelAdjustRate = None

KPC_HubAnalogueModes = None

KPC_IOSettings = None

KPC_MonitorOutputMode = None

KPC_TriggerPortMode = None

KPC_TriggerPortPolarity = None

KPZ_TriggerPortMode = None

KPZ_TriggerPortPolarity = None

KPZ_WheelChangeRate = c_int16
KPZ_WM_High = c_int16(0x01)
KPZ_WM_Medium = c_int16(0x02)
KPZ_WM_Low = c_int16(0x03)

KPZ_WheelDirectionSense = c_int16
KPZ_WM_Positive = c_int16(0x01)
KPZ_WM_Negative = c_int16(0x02)

KPZ_WheelMode = c_int16
KPZ_WM_MoveAtVoltage = c_int16(0x01)
KPZ_WM_JogVoltage = c_int16(0x02)
KPZ_WM_SetVoltage = c_int16(0x03)

KSC_TriggerPortMode = c_int16
KSC_TrigDisabled = c_int16(0x00)
KSC_TrigIn_GPI = c_int16(0x01)
KSC_TrigOut_GPO = c_int16(0x0A)

KSC_TriggerPortPolarity = c_int16
KSC_TrigPolarityHigh = c_int16(0x01)
KSC_TrigPolarityLow = c_int16(0x02)

KSG_TriggerPortMode = c_int16
KSG_TrigDisabled = c_int16(0x00)
KSG_TrigIn_GPI = c_int16(0x01)
KSG_TrigOut_GPO = c_int16(0x0A)
KSG_TrigOut_LessThanLowerLimit = c_int16(0x0B)
KSG_TrigOut_MoreThanLowerLimit = c_int16(0x0C)
KSG_TrigOut_LessThanUpperLimit = c_int16(0x0D)
KSG_TrigOut_MoreThanUpperLimit = c_int16(0x0E)
KSG_TrigOut_BetweenLimits = c_int16(0x0F)
KSG_TrigOut_OutsideLimits = c_int16(0x10)

KSG_TriggerPortPolarity = c_int16
KSG_TrigPolarityHigh = c_int16(0x01)
KSG_TrigPolarityLow = c_int16(0x02)

KST_Stages = None

LD_DisplayUnits = c_ushort
LD_ILim = c_ushort(0x01)
LD_ILD = c_ushort(0x02)
LD_IPD = c_ushort(0x03)
LD_PLD = c_ushort(0x04)

LD_InputSourceFlags = c_ushort
LD_SoftwareOnly = c_ushort(0)
LD_SoftwareOnly = c_ushort(0x01)
LD_Potentiometer = c_ushort(0x01)
LD_ExternalSignal = c_ushort(0x02)
LD_Potentiometer = c_ushort(0x04)
LD_WheelAndSoftware = c_ushort(0x04)

LD_POLARITY = c_int16
LD_CathodeGrounded = c_int16(1)
LD_AnodeGrounded = c_int16(2)

LD_TIA_RANGES = c_int16
LD_TIA_10uA = c_int16(1)
LD_TIA_1_10uA = c_int16(1)
LD_TIA_100uA = c_int16(2)
LD_TIA_2_100uA = c_int16(2)
LD_TIA_1mA = c_int16(4)
LD_TIA_3_1mA = c_int16(4)
LD_TIA_10mA = c_int16(8)
LD_TIA_4_10mA = c_int16(8)

LS_DisplayUnits = c_ushort
LS_mAmps = c_ushort(0x01)
LS_mWatts = c_ushort(0x02)
LS_mDb = c_ushort(0x03)

LS_InputSourceFlags = c_ushort
LS_SoftwareOnly = c_ushort(0)
LS_ExternalSignal = c_ushort(0x01)
LS_Potentiometer = c_ushort(0x04)
LS_WheelAndSoftware = c_ushort(0x04)

MOD_AuxIOPortMode = None

MOD_IOPortMode = None

MOD_IOPortSource = None

MOD_Monitor_Variable = None

MOT_ButtonModes = None

MOT_JogModes = None

MOT_LimitSwitchModes = None

MOT_LimitSwitchSWModes = None

MOT_LimitsSoftwareApproachPolicy = None

MOT_MovementDirections = None

MOT_MovementModes = None

MOT_RasterScanMoveCmd = None

MOT_StopModes = None

MOT_TravelDirection = None

MOT_TravelModes = None

MOT_TriggerInputConfigModes = None

MOT_TriggerInputSource = None

MOT_TriggerOutputConfigModes = None

MOT_TriggerPolarity = None

MOT_TriggerState = None

MPC_IOModes = c_long
MPC_ToggleOnPositiveEdge = c_long(0x01)
MPC_SetPositionOnPositiveEdge = c_long(0x02)
MPC_OutputHighAtSetPosition = c_long(0x04)
MPC_OutputHighWhemMoving = c_long(0x08)

MPC_SignalModes = c_long
MPC_InputButton = c_long(0x01)
MPC_InputLogic = c_long(0x02)
MPC_InputSwap = c_long(0x04)
MPC_OutputLevel = c_long(0x10)
MPC_OutputPulse = c_long(0x20)
MPC_OutputSwap = c_long(0x40)

NT_ControlMode = None

NT_FeedbackSource = None

NT_Mode = None

NT_OddOrEven = None

NT_OutputVoltageRoute = None

NT_SignalState = None

NT_TIARange = None

NT_TIARangeMode = None

NT_VoltageRange = None

PDXC2_TriggerModes = c_uin16
Manual = c_uin16(0x00)
AnalogRising = c_uin16(0x01)
AnalogFalling = c_uin16(0x02)
FixedStepRising = c_uin16(0x03)
FixedStepFalling = c_uin16(0x04)
TwoPositionRising = c_uin16(0x05)
TwoPositionFalling = c_uin16(0x06)

POL_PaddleBits = None

POL_Paddles = None

PPC_DerivFilterState = c_short
DerivFilterOn = c_short(0x01)
DerivFilterOff = c_short(0x02)
DerivFilterOn = c_short(0x1)
DerivFilterOff = c_short(0x2)

PPC_DisplayIntensity = c_short
Bright = c_short(0x01)
Dim = c_short(0x02)
Off = c_short(0x03)

PPC_FeedbackPolarity = c_long
Inverted = c_long((WORD) - 1)
Inverted = c_long(-1)
NonInverted = c_long(0)

PPC_IOControlMode = c_short
SWOnly = c_short(0x00)
ExtBNC = c_short(0x01)
Joystick = c_short(0x02)
JoystickBnc = c_short(0x03)

PPC_IOFeedbackSourceDefinition = c_short
StrainGauge = c_short(0x01)
Capacitive = c_short(0x02)
Optical = c_short(0x03)

PPC_IOOutputBandwidth = c_short
OP_Unfiltered = c_short(0x01)
OP_200Hz = c_short(0x02)

PPC_IOOutputMode = c_short
HV = c_short(0x01)
PosRaw = c_short(0x02)
PosCorrected = c_short(0x03)

PPC_NotchFilterChannel = c_short
NotchFilter1 = c_short(0x01)
NotchFilter2 = c_short(0x02)
NotchFilterBoth = c_short(0x03)

PPC_NotchFilterState = c_short
NotchFilterOn = c_short(0x01)
NotchFilterOff = c_short(0x02)

PZ_AmpOutParameters = None

PZ_ControlModeTypes = None

PZ_InputSourceFlags = None

PZ_StageAxisParameters = None

PolarizerParameters = None

QD_FilterEnable = c_long
QD_Undefined = c_long(0)
QD_Enabled = c_long(1)
QD_Disabled = c_long(2)

QD_KPA_TrigModes = c_long
QD_Trig_Disabled = c_long(0x00)
QD_TrigIn_GPI = c_long(0x01)
QD_TrigIn_LoopOpenClose = c_long(0x02)
KD_TrigOut_GPO = c_long(0x0A)
KD_TrigOut_Sum = c_long(0x0B)
KD_TrigOut_Diff = c_long(0x0C)
KD_TrigOut_SumDiff = c_long(0x0D)

QD_KPA_TrigPolarities = c_long
GD_Trig_High = c_long(0x01)
GD_Trig_Low = c_long(0x02)

QD_LowVoltageRoute = c_short
QD_RouteUndefined = c_short(0)
QD_SMAOnly = c_short(1)
QD_HubAndSMA = c_short(2)

QD_OpenLoopHoldValues = c_short
QD_HoldOnZero = c_short(1)
QD_HoldOnLastValue = c_short(2)

QD_OperatingMode = c_short
QD_ModeUndefined = c_short(0)
QD_Monitor = c_short(1)
QD_OpenLoop = c_short(2)
QD_ClosedLoop = c_short(3)
QD_AutoOpenClosedLoop = c_short(4)

SC_OperatingModes = c_byte
SC_Manual = c_byte(0x01)
SC_Single = c_byte(0x02)
SC_Auto = c_byte(0x03)
SC_Triggered = c_byte(0x04)

SC_OperatingStates = c_byte
SC_Active = c_byte(0x01)
SC_Inactive = c_byte(0x02)

SC_SolenoidStates = c_byte
SC_SolenoidOpen = c_byte(0x01)
SC_SolenoidClosed = c_byte(0x02)

TC_DisplayModes = c_ushort
TC_ActualTemperature = c_ushort(0x00)
TC_TargetTemperature = c_ushort(0x01)
TC_TempDifference = c_ushort(0x02)
TC_Current = c_ushort(0x03)

TC_SensorTypes = c_ushort
TC_Transducer = c_ushort(0x00)
TC_TH20kOhm = c_ushort(0x01)
TC_TH200kOhm = c_ushort(0x02)

TIM_ButtonParameters = None

TIM_ButtonsMode = None

TIM_Channels = None

TIM_Direction = None

TIM_DriveOPParameters = None

TIM_JogMode = None

TIM_JogParameters = None

TSG_Display_Modes = c_short
TSG_Undefined = c_short(0)
TSG_Position = c_short(1)
TSG_Voltage = c_short(2)
TSG_Force = c_short(3)

TSG_Hub_Analogue_Modes = c_short
TSG_HubChannel1 = c_short(1)
TSG_HubChannel2 = c_short(2)

TST_Stages = None
