from ctypes import (POINTER, c_bool, c_byte, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (PZ_ControlModeTypes, PZ_InputSourceFlags)
from .definitions.structures import (
    PZ_FeedbackLoopConstants,
    PZ_LUTWaveParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Benchtop.Piezo.dll")

PBC_CheckConnection = lib.PBC_CheckConnection
PBC_CheckConnection.restype = c_bool
PBC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

PBC_ClearMessageQueue = lib.PBC_ClearMessageQueue
PBC_ClearMessageQueue.restype = c_short
PBC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_Close = lib.PBC_Close
PBC_Close.restype = c_void_p
PBC_Close.argtypes = [POINTER(c_char)]
# *serialNo

PBC_DisableChannel = lib.PBC_DisableChannel
PBC_DisableChannel.restype = c_short
PBC_DisableChannel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_Disconnect = lib.PBC_Disconnect
PBC_Disconnect.restype = c_short
PBC_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

PBC_EnableChannel = lib.PBC_EnableChannel
PBC_EnableChannel.restype = c_short
PBC_EnableChannel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_EnableLastMsgTimer = lib.PBC_EnableLastMsgTimer
PBC_EnableLastMsgTimer.restype = c_void_p
PBC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]
# *serialNo, channel, enable, lastMsgTimeout

PBC_GetFeedbackLoopPIconsts = lib.PBC_GetFeedbackLoopPIconsts
PBC_GetFeedbackLoopPIconsts.restype = c_short
PBC_GetFeedbackLoopPIconsts.argtypes = [c_short, c_short, POINTER(c_char), c_short]
# *integralTerm, *proportionalTerm, *serialNo, channel

PBC_GetFeedbackLoopPIconstsBlock = lib.PBC_GetFeedbackLoopPIconstsBlock
PBC_GetFeedbackLoopPIconstsBlock.restype = c_short
PBC_GetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char), c_short]
# *proportionalAndIntegralConstants, *serialNo, channel

PBC_GetFirmwareVersion = lib.PBC_GetFirmwareVersion
PBC_GetFirmwareVersion.restype = c_ulong
PBC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

PBC_GetHardwareInfo = lib.PBC_GetHardwareInfo
PBC_GetHardwareInfo.restype = c_short
PBC_GetHardwareInfo.argtypes = [
    c_ulong,
    c_long,
    POINTER(c_char),
    c_long,
    POINTER(c_char),
    c_long,
    POINTER(c_char),
    c_long,
    c_short,
    c_ulong,
    c_ulong]
# *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numChannels, *serialNo, *type, channel, sizeOfModelNo, sizeOfNotes

PBC_GetHardwareInfoBlock = lib.PBC_GetHardwareInfoBlock
PBC_GetHardwareInfoBlock.restype = c_short
PBC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char), c_short]
# *hardwareInfo, *serialNo, channel

PBC_GetMaxOutputVoltage = lib.PBC_GetMaxOutputVoltage
PBC_GetMaxOutputVoltage.restype = c_short
PBC_GetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_GetMaximumTravel = lib.PBC_GetMaximumTravel
PBC_GetMaximumTravel.restype = c_long
PBC_GetMaximumTravel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_GetNextMessage = lib.PBC_GetNextMessage
PBC_GetNextMessage.restype = c_bool
PBC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
# *messageData, *messageID, *messageType, *serialNo, channel

PBC_GetNumChannels = lib.PBC_GetNumChannels
PBC_GetNumChannels.restype = c_short
PBC_GetNumChannels.argtypes = [POINTER(c_char)]
# *serialNo

PBC_GetOutputVoltage = lib.PBC_GetOutputVoltage
PBC_GetOutputVoltage.restype = c_short
PBC_GetOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_GetPosition = lib.PBC_GetPosition
PBC_GetPosition.restype = c_short
PBC_GetPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_GetPositionControlMode = lib.PBC_GetPositionControlMode
PBC_GetPositionControlMode.restype = PZ_ControlModeTypes
PBC_GetPositionControlMode.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_GetRackDigitalOutputs = lib.PBC_GetRackDigitalOutputs
PBC_GetRackDigitalOutputs.restype = c_byte
PBC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

