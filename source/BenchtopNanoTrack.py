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
    c_ulong,
    cdll)
from .safearray import SafeArray
from .definitions.enumerations import (
    KNA_FeedbackSource,
    KNA_TIARange,
    NT_ControlMode,
    NT_FeedbackSource,
    NT_Mode,
    NT_OddOrEven,
    NT_TIARange,
    NT_TIARangeMode)
from .definitions.structures import (
    BNT_IO_Settings,
    KNA_IOSettings,
    KNA_TIARangeParameters,
    KNA_TIAReading,
    NT_CircleDiameterLUT,
    NT_CircleParameters,
    NT_HVComponent,
    NT_IOSettings,
    NT_LowPassFilterParameters,
    NT_TIARangeParameters,
    NT_TIAReading,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class BenchtopNanoTrack(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.Benchtop.NanoTrak.dll")

        self.NT_ChannelEnable = self.lib.NT_ChannelEnable
        self.NT_ChannelEnable.restype = c_short
        self.NT_ChannelEnable.argtypes = [POINTER(c_char), c_long, c_bool]
        # *serialNo, channel, enable

        self.NT_CheckConnection = self.lib.NT_CheckConnection
        self.NT_CheckConnection.restype = c_bool
        self.NT_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_ClearMessageQueue = self.lib.NT_ClearMessageQueue
        self.NT_ClearMessageQueue.restype = None
        self.NT_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_Close = self.lib.NT_Close
        self.NT_Close.restype = None
        self.NT_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_Disconnect = self.lib.NT_Disconnect
        self.NT_Disconnect.restype = c_short
        self.NT_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_EnableLastMsgTimer = self.lib.NT_EnableLastMsgTimer
        self.NT_EnableLastMsgTimer.restype = None
        self.NT_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.NT_GetCircleDiameter = self.lib.NT_GetCircleDiameter
        self.NT_GetCircleDiameter.restype = c_long
        self.NT_GetCircleDiameter.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetCircleDiameterLUT = self.lib.NT_GetCircleDiameterLUT
        self.NT_GetCircleDiameterLUT.restype = c_short
        self.NT_GetCircleDiameterLUT.argtypes = [NT_CircleDiameterLUT, POINTER(c_char)]
        # *LUT, *serialNo

        self.NT_GetCircleHomePosition = self.lib.NT_GetCircleHomePosition
        self.NT_GetCircleHomePosition.restype = c_short
        self.NT_GetCircleHomePosition.argtypes = [NT_HVComponent, POINTER(c_char)]
        # *position, *serialNo

        self.NT_GetCircleParams = self.lib.NT_GetCircleParams
        self.NT_GetCircleParams.restype = c_short
        self.NT_GetCircleParams.argtypes = [NT_CircleParameters, POINTER(c_char)]
        # *params, *serialNo

        self.NT_GetCirclePosition = self.lib.NT_GetCirclePosition
        self.NT_GetCirclePosition.restype = c_short
        self.NT_GetCirclePosition.argtypes = [NT_HVComponent, POINTER(c_char)]
        # *position, *serialNo

        self.NT_GetControlMode = self.lib.NT_GetControlMode
        self.NT_GetControlMode.restype = NT_ControlMode
        self.NT_GetControlMode.argtypes = [POINTER(c_char), c_long]
        # *serialNo, channel

        self.NT_GetFeedbackSource = self.lib.NT_GetFeedbackSource
        self.NT_GetFeedbackSource.restype = NT_FeedbackSource
        self.NT_GetFeedbackSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetFirmwareVersion = self.lib.NT_GetFirmwareVersion
        self.NT_GetFirmwareVersion.restype = c_ulong
        self.NT_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetGain = self.lib.NT_GetGain
        self.NT_GetGain.restype = c_short
        self.NT_GetGain.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetHardwareInfo = self.lib.NT_GetHardwareInfo
        self.NT_GetHardwareInfo.restype = c_short
        self.NT_GetHardwareInfo.argtypes = [
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

        self.NT_GetHardwareInfoBlock = self.lib.NT_GetHardwareInfoBlock
        self.NT_GetHardwareInfoBlock.restype = c_short
        self.NT_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.NT_GetIOsettingsBlock = self.lib.NT_GetIOsettingsBlock
        self.NT_GetIOsettingsBlock.restype = c_short
        self.NT_GetIOsettingsBlock.argtypes = [BNT_IO_Settings, KNA_IOSettings, NT_IOSettings, POINTER(c_char), c_long]
        # *IOsettings, *IOsettings, *IOsettings, *serialNo, channel

        self.NT_GetMaxTravel = self.lib.NT_GetMaxTravel
        self.NT_GetMaxTravel.restype = c_short
        self.NT_GetMaxTravel.argtypes = [c_double, c_double, POINTER(c_char)]
        # &chanA, &chanB, *serialNo

        self.NT_GetMode = self.lib.NT_GetMode
        self.NT_GetMode.restype = NT_Mode
        self.NT_GetMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetNTChannels = self.lib.NT_GetNTChannels
        self.NT_GetNTChannels.restype = c_short
        self.NT_GetNTChannels.argtypes = [c_short, c_short, POINTER(c_char)]
        # &chanA, &chanB, *serialNo

        self.NT_GetNextMessage = self.lib.NT_GetNextMessage
        self.NT_GetNextMessage.restype = c_bool
        self.NT_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.NT_GetPhaseCompensationParams = self.lib.NT_GetPhaseCompensationParams
        self.NT_GetPhaseCompensationParams.restype = c_short
        self.NT_GetPhaseCompensationParams.argtypes = [NT_HVComponent, POINTER(c_char)]
        # *params, *serialNo

        self.NT_GetRangeMode = self.lib.NT_GetRangeMode
        self.NT_GetRangeMode.restype = c_short
        self.NT_GetRangeMode.argtypes = [NT_TIARangeMode, NT_OddOrEven, POINTER(c_char)]
        # *mode, *oddOrEven, *serialNo

        self.NT_GetReading = self.lib.NT_GetReading
        self.NT_GetReading.restype = c_short
        self.NT_GetReading.argtypes = [NT_TIAReading, KNA_TIAReading, POINTER(c_char)]
        # *reading, *reading, *serialNo

        self.NT_GetSignalState = self.lib.NT_GetSignalState
        self.NT_GetSignalState.restype = NT_SignalState
        self.NT_GetSignalState.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetSoftwareVersion = self.lib.NT_GetSoftwareVersion
        self.NT_GetSoftwareVersion.restype = c_ulong
        self.NT_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetStatusBits = self.lib.NT_GetStatusBits
        self.NT_GetStatusBits.restype = c_ulong
        self.NT_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetTIALPFilterParams = self.lib.NT_GetTIALPFilterParams
        self.NT_GetTIALPFilterParams.restype = c_short
        self.NT_GetTIALPFilterParams.argtypes = [NT_LowPassFilterParameters, POINTER(c_char)]
        # *params, *serialNo

        self.NT_GetTIARange = self.lib.NT_GetTIARange
        self.NT_GetTIARange.restype = NT_TIARange
        self.NT_GetTIARange.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_GetTIArangeParams = self.lib.NT_GetTIArangeParams
        self.NT_GetTIArangeParams.restype = c_short
        self.NT_GetTIArangeParams.argtypes = [NT_TIARangeParameters, KNA_TIARangeParameters, POINTER(c_char)]
        # *params, *params, *serialNo

        self.NT_GetTrackingThresholdSignal = self.lib.NT_GetTrackingThresholdSignal
        self.NT_GetTrackingThresholdSignal.restype = c_float
        self.NT_GetTrackingThresholdSignal.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_HasLastMsgTimerOverrun = self.lib.NT_HasLastMsgTimerOverrun
        self.NT_HasLastMsgTimerOverrun.restype = c_bool
        self.NT_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_HomeCircle = self.lib.NT_HomeCircle
        self.NT_HomeCircle.restype = c_short
        self.NT_HomeCircle.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_Identify = self.lib.NT_Identify
        self.NT_Identify.restype = None
        self.NT_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_IsChannelEnabled = self.lib.NT_IsChannelEnabled
        self.NT_IsChannelEnabled.restype = c_bool
        self.NT_IsChannelEnabled.argtypes = [POINTER(c_char), c_long]
        # *serialNo, channel

        self.NT_LoadNamedSettings = self.lib.NT_LoadNamedSettings
        self.NT_LoadNamedSettings.restype = c_bool
        self.NT_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.NT_LoadSettings = self.lib.NT_LoadSettings
        self.NT_LoadSettings.restype = c_bool
        self.NT_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_MessageQueueSize = self.lib.NT_MessageQueueSize
        self.NT_MessageQueueSize.restype = c_int
        self.NT_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_Open = self.lib.NT_Open
        self.NT_Open.restype = c_short
        self.NT_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_PersistSettings = self.lib.NT_PersistSettings
        self.NT_PersistSettings.restype = c_bool
        self.NT_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_PollingDuration = self.lib.NT_PollingDuration
        self.NT_PollingDuration.restype = c_long
        self.NT_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RegisterMessageCallback = self.lib.NT_RegisterMessageCallback
        self.NT_RegisterMessageCallback.restype = None
        self.NT_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.NT_RequestChannelStates = self.lib.NT_RequestChannelStates
        self.NT_RequestChannelStates.restype = c_short
        self.NT_RequestChannelStates.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestCircleDiameterLUT = self.lib.NT_RequestCircleDiameterLUT
        self.NT_RequestCircleDiameterLUT.restype = c_short
        self.NT_RequestCircleDiameterLUT.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestCircleHomePosition = self.lib.NT_RequestCircleHomePosition
        self.NT_RequestCircleHomePosition.restype = c_short
        self.NT_RequestCircleHomePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestCircleParams = self.lib.NT_RequestCircleParams
        self.NT_RequestCircleParams.restype = c_short
        self.NT_RequestCircleParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestCirclePosition = self.lib.NT_RequestCirclePosition
        self.NT_RequestCirclePosition.restype = c_short
        self.NT_RequestCirclePosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestControlMode = self.lib.NT_RequestControlMode
        self.NT_RequestControlMode.restype = c_short
        self.NT_RequestControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestFeedbackSource = self.lib.NT_RequestFeedbackSource
        self.NT_RequestFeedbackSource.restype = c_short
        self.NT_RequestFeedbackSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestGain = self.lib.NT_RequestGain
        self.NT_RequestGain.restype = c_short
        self.NT_RequestGain.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestMaxTravel = self.lib.NT_RequestMaxTravel
        self.NT_RequestMaxTravel.restype = c_short
        self.NT_RequestMaxTravel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestMode = self.lib.NT_RequestMode
        self.NT_RequestMode.restype = c_short
        self.NT_RequestMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestNTChannels = self.lib.NT_RequestNTChannels
        self.NT_RequestNTChannels.restype = c_short
        self.NT_RequestNTChannels.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestPhaseCompensationParams = self.lib.NT_RequestPhaseCompensationParams
        self.NT_RequestPhaseCompensationParams.restype = c_short
        self.NT_RequestPhaseCompensationParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestReading = self.lib.NT_RequestReading
        self.NT_RequestReading.restype = c_short
        self.NT_RequestReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestSettings = self.lib.NT_RequestSettings
        self.NT_RequestSettings.restype = c_short
        self.NT_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestSignalState = self.lib.NT_RequestSignalState
        self.NT_RequestSignalState.restype = c_short
        self.NT_RequestSignalState.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestStatus = self.lib.NT_RequestStatus
        self.NT_RequestStatus.restype = c_short
        self.NT_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestStatusBits = self.lib.NT_RequestStatusBits
        self.NT_RequestStatusBits.restype = c_short
        self.NT_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestTIALPFilterParams = self.lib.NT_RequestTIALPFilterParams
        self.NT_RequestTIALPFilterParams.restype = c_short
        self.NT_RequestTIALPFilterParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestTIArangeParams = self.lib.NT_RequestTIArangeParams
        self.NT_RequestTIArangeParams.restype = c_short
        self.NT_RequestTIArangeParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_RequestTrackingThresholdSignal = self.lib.NT_RequestTrackingThresholdSignal
        self.NT_RequestTrackingThresholdSignal.restype = c_short
        self.NT_RequestTrackingThresholdSignal.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_SetCircleDiameter = self.lib.NT_SetCircleDiameter
        self.NT_SetCircleDiameter.restype = c_short
        self.NT_SetCircleDiameter.argtypes = [POINTER(c_char), c_long]
        # *serialNo, diameter

        self.NT_SetCircleDiameterLUT = self.lib.NT_SetCircleDiameterLUT
        self.NT_SetCircleDiameterLUT.restype = c_short
        self.NT_SetCircleDiameterLUT.argtypes = [NT_CircleDiameterLUT, POINTER(c_char)]
        # *LUT, *serialNo

        self.NT_SetCircleHomePosition = self.lib.NT_SetCircleHomePosition
        self.NT_SetCircleHomePosition.restype = c_short
        self.NT_SetCircleHomePosition.argtypes = [NT_HVComponent, POINTER(c_char)]
        # *position, *serialNo

        self.NT_SetCircleParams = self.lib.NT_SetCircleParams
        self.NT_SetCircleParams.restype = c_short
        self.NT_SetCircleParams.argtypes = [NT_CircleParameters, POINTER(c_char)]
        # *params, *serialNo

        self.NT_SetControlMode = self.lib.NT_SetControlMode
        self.NT_SetControlMode.restype = c_short
        self.NT_SetControlMode.argtypes = [POINTER(c_char), c_long, NT_ControlMode]
        # *serialNo, channel, mode

        self.NT_SetFeedbackSource = self.lib.NT_SetFeedbackSource
        self.NT_SetFeedbackSource.restype = c_short
        self.NT_SetFeedbackSource.argtypes = [POINTER(c_char), NT_FeedbackSource, KNA_FeedbackSource]
        # *serialNo, input, input

        self.NT_SetGain = self.lib.NT_SetGain
        self.NT_SetGain.restype = c_short
        self.NT_SetGain.argtypes = [POINTER(c_char), c_short]
        # *serialNo, gain

        self.NT_SetIOsettingsBlock = self.lib.NT_SetIOsettingsBlock
        self.NT_SetIOsettingsBlock.restype = c_short
        self.NT_SetIOsettingsBlock.argtypes = [BNT_IO_Settings, KNA_IOSettings, NT_IOSettings, POINTER(c_char), c_long]
        # *IOsettings, *IOsettings, *IOsettings, *serialNo, channel

        self.NT_SetMode = self.lib.NT_SetMode
        self.NT_SetMode.restype = c_short
        self.NT_SetMode.argtypes = [POINTER(c_char), NT_Mode]
        # *serialNo, mode

        self.NT_SetNTChannels = self.lib.NT_SetNTChannels
        self.NT_SetNTChannels.restype = c_short
        self.NT_SetNTChannels.argtypes = [POINTER(c_char), c_short, c_short]
        # *serialNo, chanA, chanB

        self.NT_SetPhaseCompensationParams = self.lib.NT_SetPhaseCompensationParams
        self.NT_SetPhaseCompensationParams.restype = c_short
        self.NT_SetPhaseCompensationParams.argtypes = [NT_HVComponent, POINTER(c_char)]
        # *params, *serialNo

        self.NT_SetRangeMode = self.lib.NT_SetRangeMode
        self.NT_SetRangeMode.restype = c_short
        self.NT_SetRangeMode.argtypes = [POINTER(c_char), NT_TIARangeMode, NT_OddOrEven]
        # *serialNo, mode, oddOrEven

        self.NT_SetTIALPFilterParams = self.lib.NT_SetTIALPFilterParams
        self.NT_SetTIALPFilterParams.restype = c_short
        self.NT_SetTIALPFilterParams.argtypes = [NT_LowPassFilterParameters, POINTER(c_char)]
        # *params, *serialNo

        self.NT_SetTIARange = self.lib.NT_SetTIARange
        self.NT_SetTIARange.restype = c_short
        self.NT_SetTIARange.argtypes = [POINTER(c_char), NT_TIARange, KNA_TIARange]
        # *serialNo, range, range

        self.NT_SetTIArangeParams = self.lib.NT_SetTIArangeParams
        self.NT_SetTIArangeParams.restype = c_short
        self.NT_SetTIArangeParams.argtypes = [NT_TIARangeParameters, KNA_TIARangeParameters, POINTER(c_char)]
        # *params, *params, *serialNo

        self.NT_SetTrackingThresholdSignal = self.lib.NT_SetTrackingThresholdSignal
        self.NT_SetTrackingThresholdSignal.restype = c_short
        self.NT_SetTrackingThresholdSignal.argtypes = [POINTER(c_char), c_float]
        # *serialNo, threshold

        self.NT_StartPolling = self.lib.NT_StartPolling
        self.NT_StartPolling.restype = c_bool
        self.NT_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.NT_StopPolling = self.lib.NT_StopPolling
        self.NT_StopPolling.restype = None
        self.NT_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.NT_TimeSinceLastMsgReceived = self.lib.NT_TimeSinceLastMsgReceived
        self.NT_TimeSinceLastMsgReceived.restype = c_bool
        self.NT_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.NT_WaitForMessage = self.lib.NT_WaitForMessage
        self.NT_WaitForMessage.restype = c_bool
        self.NT_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
