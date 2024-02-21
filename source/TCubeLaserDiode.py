from c_types import (POINTER, c_bool, c_char, c_float, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (LD_DisplayUnits, LD_InputSourceFlags, LD_POLARITY)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation)
from pathlib import Path


class TCubeLaserDiode(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.TCube.LaserDiode.DLL")

        self.LD_CheckConnection = self.lib.LD_CheckConnection
        self.LD_CheckConnection.restype = c_bool
        self.LD_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_ClearMessageQueue = self.lib.LD_ClearMessageQueue
        self.LD_ClearMessageQueue.restype = None
        self.LD_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_Close = self.lib.LD_Close
        self.LD_Close.restype = None
        self.LD_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_Disable = self.lib.LD_Disable
        self.LD_Disable.restype = c_short
        self.LD_Disable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_DisableOutput = self.lib.LD_DisableOutput
        self.LD_DisableOutput.restype = c_short
        self.LD_DisableOutput.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_Enable = self.lib.LD_Enable
        self.LD_Enable.restype = c_short
        self.LD_Enable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_EnableLastMsgTimer = self.lib.LD_EnableLastMsgTimer
        self.LD_EnableLastMsgTimer.restype = None
        self.LD_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.LD_EnableMaxCurrentAdjust = self.lib.LD_EnableMaxCurrentAdjust
        self.LD_EnableMaxCurrentAdjust.restype = c_short
        self.LD_EnableMaxCurrentAdjust.argtypes = [POINTER(c_char), c_bool, c_bool]
        # *serialNo, enableAdjust, enableDiode

        self.LD_EnableOutput = self.lib.LD_EnableOutput
        self.LD_EnableOutput.restype = c_short
        self.LD_EnableOutput.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_EnableTIAGainAdjust = self.lib.LD_EnableTIAGainAdjust
        self.LD_EnableTIAGainAdjust.restype = c_short
        self.LD_EnableTIAGainAdjust.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, enable

        self.LD_FindTIAGain = self.lib.LD_FindTIAGain
        self.LD_FindTIAGain.restype = c_short
        self.LD_FindTIAGain.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetControlSource = self.lib.LD_GetControlSource
        self.LD_GetControlSource.restype = LD_InputSourceFlags
        self.LD_GetControlSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetDisplayUnits = self.lib.LD_GetDisplayUnits
        self.LD_GetDisplayUnits.restype = LD_DisplayUnits
        self.LD_GetDisplayUnits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetFirmwareVersion = self.lib.LD_GetFirmwareVersion
        self.LD_GetFirmwareVersion.restype = c_ulong
        self.LD_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetHardwareInfo = self.lib.LD_GetHardwareInfo
        self.LD_GetHardwareInfo.restype = c_short
        self.LD_GetHardwareInfo.argtypes = [
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

        self.LD_GetHardwareInfoBlock = self.lib.LD_GetHardwareInfoBlock
        self.LD_GetHardwareInfoBlock.restype = c_short
        self.LD_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.LD_GetInterlockState = self.lib.LD_GetInterlockState
        self.LD_GetInterlockState.restype = c_byte
        self.LD_GetInterlockState.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetLEDBrightness = self.lib.LD_GetLEDBrightness
        self.LD_GetLEDBrightness.restype = c_long
        self.LD_GetLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetLaserDiodeCurrentReading = self.lib.LD_GetLaserDiodeCurrentReading
        self.LD_GetLaserDiodeCurrentReading.restype = c_long
        self.LD_GetLaserDiodeCurrentReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetLaserDiodeMaxCurrentLimit = self.lib.LD_GetLaserDiodeMaxCurrentLimit
        self.LD_GetLaserDiodeMaxCurrentLimit.restype = c_long
        self.LD_GetLaserDiodeMaxCurrentLimit.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetLaserPolarity = self.lib.LD_GetLaserPolarity
        self.LD_GetLaserPolarity.restype = LD_POLARITY
        self.LD_GetLaserPolarity.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetLaserSetPoint = self.lib.LD_GetLaserSetPoint
        self.LD_GetLaserSetPoint.restype = c_long
        self.LD_GetLaserSetPoint.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetMaxCurrentDigPot = self.lib.LD_GetMaxCurrentDigPot
        self.LD_GetMaxCurrentDigPot.restype = c_long
        self.LD_GetMaxCurrentDigPot.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetNextMessage = self.lib.LD_GetNextMessage
        self.LD_GetNextMessage.restype = c_bool
        self.LD_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.LD_GetPhotoCurrentReading = self.lib.LD_GetPhotoCurrentReading
        self.LD_GetPhotoCurrentReading.restype = c_long
        self.LD_GetPhotoCurrentReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetSoftwareVersion = self.lib.LD_GetSoftwareVersion
        self.LD_GetSoftwareVersion.restype = c_ulong
        self.LD_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetStatusBits = self.lib.LD_GetStatusBits
        self.LD_GetStatusBits.restype = c_ulong
        self.LD_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetVoltageReading = self.lib.LD_GetVoltageReading
        self.LD_GetVoltageReading.restype = c_long
        self.LD_GetVoltageReading.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_GetWACalibFactor = self.lib.LD_GetWACalibFactor
        self.LD_GetWACalibFactor.restype = c_float
        self.LD_GetWACalibFactor.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_HasLastMsgTimerOverrun = self.lib.LD_HasLastMsgTimerOverrun
        self.LD_HasLastMsgTimerOverrun.restype = c_bool
        self.LD_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_Identify = self.lib.LD_Identify
        self.LD_Identify.restype = None
        self.LD_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_LoadNamedSettings = self.lib.LD_LoadNamedSettings
        self.LD_LoadNamedSettings.restype = c_bool
        self.LD_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.LD_LoadSettings = self.lib.LD_LoadSettings
        self.LD_LoadSettings.restype = c_bool
        self.LD_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_MessageQueueSize = self.lib.LD_MessageQueueSize
        self.LD_MessageQueueSize.restype = c_int
        self.LD_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_Open = self.lib.LD_Open
        self.LD_Open.restype = c_short
        self.LD_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_PersistSettings = self.lib.LD_PersistSettings
        self.LD_PersistSettings.restype = c_bool
        self.LD_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_PollingDuration = self.lib.LD_PollingDuration
        self.LD_PollingDuration.restype = c_long
        self.LD_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RegisterMessageCallback = self.lib.LD_RegisterMessageCallback
        self.LD_RegisterMessageCallback.restype = None
        self.LD_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.LD_RequestControlSource = self.lib.LD_RequestControlSource
        self.LD_RequestControlSource.restype = c_short
        self.LD_RequestControlSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestDisplay = self.lib.LD_RequestDisplay
        self.LD_RequestDisplay.restype = c_short
        self.LD_RequestDisplay.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestLaserDiodeMaxCurrentLimit = self.lib.LD_RequestLaserDiodeMaxCurrentLimit
        self.LD_RequestLaserDiodeMaxCurrentLimit.restype = c_short
        self.LD_RequestLaserDiodeMaxCurrentLimit.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestLaserPolarity = self.lib.LD_RequestLaserPolarity
        self.LD_RequestLaserPolarity.restype = c_short
        self.LD_RequestLaserPolarity.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestLaserSetPoint = self.lib.LD_RequestLaserSetPoint
        self.LD_RequestLaserSetPoint.restype = c_short
        self.LD_RequestLaserSetPoint.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestMaxCurrentDigPot = self.lib.LD_RequestMaxCurrentDigPot
        self.LD_RequestMaxCurrentDigPot.restype = c_short
        self.LD_RequestMaxCurrentDigPot.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestReadings = self.lib.LD_RequestReadings
        self.LD_RequestReadings.restype = c_short
        self.LD_RequestReadings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestSettings = self.lib.LD_RequestSettings
        self.LD_RequestSettings.restype = c_short
        self.LD_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestStatus = self.lib.LD_RequestStatus
        self.LD_RequestStatus.restype = c_short
        self.LD_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestStatusBits = self.lib.LD_RequestStatusBits
        self.LD_RequestStatusBits.restype = c_short
        self.LD_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_RequestWACalibFactor = self.lib.LD_RequestWACalibFactor
        self.LD_RequestWACalibFactor.restype = c_short
        self.LD_RequestWACalibFactor.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_SetClosedLoopMode = self.lib.LD_SetClosedLoopMode
        self.LD_SetClosedLoopMode.restype = c_short
        self.LD_SetClosedLoopMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_SetControlSource = self.lib.LD_SetControlSource
        self.LD_SetControlSource.restype = c_short
        self.LD_SetControlSource.argtypes = [POINTER(c_char), LD_InputSourceFlags]
        # *serialNo, source

        self.LD_SetDisplayUnits = self.lib.LD_SetDisplayUnits
        self.LD_SetDisplayUnits.restype = c_short
        self.LD_SetDisplayUnits.argtypes = [POINTER(c_char), LD_DisplayUnits]
        # *serialNo, units

        self.LD_SetLEDBrightness = self.lib.LD_SetLEDBrightness
        self.LD_SetLEDBrightness.restype = c_short
        self.LD_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
        # *serialNo, brightness

        self.LD_SetLaserPolarity = self.lib.LD_SetLaserPolarity
        self.LD_SetLaserPolarity.restype = c_short
        self.LD_SetLaserPolarity.argtypes = [POINTER(c_char), LD_POLARITY]
        # *serialNo, polarity

        self.LD_SetLaserSetPoint = self.lib.LD_SetLaserSetPoint
        self.LD_SetLaserSetPoint.restype = c_short
        self.LD_SetLaserSetPoint.argtypes = [POINTER(c_char), c_long]
        # *serialNo, laserDiodeCurrent

        self.LD_SetMaxCurrentDigPot = self.lib.LD_SetMaxCurrentDigPot
        self.LD_SetMaxCurrentDigPot.restype = c_short
        self.LD_SetMaxCurrentDigPot.argtypes = [POINTER(c_char), c_long]
        # *serialNo, maxCurrent

        self.LD_SetOpenLoopMode = self.lib.LD_SetOpenLoopMode
        self.LD_SetOpenLoopMode.restype = c_short
        self.LD_SetOpenLoopMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_SetWACalibFactor = self.lib.LD_SetWACalibFactor
        self.LD_SetWACalibFactor.restype = c_short
        self.LD_SetWACalibFactor.argtypes = [POINTER(c_char), c_float]
        # *serialNo, calibFactor

        self.LD_StartPolling = self.lib.LD_StartPolling
        self.LD_StartPolling.restype = c_bool
        self.LD_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.LD_StopPolling = self.lib.LD_StopPolling
        self.LD_StopPolling.restype = None
        self.LD_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.LD_TimeSinceLastMsgReceived = self.lib.LD_TimeSinceLastMsgReceived
        self.LD_TimeSinceLastMsgReceived.restype = c_bool
        self.LD_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.LD_WaitForMessage = self.lib.LD_WaitForMessage
        self.LD_WaitForMessage.restype = c_bool
        self.LD_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
