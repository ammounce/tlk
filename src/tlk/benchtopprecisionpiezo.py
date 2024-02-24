from ctypes import (POINTER, c_byte, c_char, c_int, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (PZ_ControlModeTypes, PZ_InputSourceFlags)
from .definitions.structures import (
    PPC_IOSettings,
    PPC_NotchParams,
    PPC_PIDConsts,
    TLI_DeviceInfo,
    TLI_HardwareInformation)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Benchtop.PrecisionPiezo.dll")

PPC2_ClearMessageQueue = lib.PPC2_ClearMessageQueue
PPC2_ClearMessageQueue.restype = c_short
PPC2_ClearMessageQueue.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_DisableChannel = lib.PPC2_DisableChannel
PPC2_DisableChannel.restype = c_short
PPC2_DisableChannel.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_EnableChannel = lib.PPC2_EnableChannel
PPC2_EnableChannel.restype = c_short
PPC2_EnableChannel.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_GetHardwareInfo = lib.PPC2_GetHardwareInfo
PPC2_GetHardwareInfo.restype = c_short
PPC2_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    c_int,
    POINTER(c_char),
    c_ulong,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]
# *serialNo, channel, *modelNo, sizeOfModelNo, *type, *numChannels, *notes, sizeOfNotes, *firmwareVersion, *hardwareVersion, *modificationState

PPC2_GetHardwareInfoBlock = lib.PPC2_GetHardwareInfoBlock
PPC2_GetHardwareInfoBlock.restype = c_short
PPC2_GetHardwareInfoBlock.argtypes = [POINTER(c_char), c_int, TLI_HardwareInformation]
# *serialNo, channel, *hardwareInfo

PPC2_GetIOSettings = lib.PPC2_GetIOSettings
PPC2_GetIOSettings.restype = c_short
PPC2_GetIOSettings.argtypes = [POINTER(c_char), c_int, PPC_IOSettings]
# *serialNo, channel, *ioSettings

PPC2_GetMaxOutputVoltage = lib.PPC2_GetMaxOutputVoltage
PPC2_GetMaxOutputVoltage.restype = c_short
PPC2_GetMaxOutputVoltage.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_GetMaximumTravel = lib.PPC2_GetMaximumTravel
PPC2_GetMaximumTravel.restype = c_long
PPC2_GetMaximumTravel.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_GetMinOutputVoltage = lib.PPC2_GetMinOutputVoltage
PPC2_GetMinOutputVoltage.restype = c_short
PPC2_GetMinOutputVoltage.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_GetNextMessage = lib.PPC2_GetNextMessage
PPC2_GetNextMessage.restype = c_bool
PPC2_GetNextMessage.argtypes = [POINTER(c_char), c_int, c_long, c_long, c_ulong]
# *serialNo, channel, *messageType, *messageID, *messageData

PPC2_GetNotchParams = lib.PPC2_GetNotchParams
PPC2_GetNotchParams.restype = c_short
PPC2_GetNotchParams.argtypes = [POINTER(c_char), c_int, PPC_NotchParams]
# *serialNo, channel, *notchParams

PPC2_GetOutputVoltage = lib.PPC2_GetOutputVoltage
PPC2_GetOutputVoltage.restype = c_short
PPC2_GetOutputVoltage.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_GetPIDConsts = lib.PPC2_GetPIDConsts
PPC2_GetPIDConsts.restype = c_short
PPC2_GetPIDConsts.argtypes = [POINTER(c_char), c_int, PPC_PIDConsts]
# *serialNo, channel, *pidConsts

PPC2_GetPosition = lib.PPC2_GetPosition
PPC2_GetPosition.restype = c_short
PPC2_GetPosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_GetPositionControlMode = lib.PPC2_GetPositionControlMode
PPC2_GetPositionControlMode.restype = PZ_ControlModeTypes
PPC2_GetPositionControlMode.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_GetRackDigitalOutputs = lib.PPC2_GetRackDigitalOutputs
PPC2_GetRackDigitalOutputs.restype = c_byte
PPC2_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

