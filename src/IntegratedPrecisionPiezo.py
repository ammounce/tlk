from c_types import (POINTER, c_bool, c_byte, c_char, c_int, c_int16, c_int32, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (
    KPZ_WheelChangeRate,
    KPZ_WheelDirectionSense,
    KPZ_WheelMode,
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    PZ_ControlModeTypes,
    PZ_InputSourceFlags)
from .definitions.structures import (
    KSG_TriggerConfig,
    PPC_IOSettings,
    PPC_PIDConsts,
    PPC_PIDCriteria,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class IntegratedPrecisionPiezo(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.IntegratedPrecisionPiezo.DLL")

        self.IPP_CanDeviceLockFrontPanel = self.lib.IPP_CanDeviceLockFrontPanel
        self.IPP_CanDeviceLockFrontPanel.restype = c_bool
        self.IPP_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_CheckConnection = self.lib.IPP_CheckConnection
        self.IPP_CheckConnection.restype = c_bool
        self.IPP_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_ClearMessageQueue = self.lib.IPP_ClearMessageQueue
        self.IPP_ClearMessageQueue.restype = c_short
        self.IPP_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_Close = self.lib.IPP_Close
        self.IPP_Close.restype = None
        self.IPP_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_DisableChannel = self.lib.IPP_DisableChannel
        self.IPP_DisableChannel.restype = c_short
        self.IPP_DisableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_Disconnect = self.lib.IPP_Disconnect
        self.IPP_Disconnect.restype = c_short
        self.IPP_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_EnableChannel = self.lib.IPP_EnableChannel
        self.IPP_EnableChannel.restype = c_short
        self.IPP_EnableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetFirmwareVersion = self.lib.IPP_GetFirmwareVersion
        self.IPP_GetFirmwareVersion.restype = c_ulong
        self.IPP_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetFrontPanelLocked = self.lib.IPP_GetFrontPanelLocked
        self.IPP_GetFrontPanelLocked.restype = c_bool
        self.IPP_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetHardwareInfo = self.lib.IPP_GetHardwareInfo
        self.IPP_GetHardwareInfo.restype = c_short
        self.IPP_GetHardwareInfo.argtypes = [
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

        self.IPP_GetHardwareInfoBlock = self.lib.IPP_GetHardwareInfoBlock
        self.IPP_GetHardwareInfoBlock.restype = c_short
        self.IPP_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.IPP_GetIOSettings = self.lib.IPP_GetIOSettings
        self.IPP_GetIOSettings.restype = c_short
        self.IPP_GetIOSettings.argtypes = [PPC_IOSettings, POINTER(c_char)]
        # *ioSettings, *serialNo

        self.IPP_GetMMIParams = self.lib.IPP_GetMMIParams
        self.IPP_GetMMIParams.restype = c_short
        self.IPP_GetMMIParams.argtypes = [
            KPZ_WheelDirectionSense,
            c_int16,
            c_int16,
            c_int16,
            c_int32,
            c_int32,
            POINTER(c_char),
            KPZ_WheelChangeRate,
            c_int32,
            KPZ_WheelMode]
        # *directionSense, *displayDimIntensity, *displayIntensity, *displayTimeout, *presetVoltage1, *presetVoltage2, *serialNo, *voltageAdjustRate, *voltageStep, *wheelMode

        self.IPP_GetMaxOutputVoltage = self.lib.IPP_GetMaxOutputVoltage
        self.IPP_GetMaxOutputVoltage.restype = c_short
        self.IPP_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetMinOutputVoltage = self.lib.IPP_GetMinOutputVoltage
        self.IPP_GetMinOutputVoltage.restype = c_short
        self.IPP_GetMinOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetNextMessage = self.lib.IPP_GetNextMessage
        self.IPP_GetNextMessage.restype = c_bool
        self.IPP_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.IPP_GetOutputVoltage = self.lib.IPP_GetOutputVoltage
        self.IPP_GetOutputVoltage.restype = c_short
        self.IPP_GetOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetPIDConsts = self.lib.IPP_GetPIDConsts
        self.IPP_GetPIDConsts.restype = c_short
        self.IPP_GetPIDConsts.argtypes = [PPC_PIDConsts, POINTER(c_char), c_byte]
        # *pidConsts, *serialNo, index

        self.IPP_GetPIDCriteria = self.lib.IPP_GetPIDCriteria
        self.IPP_GetPIDCriteria.restype = c_short
        self.IPP_GetPIDCriteria.argtypes = [PPC_PIDCriteria, POINTER(c_char), c_byte]
        # *pidCriteria, *serialNo, criteriaID

        self.IPP_GetPosition = self.lib.IPP_GetPosition
        self.IPP_GetPosition.restype = c_short
        self.IPP_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetPositionControlMode = self.lib.IPP_GetPositionControlMode
        self.IPP_GetPositionControlMode.restype = PZ_ControlModeTypes
        self.IPP_GetPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetSoftwareVersion = self.lib.IPP_GetSoftwareVersion
        self.IPP_GetSoftwareVersion.restype = c_ulong
        self.IPP_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetStatusBits = self.lib.IPP_GetStatusBits
        self.IPP_GetStatusBits.restype = c_ulong
        self.IPP_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_GetTriggerConfigParams = self.lib.IPP_GetTriggerConfigParams
        self.IPP_GetTriggerConfigParams.restype = c_short
        self.IPP_GetTriggerConfigParams.argtypes = [
            c_int32,
            POINTER(c_char),
            c_int16,
            KSG_TriggerPortMode,
            KSG_TriggerPortPolarity,
            KSG_TriggerPortMode,
            KSG_TriggerPortPolarity,
            c_int32]
        # *lowerLimit, *serialNo, *smoothingSamples, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity, *upperLimit

        self.IPP_GetTriggerConfigParamsBlock = self.lib.IPP_GetTriggerConfigParamsBlock
        self.IPP_GetTriggerConfigParamsBlock.restype = c_short
        self.IPP_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KSG_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.IPP_GetVoltageSource = self.lib.IPP_GetVoltageSource
        self.IPP_GetVoltageSource.restype = PZ_InputSourceFlags
        self.IPP_GetVoltageSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_Identify = self.lib.IPP_Identify
        self.IPP_Identify.restype = None
        self.IPP_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_LoadNamedSettings = self.lib.IPP_LoadNamedSettings
        self.IPP_LoadNamedSettings.restype = c_bool
        self.IPP_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.IPP_LoadSettings = self.lib.IPP_LoadSettings
        self.IPP_LoadSettings.restype = c_bool
        self.IPP_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_MessageQueueSize = self.lib.IPP_MessageQueueSize
        self.IPP_MessageQueueSize.restype = c_int
        self.IPP_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_Open = self.lib.IPP_Open
        self.IPP_Open.restype = c_short
        self.IPP_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_PersistSettings = self.lib.IPP_PersistSettings
        self.IPP_PersistSettings.restype = c_bool
        self.IPP_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_PollingDuration = self.lib.IPP_PollingDuration
        self.IPP_PollingDuration.restype = c_long
        self.IPP_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RegisterMessageCallback = self.lib.IPP_RegisterMessageCallback
        self.IPP_RegisterMessageCallback.restype = c_short
        self.IPP_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.IPP_RequestFrontPanelLocked = self.lib.IPP_RequestFrontPanelLocked
        self.IPP_RequestFrontPanelLocked.restype = c_short
        self.IPP_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestIOSettings = self.lib.IPP_RequestIOSettings
        self.IPP_RequestIOSettings.restype = c_bool
        self.IPP_RequestIOSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestMMIParams = self.lib.IPP_RequestMMIParams
        self.IPP_RequestMMIParams.restype = c_bool
        self.IPP_RequestMMIParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestOutputVoltage = self.lib.IPP_RequestOutputVoltage
        self.IPP_RequestOutputVoltage.restype = c_bool
        self.IPP_RequestOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestPIDConsts = self.lib.IPP_RequestPIDConsts
        self.IPP_RequestPIDConsts.restype = c_short
        self.IPP_RequestPIDConsts.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, index

        self.IPP_RequestPIDCriteria = self.lib.IPP_RequestPIDCriteria
        self.IPP_RequestPIDCriteria.restype = c_short
        self.IPP_RequestPIDCriteria.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, criteriaID

        self.IPP_RequestPosition = self.lib.IPP_RequestPosition
        self.IPP_RequestPosition.restype = c_bool
        self.IPP_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestPositionControlMode = self.lib.IPP_RequestPositionControlMode
        self.IPP_RequestPositionControlMode.restype = c_bool
        self.IPP_RequestPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestSettings = self.lib.IPP_RequestSettings
        self.IPP_RequestSettings.restype = c_short
        self.IPP_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestStatus = self.lib.IPP_RequestStatus
        self.IPP_RequestStatus.restype = c_short
        self.IPP_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestStatusBits = self.lib.IPP_RequestStatusBits
        self.IPP_RequestStatusBits.restype = c_short
        self.IPP_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestTriggerConfigParams = self.lib.IPP_RequestTriggerConfigParams
        self.IPP_RequestTriggerConfigParams.restype = c_short
        self.IPP_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_RequestVoltageSource = self.lib.IPP_RequestVoltageSource
        self.IPP_RequestVoltageSource.restype = c_bool
        self.IPP_RequestVoltageSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_ResetParameters = self.lib.IPP_ResetParameters
        self.IPP_ResetParameters.restype = c_short
        self.IPP_ResetParameters.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_SetFrontPanelLock = self.lib.IPP_SetFrontPanelLock
        self.IPP_SetFrontPanelLock.restype = c_short
        self.IPP_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
        # *serialNo, locked

        self.IPP_SetIOSettings = self.lib.IPP_SetIOSettings
        self.IPP_SetIOSettings.restype = c_short
        self.IPP_SetIOSettings.argtypes = [PPC_IOSettings, POINTER(c_char)]
        # *ioSettings, *serialNo

        self.IPP_SetMMIParams = self.lib.IPP_SetMMIParams
        self.IPP_SetMMIParams.restype = c_short
        self.IPP_SetMMIParams.argtypes = [
            POINTER(c_char),
            KPZ_WheelDirectionSense,
            c_int16,
            c_int16,
            c_int16,
            c_int32,
            c_int32,
            KPZ_WheelChangeRate,
            c_int32,
            KPZ_WheelMode]
        # *serialNo, directionSense, displayDimIntensity, displayIntensity, displayTimeout, presetVoltage1, presetVoltage2, voltageAdjustRate, voltageStep, wheelMode

        self.IPP_SetOutputVoltage = self.lib.IPP_SetOutputVoltage
        self.IPP_SetOutputVoltage.restype = c_short
        self.IPP_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, volts

        self.IPP_SetPIDConsts = self.lib.IPP_SetPIDConsts
        self.IPP_SetPIDConsts.restype = c_short
        self.IPP_SetPIDConsts.argtypes = [PPC_PIDConsts, POINTER(c_char)]
        # *pidConsts, *serialNo

        self.IPP_SetPIDCriteria = self.lib.IPP_SetPIDCriteria
        self.IPP_SetPIDCriteria.restype = c_short
        self.IPP_SetPIDCriteria.argtypes = [PPC_PIDCriteria, POINTER(c_char)]
        # *pidCriteria, *serialNo

        self.IPP_SetPosition = self.lib.IPP_SetPosition
        self.IPP_SetPosition.restype = c_short
        self.IPP_SetPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, position

        self.IPP_SetPositionControlMode = self.lib.IPP_SetPositionControlMode
        self.IPP_SetPositionControlMode.restype = c_short
        self.IPP_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
        # *serialNo, mode

        self.IPP_SetTriggerConfigParams = self.lib.IPP_SetTriggerConfigParams
        self.IPP_SetTriggerConfigParams.restype = c_short
        self.IPP_SetTriggerConfigParams.argtypes = [
            POINTER(c_char),
            c_int32,
            c_int16,
            KSG_TriggerPortMode,
            KSG_TriggerPortPolarity,
            KSG_TriggerPortMode,
            KSG_TriggerPortPolarity,
            c_int32]
        # *serialNo, lowerLimit, smoothingSamples, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity, upperLimit

        self.IPP_SetTriggerConfigParamsBlock = self.lib.IPP_SetTriggerConfigParamsBlock
        self.IPP_SetTriggerConfigParamsBlock.restype = c_short
        self.IPP_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KSG_TriggerConfig]
        # *serialNo, *triggerConfigParams

        self.IPP_SetVoltageSource = self.lib.IPP_SetVoltageSource
        self.IPP_SetVoltageSource.restype = c_short
        self.IPP_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]
        # *serialNo, source

        self.IPP_SetZero = self.lib.IPP_SetZero
        self.IPP_SetZero.restype = c_short
        self.IPP_SetZero.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_StartPolling = self.lib.IPP_StartPolling
        self.IPP_StartPolling.restype = c_bool
        self.IPP_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.IPP_StopPolling = self.lib.IPP_StopPolling
        self.IPP_StopPolling.restype = None
        self.IPP_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.IPP_WaitForMessage = self.lib.IPP_WaitForMessage
        self.IPP_WaitForMessage.restype = c_bool
        self.IPP_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
