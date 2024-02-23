from ctypes import (POINTER, c_bool, c_byte, c_char, c_int, c_int16, c_int32, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
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


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.IntegratedPrecisionPiezo.DLL")

IPP_CanDeviceLockFrontPanel = lib.IPP_CanDeviceLockFrontPanel
IPP_CanDeviceLockFrontPanel.restype = c_bool
IPP_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]
# *serialNo

IPP_CheckConnection = lib.IPP_CheckConnection
IPP_CheckConnection.restype = c_bool
IPP_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

IPP_ClearMessageQueue = lib.IPP_ClearMessageQueue
IPP_ClearMessageQueue.restype = c_short
IPP_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

IPP_Close = lib.IPP_Close
IPP_Close.restype = c_void_p
IPP_Close.argtypes = [POINTER(c_char)]
# *serialNo

IPP_DisableChannel = lib.IPP_DisableChannel
IPP_DisableChannel.restype = c_short
IPP_DisableChannel.argtypes = [POINTER(c_char)]
# *serialNo

IPP_Disconnect = lib.IPP_Disconnect
IPP_Disconnect.restype = c_short
IPP_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

IPP_EnableChannel = lib.IPP_EnableChannel
IPP_EnableChannel.restype = c_short
IPP_EnableChannel.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetFirmwareVersion = lib.IPP_GetFirmwareVersion
IPP_GetFirmwareVersion.restype = c_ulong
IPP_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetFrontPanelLocked = lib.IPP_GetFrontPanelLocked
IPP_GetFrontPanelLocked.restype = c_bool
IPP_GetFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetHardwareInfo = lib.IPP_GetHardwareInfo
IPP_GetHardwareInfo.restype = c_short
IPP_GetHardwareInfo.argtypes = [
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

IPP_GetHardwareInfoBlock = lib.IPP_GetHardwareInfoBlock
IPP_GetHardwareInfoBlock.restype = c_short
IPP_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

IPP_GetIOSettings = lib.IPP_GetIOSettings
IPP_GetIOSettings.restype = c_short
IPP_GetIOSettings.argtypes = [PPC_IOSettings, POINTER(c_char)]
# *ioSettings, *serialNo

IPP_GetMMIParams = lib.IPP_GetMMIParams
IPP_GetMMIParams.restype = c_short
IPP_GetMMIParams.argtypes = [
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

IPP_GetMaxOutputVoltage = lib.IPP_GetMaxOutputVoltage
IPP_GetMaxOutputVoltage.restype = c_short
IPP_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetMinOutputVoltage = lib.IPP_GetMinOutputVoltage
IPP_GetMinOutputVoltage.restype = c_short
IPP_GetMinOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetNextMessage = lib.IPP_GetNextMessage
IPP_GetNextMessage.restype = c_bool
IPP_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

IPP_GetOutputVoltage = lib.IPP_GetOutputVoltage
IPP_GetOutputVoltage.restype = c_short
IPP_GetOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetPIDConsts = lib.IPP_GetPIDConsts
IPP_GetPIDConsts.restype = c_short
IPP_GetPIDConsts.argtypes = [PPC_PIDConsts, POINTER(c_char), c_byte]
# *pidConsts, *serialNo, index

IPP_GetPIDCriteria = lib.IPP_GetPIDCriteria
IPP_GetPIDCriteria.restype = c_short
IPP_GetPIDCriteria.argtypes = [PPC_PIDCriteria, POINTER(c_char), c_byte]
# *pidCriteria, *serialNo, criteriaID

IPP_GetPosition = lib.IPP_GetPosition
IPP_GetPosition.restype = c_short
IPP_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetPositionControlMode = lib.IPP_GetPositionControlMode
IPP_GetPositionControlMode.restype = PZ_ControlModeTypes
IPP_GetPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetSoftwareVersion = lib.IPP_GetSoftwareVersion
IPP_GetSoftwareVersion.restype = c_ulong
IPP_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetStatusBits = lib.IPP_GetStatusBits
IPP_GetStatusBits.restype = c_ulong
IPP_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

IPP_GetTriggerConfigParams = lib.IPP_GetTriggerConfigParams
IPP_GetTriggerConfigParams.restype = c_short
IPP_GetTriggerConfigParams.argtypes = [
    c_int32,
    POINTER(c_char),
    c_int16,
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    c_int32]
# *lowerLimit, *serialNo, *smoothingSamples, *trigger1Mode, *trigger1Polarity, *trigger2Mode, *trigger2Polarity, *upperLimit

IPP_GetTriggerConfigParamsBlock = lib.IPP_GetTriggerConfigParamsBlock
IPP_GetTriggerConfigParamsBlock.restype = c_short
IPP_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KSG_TriggerConfig]
# *serialNo, *triggerConfigParams

IPP_GetVoltageSource = lib.IPP_GetVoltageSource
IPP_GetVoltageSource.restype = PZ_InputSourceFlags
IPP_GetVoltageSource.argtypes = [POINTER(c_char)]
# *serialNo

IPP_Identify = lib.IPP_Identify
IPP_Identify.restype = c_void_p
IPP_Identify.argtypes = [POINTER(c_char)]
# *serialNo

IPP_LoadNamedSettings = lib.IPP_LoadNamedSettings
IPP_LoadNamedSettings.restype = c_bool
IPP_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

IPP_LoadSettings = lib.IPP_LoadSettings
IPP_LoadSettings.restype = c_bool
IPP_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

IPP_MessageQueueSize = lib.IPP_MessageQueueSize
IPP_MessageQueueSize.restype = c_int
IPP_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

IPP_Open = lib.IPP_Open
IPP_Open.restype = c_short
IPP_Open.argtypes = [POINTER(c_char)]
# *serialNo

IPP_PersistSettings = lib.IPP_PersistSettings
IPP_PersistSettings.restype = c_bool
IPP_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

IPP_PollingDuration = lib.IPP_PollingDuration
IPP_PollingDuration.restype = c_long
IPP_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RegisterMessageCallback = lib.IPP_RegisterMessageCallback
IPP_RegisterMessageCallback.restype = c_short
IPP_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNo, void

IPP_RequestFrontPanelLocked = lib.IPP_RequestFrontPanelLocked
IPP_RequestFrontPanelLocked.restype = c_short
IPP_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestIOSettings = lib.IPP_RequestIOSettings
IPP_RequestIOSettings.restype = c_bool
IPP_RequestIOSettings.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestMMIParams = lib.IPP_RequestMMIParams
IPP_RequestMMIParams.restype = c_bool
IPP_RequestMMIParams.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestOutputVoltage = lib.IPP_RequestOutputVoltage
IPP_RequestOutputVoltage.restype = c_bool
IPP_RequestOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestPIDConsts = lib.IPP_RequestPIDConsts
IPP_RequestPIDConsts.restype = c_short
IPP_RequestPIDConsts.argtypes = [POINTER(c_char), c_byte]
# *serialNo, index

IPP_RequestPIDCriteria = lib.IPP_RequestPIDCriteria
IPP_RequestPIDCriteria.restype = c_short
IPP_RequestPIDCriteria.argtypes = [POINTER(c_char), c_byte]
# *serialNo, criteriaID

IPP_RequestPosition = lib.IPP_RequestPosition
IPP_RequestPosition.restype = c_bool
IPP_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestPositionControlMode = lib.IPP_RequestPositionControlMode
IPP_RequestPositionControlMode.restype = c_bool
IPP_RequestPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestSettings = lib.IPP_RequestSettings
IPP_RequestSettings.restype = c_short
IPP_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestStatus = lib.IPP_RequestStatus
IPP_RequestStatus.restype = c_short
IPP_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestStatusBits = lib.IPP_RequestStatusBits
IPP_RequestStatusBits.restype = c_short
IPP_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestTriggerConfigParams = lib.IPP_RequestTriggerConfigParams
IPP_RequestTriggerConfigParams.restype = c_short
IPP_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]
# *serialNo