PPC2_GetRackStatusBits = lib.PPC2_GetRackStatusBits
PPC2_GetRackStatusBits.restype = c_ulong
PPC2_GetRackStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PPC2_GetStatusBits = lib.PPC2_GetStatusBits
PPC2_GetStatusBits.restype = c_ulong
PPC2_GetStatusBits.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_GetVoltageSource = lib.PPC2_GetVoltageSource
PPC2_GetVoltageSource.restype = PZ_InputSourceFlags
PPC2_GetVoltageSource.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_Identify = lib.PPC2_Identify
PPC2_Identify.restype = c_void_p
PPC2_Identify.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_LoadNamedSettings = lib.PPC2_LoadNamedSettings
PPC2_LoadNamedSettings.restype = c_bool
PPC2_LoadNamedSettings.argtypes = [POINTER(c_char), c_short, POINTER(c_char)]
# *serialNo, channel, *settingsName

PPC2_LoadSettings = lib.PPC2_LoadSettings
PPC2_LoadSettings.restype = c_bool
PPC2_LoadSettings.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_MessageQueueSize = lib.PPC2_MessageQueueSize
PPC2_MessageQueueSize.restype = c_int
PPC2_MessageQueueSize.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_PersistSettings = lib.PPC2_PersistSettings
PPC2_PersistSettings.restype = c_bool
PPC2_PersistSettings.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_PollingDuration = lib.PPC2_PollingDuration
PPC2_PollingDuration.restype = c_long
PPC2_PollingDuration.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RegisterMessageCallback = lib.PPC2_RegisterMessageCallback
PPC2_RegisterMessageCallback.restype = c_short
PPC2_RegisterMessageCallback.argtypes = [POINTER(c_char), c_int, c_void_p]
# *serialNo, channel, void

PPC2_RequestActualPosition = lib.PPC2_RequestActualPosition
PPC2_RequestActualPosition.restype = c_short
PPC2_RequestActualPosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RequestMaxOutputVoltage = lib.PPC2_RequestMaxOutputVoltage
PPC2_RequestMaxOutputVoltage.restype = c_bool
PPC2_RequestMaxOutputVoltage.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RequestOutputVoltage = lib.PPC2_RequestOutputVoltage
PPC2_RequestOutputVoltage.restype = c_bool
PPC2_RequestOutputVoltage.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RequestPIDConsts = lib.PPC2_RequestPIDConsts
PPC2_RequestPIDConsts.restype = c_bool
PPC2_RequestPIDConsts.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RequestPosition = lib.PPC2_RequestPosition
PPC2_RequestPosition.restype = c_short
PPC2_RequestPosition.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RequestRackDigitalOutputs = lib.PPC2_RequestRackDigitalOutputs
PPC2_RequestRackDigitalOutputs.restype = c_short
PPC2_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

PPC2_RequestRackStatusBits = lib.PPC2_RequestRackStatusBits
PPC2_RequestRackStatusBits.restype = c_short
PPC2_RequestRackStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PPC2_RequestSettings = lib.PPC2_RequestSettings
PPC2_RequestSettings.restype = c_short
PPC2_RequestSettings.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RequestStatus = lib.PPC2_RequestStatus
PPC2_RequestStatus.restype = c_short
PPC2_RequestStatus.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RequestStatusBits = lib.PPC2_RequestStatusBits
PPC2_RequestStatusBits.restype = c_short
PPC2_RequestStatusBits.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_RequestVoltageSource = lib.PPC2_RequestVoltageSource
PPC2_RequestVoltageSource.restype = c_bool
PPC2_RequestVoltageSource.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_ResetParameters = lib.PPC2_ResetParameters
PPC2_ResetParameters.restype = c_short
PPC2_ResetParameters.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_SetIOSettings = lib.PPC2_SetIOSettings
PPC2_SetIOSettings.restype = c_short
PPC2_SetIOSettings.argtypes = [POINTER(c_char), c_int, PPC_IOSettings]
# *serialNo, channel, *ioSettings

PPC2_SetMaxOutputVoltage = lib.PPC2_SetMaxOutputVoltage
PPC2_SetMaxOutputVoltage.restype = c_short
PPC2_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_int, c_short]
# *serialNo, channel, maxVoltage

PPC2_SetNotchParams = lib.PPC2_SetNotchParams
PPC2_SetNotchParams.restype = c_short
PPC2_SetNotchParams.argtypes = [POINTER(c_char), c_int, PPC_NotchParams]
# *serialNo, channel, *notchParams