PBC_GetRackStatusBits = lib.PBC_GetRackStatusBits
PBC_GetRackStatusBits.restype = c_ulong
PBC_GetRackStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PBC_GetSoftwareVersion = lib.PBC_GetSoftwareVersion
PBC_GetSoftwareVersion.restype = c_ulong
PBC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

PBC_GetStatusBits = lib.PBC_GetStatusBits
PBC_GetStatusBits.restype = c_ulong
PBC_GetStatusBits.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_GetVoltageSource = lib.PBC_GetVoltageSource
PBC_GetVoltageSource.restype = PZ_InputSourceFlags
PBC_GetVoltageSource.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_HasLastMsgTimerOverrun = lib.PBC_HasLastMsgTimerOverrun
PBC_HasLastMsgTimerOverrun.restype = c_bool
PBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_Identify = lib.PBC_Identify
PBC_Identify.restype = c_void_p
PBC_Identify.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_IsChannelValid = lib.PBC_IsChannelValid
PBC_IsChannelValid.restype = c_bool
PBC_IsChannelValid.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_LoadNamedSettings = lib.PBC_LoadNamedSettings
PBC_LoadNamedSettings.restype = c_bool
PBC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
# *serialNo, *settingsName, channel

PBC_LoadSettings = lib.PBC_LoadSettings
PBC_LoadSettings.restype = c_bool
PBC_LoadSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_MaxChannelCount = lib.PBC_MaxChannelCount
PBC_MaxChannelCount.restype = c_int
PBC_MaxChannelCount.argtypes = [POINTER(c_char)]
# *serialNo

PBC_MessageQueueSize = lib.PBC_MessageQueueSize
PBC_MessageQueueSize.restype = c_int
PBC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_Open = lib.PBC_Open
PBC_Open.restype = c_short
PBC_Open.argtypes = [POINTER(c_char)]
# *serialNo

PBC_PersistSettings = lib.PBC_PersistSettings
PBC_PersistSettings.restype = c_bool
PBC_PersistSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_PollingDuration = lib.PBC_PollingDuration
PBC_PollingDuration.restype = c_long
PBC_PollingDuration.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RegisterMessageCallback = lib.PBC_RegisterMessageCallback
PBC_RegisterMessageCallback.restype = c_short
PBC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, c_void_p]
# *serialNo, channel, void

PBC_RequestActualPosition = lib.PBC_RequestActualPosition
PBC_RequestActualPosition.restype = c_short
PBC_RequestActualPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestFeedbackLoopPIconsts = lib.PBC_RequestFeedbackLoopPIconsts
PBC_RequestFeedbackLoopPIconsts.restype = c_bool
PBC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestMaxOutputVoltage = lib.PBC_RequestMaxOutputVoltage
PBC_RequestMaxOutputVoltage.restype = c_bool
PBC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestMaximumTravel = lib.PBC_RequestMaximumTravel
PBC_RequestMaximumTravel.restype = c_bool
PBC_RequestMaximumTravel.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestOutputVoltage = lib.PBC_RequestOutputVoltage
PBC_RequestOutputVoltage.restype = c_bool
PBC_RequestOutputVoltage.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestPosition = lib.PBC_RequestPosition
PBC_RequestPosition.restype = c_short
PBC_RequestPosition.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestPositionControlMode = lib.PBC_RequestPositionControlMode
PBC_RequestPositionControlMode.restype = c_bool
PBC_RequestPositionControlMode.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestRackDigitalOutputs = lib.PBC_RequestRackDigitalOutputs
PBC_RequestRackDigitalOutputs.restype = c_short
PBC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
# *serialNo

PBC_RequestRackStatusBits = lib.PBC_RequestRackStatusBits
PBC_RequestRackStatusBits.restype = c_short
PBC_RequestRackStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

