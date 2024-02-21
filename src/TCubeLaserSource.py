from c_types import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (LS_DisplayUnits, LS_InputSourceFlags)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation)
from pathlib import Path


class TCubeLaserSource(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.TCube.LaserSource.DLL")

        self.LS_CheckConnection = self.lib.LS_CheckConnection
        self.LS_CheckConnection.restype = c_bool
        self.LS_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_ClearMessageQueue = self.lib.LS_ClearMessageQueue
        self.LS_ClearMessageQueue.restype = None
        self.LS_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_Close = self.lib.LS_Close
        self.LS_Close.restype = None
        self.LS_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_Disable = self.lib.LS_Disable
        self.LS_Disable.restype = c_short
        self.LS_Disable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_DisableOutput = self.lib.LS_DisableOutput
        self.LS_DisableOutput.restype = c_short
        self.LS_DisableOutput.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_Enable = self.lib.LS_Enable
        self.LS_Enable.restype = c_short
        self.LS_Enable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_EnableLastMsgTimer = self.lib.LS_EnableLastMsgTimer
        self.LS_EnableLastMsgTimer.restype = None
        self.LS_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.LS_EnableOutput = self.lib.LS_EnableOutput
        self.LS_EnableOutput.restype = c_short
        self.LS_EnableOutput.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetControlSource = self.lib.LS_GetControlSource
        self.LS_GetControlSource.restype = LS_InputSourceFlags
        self.LS_GetControlSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetCurrentReading = self.lib.LS_GetCurrentReading
        self.LS_GetCurrentReading.restype = c_long
        self.LS_GetCurrentReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetDisplayUnits = self.lib.LS_GetDisplayUnits
        self.LS_GetDisplayUnits.restype = LS_DisplayUnits
        self.LS_GetDisplayUnits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetFirmwareVersion = self.lib.LS_GetFirmwareVersion
        self.LS_GetFirmwareVersion.restype = c_ulong
        self.LS_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetHardwareInfo = self.lib.LS_GetHardwareInfo
        self.LS_GetHardwareInfo.restype = c_short
        self.LS_GetHardwareInfo.argtypes = [
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

        self.LS_GetHardwareInfoBlock = self.lib.LS_GetHardwareInfoBlock
        self.LS_GetHardwareInfoBlock.restype = c_short
        self.LS_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.LS_GetInterlockState = self.lib.LS_GetInterlockState
        self.LS_GetInterlockState.restype = c_byte
        self.LS_GetInterlockState.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetLEDBrightness = self.lib.LS_GetLEDBrightness
        self.LS_GetLEDBrightness.restype = c_long
        self.LS_GetLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetLimits = self.lib.LS_GetLimits
        self.LS_GetLimits.restype = c_short
        self.LS_GetLimits.argtypes = [c_long, c_long, POINTER(c_char)]
        # &maxCurrent, &maxPower, *serialNo

        self.LS_GetNextMessage = self.lib.LS_GetNextMessage
        self.LS_GetNextMessage.restype = c_bool
        self.LS_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.LS_GetPowerReading = self.lib.LS_GetPowerReading
        self.LS_GetPowerReading.restype = c_long
        self.LS_GetPowerReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetPowerSet = self.lib.LS_GetPowerSet
        self.LS_GetPowerSet.restype = c_long
        self.LS_GetPowerSet.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetSoftwareVersion = self.lib.LS_GetSoftwareVersion
        self.LS_GetSoftwareVersion.restype = c_ulong
        self.LS_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetStatusBits = self.lib.LS_GetStatusBits
        self.LS_GetStatusBits.restype = c_ulong
        self.LS_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_GetWavelength = self.lib.LS_GetWavelength
        self.LS_GetWavelength.restype = c_long
        self.LS_GetWavelength.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_HasLastMsgTimerOverrun = self.lib.LS_HasLastMsgTimerOverrun
        self.LS_HasLastMsgTimerOverrun.restype = c_bool
        self.LS_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_Identify = self.lib.LS_Identify
        self.LS_Identify.restype = None
        self.LS_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_LoadNamedSettings = self.lib.LS_LoadNamedSettings
        self.LS_LoadNamedSettings.restype = c_bool
        self.LS_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.LS_LoadSettings = self.lib.LS_LoadSettings
        self.LS_LoadSettings.restype = c_bool
        self.LS_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_MessageQueueSize = self.lib.LS_MessageQueueSize
        self.LS_MessageQueueSize.restype = c_int
        self.LS_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_Open = self.lib.LS_Open
        self.LS_Open.restype = c_short
        self.LS_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_PersistSettings = self.lib.LS_PersistSettings
        self.LS_PersistSettings.restype = c_bool
        self.LS_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_PollingDuration = self.lib.LS_PollingDuration
        self.LS_PollingDuration.restype = c_long
        self.LS_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RegisterMessageCallback = self.lib.LS_RegisterMessageCallback
        self.LS_RegisterMessageCallback.restype = None
        self.LS_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.LS_RequestControlSource = self.lib.LS_RequestControlSource
        self.LS_RequestControlSource.restype = c_short
        self.LS_RequestControlSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestDisplayUnits = self.lib.LS_RequestDisplayUnits
        self.LS_RequestDisplayUnits.restype = c_short
        self.LS_RequestDisplayUnits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestLEDBrightness = self.lib.LS_RequestLEDBrightness
        self.LS_RequestLEDBrightness.restype = c_short
        self.LS_RequestLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestLimits = self.lib.LS_RequestLimits
        self.LS_RequestLimits.restype = c_short
        self.LS_RequestLimits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestReadings = self.lib.LS_RequestReadings
        self.LS_RequestReadings.restype = c_short
        self.LS_RequestReadings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestSetPower = self.lib.LS_RequestSetPower
        self.LS_RequestSetPower.restype = c_short
        self.LS_RequestSetPower.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestSettings = self.lib.LS_RequestSettings
        self.LS_RequestSettings.restype = c_short
        self.LS_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestStatus = self.lib.LS_RequestStatus
        self.LS_RequestStatus.restype = c_short
        self.LS_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestStatusBits = self.lib.LS_RequestStatusBits
        self.LS_RequestStatusBits.restype = c_short
        self.LS_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_RequestWavelength = self.lib.LS_RequestWavelength
        self.LS_RequestWavelength.restype = c_short
        self.LS_RequestWavelength.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_SetControlSource = self.lib.LS_SetControlSource
        self.LS_SetControlSource.restype = c_short
        self.LS_SetControlSource.argtypes = [POINTER(c_char), LS_InputSourceFlags]
        # *serialNo, source

        self.LS_SetDisplayUnits = self.lib.LS_SetDisplayUnits
        self.LS_SetDisplayUnits.restype = c_short
        self.LS_SetDisplayUnits.argtypes = [POINTER(c_char), LS_DisplayUnits]
        # *serialNo, units

        self.LS_SetLEDBrightness = self.lib.LS_SetLEDBrightness
        self.LS_SetLEDBrightness.restype = c_short
        self.LS_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
        # *serialNo, brightness

        self.LS_SetPower = self.lib.LS_SetPower
        self.LS_SetPower.restype = c_short
        self.LS_SetPower.argtypes = [POINTER(c_char), c_long]
        # *serialNo, power

        self.LS_StartPolling = self.lib.LS_StartPolling
        self.LS_StartPolling.restype = c_bool
        self.LS_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.LS_StopPolling = self.lib.LS_StopPolling
        self.LS_StopPolling.restype = None
        self.LS_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LS_TimeSinceLastMsgReceived = self.lib.LS_TimeSinceLastMsgReceived
        self.LS_TimeSinceLastMsgReceived.restype = c_bool
        self.LS_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.LS_WaitForMessage = self.lib.LS_WaitForMessage
        self.LS_WaitForMessage.restype = c_bool
        self.LS_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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