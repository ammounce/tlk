from c_types import (POINTER, c_bool, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (
    TIM_ButtonParameters,
    TIM_ButtonsMode,
    TIM_Channels,
    TIM_Direction,
    TIM_DriveOPParameters,
    TIM_JogMode,
    TIM_JogParameters)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation)
from pathlib import Path


class TCubeInertialMotor(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.TCube.InertialMotor.DLL")

        self.TIM_CheckConnection = self.lib.TIM_CheckConnection
        self.TIM_CheckConnection.restype = c_bool
        self.TIM_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_ClearMessageQueue = self.lib.TIM_ClearMessageQueue
        self.TIM_ClearMessageQueue.restype = None
        self.TIM_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_Close = self.lib.TIM_Close
        self.TIM_Close.restype = None
        self.TIM_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_Disable = self.lib.TIM_Disable
        self.TIM_Disable.restype = c_short
        self.TIM_Disable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_Disconnect = self.lib.TIM_Disconnect
        self.TIM_Disconnect.restype = c_short
        self.TIM_Disconnect.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_Enable = self.lib.TIM_Enable
        self.TIM_Enable.restype = c_short
        self.TIM_Enable.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_EnableLastMsgTimer = self.lib.TIM_EnableLastMsgTimer
        self.TIM_EnableLastMsgTimer.restype = None
        self.TIM_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.TIM_GetButtonParameters = self.lib.TIM_GetButtonParameters
        self.TIM_GetButtonParameters.restype = c_short
        self.TIM_GetButtonParameters.argtypes = [TIM_ButtonsMode, c_int32, c_int32, POINTER(c_char), TIM_Channels]
        # &buttonMode, &position1, &position2, *serialNo, channel

        self.TIM_GetButtonParametersStruct = self.lib.TIM_GetButtonParametersStruct
        self.TIM_GetButtonParametersStruct.restype = c_short
        self.TIM_GetButtonParametersStruct.argtypes = [TIM_ButtonParameters, POINTER(c_char), TIM_Channels]
        # &buttonParameters, *serialNo, channel

        self.TIM_GetCurrentPosition = self.lib.TIM_GetCurrentPosition
        self.TIM_GetCurrentPosition.restype = c_int32
        self.TIM_GetCurrentPosition.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_GetDriveOPParameters = self.lib.TIM_GetDriveOPParameters
        self.TIM_GetDriveOPParameters.restype = c_short
        self.TIM_GetDriveOPParameters.argtypes = [c_int16, c_int32, c_int32, POINTER(c_char), TIM_Channels]
        # &maxVoltage, &stepAcceleration, &stepRate, *serialNo, channel

        self.TIM_GetDriveOPParametersStruct = self.lib.TIM_GetDriveOPParametersStruct
        self.TIM_GetDriveOPParametersStruct.restype = c_short
        self.TIM_GetDriveOPParametersStruct.argtypes = [TIM_DriveOPParameters, POINTER(c_char), TIM_Channels]
        # &driveOPParameters, *serialNo, channel

        self.TIM_GetFirmwareVersion = self.lib.TIM_GetFirmwareVersion
        self.TIM_GetFirmwareVersion.restype = c_ulong
        self.TIM_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_GetHardwareInfo = self.lib.TIM_GetHardwareInfo
        self.TIM_GetHardwareInfo.restype = c_short
        self.TIM_GetHardwareInfo.argtypes = [
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

        self.TIM_GetHardwareInfoBlock = self.lib.TIM_GetHardwareInfoBlock
        self.TIM_GetHardwareInfoBlock.restype = c_short
        self.TIM_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
        # *hardwareInfo, *serialNo

        self.TIM_GetJogParameters = self.lib.TIM_GetJogParameters
        self.TIM_GetJogParameters.restype = c_short
        self.TIM_GetJogParameters.argtypes = [TIM_JogMode, c_int32, c_int32, c_int32, POINTER(c_char), TIM_Channels]
        # &jogMode, &jogStepAcceleration, &jogStepRate, &jogStepSize, *serialNo, channel

        self.TIM_GetJogParametersStruct = self.lib.TIM_GetJogParametersStruct
        self.TIM_GetJogParametersStruct.restype = c_short
        self.TIM_GetJogParametersStruct.argtypes = [TIM_JogParameters, POINTER(c_char), TIM_Channels]
        # &jogParameters, *serialNo, channel

        self.TIM_GetLEDBrightness = self.lib.TIM_GetLEDBrightness
        self.TIM_GetLEDBrightness.restype = c_short
        self.TIM_GetLEDBrightness.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_GetMaxPotStepRate = self.lib.TIM_GetMaxPotStepRate
        self.TIM_GetMaxPotStepRate.restype = c_int32
        self.TIM_GetMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_GetNextMessage = self.lib.TIM_GetNextMessage
        self.TIM_GetNextMessage.restype = c_bool
        self.TIM_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.TIM_GetSoftwareVersion = self.lib.TIM_GetSoftwareVersion
        self.TIM_GetSoftwareVersion.restype = c_ulong
        self.TIM_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_GetStatusBits = self.lib.TIM_GetStatusBits
        self.TIM_GetStatusBits.restype = c_ulong
        self.TIM_GetStatusBits.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_HasLastMsgTimerOverrun = self.lib.TIM_HasLastMsgTimerOverrun
        self.TIM_HasLastMsgTimerOverrun.restype = c_bool
        self.TIM_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_Home = self.lib.TIM_Home
        self.TIM_Home.restype = c_short
        self.TIM_Home.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_Identify = self.lib.TIM_Identify
        self.TIM_Identify.restype = None
        self.TIM_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_LoadNamedSettings = self.lib.TIM_LoadNamedSettings
        self.TIM_LoadNamedSettings.restype = c_bool
        self.TIM_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.TIM_LoadSettings = self.lib.TIM_LoadSettings
        self.TIM_LoadSettings.restype = c_bool
        self.TIM_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_MessageQueueSize = self.lib.TIM_MessageQueueSize
        self.TIM_MessageQueueSize.restype = c_int
        self.TIM_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_MoveAbsolute = self.lib.TIM_MoveAbsolute
        self.TIM_MoveAbsolute.restype = c_short
        self.TIM_MoveAbsolute.argtypes = [POINTER(c_char), TIM_Channels, c_int32]
        # *serialNo, channel, position

        self.TIM_MoveJog = self.lib.TIM_MoveJog
        self.TIM_MoveJog.restype = c_short
        self.TIM_MoveJog.argtypes = [POINTER(c_char), TIM_Channels, TIM_Direction]
        # *serialNo, channel, jogDirection

        self.TIM_MoveStop = self.lib.TIM_MoveStop
        self.TIM_MoveStop.restype = c_short
        self.TIM_MoveStop.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_Open = self.lib.TIM_Open
        self.TIM_Open.restype = c_short
        self.TIM_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_PersistSettings = self.lib.TIM_PersistSettings
        self.TIM_PersistSettings.restype = c_bool
        self.TIM_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_PollingDuration = self.lib.TIM_PollingDuration
        self.TIM_PollingDuration.restype = c_long
        self.TIM_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_RegisterMessageCallback = self.lib.TIM_RegisterMessageCallback
        self.TIM_RegisterMessageCallback.restype = None
        self.TIM_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.TIM_RequestButtonParameters = self.lib.TIM_RequestButtonParameters
        self.TIM_RequestButtonParameters.restype = c_short
        self.TIM_RequestButtonParameters.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_RequestCurrentPosition = self.lib.TIM_RequestCurrentPosition
        self.TIM_RequestCurrentPosition.restype = c_short
        self.TIM_RequestCurrentPosition.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_RequestDriveOPParameters = self.lib.TIM_RequestDriveOPParameters
        self.TIM_RequestDriveOPParameters.restype = c_short
        self.TIM_RequestDriveOPParameters.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_RequestJogParameters = self.lib.TIM_RequestJogParameters
        self.TIM_RequestJogParameters.restype = c_short
        self.TIM_RequestJogParameters.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_RequestMaxPotStepRate = self.lib.TIM_RequestMaxPotStepRate
        self.TIM_RequestMaxPotStepRate.restype = c_short
        self.TIM_RequestMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels]
        # *serialNo, channel

        self.TIM_RequestSettings = self.lib.TIM_RequestSettings
        self.TIM_RequestSettings.restype = c_short
        self.TIM_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_RequestStatus = self.lib.TIM_RequestStatus
        self.TIM_RequestStatus.restype = c_short
        self.TIM_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_RequestStatusBits = self.lib.TIM_RequestStatusBits
        self.TIM_RequestStatusBits.restype = c_short
        self.TIM_RequestStatusBits.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_Reset = self.lib.TIM_Reset
        self.TIM_Reset.restype = c_short
        self.TIM_Reset.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_SetButtonParameters = self.lib.TIM_SetButtonParameters
        self.TIM_SetButtonParameters.restype = c_short
        self.TIM_SetButtonParameters.argtypes = [POINTER(c_char), TIM_ButtonsMode, TIM_Channels, c_int32, c_int32]
        # *serialNo, buttonMode, channel, position1, position2

        self.TIM_SetButtonParametersStruct = self.lib.TIM_SetButtonParametersStruct
        self.TIM_SetButtonParametersStruct.restype = c_short
        self.TIM_SetButtonParametersStruct.argtypes = [TIM_ButtonParameters, POINTER(c_char), TIM_Channels]
        # &buttonParameters, *serialNo, channel

        self.TIM_SetDriveOPParameters = self.lib.TIM_SetDriveOPParameters
        self.TIM_SetDriveOPParameters.restype = c_short
        self.TIM_SetDriveOPParameters.argtypes = [POINTER(c_char), TIM_Channels, c_int16, c_int32, c_int32]
        # *serialNo, channel, maxVoltage, stepAcceleration, stepRate

        self.TIM_SetDriveOPParametersStruct = self.lib.TIM_SetDriveOPParametersStruct
        self.TIM_SetDriveOPParametersStruct.restype = c_short
        self.TIM_SetDriveOPParametersStruct.argtypes = [TIM_DriveOPParameters, POINTER(c_char), TIM_Channels]
        # &driveOPParameters, *serialNo, channel

        self.TIM_SetJogParameters = self.lib.TIM_SetJogParameters
        self.TIM_SetJogParameters.restype = c_short
        self.TIM_SetJogParameters.argtypes = [POINTER(c_char), TIM_Channels, TIM_JogMode, c_int32, c_int32, c_int32]
        # *serialNo, channel, jogMode, jogStepAcceleration, jogStepRate, jogStepSize

        self.TIM_SetJogParametersStruct = self.lib.TIM_SetJogParametersStruct
        self.TIM_SetJogParametersStruct.restype = c_short
        self.TIM_SetJogParametersStruct.argtypes = [TIM_JogParameters, POINTER(c_char), TIM_Channels]
        # &jogParameters, *serialNo, channel

        self.TIM_SetLEDBrightness = self.lib.TIM_SetLEDBrightness
        self.TIM_SetLEDBrightness.restype = c_short
        self.TIM_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
        # *serialNo, brightness

        self.TIM_SetMaxPotStepRate = self.lib.TIM_SetMaxPotStepRate
        self.TIM_SetMaxPotStepRate.restype = c_short
        self.TIM_SetMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels, c_int32]
        # *serialNo, channel, maxPotStepRate

        self.TIM_SetPosition = self.lib.TIM_SetPosition
        self.TIM_SetPosition.restype = c_short
        self.TIM_SetPosition.argtypes = [POINTER(c_char), TIM_Channels, c_long]
        # *serialNo, channel, position

        self.TIM_StartPolling = self.lib.TIM_StartPolling
        self.TIM_StartPolling.restype = c_bool
        self.TIM_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.TIM_StopPolling = self.lib.TIM_StopPolling
        self.TIM_StopPolling.restype = None
        self.TIM_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.TIM_TimeSinceLastMsgReceived = self.lib.TIM_TimeSinceLastMsgReceived
        self.TIM_TimeSinceLastMsgReceived.restype = c_bool
        self.TIM_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.TIM_WaitForMessage = self.lib.TIM_WaitForMessage
        self.TIM_WaitForMessage.restype = c_bool
        self.TIM_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