PBC_RequestSettings = lib.PBC_RequestSettings
PBC_RequestSettings.restype = c_short
PBC_RequestSettings.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestStatus = lib.PBC_RequestStatus
PBC_RequestStatus.restype = c_short
PBC_RequestStatus.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestStatusBits = lib.PBC_RequestStatusBits
PBC_RequestStatusBits.restype = c_short
PBC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_RequestVoltageSource = lib.PBC_RequestVoltageSource
PBC_RequestVoltageSource.restype = c_bool
PBC_RequestVoltageSource.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_ResetParameters = lib.PBC_ResetParameters
PBC_ResetParameters.restype = c_short
PBC_ResetParameters.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_SetFeedbackLoopPIconsts = lib.PBC_SetFeedbackLoopPIconsts
PBC_SetFeedbackLoopPIconsts.restype = c_short
PBC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short, c_short]
# *serialNo, channel, integralTerm, proportionalTerm

PBC_SetFeedbackLoopPIconstsBlock = lib.PBC_SetFeedbackLoopPIconstsBlock
PBC_SetFeedbackLoopPIconstsBlock.restype = c_short
PBC_SetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char), c_short]
# *proportionalAndIntegralConstants, *serialNo, channel

PBC_SetLUTwaveParams = lib.PBC_SetLUTwaveParams
PBC_SetLUTwaveParams.restype = c_short
PBC_SetLUTwaveParams.argtypes = [PZ_LUTWaveParameters, POINTER(c_char), c_short]
# *LUTwaveParams, *serialNo, channel

PBC_SetLUTwaveSample = lib.PBC_SetLUTwaveSample
PBC_SetLUTwaveSample.restype = c_short
PBC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_short, c_long]
# *serialNo, channel, index, value

PBC_SetMaxOutputVoltage = lib.PBC_SetMaxOutputVoltage
PBC_SetMaxOutputVoltage.restype = c_short
PBC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short, c_short]
# *serialNo, channel, maxVoltage

PBC_SetOutputVoltage = lib.PBC_SetOutputVoltage
PBC_SetOutputVoltage.restype = c_short
PBC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short, c_short]
# *serialNo, channel, volts

PBC_SetPosition = lib.PBC_SetPosition
PBC_SetPosition.restype = c_short
PBC_SetPosition.argtypes = [POINTER(c_char), c_short, c_short]
# *serialNo, channel, position

PBC_SetPositionControlMode = lib.PBC_SetPositionControlMode
PBC_SetPositionControlMode.restype = c_short
PBC_SetPositionControlMode.argtypes = [POINTER(c_char), c_short, PZ_ControlModeTypes]
# *serialNo, channel, mode

PBC_SetPositionToTolerance = lib.PBC_SetPositionToTolerance
PBC_SetPositionToTolerance.restype = c_short
PBC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_short, c_short, c_short]
# *serialNo, channel, position, tolerance

PBC_SetRackDigitalOutputs = lib.PBC_SetRackDigitalOutputs
PBC_SetRackDigitalOutputs.restype = c_short
PBC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
# *serialNo, outputsBits

PBC_SetVoltageSource = lib.PBC_SetVoltageSource
PBC_SetVoltageSource.restype = c_short
PBC_SetVoltageSource.argtypes = [POINTER(c_char), c_short, PZ_InputSourceFlags]
# *serialNo, channel, source

PBC_SetZero = lib.PBC_SetZero
PBC_SetZero.restype = c_short
PBC_SetZero.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_StartLUTwave = lib.PBC_StartLUTwave
PBC_StartLUTwave.restype = c_short
PBC_StartLUTwave.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_StartPolling = lib.PBC_StartPolling
PBC_StartPolling.restype = c_bool
PBC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]
# *serialNo, channel, milliseconds

PBC_StopLUTwave = lib.PBC_StopLUTwave
PBC_StopLUTwave.restype = c_short
PBC_StopLUTwave.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_StopPolling = lib.PBC_StopPolling
PBC_StopPolling.restype = c_void_p
PBC_StopPolling.argtypes = [POINTER(c_char), c_short]
# *serialNo, channel

PBC_TimeSinceLastMsgReceived = lib.PBC_TimeSinceLastMsgReceived
PBC_TimeSinceLastMsgReceived.restype = c_bool
PBC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char), c_short]
# &lastUpdateTimeMS, *serialNo, channel

PBC_WaitForMessage = lib.PBC_WaitForMessage
PBC_WaitForMessage.restype = c_bool
PBC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
# *messageData, *messageID, *messageType, *serialNo, channel

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
