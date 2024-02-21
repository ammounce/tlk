from c_types import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_uint, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (FF_Positions)
from .definitions.structures import (FF_IOSettings, TLI_DeviceInfo)
from pathlib import Path


class FilterFlipper(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.FilterFlipper.DLL")

        self.FF_CheckConnection = self.lib.FF_CheckConnection
        self.FF_CheckConnection.restype = c_bool
        self.FF_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_ClearMessageQueue = self.lib.FF_ClearMessageQueue
        self.FF_ClearMessageQueue.restype = None
        self.FF_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_Close = self.lib.FF_Close
        self.FF_Close.restype = None
        self.FF_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_EnableLastMsgTimer = self.lib.FF_EnableLastMsgTimer
        self.FF_EnableLastMsgTimer.restype = None
        self.FF_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.FF_GetFirmwareVersion = self.lib.FF_GetFirmwareVersion
        self.FF_GetFirmwareVersion.restype = c_ulong
        self.FF_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_GetHardwareInfo = self.lib.FF_GetHardwareInfo
        self.FF_GetHardwareInfo.restype = c_short
        self.FF_GetHardwareInfo.argtypes = [
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

        self.FF_GetIOSettings = self.lib.FF_GetIOSettings
        self.FF_GetIOSettings.restype = c_short
        self.FF_GetIOSettings.argtypes = [POINTER(c_char), FF_IOSettings]
        # *serialNo, *settings

        self.FF_GetNextMessage = self.lib.FF_GetNextMessage
        self.FF_GetNextMessage.restype = c_bool
        self.FF_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.FF_GetNumberPositions = self.lib.FF_GetNumberPositions
        self.FF_GetNumberPositions.restype = c_int
        self.FF_GetNumberPositions.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_GetPosition = self.lib.FF_GetPosition
        self.FF_GetPosition.restype = FF_Positions
        self.FF_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_GetSoftwareVersion = self.lib.FF_GetSoftwareVersion
        self.FF_GetSoftwareVersion.restype = c_ulong
        self.FF_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_GetStatusBits = self.lib.FF_GetStatusBits
        self.FF_GetStatusBits.restype = c_ulong
        self.FF_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_GetTransitTime = self.lib.FF_GetTransitTime
        self.FF_GetTransitTime.restype = c_uint
        self.FF_GetTransitTime.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_HasLastMsgTimerOverrun = self.lib.FF_HasLastMsgTimerOverrun
        self.FF_HasLastMsgTimerOverrun.restype = c_bool
        self.FF_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_Home = self.lib.FF_Home
        self.FF_Home.restype = c_short
        self.FF_Home.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_Identify = self.lib.FF_Identify
        self.FF_Identify.restype = None
        self.FF_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_LoadNamedSettings = self.lib.FF_LoadNamedSettings
        self.FF_LoadNamedSettings.restype = c_bool
        self.FF_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.FF_LoadSettings = self.lib.FF_LoadSettings
        self.FF_LoadSettings.restype = c_bool
        self.FF_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_MessageQueueSize = self.lib.FF_MessageQueueSize
        self.FF_MessageQueueSize.restype = c_int
        self.FF_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_MoveToPosition = self.lib.FF_MoveToPosition
        self.FF_MoveToPosition.restype = c_short
        self.FF_MoveToPosition.argtypes = [POINTER(c_char), FF_Positions]
        # *serialNo, position

        self.FF_Open = self.lib.FF_Open
        self.FF_Open.restype = c_short
        self.FF_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_PersistSettings = self.lib.FF_PersistSettings
        self.FF_PersistSettings.restype = c_bool
        self.FF_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_PollingDuration = self.lib.FF_PollingDuration
        self.FF_PollingDuration.restype = c_long
        self.FF_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_RegisterMessageCallback = self.lib.FF_RegisterMessageCallback
        self.FF_RegisterMessageCallback.restype = None
        self.FF_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.FF_RequestIOSettings = self.lib.FF_RequestIOSettings
        self.FF_RequestIOSettings.restype = c_short
        self.FF_RequestIOSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_RequestSettings = self.lib.FF_RequestSettings
        self.FF_RequestSettings.restype = c_short
        self.FF_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_RequestStatus = self.lib.FF_RequestStatus
        self.FF_RequestStatus.restype = c_short
        self.FF_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_SetIOSettings = self.lib.FF_SetIOSettings
        self.FF_SetIOSettings.restype = c_short
        self.FF_SetIOSettings.argtypes = [POINTER(c_char), FF_IOSettings]
        # *serialNo, *settings

        self.FF_SetTransitTime = self.lib.FF_SetTransitTime
        self.FF_SetTransitTime.restype = c_short
        self.FF_SetTransitTime.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, transitTime

        self.FF_StartPolling = self.lib.FF_StartPolling
        self.FF_StartPolling.restype = c_bool
        self.FF_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.FF_StopPolling = self.lib.FF_StopPolling
        self.FF_StopPolling.restype = None
        self.FF_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.FF_TimeSinceLastMsgReceived = self.lib.FF_TimeSinceLastMsgReceived
        self.FF_TimeSinceLastMsgReceived.restype = c_bool
        self.FF_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.FF_WaitForMessage = self.lib.FF_WaitForMessage
        self.FF_WaitForMessage.restype = c_bool
        self.FF_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