IPP_RequestVoltageSource = lib.IPP_RequestVoltageSource
IPP_RequestVoltageSource.restype = c_bool
IPP_RequestVoltageSource.argtypes = [POINTER(c_char)]
# *serialNo

IPP_ResetParameters = lib.IPP_ResetParameters
IPP_ResetParameters.restype = c_short
IPP_ResetParameters.argtypes = [POINTER(c_char)]
# *serialNo

IPP_SetFrontPanelLock = lib.IPP_SetFrontPanelLock
IPP_SetFrontPanelLock.restype = c_short
IPP_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]
# *serialNo, locked

IPP_SetIOSettings = lib.IPP_SetIOSettings
IPP_SetIOSettings.restype = c_short
IPP_SetIOSettings.argtypes = [PPC_IOSettings, POINTER(c_char)]
# *ioSettings, *serialNo

IPP_SetMMIParams = lib.IPP_SetMMIParams
IPP_SetMMIParams.restype = c_short
IPP_SetMMIParams.argtypes = [
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

IPP_SetOutputVoltage = lib.IPP_SetOutputVoltage
IPP_SetOutputVoltage.restype = c_short
IPP_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, volts

IPP_SetPIDConsts = lib.IPP_SetPIDConsts
IPP_SetPIDConsts.restype = c_short
IPP_SetPIDConsts.argtypes = [PPC_PIDConsts, POINTER(c_char)]
# *pidConsts, *serialNo

IPP_SetPIDCriteria = lib.IPP_SetPIDCriteria
IPP_SetPIDCriteria.restype = c_short
IPP_SetPIDCriteria.argtypes = [PPC_PIDCriteria, POINTER(c_char)]
# *pidCriteria, *serialNo

IPP_SetPosition = lib.IPP_SetPosition
IPP_SetPosition.restype = c_short
IPP_SetPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, position

IPP_SetPositionControlMode = lib.IPP_SetPositionControlMode
IPP_SetPositionControlMode.restype = c_short
IPP_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
# *serialNo, mode

IPP_SetTriggerConfigParams = lib.IPP_SetTriggerConfigParams
IPP_SetTriggerConfigParams.restype = c_short
IPP_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    c_int32,
    c_int16,
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    c_int32]
# *serialNo, lowerLimit, smoothingSamples, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity, upperLimit

