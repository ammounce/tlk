from c_types import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (QD_OperatingMode)
from .definitions.structures import (
    QD_LoopParameters,
    QD_LowPassFilterParameters,
    QD_NotchFilterParameters,
    QD_PIDParameters,
    QD_Position,
    QD_PositionDemandParameters,
    QD_Readings,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class TCubeQuad(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.TCube.Quad.DLL")

        self.QD_CheckConnection = self.lib.QD_CheckConnection
        self.QD_CheckConnection.restype = c_bool
        self.QD_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_ClearMessageQueue = self.lib.QD_ClearMessageQueue
        self.QD_ClearMessageQueue.restype = None
        self.QD_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_Close = self.lib.QD_Close
        self.QD_Close.restype = None
        self.QD_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_EnableLastMsgTimer = self.lib.QD_EnableLastMsgTimer
        self.QD_EnableLastMsgTimer.restype = None
        self.QD_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.QD_GetDemandedPosition = self.lib.QD_GetDemandedPosition
        self.QD_GetDemandedPosition.restype = c_short
        self.QD_GetDemandedPosition.argtypes = [QD_Position, POINTER(c_char)]
        # *position, *serialNo

        self.QD_GetFirmwareVersion = self.lib.QD_GetFirmwareVersion
        self.QD_GetFirmwareVersion.restype = c_ulong
        self.QD_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_GetHardwareInfo = self.lib.QD_GetHardwareInfo
        self.QD_GetHardwareInfo.restype = c_short
        self.QD_GetHardwareInfo.argtypes = [
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

        self.QD_GetHardwareInfoBlock = self.lib.QD_GetHardwareInfoBlock
        self.QD_GetHardwareInfoBlock.restype = c_short
        self.QD_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.QD_GetLEDBrightness = self.lib.QD_GetLEDBrightness
        self.QD_GetLEDBrightness.restype = c_long
        self.QD_GetLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_GetLoopPIDparams = self.lib.QD_GetLoopPIDparams
        self.QD_GetLoopPIDparams.restype = c_short
        self.QD_GetLoopPIDparams.argtypes = [QD_LoopParameters, POINTER(c_char)]
        # *loopParams, *serialNo

        self.QD_GetLowPassFilterparams = self.lib.QD_GetLowPassFilterparams
        self.QD_GetLowPassFilterparams.restype = c_short
        self.QD_GetLowPassFilterparams.argtypes = [QD_LowPassFilterParameters, POINTER(c_char)]
        # *lowPassParams, *serialNo

        self.QD_GetNextMessage = self.lib.QD_GetNextMessage
        self.QD_GetNextMessage.restype = c_bool
        self.QD_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.QD_GetNotchFilterparams = self.lib.QD_GetNotchFilterparams
        self.QD_GetNotchFilterparams.restype = c_short
        self.QD_GetNotchFilterparams.argtypes = [QD_NotchFilterParameters, POINTER(c_char)]
        # *notchParams, *serialNo

        self.QD_GetOperatingMode = self.lib.QD_GetOperatingMode
        self.QD_GetOperatingMode.restype = QD_OperatingMode
        self.QD_GetOperatingMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_GetPIDparams = self.lib.QD_GetPIDparams
        self.QD_GetPIDparams.restype = c_short
        self.QD_GetPIDparams.argtypes = [QD_PIDParameters, POINTER(c_char)]
        # *proportionalIntegralDerivativeParams, *serialNo

        self.QD_GetPosDemandParams = self.lib.QD_GetPosDemandParams
        self.QD_GetPosDemandParams.restype = c_short
        self.QD_GetPosDemandParams.argtypes = [QD_PositionDemandParameters, POINTER(c_char)]
        # *demandParams, *serialNo

        self.QD_GetReading = self.lib.QD_GetReading
        self.QD_GetReading.restype = c_short
        self.QD_GetReading.argtypes = [QD_Readings, POINTER(c_char)]
        # *reading, *serialNo

        self.QD_GetSoftwareVersion = self.lib.QD_GetSoftwareVersion
        self.QD_GetSoftwareVersion.restype = c_ulong
        self.QD_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_GetStatusBits = self.lib.QD_GetStatusBits
        self.QD_GetStatusBits.restype = c_ulong
        self.QD_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_HasLastMsgTimerOverrun = self.lib.QD_HasLastMsgTimerOverrun
        self.QD_HasLastMsgTimerOverrun.restype = c_bool
        self.QD_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_Identify = self.lib.QD_Identify
        self.QD_Identify.restype = None
        self.QD_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_LoadNamedSettings = self.lib.QD_LoadNamedSettings
        self.QD_LoadNamedSettings.restype = c_bool
        self.QD_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.QD_LoadSettings = self.lib.QD_LoadSettings
        self.QD_LoadSettings.restype = c_bool
        self.QD_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_MessageQueueSize = self.lib.QD_MessageQueueSize
        self.QD_MessageQueueSize.restype = c_int
        self.QD_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_Open = self.lib.QD_Open
        self.QD_Open.restype = c_short
        self.QD_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_PersistSettings = self.lib.QD_PersistSettings
        self.QD_PersistSettings.restype = c_bool
        self.QD_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_PollingDuration = self.lib.QD_PollingDuration
        self.QD_PollingDuration.restype = c_long
        self.QD_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_RegisterMessageCallback = self.lib.QD_RegisterMessageCallback
        self.QD_RegisterMessageCallback.restype = None
        self.QD_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.QD_RequestLEDBrightness = self.lib.QD_RequestLEDBrightness
        self.QD_RequestLEDBrightness.restype = c_short
        self.QD_RequestLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_RequestLoopPIDparams = self.lib.QD_RequestLoopPIDparams
        self.QD_RequestLoopPIDparams.restype = c_short
        self.QD_RequestLoopPIDparams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_RequestOperatingMode = self.lib.QD_RequestOperatingMode
        self.QD_RequestOperatingMode.restype = c_short
        self.QD_RequestOperatingMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_RequestPosDemandParams = self.lib.QD_RequestPosDemandParams
        self.QD_RequestPosDemandParams.restype = c_short
        self.QD_RequestPosDemandParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_RequestReading = self.lib.QD_RequestReading
        self.QD_RequestReading.restype = c_short
        self.QD_RequestReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_RequestSettings = self.lib.QD_RequestSettings
        self.QD_RequestSettings.restype = c_short
        self.QD_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_RequestStatus = self.lib.QD_RequestStatus
        self.QD_RequestStatus.restype = c_short
        self.QD_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_RequestStatusBits = self.lib.QD_RequestStatusBits
        self.QD_RequestStatusBits.restype = c_short
        self.QD_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_SetLEDBrightness = self.lib.QD_SetLEDBrightness
        self.QD_SetLEDBrightness.restype = c_short
        self.QD_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
        # *serialNo, brightness

        self.QD_SetLoopPIDparams = self.lib.QD_SetLoopPIDparams
        self.QD_SetLoopPIDparams.restype = c_short
        self.QD_SetLoopPIDparams.argtypes = [QD_LoopParameters, POINTER(c_char)]
        # *loopParams, *serialNo

        self.QD_SetLowPassFilterparams = self.lib.QD_SetLowPassFilterparams
        self.QD_SetLowPassFilterparams.restype = c_short
        self.QD_SetLowPassFilterparams.argtypes = [QD_LowPassFilterParameters, POINTER(c_char)]
        # *lowPassParams, *serialNo

        self.QD_SetNotchFilterparams = self.lib.QD_SetNotchFilterparams
        self.QD_SetNotchFilterparams.restype = c_short
        self.QD_SetNotchFilterparams.argtypes = [QD_NotchFilterParameters, POINTER(c_char)]
        # *proportionalIntegralDerivativeParams, *serialNo

        self.QD_SetOperatingMode = self.lib.QD_SetOperatingMode
        self.QD_SetOperatingMode.restype = c_short
        self.QD_SetOperatingMode.argtypes = [POINTER(c_char), c_bool, QD_OperatingMode]
        # *serialNo, autoOpenCloseLoop, mode

        self.QD_SetPIDparams = self.lib.QD_SetPIDparams
        self.QD_SetPIDparams.restype = c_short
        self.QD_SetPIDparams.argtypes = [QD_PIDParameters, POINTER(c_char)]
        # *proportionalIntegralDerivativeParams, *serialNo

        self.QD_SetPosDemandParams = self.lib.QD_SetPosDemandParams
        self.QD_SetPosDemandParams.restype = c_short
        self.QD_SetPosDemandParams.argtypes = [QD_PositionDemandParameters, POINTER(c_char)]
        # *demandParams, *serialNo

        self.QD_SetPosition = self.lib.QD_SetPosition
        self.QD_SetPosition.restype = c_short
        self.QD_SetPosition.argtypes = [QD_Position, POINTER(c_char)]
        # *position, *serialNo

        self.QD_StartPolling = self.lib.QD_StartPolling
        self.QD_StartPolling.restype = c_bool
        self.QD_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.QD_StopPolling = self.lib.QD_StopPolling
        self.QD_StopPolling.restype = None
        self.QD_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.QD_TimeSinceLastMsgReceived = self.lib.QD_TimeSinceLastMsgReceived
        self.QD_TimeSinceLastMsgReceived.restype = c_bool
        self.QD_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.QD_WaitForMessage = self.lib.QD_WaitForMessage
        self.QD_WaitForMessage.restype = c_bool
        self.QD_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