PPC2_SetOutputVoltage = lib.PPC2_SetOutputVoltage
PPC2_SetOutputVoltage.restype = c_short
PPC2_SetOutputVoltage.argtypes = [POINTER(c_char), c_int, c_short]
# *serialNo, channel, volts

PPC2_SetPIDConsts = lib.PPC2_SetPIDConsts
PPC2_SetPIDConsts.restype = c_short
PPC2_SetPIDConsts.argtypes = [POINTER(c_char), c_int, PPC_PIDConsts]
# *serialNo, channel, *pidConsts

PPC2_SetPosition = lib.PPC2_SetPosition
PPC2_SetPosition.restype = c_short
PPC2_SetPosition.argtypes = [POINTER(c_char), c_int, c_short]
# *serialNo, channel, position

PPC2_SetPositionControlMode = lib.PPC2_SetPositionControlMode
PPC2_SetPositionControlMode.restype = c_short
PPC2_SetPositionControlMode.argtypes = [POINTER(c_char), c_int, PZ_ControlModeTypes]
# *serialNo, channel, mode

PPC2_SetPositionToTolerance = lib.PPC2_SetPositionToTolerance
PPC2_SetPositionToTolerance.restype = c_short
PPC2_SetPositionToTolerance.argtypes = [POINTER(c_char), c_int, c_short, c_short]
# *serialNo, channel, position, tolerance

PPC2_SetRackDigitalOutputs = lib.PPC2_SetRackDigitalOutputs
PPC2_SetRackDigitalOutputs.restype = c_short
PPC2_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
# *serialNo, outputsBits

PPC2_SetVoltageSource = lib.PPC2_SetVoltageSource
PPC2_SetVoltageSource.restype = c_short
PPC2_SetVoltageSource.argtypes = [POINTER(c_char), c_int, PZ_InputSourceFlags]
# *serialNo, channel, source

PPC2_SetZero = lib.PPC2_SetZero
PPC2_SetZero.restype = c_short
PPC2_SetZero.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_StartPolling = lib.PPC2_StartPolling
PPC2_StartPolling.restype = c_bool
PPC2_StartPolling.argtypes = [POINTER(c_char), c_int, c_int]
# *serialNo, channel, milliseconds

PPC2_StopPolling = lib.PPC2_StopPolling
PPC2_StopPolling.restype = c_void_p
PPC2_StopPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, channel

PPC2_WaitForMessage = lib.PPC2_WaitForMessage
PPC2_WaitForMessage.restype = c_bool
PPC2_WaitForMessage.argtypes = [POINTER(c_char), c_int, c_long, c_long, c_ulong]
# *serialNo, channel, *messageType, *messageID, *messageData

PPC_CheckConnection = lib.PPC_CheckConnection
PPC_CheckConnection.restype = c_bool
PPC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

PPC_ClearMessageQueue = lib.PPC_ClearMessageQueue
PPC_ClearMessageQueue.restype = c_short
PPC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

PPC_Close = lib.PPC_Close
PPC_Close.restype = c_void_p
PPC_Close.argtypes = [POINTER(c_char)]
# *serialNo

PPC_DisableChannel = lib.PPC_DisableChannel
PPC_DisableChannel.restype = c_short
PPC_DisableChannel.argtypes = [POINTER(c_char)]
# *serialNo

PPC_Disconnect = lib.PPC_Disconnect
PPC_Disconnect.restype = c_short
PPC_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

PPC_EnableChannel = lib.PPC_EnableChannel
PPC_EnableChannel.restype = c_short
PPC_EnableChannel.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetFirmwareVersion = lib.PPC_GetFirmwareVersion
PPC_GetFirmwareVersion.restype = c_ulong
PPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetHardwareInfo = lib.PPC_GetHardwareInfo
PPC_GetHardwareInfo.restype = c_short
PPC_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    POINTER(c_char),
    c_ulong,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]
# *serialNo, *modelNo, sizeOfModelNo, *type, *numChannels, *notes, sizeOfNotes, *firmwareVersion, *hardwareVersion, *modificationState

PPC_GetHardwareInfoBlock = lib.PPC_GetHardwareInfoBlock
PPC_GetHardwareInfoBlock.restype = c_short
PPC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]
# *serialNo, *hardwareInfo