IPP_SetTriggerConfigParamsBlock = lib.IPP_SetTriggerConfigParamsBlock
IPP_SetTriggerConfigParamsBlock.restype = c_short
IPP_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KSG_TriggerConfig]
# *serialNo, *triggerConfigParams

IPP_SetVoltageSource = lib.IPP_SetVoltageSource
IPP_SetVoltageSource.restype = c_short
IPP_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]
# *serialNo, source

IPP_SetZero = lib.IPP_SetZero
IPP_SetZero.restype = c_short
IPP_SetZero.argtypes = [POINTER(c_char)]
# *serialNo

IPP_StartPolling = lib.IPP_StartPolling
IPP_StartPolling.restype = c_bool
IPP_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

IPP_StopPolling = lib.IPP_StopPolling
IPP_StopPolling.restype = c_void_p
IPP_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

IPP_WaitForMessage = lib.IPP_WaitForMessage
IPP_WaitForMessage.restype = c_bool
IPP_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
#

TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [TLI_DeviceInfo, POINTER(c_char), POINTER(c_char)]
# *info, *serialNo, *serialNumber

TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = [SafeArray]
# **stringsReceiver

TLI_GetDeviceListByType = lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype = c_short
TLI_GetDeviceListByType.argtypes = [SafeArray, c_int]
# **stringsReceiver, typeID

TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char), c_ulong, c_int]
# *receiveBuffer, sizeOfBuffer, typeID

TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = [SafeArray, c_int, c_int]
# **stringsReceiver, *typeIDs, length

TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_int, c_int, c_ulong]
# *receiveBuffer, *typeIDs, length, sizeOfBuffer

TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_ulong]
# *receiveBuffer, sizeOfBuffer

TLI_GetDeviceListSize = lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype = c_short
#

TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p
#
