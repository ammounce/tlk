from c_types import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (TC_DisplayModes, TC_SensorTypes)
from .definitions.structures import (TC_LoopParameters, TLI_DeviceInfo, TLI_HardwareInformation)
from pathlib import Path


class TCubeTEC(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.TCube.TEC.DLL")

        self.TC_CheckConnection = self.lib.TC_CheckConnection
        self.TC_CheckConnection.restype = c_bool
        self.TC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_ClearMessageQueue = self.lib.TC_ClearMessageQueue
        self.TC_ClearMessageQueue.restype = None
        self.TC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_Close = self.lib.TC_Close
        self.TC_Close.restype = None
        self.TC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_Disable = self.lib.TC_Disable
        self.TC_Disable.restype = c_short
        self.TC_Disable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_Disconnect = self.lib.TC_Disconnect
        self.TC_Disconnect.restype = c_short
        self.TC_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_Enable = self.lib.TC_Enable
        self.TC_Enable.restype = c_short
        self.TC_Enable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_EnableLastMsgTimer = self.lib.TC_EnableLastMsgTimer
        self.TC_EnableLastMsgTimer.restype = None
        self.TC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.TC_GetCurrentLimit = self.lib.TC_GetCurrentLimit
        self.TC_GetCurrentLimit.restype = c_long
        self.TC_GetCurrentLimit.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetCurrentReading = self.lib.TC_GetCurrentReading
        self.TC_GetCurrentReading.restype = c_long
        self.TC_GetCurrentReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetFirmwareVersion = self.lib.TC_GetFirmwareVersion
        self.TC_GetFirmwareVersion.restype = c_ulong
        self.TC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetHWDisplayMode = self.lib.TC_GetHWDisplayMode
        self.TC_GetHWDisplayMode.restype = TC_DisplayModes
        self.TC_GetHWDisplayMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetHardwareInfo = self.lib.TC_GetHardwareInfo
        self.TC_GetHardwareInfo.restype = c_short
        self.TC_GetHardwareInfo.argtypes = [
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

        self.TC_GetHardwareInfoBlock = self.lib.TC_GetHardwareInfoBlock
        self.TC_GetHardwareInfoBlock.restype = c_short
        self.TC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.TC_GetLEDBrightness = self.lib.TC_GetLEDBrightness
        self.TC_GetLEDBrightness.restype = c_short
        self.TC_GetLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetNextMessage = self.lib.TC_GetNextMessage
        self.TC_GetNextMessage.restype = c_bool
        self.TC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.TC_GetSensorType = self.lib.TC_GetSensorType
        self.TC_GetSensorType.restype = TC_SensorTypes
        self.TC_GetSensorType.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetSoftwareVersion = self.lib.TC_GetSoftwareVersion
        self.TC_GetSoftwareVersion.restype = c_ulong
        self.TC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetStatusBits = self.lib.TC_GetStatusBits
        self.TC_GetStatusBits.restype = c_ulong
        self.TC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetTempLoopParams = self.lib.TC_GetTempLoopParams
        self.TC_GetTempLoopParams.restype = c_short
        self.TC_GetTempLoopParams.argtypes = [TC_LoopParameters, POINTER(c_char)]
        # *proportionalIntegralDerivativeParams, *serialNo

        self.TC_GetTemperatureReading = self.lib.TC_GetTemperatureReading
        self.TC_GetTemperatureReading.restype = c_short
        self.TC_GetTemperatureReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_GetTemperatureSet = self.lib.TC_GetTemperatureSet
        self.TC_GetTemperatureSet.restype = c_short
        self.TC_GetTemperatureSet.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_HasLastMsgTimerOverrun = self.lib.TC_HasLastMsgTimerOverrun
        self.TC_HasLastMsgTimerOverrun.restype = c_bool
        self.TC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_Identify = self.lib.TC_Identify
        self.TC_Identify.restype = None
        self.TC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_LoadNamedSettings = self.lib.TC_LoadNamedSettings
        self.TC_LoadNamedSettings.restype = c_bool
        self.TC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.TC_LoadSettings = self.lib.TC_LoadSettings
        self.TC_LoadSettings.restype = c_bool
        self.TC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_MessageQueueSize = self.lib.TC_MessageQueueSize
        self.TC_MessageQueueSize.restype = c_int
        self.TC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_Open = self.lib.TC_Open
        self.TC_Open.restype = c_short
        self.TC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_PersistSettings = self.lib.TC_PersistSettings
        self.TC_PersistSettings.restype = c_bool
        self.TC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_PollingDuration = self.lib.TC_PollingDuration
        self.TC_PollingDuration.restype = c_long
        self.TC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RegisterMessageCallback = self.lib.TC_RegisterMessageCallback
        self.TC_RegisterMessageCallback.restype = None
        self.TC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.TC_RequestCurrentLimit = self.lib.TC_RequestCurrentLimit
        self.TC_RequestCurrentLimit.restype = c_short
        self.TC_RequestCurrentLimit.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestHWDisplayMode = self.lib.TC_RequestHWDisplayMode
        self.TC_RequestHWDisplayMode.restype = c_short
        self.TC_RequestHWDisplayMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestLEDBrightness = self.lib.TC_RequestLEDBrightness
        self.TC_RequestLEDBrightness.restype = c_short
        self.TC_RequestLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestReadings = self.lib.TC_RequestReadings
        self.TC_RequestReadings.restype = c_short
        self.TC_RequestReadings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestSensorType = self.lib.TC_RequestSensorType
        self.TC_RequestSensorType.restype = c_short
        self.TC_RequestSensorType.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestSettings = self.lib.TC_RequestSettings
        self.TC_RequestSettings.restype = c_short
        self.TC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestStatus = self.lib.TC_RequestStatus
        self.TC_RequestStatus.restype = c_short
        self.TC_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestStatusBits = self.lib.TC_RequestStatusBits
        self.TC_RequestStatusBits.restype = c_short
        self.TC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestTempLoopParams = self.lib.TC_RequestTempLoopParams
        self.TC_RequestTempLoopParams.restype = c_short
        self.TC_RequestTempLoopParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_RequestTemperatureSet = self.lib.TC_RequestTemperatureSet
        self.TC_RequestTemperatureSet.restype = c_short
        self.TC_RequestTemperatureSet.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_Reset = self.lib.TC_Reset
        self.TC_Reset.restype = c_short
        self.TC_Reset.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_SetCurrentLimit = self.lib.TC_SetCurrentLimit
        self.TC_SetCurrentLimit.restype = c_short
        self.TC_SetCurrentLimit.argtypes = [POINTER(c_char), c_long]
        # *serialNo, maxCurrent

        self.TC_SetHWDisplayMode = self.lib.TC_SetHWDisplayMode
        self.TC_SetHWDisplayMode.restype = c_short
        self.TC_SetHWDisplayMode.argtypes = [POINTER(c_char), TC_DisplayModes]
        # *serialNo, mode

        self.TC_SetLEDBrightness = self.lib.TC_SetLEDBrightness
        self.TC_SetLEDBrightness.restype = c_short
        self.TC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
        # *serialNo, brightness

        self.TC_SetSensorType = self.lib.TC_SetSensorType
        self.TC_SetSensorType.restype = c_short
        self.TC_SetSensorType.argtypes = [POINTER(c_char), TC_SensorTypes]
        # *serialNo, sensor

        self.TC_SetTempLoopParams = self.lib.TC_SetTempLoopParams
        self.TC_SetTempLoopParams.restype = c_short
        self.TC_SetTempLoopParams.argtypes = [TC_LoopParameters, POINTER(c_char)]
        # *proportionalIntegralDerivativeParams, *serialNo

        self.TC_SetTemperature = self.lib.TC_SetTemperature
        self.TC_SetTemperature.restype = c_short
        self.TC_SetTemperature.argtypes = [POINTER(c_char), c_short]
        # *serialNo, temperature

        self.TC_StartPolling = self.lib.TC_StartPolling
        self.TC_StartPolling.restype = c_bool
        self.TC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.TC_StopPolling = self.lib.TC_StopPolling
        self.TC_StopPolling.restype = None
        self.TC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TC_TimeSinceLastMsgReceived = self.lib.TC_TimeSinceLastMsgReceived
        self.TC_TimeSinceLastMsgReceived.restype = c_bool
        self.TC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.TC_WaitForMessage = self.lib.TC_WaitForMessage
        self.TC_WaitForMessage.restype = c_bool
        self.TC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
