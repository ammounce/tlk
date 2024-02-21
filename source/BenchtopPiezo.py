from c_types import (POINTER, c_bool, c_byte, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (PZ_ControlModeTypes, PZ_InputSourceFlags)
from .definitions.structures import (
    PZ_FeedbackLoopConstants,
    PZ_LUTWaveParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from pathlib import Path


class BenchtopPiezo(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.Benchtop.Piezo.dll")

        self.PBC_CheckConnection = self.lib.PBC_CheckConnection
        self.PBC_CheckConnection.restype = c_bool
        self.PBC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_ClearMessageQueue = self.lib.PBC_ClearMessageQueue
        self.PBC_ClearMessageQueue.restype = c_short
        self.PBC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_Close = self.lib.PBC_Close
        self.PBC_Close.restype = None
        self.PBC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_DisableChannel = self.lib.PBC_DisableChannel
        self.PBC_DisableChannel.restype = c_short
        self.PBC_DisableChannel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_Disconnect = self.lib.PBC_Disconnect
        self.PBC_Disconnect.restype = c_short
        self.PBC_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_EnableChannel = self.lib.PBC_EnableChannel
        self.PBC_EnableChannel.restype = c_short
        self.PBC_EnableChannel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_EnableLastMsgTimer = self.lib.PBC_EnableLastMsgTimer
        self.PBC_EnableLastMsgTimer.restype = None
        self.PBC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]
        # *serialNo, channel, enable, lastMsgTimeout

        self.PBC_GetFeedbackLoopPIconsts = self.lib.PBC_GetFeedbackLoopPIconsts
        self.PBC_GetFeedbackLoopPIconsts.restype = c_short
        self.PBC_GetFeedbackLoopPIconsts.argtypes = [c_short, c_short, POINTER(c_char), c_short]
        # *integralTerm, *proportionalTerm, *serialNo, channel

        self.PBC_GetFeedbackLoopPIconstsBlock = self.lib.PBC_GetFeedbackLoopPIconstsBlock
        self.PBC_GetFeedbackLoopPIconstsBlock.restype = c_short
        self.PBC_GetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char), c_short]
        # *proportionalAndIntegralConstants, *serialNo, channel

        self.PBC_GetFirmwareVersion = self.lib.PBC_GetFirmwareVersion
        self.PBC_GetFirmwareVersion.restype = c_ulong
        self.PBC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_GetHardwareInfo = self.lib.PBC_GetHardwareInfo
        self.PBC_GetHardwareInfo.restype = c_short
        self.PBC_GetHardwareInfo.argtypes = [
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

        self.PBC_GetHardwareInfoBlock = self.lib.PBC_GetHardwareInfoBlock
        self.PBC_GetHardwareInfoBlock.restype = c_short
        self.PBC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char), c_short]
        # *hardwareInfo, *serialNo, channel

        self.PBC_GetMaxOutputVoltage = self.lib.PBC_GetMaxOutputVoltage
        self.PBC_GetMaxOutputVoltage.restype = c_short
        self.PBC_GetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_GetMaximumTravel = self.lib.PBC_GetMaximumTravel
        self.PBC_GetMaximumTravel.restype = c_long
        self.PBC_GetMaximumTravel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_GetNextMessage = self.lib.PBC_GetNextMessage
        self.PBC_GetNextMessage.restype = c_bool
        self.PBC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
        # *messageData, *messageID, *messageType, *serialNo, channel

        self.PBC_GetNumChannels = self.lib.PBC_GetNumChannels
        self.PBC_GetNumChannels.restype = c_short
        self.PBC_GetNumChannels.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_GetOutputVoltage = self.lib.PBC_GetOutputVoltage
        self.PBC_GetOutputVoltage.restype = c_short
        self.PBC_GetOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_GetPosition = self.lib.PBC_GetPosition
        self.PBC_GetPosition.restype = c_short
        self.PBC_GetPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_GetPositionControlMode = self.lib.PBC_GetPositionControlMode
        self.PBC_GetPositionControlMode.restype = PZ_ControlModeTypes
        self.PBC_GetPositionControlMode.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_GetRackDigitalOutputs = self.lib.PBC_GetRackDigitalOutputs
        self.PBC_GetRackDigitalOutputs.restype = c_byte
        self.PBC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_GetRackStatusBits = self.lib.PBC_GetRackStatusBits
        self.PBC_GetRackStatusBits.restype = c_ulong
        self.PBC_GetRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_GetSoftwareVersion = self.lib.PBC_GetSoftwareVersion
        self.PBC_GetSoftwareVersion.restype = c_ulong
        self.PBC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_GetStatusBits = self.lib.PBC_GetStatusBits
        self.PBC_GetStatusBits.restype = c_ulong
        self.PBC_GetStatusBits.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_GetVoltageSource = self.lib.PBC_GetVoltageSource
        self.PBC_GetVoltageSource.restype = PZ_InputSourceFlags
        self.PBC_GetVoltageSource.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_HasLastMsgTimerOverrun = self.lib.PBC_HasLastMsgTimerOverrun
        self.PBC_HasLastMsgTimerOverrun.restype = c_bool
        self.PBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_Identify = self.lib.PBC_Identify
        self.PBC_Identify.restype = None
        self.PBC_Identify.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_IsChannelValid = self.lib.PBC_IsChannelValid
        self.PBC_IsChannelValid.restype = c_bool
        self.PBC_IsChannelValid.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_LoadNamedSettings = self.lib.PBC_LoadNamedSettings
        self.PBC_LoadNamedSettings.restype = c_bool
        self.PBC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char), c_short]
        # *serialNo, *settingsName, channel

        self.PBC_LoadSettings = self.lib.PBC_LoadSettings
        self.PBC_LoadSettings.restype = c_bool
        self.PBC_LoadSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_MaxChannelCount = self.lib.PBC_MaxChannelCount
        self.PBC_MaxChannelCount.restype = c_int
        self.PBC_MaxChannelCount.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_MessageQueueSize = self.lib.PBC_MessageQueueSize
        self.PBC_MessageQueueSize.restype = c_int
        self.PBC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_Open = self.lib.PBC_Open
        self.PBC_Open.restype = c_short
        self.PBC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_PersistSettings = self.lib.PBC_PersistSettings
        self.PBC_PersistSettings.restype = c_bool
        self.PBC_PersistSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_PollingDuration = self.lib.PBC_PollingDuration
        self.PBC_PollingDuration.restype = c_long
        self.PBC_PollingDuration.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RegisterMessageCallback = self.lib.PBC_RegisterMessageCallback
        self.PBC_RegisterMessageCallback.restype = c_short
        self.PBC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, None]
        # *serialNo, channel, void

        self.PBC_RequestActualPosition = self.lib.PBC_RequestActualPosition
        self.PBC_RequestActualPosition.restype = c_short
        self.PBC_RequestActualPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestFeedbackLoopPIconsts = self.lib.PBC_RequestFeedbackLoopPIconsts
        self.PBC_RequestFeedbackLoopPIconsts.restype = c_bool
        self.PBC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestMaxOutputVoltage = self.lib.PBC_RequestMaxOutputVoltage
        self.PBC_RequestMaxOutputVoltage.restype = c_bool
        self.PBC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestMaximumTravel = self.lib.PBC_RequestMaximumTravel
        self.PBC_RequestMaximumTravel.restype = c_bool
        self.PBC_RequestMaximumTravel.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestOutputVoltage = self.lib.PBC_RequestOutputVoltage
        self.PBC_RequestOutputVoltage.restype = c_bool
        self.PBC_RequestOutputVoltage.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestPosition = self.lib.PBC_RequestPosition
        self.PBC_RequestPosition.restype = c_short
        self.PBC_RequestPosition.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestPositionControlMode = self.lib.PBC_RequestPositionControlMode
        self.PBC_RequestPositionControlMode.restype = c_bool
        self.PBC_RequestPositionControlMode.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestRackDigitalOutputs = self.lib.PBC_RequestRackDigitalOutputs
        self.PBC_RequestRackDigitalOutputs.restype = c_short
        self.PBC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_RequestRackStatusBits = self.lib.PBC_RequestRackStatusBits
        self.PBC_RequestRackStatusBits.restype = c_short
        self.PBC_RequestRackStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.PBC_RequestSettings = self.lib.PBC_RequestSettings
        self.PBC_RequestSettings.restype = c_short
        self.PBC_RequestSettings.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestStatus = self.lib.PBC_RequestStatus
        self.PBC_RequestStatus.restype = c_short
        self.PBC_RequestStatus.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestStatusBits = self.lib.PBC_RequestStatusBits
        self.PBC_RequestStatusBits.restype = c_short
        self.PBC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_RequestVoltageSource = self.lib.PBC_RequestVoltageSource
        self.PBC_RequestVoltageSource.restype = c_bool
        self.PBC_RequestVoltageSource.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_ResetParameters = self.lib.PBC_ResetParameters
        self.PBC_ResetParameters.restype = c_short
        self.PBC_ResetParameters.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_SetFeedbackLoopPIconsts = self.lib.PBC_SetFeedbackLoopPIconsts
        self.PBC_SetFeedbackLoopPIconsts.restype = c_short
        self.PBC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short, c_short]
        # *serialNo, channel, integralTerm, proportionalTerm

        self.PBC_SetFeedbackLoopPIconstsBlock = self.lib.PBC_SetFeedbackLoopPIconstsBlock
        self.PBC_SetFeedbackLoopPIconstsBlock.restype = c_short
        self.PBC_SetFeedbackLoopPIconstsBlock.argtypes = [PZ_FeedbackLoopConstants, POINTER(c_char), c_short]
        # *proportionalAndIntegralConstants, *serialNo, channel

        self.PBC_SetLUTwaveParams = self.lib.PBC_SetLUTwaveParams
        self.PBC_SetLUTwaveParams.restype = c_short
        self.PBC_SetLUTwaveParams.argtypes = [PZ_LUTWaveParameters, POINTER(c_char), c_short]
        # *LUTwaveParams, *serialNo, channel

        self.PBC_SetLUTwaveSample = self.lib.PBC_SetLUTwaveSample
        self.PBC_SetLUTwaveSample.restype = c_short
        self.PBC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_short, c_long]
        # *serialNo, channel, index, value

        self.PBC_SetMaxOutputVoltage = self.lib.PBC_SetMaxOutputVoltage
        self.PBC_SetMaxOutputVoltage.restype = c_short
        self.PBC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short, c_short]
        # *serialNo, channel, maxVoltage

        self.PBC_SetOutputVoltage = self.lib.PBC_SetOutputVoltage
        self.PBC_SetOutputVoltage.restype = c_short
        self.PBC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short, c_short]
        # *serialNo, channel, volts

        self.PBC_SetPosition = self.lib.PBC_SetPosition
        self.PBC_SetPosition.restype = c_short
        self.PBC_SetPosition.argtypes = [POINTER(c_char), c_short, c_short]
        # *serialNo, channel, position

        self.PBC_SetPositionControlMode = self.lib.PBC_SetPositionControlMode
        self.PBC_SetPositionControlMode.restype = c_short
        self.PBC_SetPositionControlMode.argtypes = [POINTER(c_char), c_short, PZ_ControlModeTypes]
        # *serialNo, channel, mode

        self.PBC_SetPositionToTolerance = self.lib.PBC_SetPositionToTolerance
        self.PBC_SetPositionToTolerance.restype = c_short
        self.PBC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_short, c_short, c_short]
        # *serialNo, channel, position, tolerance

        self.PBC_SetRackDigitalOutputs = self.lib.PBC_SetRackDigitalOutputs
        self.PBC_SetRackDigitalOutputs.restype = c_short
        self.PBC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]
        # *serialNo, outputsBits

        self.PBC_SetVoltageSource = self.lib.PBC_SetVoltageSource
        self.PBC_SetVoltageSource.restype = c_short
        self.PBC_SetVoltageSource.argtypes = [POINTER(c_char), c_short, PZ_InputSourceFlags]
        # *serialNo, channel, source

        self.PBC_SetZero = self.lib.PBC_SetZero
        self.PBC_SetZero.restype = c_short
        self.PBC_SetZero.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_StartLUTwave = self.lib.PBC_StartLUTwave
        self.PBC_StartLUTwave.restype = c_short
        self.PBC_StartLUTwave.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_StartPolling = self.lib.PBC_StartPolling
        self.PBC_StartPolling.restype = c_bool
        self.PBC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]
        # *serialNo, channel, milliseconds

        self.PBC_StopLUTwave = self.lib.PBC_StopLUTwave
        self.PBC_StopLUTwave.restype = c_short
        self.PBC_StopLUTwave.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_StopPolling = self.lib.PBC_StopPolling
        self.PBC_StopPolling.restype = None
        self.PBC_StopPolling.argtypes = [POINTER(c_char), c_short]
        # *serialNo, channel

        self.PBC_TimeSinceLastMsgReceived = self.lib.PBC_TimeSinceLastMsgReceived
        self.PBC_TimeSinceLastMsgReceived.restype = c_bool
        self.PBC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char), c_short]
        # &lastUpdateTimeMS, *serialNo, channel

        self.PBC_WaitForMessage = self.lib.PBC_WaitForMessage
        self.PBC_WaitForMessage.restype = c_bool
        self.PBC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char), c_short]
        # *messageData, *messageID, *messageType, *serialNo, channel

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
