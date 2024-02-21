from c_types import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_uint, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (TSG_Display_Modes, TSG_Hub_Analogue_Modes)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation, TSG_IOSettings)
from pathlib import Path


class TCubeStrainGauge(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.TCube.StrainGauge.DLL")

        self.SG_CheckConnection = self.lib.SG_CheckConnection
        self.SG_CheckConnection.restype = c_bool
        self.SG_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_ClearMessageQueue = self.lib.SG_ClearMessageQueue
        self.SG_ClearMessageQueue.restype = None
        self.SG_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_Close = self.lib.SG_Close
        self.SG_Close.restype = None
        self.SG_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_Disable = self.lib.SG_Disable
        self.SG_Disable.restype = c_short
        self.SG_Disable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_Disconnect = self.lib.SG_Disconnect
        self.SG_Disconnect.restype = c_short
        self.SG_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_Enable = self.lib.SG_Enable
        self.SG_Enable.restype = c_short
        self.SG_Enable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_EnableLastMsgTimer = self.lib.SG_EnableLastMsgTimer
        self.SG_EnableLastMsgTimer.restype = None
        self.SG_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.SG_GetDisplayMode = self.lib.SG_GetDisplayMode
        self.SG_GetDisplayMode.restype = TSG_Display_Modes
        self.SG_GetDisplayMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_GetFirmwareVersion = self.lib.SG_GetFirmwareVersion
        self.SG_GetFirmwareVersion.restype = c_ulong
        self.SG_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_GetForceCalib = self.lib.SG_GetForceCalib
        self.SG_GetForceCalib.restype = c_uint
        self.SG_GetForceCalib.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_GetHardwareInfo = self.lib.SG_GetHardwareInfo
        self.SG_GetHardwareInfo.restype = c_short
        self.SG_GetHardwareInfo.argtypes = [
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

        self.SG_GetHardwareInfoBlock = self.lib.SG_GetHardwareInfoBlock
        self.SG_GetHardwareInfoBlock.restype = c_short
        self.SG_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.SG_GetHubAnalogOutput = self.lib.SG_GetHubAnalogOutput
        self.SG_GetHubAnalogOutput.restype = TSG_Hub_Analogue_Modes
        self.SG_GetHubAnalogOutput.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_GetHubBay = self.lib.SG_GetHubBay
        self.SG_GetHubBay.restype = POINTER(c_char)
        self.SG_GetHubBay.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_GetIOsettingsBlock = self.lib.SG_GetIOsettingsBlock
        self.SG_GetIOsettingsBlock.restype = c_short
        self.SG_GetIOsettingsBlock.argtypes = [TSG_IOSettings, POINTER(c_char)]
        # *inputOutputSettings, *serialNo

        self.SG_GetLEDBrightness = self.lib.SG_GetLEDBrightness
        self.SG_GetLEDBrightness.restype = c_short
        self.SG_GetLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_GetMaximumTravel = self.lib.SG_GetMaximumTravel
        self.SG_GetMaximumTravel.restype = c_long
        self.SG_GetMaximumTravel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_GetNextMessage = self.lib.SG_GetNextMessage
        self.SG_GetNextMessage.restype = c_bool
        self.SG_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.SG_GetReading = self.lib.SG_GetReading
        self.SG_GetReading.restype = c_short
        self.SG_GetReading.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, smoothed

        self.SG_GetReadingExt = self.lib.SG_GetReadingExt
        self.SG_GetReadingExt.restype = c_int
        self.SG_GetReadingExt.argtypes = [c_bool, POINTER(c_char), c_bool]
        # *overrange, *serialNo, clipReadng

        self.SG_GetSoftwareVersion = self.lib.SG_GetSoftwareVersion
        self.SG_GetSoftwareVersion.restype = c_ulong
        self.SG_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_GetStatusBits = self.lib.SG_GetStatusBits
        self.SG_GetStatusBits.restype = c_ulong
        self.SG_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_HasLastMsgTimerOverrun = self.lib.SG_HasLastMsgTimerOverrun
        self.SG_HasLastMsgTimerOverrun.restype = c_bool
        self.SG_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_Identify = self.lib.SG_Identify
        self.SG_Identify.restype = None
        self.SG_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_LoadNamedSettings = self.lib.SG_LoadNamedSettings
        self.SG_LoadNamedSettings.restype = c_bool
        self.SG_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.SG_LoadSettings = self.lib.SG_LoadSettings
        self.SG_LoadSettings.restype = c_bool
        self.SG_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_MessageQueueSize = self.lib.SG_MessageQueueSize
        self.SG_MessageQueueSize.restype = c_int
        self.SG_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_Open = self.lib.SG_Open
        self.SG_Open.restype = c_short
        self.SG_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_PersistSettings = self.lib.SG_PersistSettings
        self.SG_PersistSettings.restype = c_bool
        self.SG_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_PollingDuration = self.lib.SG_PollingDuration
        self.SG_PollingDuration.restype = c_long
        self.SG_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RegisterMessageCallback = self.lib.SG_RegisterMessageCallback
        self.SG_RegisterMessageCallback.restype = None
        self.SG_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.SG_RequestDisplayMode = self.lib.SG_RequestDisplayMode
        self.SG_RequestDisplayMode.restype = c_short
        self.SG_RequestDisplayMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RequestForceCalib = self.lib.SG_RequestForceCalib
        self.SG_RequestForceCalib.restype = c_short
        self.SG_RequestForceCalib.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RequestHubAnalogOutput = self.lib.SG_RequestHubAnalogOutput
        self.SG_RequestHubAnalogOutput.restype = c_short
        self.SG_RequestHubAnalogOutput.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RequestIOsettings = self.lib.SG_RequestIOsettings
        self.SG_RequestIOsettings.restype = c_short
        self.SG_RequestIOsettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RequestLEDBrightness = self.lib.SG_RequestLEDBrightness
        self.SG_RequestLEDBrightness.restype = c_short
        self.SG_RequestLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RequestMaximumTravel = self.lib.SG_RequestMaximumTravel
        self.SG_RequestMaximumTravel.restype = c_short
        self.SG_RequestMaximumTravel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RequestReading = self.lib.SG_RequestReading
        self.SG_RequestReading.restype = c_short
        self.SG_RequestReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RequestSettings = self.lib.SG_RequestSettings
        self.SG_RequestSettings.restype = c_short
        self.SG_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_RequestStatus = self.lib.SG_RequestStatus
        self.SG_RequestStatus.restype = c_short
        self.SG_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_SetDisplayMode = self.lib.SG_SetDisplayMode
        self.SG_SetDisplayMode.restype = c_short
        self.SG_SetDisplayMode.argtypes = [POINTER(c_char), TSG_Display_Modes]
        # *serialNo, mode

        self.SG_SetForceCalib = self.lib.SG_SetForceCalib
        self.SG_SetForceCalib.restype = c_short
        self.SG_SetForceCalib.argtypes = [POINTER(c_char), c_uint]
        # *serialNo, forceCalibration

        self.SG_SetHubAnalogOutput = self.lib.SG_SetHubAnalogOutput
        self.SG_SetHubAnalogOutput.restype = c_short
        self.SG_SetHubAnalogOutput.argtypes = [POINTER(c_char), TSG_Hub_Analogue_Modes]
        # *serialNo, hubAnalogOutput

        self.SG_SetIOsettings = self.lib.SG_SetIOsettings
        self.SG_SetIOsettings.restype = c_short
        self.SG_SetIOsettings.argtypes = [POINTER(c_char), c_uint, TSG_Display_Modes, TSG_Hub_Analogue_Modes]
        # *serialNo, calibrationForce, displayMode, hubAnalogOutput

        self.SG_SetIOsettingsBlock = self.lib.SG_SetIOsettingsBlock
        self.SG_SetIOsettingsBlock.restype = c_short
        self.SG_SetIOsettingsBlock.argtypes = [TSG_IOSettings, POINTER(c_char)]
        # *inputOutputSettings, *serialNo

        self.SG_SetLEDBrightness = self.lib.SG_SetLEDBrightness
        self.SG_SetLEDBrightness.restype = c_short
        self.SG_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
        # *serialNo, brightness

        self.SG_SetZero = self.lib.SG_SetZero
        self.SG_SetZero.restype = c_short
        self.SG_SetZero.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_StartPolling = self.lib.SG_StartPolling
        self.SG_StartPolling.restype = c_bool
        self.SG_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.SG_StopPolling = self.lib.SG_StopPolling
        self.SG_StopPolling.restype = None
        self.SG_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SG_TimeSinceLastMsgReceived = self.lib.SG_TimeSinceLastMsgReceived
        self.SG_TimeSinceLastMsgReceived.restype = c_bool
        self.SG_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.SG_WaitForMessage = self.lib.SG_WaitForMessage
        self.SG_WaitForMessage.restype = c_bool
        self.SG_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
