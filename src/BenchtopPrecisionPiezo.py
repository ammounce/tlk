from c_types import (POINTER, c_byte, c_char, c_int, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (PZ_ControlModeTypes, PZ_InputSourceFlags)
from .definitions.structures import (
    PPC_IOSettings,
    PPC_NotchParams,
    PPC_PIDConsts,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class BenchtopPrecisionPiezo(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.Benchtop.PrecisionPiezo.dll")

        self.PPC2_ClearMessageQueue = self.lib.PPC2_ClearMessageQueue
        self.PPC2_ClearMessageQueue.restype = c_short
        self.PPC2_ClearMessageQueue.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_DisableChannel = self.lib.PPC2_DisableChannel
        self.PPC2_DisableChannel.restype = c_short
        self.PPC2_DisableChannel.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_EnableChannel = self.lib.PPC2_EnableChannel
        self.PPC2_EnableChannel.restype = c_short
        self.PPC2_EnableChannel.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_GetHardwareInfo = self.lib.PPC2_GetHardwareInfo
        self.PPC2_GetHardwareInfo.restype = c_short
        self.PPC2_GetHardwareInfo.argtypes = [
            c_ulong,
            c_long,
            POINTER(c_char),
            c_long,
            POINTER(c_char),
            c_long,
            POINTER(c_char),
            c_long,
            c_int,
            c_ulong,
            c_ulong]
        # *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numChannels, *serialNo, *type, channel, sizeOfModelNo, sizeOfNotes

        self.PPC2_GetHardwareInfoBlock = self.lib.PPC2_GetHardwareInfoBlock
        self.PPC2_GetHardwareInfoBlock.restype = c_short
        self.PPC2_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char), c_int]
        # *hardwareInfo, *serialNo, channel

        self.PPC2_GetIOSettings = self.lib.PPC2_GetIOSettings
        self.PPC2_GetIOSettings.restype = c_short
        self.PPC2_GetIOSettings.argtypes = [PPC_IOSettings, POINTER(c_char), c_int]
        # *ioSettings, *serialNo, channel

        self.PPC2_GetMaxOutputVoltage = self.lib.PPC2_GetMaxOutputVoltage
        self.PPC2_GetMaxOutputVoltage.restype = c_short
        self.PPC2_GetMaxOutputVoltage.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_GetMaximumTravel = self.lib.PPC2_GetMaximumTravel
        self.PPC2_GetMaximumTravel.restype = c_long
        self.PPC2_GetMaximumTravel.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_GetMinOutputVoltage = self.lib.PPC2_GetMinOutputVoltage
        self.PPC2_GetMinOutputVoltage.restype = c_short
        self.PPC2_GetMinOutputVoltage.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_GetNextMessage = self.lib.PPC2_GetNextMessage
        self.PPC2_GetNextMessage.restype = c_bool
        self.PPC2_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_int]
        # *messageData, *messageID, *messageType, *serialNo, channel

        self.PPC2_GetNotchParams = self.lib.PPC2_GetNotchParams
        self.PPC2_GetNotchParams.restype = c_short
        self.PPC2_GetNotchParams.argtypes = [PPC_NotchParams, POINTER(c_char), c_int]
        # *notchParams, *serialNo, channel

        self.PPC2_GetOutputVoltage = self.lib.PPC2_GetOutputVoltage
        self.PPC2_GetOutputVoltage.restype = c_short
        self.PPC2_GetOutputVoltage.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_GetPIDConsts = self.lib.PPC2_GetPIDConsts
        self.PPC2_GetPIDConsts.restype = c_short
        self.PPC2_GetPIDConsts.argtypes = [PPC_PIDConsts, POINTER(c_char), c_int]
        # *pidConsts, *serialNo, channel

        self.PPC2_GetPosition = self.lib.PPC2_GetPosition
        self.PPC2_GetPosition.restype = c_short
        self.PPC2_GetPosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_GetPositionControlMode = self.lib.PPC2_GetPositionControlMode
        self.PPC2_GetPositionControlMode.restype = PZ_ControlModeTypes
        self.PPC2_GetPositionControlMode.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_GetRackDigitalOutputs = self.lib.PPC2_GetRackDigitalOutputs
        self.PPC2_GetRackDigitalOutputs.restype = c_byte
        self.PPC2_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC2_GetRackStatusBits = self.lib.PPC2_GetRackStatusBits
        self.PPC2_GetRackStatusBits.restype = c_ulong
        self.PPC2_GetRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC2_GetStatusBits = self.lib.PPC2_GetStatusBits
        self.PPC2_GetStatusBits.restype = c_ulong
        self.PPC2_GetStatusBits.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_GetVoltageSource = self.lib.PPC2_GetVoltageSource
        self.PPC2_GetVoltageSource.restype = PZ_InputSourceFlags
        self.PPC2_GetVoltageSource.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_Identify = self.lib.PPC2_Identify
        self.PPC2_Identify.restype = None
        self.PPC2_Identify.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_LoadNamedSettings = self.lib.PPC2_LoadNamedSettings
        self.PPC2_LoadNamedSettings.restype = c_bool
        self.PPC2_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *serialNo, *settingsName, channel

        self.PPC2_LoadSettings = self.lib.PPC2_LoadSettings
        self.PPC2_LoadSettings.restype = c_bool
        self.PPC2_LoadSettings.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_MessageQueueSize = self.lib.PPC2_MessageQueueSize
        self.PPC2_MessageQueueSize.restype = c_int
        self.PPC2_MessageQueueSize.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_PersistSettings = self.lib.PPC2_PersistSettings
        self.PPC2_PersistSettings.restype = c_bool
        self.PPC2_PersistSettings.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_PollingDuration = self.lib.PPC2_PollingDuration
        self.PPC2_PollingDuration.restype = c_long
        self.PPC2_PollingDuration.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RegisterMessageCallback = self.lib.PPC2_RegisterMessageCallback
        self.PPC2_RegisterMessageCallback.restype = c_short
        self.PPC2_RegisterMessageCallback.argtypes = [POINTER(c_char), c_int, None]
        # *serialNo, channel, void

        self.PPC2_RequestActualPosition = self.lib.PPC2_RequestActualPosition
        self.PPC2_RequestActualPosition.restype = c_short
        self.PPC2_RequestActualPosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RequestMaxOutputVoltage = self.lib.PPC2_RequestMaxOutputVoltage
        self.PPC2_RequestMaxOutputVoltage.restype = c_bool
        self.PPC2_RequestMaxOutputVoltage.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RequestOutputVoltage = self.lib.PPC2_RequestOutputVoltage
        self.PPC2_RequestOutputVoltage.restype = c_bool
        self.PPC2_RequestOutputVoltage.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RequestPIDConsts = self.lib.PPC2_RequestPIDConsts
        self.PPC2_RequestPIDConsts.restype = c_bool
        self.PPC2_RequestPIDConsts.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RequestPosition = self.lib.PPC2_RequestPosition
        self.PPC2_RequestPosition.restype = c_short
        self.PPC2_RequestPosition.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RequestRackDigitalOutputs = self.lib.PPC2_RequestRackDigitalOutputs
        self.PPC2_RequestRackDigitalOutputs.restype = c_short
        self.PPC2_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC2_RequestRackStatusBits = self.lib.PPC2_RequestRackStatusBits
        self.PPC2_RequestRackStatusBits.restype = c_short
        self.PPC2_RequestRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC2_RequestSettings = self.lib.PPC2_RequestSettings
        self.PPC2_RequestSettings.restype = c_short
        self.PPC2_RequestSettings.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RequestStatus = self.lib.PPC2_RequestStatus
        self.PPC2_RequestStatus.restype = c_short
        self.PPC2_RequestStatus.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RequestStatusBits = self.lib.PPC2_RequestStatusBits
        self.PPC2_RequestStatusBits.restype = c_short
        self.PPC2_RequestStatusBits.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_RequestVoltageSource = self.lib.PPC2_RequestVoltageSource
        self.PPC2_RequestVoltageSource.restype = c_bool
        self.PPC2_RequestVoltageSource.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_ResetParameters = self.lib.PPC2_ResetParameters
        self.PPC2_ResetParameters.restype = c_short
        self.PPC2_ResetParameters.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_SetIOSettings = self.lib.PPC2_SetIOSettings
        self.PPC2_SetIOSettings.restype = c_short
        self.PPC2_SetIOSettings.argtypes = [PPC_IOSettings, POINTER(c_char), c_int]
        # *ioSettings, *serialNo, channel

        self.PPC2_SetMaxOutputVoltage = self.lib.PPC2_SetMaxOutputVoltage
        self.PPC2_SetMaxOutputVoltage.restype = c_short
        self.PPC2_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_int, c_short]
        # *serialNo, channel, maxVoltage

        self.PPC2_SetNotchParams = self.lib.PPC2_SetNotchParams
        self.PPC2_SetNotchParams.restype = c_short
        self.PPC2_SetNotchParams.argtypes = [PPC_NotchParams, POINTER(c_char), c_int]
        # *notchParams, *serialNo, channel

        self.PPC2_SetOutputVoltage = self.lib.PPC2_SetOutputVoltage
        self.PPC2_SetOutputVoltage.restype = c_short
        self.PPC2_SetOutputVoltage.argtypes = [POINTER(c_char), c_int, c_short]
        # *serialNo, channel, volts

        self.PPC2_SetPIDConsts = self.lib.PPC2_SetPIDConsts
        self.PPC2_SetPIDConsts.restype = c_short
        self.PPC2_SetPIDConsts.argtypes = [PPC_PIDConsts, POINTER(c_char), c_int]
        # *pidConsts, *serialNo, channel

        self.PPC2_SetPosition = self.lib.PPC2_SetPosition
        self.PPC2_SetPosition.restype = c_short
        self.PPC2_SetPosition.argtypes = [POINTER(c_char), c_int, c_short]
        # *serialNo, channel, position

        self.PPC2_SetPositionControlMode = self.lib.PPC2_SetPositionControlMode
        self.PPC2_SetPositionControlMode.restype = c_short
        self.PPC2_SetPositionControlMode.argtypes = [POINTER(c_char), c_int, PZ_ControlModeTypes]
        # *serialNo, channel, mode

        self.PPC2_SetPositionToTolerance = self.lib.PPC2_SetPositionToTolerance
        self.PPC2_SetPositionToTolerance.restype = c_short
        self.PPC2_SetPositionToTolerance.argtypes = [POINTER(c_char), c_int, c_short, c_short]
        # *serialNo, channel, position, tolerance

        self.PPC2_SetRackDigitalOutputs = self.lib.PPC2_SetRackDigitalOutputs
        self.PPC2_SetRackDigitalOutputs.restype = c_short
        self.PPC2_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.PPC2_SetVoltageSource = self.lib.PPC2_SetVoltageSource
        self.PPC2_SetVoltageSource.restype = c_short
        self.PPC2_SetVoltageSource.argtypes = [POINTER(c_char), c_int, PZ_InputSourceFlags]
        # *serialNo, channel, source

        self.PPC2_SetZero = self.lib.PPC2_SetZero
        self.PPC2_SetZero.restype = c_short
        self.PPC2_SetZero.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_StartPolling = self.lib.PPC2_StartPolling
        self.PPC2_StartPolling.restype = c_bool
        self.PPC2_StartPolling.argtypes = [POINTER(c_char), c_int, c_int]
        # *serialNo, channel, milliseconds

        self.PPC2_StopPolling = self.lib.PPC2_StopPolling
        self.PPC2_StopPolling.restype = None
        self.PPC2_StopPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, channel

        self.PPC2_WaitForMessage = self.lib.PPC2_WaitForMessage
        self.PPC2_WaitForMessage.restype = c_bool
        self.PPC2_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_int]
        # *messageData, *messageID, *messageType, *serialNo, channel

        self.PPC_CheckConnection = self.lib.PPC_CheckConnection
        self.PPC_CheckConnection.restype = c_bool
        self.PPC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_ClearMessageQueue = self.lib.PPC_ClearMessageQueue
        self.PPC_ClearMessageQueue.restype = c_short
        self.PPC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_Close = self.lib.PPC_Close
        self.PPC_Close.restype = None
        self.PPC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_DisableChannel = self.lib.PPC_DisableChannel
        self.PPC_DisableChannel.restype = c_short
        self.PPC_DisableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_Disconnect = self.lib.PPC_Disconnect
        self.PPC_Disconnect.restype = c_short
        self.PPC_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_EnableChannel = self.lib.PPC_EnableChannel
        self.PPC_EnableChannel.restype = c_short
        self.PPC_EnableChannel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetFirmwareVersion = self.lib.PPC_GetFirmwareVersion
        self.PPC_GetFirmwareVersion.restype = c_ulong
        self.PPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetHardwareInfo = self.lib.PPC_GetHardwareInfo
        self.PPC_GetHardwareInfo.restype = c_short
        self.PPC_GetHardwareInfo.argtypes = [
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

        self.PPC_GetHardwareInfoBlock = self.lib.PPC_GetHardwareInfoBlock
        self.PPC_GetHardwareInfoBlock.restype = c_short
        self.PPC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.PPC_GetIOSettings = self.lib.PPC_GetIOSettings
        self.PPC_GetIOSettings.restype = c_short
        self.PPC_GetIOSettings.argtypes = [PPC_IOSettings, POINTER(c_char)]
        # *ioSettings, *serialNo

        self.PPC_GetMaxOutputVoltage = self.lib.PPC_GetMaxOutputVoltage
        self.PPC_GetMaxOutputVoltage.restype = c_short
        self.PPC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetMaximumTravel = self.lib.PPC_GetMaximumTravel
        self.PPC_GetMaximumTravel.restype = c_long
        self.PPC_GetMaximumTravel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetMinOutputVoltage = self.lib.PPC_GetMinOutputVoltage
        self.PPC_GetMinOutputVoltage.restype = c_short
        self.PPC_GetMinOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetNextMessage = self.lib.PPC_GetNextMessage
        self.PPC_GetNextMessage.restype = c_bool
        self.PPC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.PPC_GetNotchParams = self.lib.PPC_GetNotchParams
        self.PPC_GetNotchParams.restype = c_short
        self.PPC_GetNotchParams.argtypes = [PPC_NotchParams, POINTER(c_char)]
        # *notchParams, *serialNo

        self.PPC_GetOutputVoltage = self.lib.PPC_GetOutputVoltage
        self.PPC_GetOutputVoltage.restype = c_short
        self.PPC_GetOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetPIDConsts = self.lib.PPC_GetPIDConsts
        self.PPC_GetPIDConsts.restype = c_short
        self.PPC_GetPIDConsts.argtypes = [PPC_PIDConsts, POINTER(c_char)]
        # *pidConsts, *serialNo

        self.PPC_GetPosition = self.lib.PPC_GetPosition
        self.PPC_GetPosition.restype = c_short
        self.PPC_GetPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetPositionControlMode = self.lib.PPC_GetPositionControlMode
        self.PPC_GetPositionControlMode.restype = PZ_ControlModeTypes
        self.PPC_GetPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetRackDigitalOutputs = self.lib.PPC_GetRackDigitalOutputs
        self.PPC_GetRackDigitalOutputs.restype = c_byte
        self.PPC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetRackStatusBits = self.lib.PPC_GetRackStatusBits
        self.PPC_GetRackStatusBits.restype = c_ulong
        self.PPC_GetRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetSoftwareVersion = self.lib.PPC_GetSoftwareVersion
        self.PPC_GetSoftwareVersion.restype = c_ulong
        self.PPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetStatusBits = self.lib.PPC_GetStatusBits
        self.PPC_GetStatusBits.restype = c_ulong
        self.PPC_GetStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_GetVoltageSource = self.lib.PPC_GetVoltageSource
        self.PPC_GetVoltageSource.restype = PZ_InputSourceFlags
        self.PPC_GetVoltageSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_Identify = self.lib.PPC_Identify
        self.PPC_Identify.restype = None
        self.PPC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_LoadNamedSettings = self.lib.PPC_LoadNamedSettings
        self.PPC_LoadNamedSettings.restype = c_bool
        self.PPC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.PPC_LoadSettings = self.lib.PPC_LoadSettings
        self.PPC_LoadSettings.restype = c_bool
        self.PPC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_MessageQueueSize = self.lib.PPC_MessageQueueSize
        self.PPC_MessageQueueSize.restype = c_int
        self.PPC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_Open = self.lib.PPC_Open
        self.PPC_Open.restype = c_short
        self.PPC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_PersistSettings = self.lib.PPC_PersistSettings
        self.PPC_PersistSettings.restype = c_bool
        self.PPC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_PollingDuration = self.lib.PPC_PollingDuration
        self.PPC_PollingDuration.restype = c_long
        self.PPC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RegisterMessageCallback = self.lib.PPC_RegisterMessageCallback
        self.PPC_RegisterMessageCallback.restype = c_short
        self.PPC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.PPC_RequestActualPosition = self.lib.PPC_RequestActualPosition
        self.PPC_RequestActualPosition.restype = c_short
        self.PPC_RequestActualPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestMaxOutputVoltage = self.lib.PPC_RequestMaxOutputVoltage
        self.PPC_RequestMaxOutputVoltage.restype = c_bool
        self.PPC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestOutputVoltage = self.lib.PPC_RequestOutputVoltage
        self.PPC_RequestOutputVoltage.restype = c_bool
        self.PPC_RequestOutputVoltage.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestPIDConsts = self.lib.PPC_RequestPIDConsts
        self.PPC_RequestPIDConsts.restype = c_bool
        self.PPC_RequestPIDConsts.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestPosition = self.lib.PPC_RequestPosition
        self.PPC_RequestPosition.restype = c_short
        self.PPC_RequestPosition.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestPositionControlMode = self.lib.PPC_RequestPositionControlMode
        self.PPC_RequestPositionControlMode.restype = c_bool
        self.PPC_RequestPositionControlMode.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestRackDigitalOutputs = self.lib.PPC_RequestRackDigitalOutputs
        self.PPC_RequestRackDigitalOutputs.restype = c_short
        self.PPC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestRackStatusBits = self.lib.PPC_RequestRackStatusBits
        self.PPC_RequestRackStatusBits.restype = c_short
        self.PPC_RequestRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestSettings = self.lib.PPC_RequestSettings
        self.PPC_RequestSettings.restype = c_short
        self.PPC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestStatus = self.lib.PPC_RequestStatus
        self.PPC_RequestStatus.restype = c_short
        self.PPC_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestStatusBits = self.lib.PPC_RequestStatusBits
        self.PPC_RequestStatusBits.restype = c_short
        self.PPC_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_RequestVoltageSource = self.lib.PPC_RequestVoltageSource
        self.PPC_RequestVoltageSource.restype = c_bool
        self.PPC_RequestVoltageSource.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_ResetParameters = self.lib.PPC_ResetParameters
        self.PPC_ResetParameters.restype = c_short
        self.PPC_ResetParameters.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_SetIOSettings = self.lib.PPC_SetIOSettings
        self.PPC_SetIOSettings.restype = c_short
        self.PPC_SetIOSettings.argtypes = [PPC_IOSettings, POINTER(c_char)]
        # *ioSettings, *serialNo

        self.PPC_SetMaxOutputVoltage = self.lib.PPC_SetMaxOutputVoltage
        self.PPC_SetMaxOutputVoltage.restype = c_short
        self.PPC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, maxVoltage

        self.PPC_SetNotchParams = self.lib.PPC_SetNotchParams
        self.PPC_SetNotchParams.restype = c_short
        self.PPC_SetNotchParams.argtypes = [PPC_NotchParams, POINTER(c_char)]
        # *notchParams, *serialNo

        self.PPC_SetOutputVoltage = self.lib.PPC_SetOutputVoltage
        self.PPC_SetOutputVoltage.restype = c_short
        self.PPC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, volts

        self.PPC_SetPIDConsts = self.lib.PPC_SetPIDConsts
        self.PPC_SetPIDConsts.restype = c_short
        self.PPC_SetPIDConsts.argtypes = [PPC_PIDConsts, POINTER(c_char)]
        # *pidConsts, *serialNo

        self.PPC_SetPosition = self.lib.PPC_SetPosition
        self.PPC_SetPosition.restype = c_short
        self.PPC_SetPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, position

        self.PPC_SetPositionControlMode = self.lib.PPC_SetPositionControlMode
        self.PPC_SetPositionControlMode.restype = c_short
        self.PPC_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]
        # *serialNo, mode

        self.PPC_SetPositionToTolerance = self.lib.PPC_SetPositionToTolerance
        self.PPC_SetPositionToTolerance.restype = c_short
        self.PPC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_short, c_short]
        # *serialNo, position, tolerance

        self.PPC_SetRackDigitalOutputs = self.lib.PPC_SetRackDigitalOutputs
        self.PPC_SetRackDigitalOutputs.restype = c_short
        self.PPC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.PPC_SetVoltageSource = self.lib.PPC_SetVoltageSource
        self.PPC_SetVoltageSource.restype = c_short
        self.PPC_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]
        # *serialNo, source

        self.PPC_SetZero = self.lib.PPC_SetZero
        self.PPC_SetZero.restype = c_short
        self.PPC_SetZero.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_StartPolling = self.lib.PPC_StartPolling
        self.PPC_StartPolling.restype = c_bool
        self.PPC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.PPC_StopPolling = self.lib.PPC_StopPolling
        self.PPC_StopPolling.restype = None
        self.PPC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PPC_WaitForMessage = self.lib.PPC_WaitForMessage
        self.PPC_WaitForMessage.restype = c_bool
        self.PPC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