PPC_GetIOSettings = lib.PPC_GetIOSettings
PPC_GetIOSettings.restype = c_short
PPC_GetIOSettings.argtypes = [POINTER(c_char), PPC_IOSettings]
# *serialNo, *ioSettings

PPC_GetMaxOutputVoltage = lib.PPC_GetMaxOutputVoltage
PPC_GetMaxOutputVoltage.restype = c_short
PPC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetMaximumTravel = lib.PPC_GetMaximumTravel
PPC_GetMaximumTravel.restype = c_long
PPC_GetMaximumTravel.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetMinOutputVoltage = lib.PPC_GetMinOutputVoltage
PPC_GetMinOutputVoltage.restype = c_short
PPC_GetMinOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetNextMessage = lib.PPC_GetNextMessage
PPC_GetNextMessage.restype = c_bool
PPC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]
# *serialNo, *messageType, *messageID, *messageData

PPC_GetNotchParams = lib.PPC_GetNotchParams
PPC_GetNotchParams.restype = c_short
PPC_GetNotchParams.argtypes = [POINTER(c_char), PPC_NotchParams]
# *serialNo, *notchParams

PPC_GetOutputVoltage = lib.PPC_GetOutputVoltage
PPC_GetOutputVoltage.restype = c_short
PPC_GetOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetPIDConsts = lib.PPC_GetPIDConsts
PPC_GetPIDConsts.restype = c_short
PPC_GetPIDConsts.argtypes = [POINTER(c_char), PPC_PIDConsts]
# *serialNo, *pidConsts

PPC_GetPosition = lib.PPC_GetPosition
PPC_GetPosition.restype = c_short
PPC_GetPosition.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetPositionControlMode = lib.PPC_GetPositionControlMode
PPC_GetPositionControlMode.restype = PZ_ControlModeTypes
PPC_GetPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetRackDigitalOutputs = lib.PPC_GetRackDigitalOutputs
PPC_GetRackDigitalOutputs.restype = c_byte
PPC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetRackStatusBits = lib.PPC_GetRackStatusBits
PPC_GetRackStatusBits.restype = c_ulong
PPC_GetRackStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetSoftwareVersion = lib.PPC_GetSoftwareVersion
PPC_GetSoftwareVersion.restype = c_ulong
PPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetStatusBits = lib.PPC_GetStatusBits
PPC_GetStatusBits.restype = c_ulong
PPC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PPC_GetVoltageSource = lib.PPC_GetVoltageSource
PPC_GetVoltageSource.restype = PZ_InputSourceFlags
PPC_GetVoltageSource.argtypes = [POINTER(c_char)]
# *serialNo

PPC_Identify = lib.PPC_Identify
PPC_Identify.restype = c_void_p
PPC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

PPC_LoadNamedSettings = lib.PPC_LoadNamedSettings
PPC_LoadNamedSettings.restype = c_bool
PPC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

PPC_LoadSettings = lib.PPC_LoadSettings
PPC_LoadSettings.restype = c_bool
PPC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

PPC_MessageQueueSize = lib.PPC_MessageQueueSize
PPC_MessageQueueSize.restype = c_int
PPC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

PPC_Open = lib.PPC_Open
PPC_Open.restype = c_short
PPC_Open.argtypes = [POINTER(c_char)]
# *serialNo

PPC_PersistSettings = lib.PPC_PersistSettings
PPC_PersistSettings.restype = c_bool
PPC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

PPC_PollingDuration = lib.PPC_PollingDuration
PPC_PollingDuration.restype = c_long
PPC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RegisterMessageCallback = lib.PPC_RegisterMessageCallback
PPC_RegisterMessageCallback.restype = c_short
PPC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNo, void

