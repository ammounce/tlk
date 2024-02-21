from c_types import (POINTER, c_bool, c_byte, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_uint, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (
    KSC_TriggerPortMode,
    KSC_TriggerPortPolarity,
    SC_OperatingModes,
    SC_OperatingStates)
from .definitions.structures import (
    KSC_MMIParams,
    KSC_TriggerConfig,
    SC_CycleParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class KCubeSolenoid(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.KCube.Solenoid.DLL")

        self.SC_CheckConnection = self.lib.SC_CheckConnection
        self.SC_CheckConnection.restype = c_bool
        self.SC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_ClearMessageQueue = self.lib.SC_ClearMessageQueue
        self.SC_ClearMessageQueue.restype = None
        self.SC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_Close = self.lib.SC_Close
        self.SC_Close.restype = None
        self.SC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_EnableLastMsgTimer = self.lib.SC_EnableLastMsgTimer
        self.SC_EnableLastMsgTimer.restype = None
        self.SC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.SC_GetCycleParams = self.lib.SC_GetCycleParams
        self.SC_GetCycleParams.restype = c_short
        self.SC_GetCycleParams.argtypes = [c_uint, c_uint, c_uint, c_uint, c_uint, POINTER(c_char)]
        # *numCycles, *offTime, *onTime, *pClosedTime, *pOpenTime, *serialNo

        self.SC_GetCycleParamsBlock = self.lib.SC_GetCycleParamsBlock
        self.SC_GetCycleParamsBlock.restype = c_short
        self.SC_GetCycleParamsBlock.argtypes = [SC_CycleParameters, POINTER(c_char)]
        # *cycleParams, *serialNo

        self.SC_GetDigitalOutputs = self.lib.SC_GetDigitalOutputs
        self.SC_GetDigitalOutputs.restype = c_byte
        self.SC_GetDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_GetHardwareInfo = self.lib.SC_GetHardwareInfo
        self.SC_GetHardwareInfo.restype = c_short
        self.SC_GetHardwareInfo.argtypes = [
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

        self.SC_GetHardwareInfoBlock = self.lib.SC_GetHardwareInfoBlock
        self.SC_GetHardwareInfoBlock.restype = c_short
        self.SC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.SC_GetHubBay = self.lib.SC_GetHubBay
        self.SC_GetHubBay.restype = POINTER(c_char)
        self.SC_GetHubBay.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_GetLEDswitches = self.lib.SC_GetLEDswitches
        self.SC_GetLEDswitches.restype = c_long
        self.SC_GetLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_GetMMIParams = self.lib.SC_GetMMIParams
        self.SC_GetMMIParams.restype = c_short
        self.SC_GetMMIParams.argtypes = [c_int16, POINTER(c_char)]
        # *displayIntensity, *serialNo

        self.SC_GetMMIParamsBlock = self.lib.SC_GetMMIParamsBlock
        self.SC_GetMMIParamsBlock.restype = c_short
        self.SC_GetMMIParamsBlock.argtypes = [KSC_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.SC_GetMMIParamsExt = self.lib.SC_GetMMIParamsExt
        self.SC_GetMMIParamsExt.restype = c_short
        self.SC_GetMMIParamsExt.argtypes = [c_int16, c_int16, c_int16, POINTER(c_char)]
        # *displayDimIntensity, *displayIntensity, *displayTimeout, *serialNo

        self.SC_GetNextMessage = self.lib.SC_GetNextMessage
        self.SC_GetNextMessage.restype = c_bool
        self.SC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.SC_GetOperatingMode = self.lib.SC_GetOperatingMode
        self.SC_GetOperatingMode.restype = SC_OperatingModes
        self.SC_GetOperatingMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_GetOperatingState = self.lib.SC_GetOperatingState
        self.SC_GetOperatingState.restype = SC_OperatingStates
        self.SC_GetOperatingState.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_GetSoftwareVersion = self.lib.SC_GetSoftwareVersion
        self.SC_GetSoftwareVersion.restype = c_ulong
        self.SC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_GetSolenoidState = self.lib.SC_GetSolenoidState
        self.SC_GetSolenoidState.restype = SC_SolenoidStates
        self.SC_GetSolenoidState.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_GetStatusBits = self.lib.SC_GetStatusBits
        self.SC_GetStatusBits.restype = c_ulong
        self.SC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_GetTriggerConfigParams = self.lib.SC_GetTriggerConfigParams
        self.SC_GetTriggerConfigParams.restype = c_short
        self.SC_GetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KSC_TriggerPortMode,
            KSC_TriggerPortPolarity,
            KSC_TriggerPortMode,
            KSC_TriggerPortPolarity]
        # *serialNo, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity

        self.SC_GetTriggerConfigParamsBlock = self.lib.SC_GetTriggerConfigParamsBlock
        self.SC_GetTriggerConfigParamsBlock.restype = c_short
        self.SC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KSC_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.SC_HasLastMsgTimerOverrun = self.lib.SC_HasLastMsgTimerOverrun
        self.SC_HasLastMsgTimerOverrun.restype = c_bool
        self.SC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_Identify = self.lib.SC_Identify
        self.SC_Identify.restype = None
        self.SC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_LoadNamedSettings = self.lib.SC_LoadNamedSettings
        self.SC_LoadNamedSettings.restype = c_bool
        self.SC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.SC_LoadSettings = self.lib.SC_LoadSettings
        self.SC_LoadSettings.restype = c_bool
        self.SC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_MessageQueueSize = self.lib.SC_MessageQueueSize
        self.SC_MessageQueueSize.restype = c_int
        self.SC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_Open = self.lib.SC_Open
        self.SC_Open.restype = c_short
        self.SC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_PersistSettings = self.lib.SC_PersistSettings
        self.SC_PersistSettings.restype = c_bool
        self.SC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_PollingDuration = self.lib.SC_PollingDuration
        self.SC_PollingDuration.restype = c_long
        self.SC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RegisterMessageCallback = self.lib.SC_RegisterMessageCallback
        self.SC_RegisterMessageCallback.restype = None
        self.SC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.SC_RequestCycleParams = self.lib.SC_RequestCycleParams
        self.SC_RequestCycleParams.restype = c_short
        self.SC_RequestCycleParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestDigitalOutputs = self.lib.SC_RequestDigitalOutputs
        self.SC_RequestDigitalOutputs.restype = c_short
        self.SC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestHubBay = self.lib.SC_RequestHubBay
        self.SC_RequestHubBay.restype = c_short
        self.SC_RequestHubBay.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestLEDswitches = self.lib.SC_RequestLEDswitches
        self.SC_RequestLEDswitches.restype = c_short
        self.SC_RequestLEDswitches.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestMMIParams = self.lib.SC_RequestMMIParams
        self.SC_RequestMMIParams.restype = c_short
        self.SC_RequestMMIParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestOperatingMode = self.lib.SC_RequestOperatingMode
        self.SC_RequestOperatingMode.restype = c_short
        self.SC_RequestOperatingMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestOperatingState = self.lib.SC_RequestOperatingState
        self.SC_RequestOperatingState.restype = c_short
        self.SC_RequestOperatingState.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestSettings = self.lib.SC_RequestSettings
        self.SC_RequestSettings.restype = c_short
        self.SC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestStatus = self.lib.SC_RequestStatus
        self.SC_RequestStatus.restype = c_short
        self.SC_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestStatusBits = self.lib.SC_RequestStatusBits
        self.SC_RequestStatusBits.restype = c_short
        self.SC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_RequestTriggerConfigParams = self.lib.SC_RequestTriggerConfigParams
        self.SC_RequestTriggerConfigParams.restype = c_short
        self.SC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_SetCycleParams = self.lib.SC_SetCycleParams
        self.SC_SetCycleParams.restype = c_short
        self.SC_SetCycleParams.argtypes = [POINTER(c_char), c_uint, c_uint, c_uint, c_uint, c_uint]
        # *serialNo, closedTime, numCycles, offTime, onTime, openTime

        self.SC_SetCycleParamsBlock = self.lib.SC_SetCycleParamsBlock
        self.SC_SetCycleParamsBlock.restype = c_short
        self.SC_SetCycleParamsBlock.argtypes = [SC_CycleParameters, POINTER(c_char)]
        # *cycleParams, *serialNo

        self.SC_SetDigitalOutputs = self.lib.SC_SetDigitalOutputs
        self.SC_SetDigitalOutputs.restype = c_short
        self.SC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.SC_SetLEDswitches = self.lib.SC_SetLEDswitches
        self.SC_SetLEDswitches.restype = c_short
        self.SC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
        # *serialNo, LEDswitches

        self.SC_SetMMIParams = self.lib.SC_SetMMIParams
        self.SC_SetMMIParams.restype = c_short
        self.SC_SetMMIParams.argtypes = [POINTER(c_char), c_int16]
        # *serialNo, displayIntensity

        self.SC_SetMMIParamsBlock = self.lib.SC_SetMMIParamsBlock
        self.SC_SetMMIParamsBlock.restype = c_short
        self.SC_SetMMIParamsBlock.argtypes = [KSC_MMIParams, POINTER(c_char)]
        # *mmiParams, *serialNo

        self.SC_SetMMIParamsExt = self.lib.SC_SetMMIParamsExt
        self.SC_SetMMIParamsExt.restype = c_short
        self.SC_SetMMIParamsExt.argtypes = [POINTER(c_char), c_int16, c_int16, c_int16]
        # *serialNo, displayDimIntensity, displayIntensity, displayTimeout

        self.SC_SetOperatingMode = self.lib.SC_SetOperatingMode
        self.SC_SetOperatingMode.restype = c_short
        self.SC_SetOperatingMode.argtypes = [POINTER(c_char), SC_OperatingModes]
        # *serialNo, mode

        self.SC_SetOperatingState = self.lib.SC_SetOperatingState
        self.SC_SetOperatingState.restype = c_short
        self.SC_SetOperatingState.argtypes = [POINTER(c_char), SC_OperatingStates]
        # *serialNo, state

        self.SC_SetTriggerConfigParams = self.lib.SC_SetTriggerConfigParams
        self.SC_SetTriggerConfigParams.restype = c_short
        self.SC_SetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            KSC_TriggerPortMode,
            KSC_TriggerPortPolarity,
            KSC_TriggerPortMode,
            KSC_TriggerPortPolarity]
        # *serialNo, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity

        self.SC_SetTriggerConfigParamsBlock = self.lib.SC_SetTriggerConfigParamsBlock
        self.SC_SetTriggerConfigParamsBlock.restype = c_short
        self.SC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KSC_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.SC_StartPolling = self.lib.SC_StartPolling
        self.SC_StartPolling.restype = c_bool
        self.SC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.SC_StopPolling = self.lib.SC_StopPolling
        self.SC_StopPolling.restype = None
        self.SC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.SC_TimeSinceLastMsgReceived = self.lib.SC_TimeSinceLastMsgReceived
        self.SC_TimeSinceLastMsgReceived.restype = c_bool
        self.SC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.SC_WaitForMessage = self.lib.SC_WaitForMessage
        self.SC_WaitForMessage.restype = c_bool
        self.SC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