PPC_RequestActualPosition = lib.PPC_RequestActualPosition
PPC_RequestActualPosition.restype = c_short
PPC_RequestActualPosition.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestMaxOutputVoltage = lib.PPC_RequestMaxOutputVoltage
PPC_RequestMaxOutputVoltage.restype = c_bool
PPC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestOutputVoltage = lib.PPC_RequestOutputVoltage
PPC_RequestOutputVoltage.restype = c_bool
PPC_RequestOutputVoltage.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestPIDConsts = lib.PPC_RequestPIDConsts
PPC_RequestPIDConsts.restype = c_bool
PPC_RequestPIDConsts.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestPosition = lib.PPC_RequestPosition
PPC_RequestPosition.restype = c_short
PPC_RequestPosition.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestPositionControlMode = lib.PPC_RequestPositionControlMode
PPC_RequestPositionControlMode.restype = c_bool
PPC_RequestPositionControlMode.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestRackDigitalOutputs = lib.PPC_RequestRackDigitalOutputs
PPC_RequestRackDigitalOutputs.restype = c_short
PPC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestRackStatusBits = lib.PPC_RequestRackStatusBits
PPC_RequestRackStatusBits.restype = c_short
PPC_RequestRackStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestSettings = lib.PPC_RequestSettings
PPC_RequestSettings.restype = c_short
PPC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestStatus = lib.PPC_RequestStatus
PPC_RequestStatus.restype = c_short
PPC_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestStatusBits = lib.PPC_RequestStatusBits
PPC_RequestStatusBits.restype = c_short
PPC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PPC_RequestVoltageSource = lib.PPC_RequestVoltageSource
PPC_RequestVoltageSource.restype = c_bool
PPC_RequestVoltageSource.argtypes = [POINTER(c_char)]
# *serialNo

PPC_ResetParameters = lib.PPC_ResetParameters
PPC_ResetParameters.restype = c_short
PPC_ResetParameters.argtypes = [POINTER(c_char)]
# *serialNo

PPC_SetIOSettings = lib.PPC_SetIOSettings
PPC_SetIOSettings.restype = c_short
PPC_SetIOSettings.argtypes = [POINTER(c_char), PPC_IOSettings]
# *serialNo, *ioSettings

PPC_SetMaxOutputVoltage = lib.PPC_SetMaxOutputVoltage
PPC_SetMaxOutputVoltage.restype = c_short
PPC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, maxVoltage

PPC_SetNotchParams = lib.PPC_SetNotchParams
PPC_SetNotchParams.restype = c_short
PPC_SetNotchParams.argtypes = [POINTER(c_char), PPC_NotchParams]
# *serialNo, *notchParams

PPC_SetOutputVoltage = lib.PPC_SetOutputVoltage
PPC_SetOutputVoltage.restype = c_short
PPC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, volts

PPC_SetPIDConsts = lib.PPC_SetPIDConsts
PPC_SetPIDConsts.restype = c_short
PPC_SetPIDConsts.argtypes = [POINTER(c_char), PPC_PIDConsts]
# *serialNo, *pidConsts

PPC_SetPosition = lib.PPC_SetPosition
PPC_SetPosition.restype = c_short
PPC_SetPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, position

PPC_SetPositionControlMode = lib.PPC_SetPositionControlMode
PPC_SetPositionControlMode.restype = c_short
PPC_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
# *serialNo, mode

PPC_SetPositionToTolerance = lib.PPC_SetPositionToTolerance
PPC_SetPositionToTolerance.restype = c_short
PPC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_short, c_short]
# *serialNo, position, tolerance

PPC_SetRackDigitalOutputs = lib.PPC_SetRackDigitalOutputs
PPC_SetRackDigitalOutputs.restype = c_short
PPC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
# *serialNo, outputsBits

PPC_SetVoltageSource = lib.PPC_SetVoltageSource
PPC_SetVoltageSource.restype = c_short
PPC_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]
# *serialNo, source

PPC_SetZero = lib.PPC_SetZero
PPC_SetZero.restype = c_short
PPC_SetZero.argtypes = [POINTER(c_char)]
# *serialNo

PPC_StartPolling = lib.PPC_StartPolling
PPC_StartPolling.restype = c_bool
PPC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

PPC_StopPolling = lib.PPC_StopPolling
PPC_StopPolling.restype = c_void_p
PPC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

PPC_WaitForMessage = lib.PPC_WaitForMessage
PPC_WaitForMessage.restype = c_bool
PPC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]
# *serialNo, *messageType, *messageID, *messageData

TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = [c_void_p]
# void

TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [POINTER(c_char), POINTER(c_char), TLI_DeviceInfo]
# *serialNo, *serialNumber, *info

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
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_ulong, c_int, c_int]
# *receiveBuffer, sizeOfBuffer, *typeIDs, length

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
