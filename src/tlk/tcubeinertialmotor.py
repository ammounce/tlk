from ctypes import (POINTER, c_bool, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    TIM_ButtonParameters,
    TIM_ButtonsMode,
    TIM_Channels,
    TIM_Direction,
    TIM_DriveOPParameters,
    TIM_JogMode,
    TIM_JogParameters)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.InertialMotor.DLL")

TIM_CheckConnection = lib.TIM_CheckConnection
TIM_CheckConnection.restype = c_bool
TIM_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

TIM_ClearMessageQueue = lib.TIM_ClearMessageQueue
TIM_ClearMessageQueue.restype = c_void_p
TIM_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

TIM_Close = lib.TIM_Close
TIM_Close.restype = c_void_p
TIM_Close.argtypes = [POINTER(c_char)]
# *serialNo

TIM_Disable = lib.TIM_Disable
TIM_Disable.restype = c_short
TIM_Disable.argtypes = [POINTER(c_char)]
# *serialNo

TIM_Disconnect = lib.TIM_Disconnect
TIM_Disconnect.restype = c_short
TIM_Disconnect.argtypes = [POINTER(c_char)]
# *serialNo

TIM_Enable = lib.TIM_Enable
TIM_Enable.restype = c_short
TIM_Enable.argtypes = [POINTER(c_char)]
# *serialNo

TIM_EnableLastMsgTimer = lib.TIM_EnableLastMsgTimer
TIM_EnableLastMsgTimer.restype = c_void_p
TIM_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

TIM_GetButtonParameters = lib.TIM_GetButtonParameters
TIM_GetButtonParameters.restype = c_short
TIM_GetButtonParameters.argtypes = [TIM_ButtonsMode, c_int32, c_int32, POINTER(c_char), TIM_Channels]
# &buttonMode, &position1, &position2, *serialNo, channel

TIM_GetButtonParametersStruct = lib.TIM_GetButtonParametersStruct
TIM_GetButtonParametersStruct.restype = c_short
TIM_GetButtonParametersStruct.argtypes = [TIM_ButtonParameters, POINTER(c_char), TIM_Channels]
# &buttonParameters, *serialNo, channel

TIM_GetCurrentPosition = lib.TIM_GetCurrentPosition
TIM_GetCurrentPosition.restype = c_int32
TIM_GetCurrentPosition.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_GetDriveOPParameters = lib.TIM_GetDriveOPParameters
TIM_GetDriveOPParameters.restype = c_short
TIM_GetDriveOPParameters.argtypes = [c_int16, c_int32, c_int32, POINTER(c_char), TIM_Channels]
# &maxVoltage, &stepAcceleration, &stepRate, *serialNo, channel

TIM_GetDriveOPParametersStruct = lib.TIM_GetDriveOPParametersStruct
TIM_GetDriveOPParametersStruct.restype = c_short
TIM_GetDriveOPParametersStruct.argtypes = [TIM_DriveOPParameters, POINTER(c_char), TIM_Channels]
# &driveOPParameters, *serialNo, channel

TIM_GetFirmwareVersion = lib.TIM_GetFirmwareVersion
TIM_GetFirmwareVersion.restype = c_ulong
TIM_GetFirmwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

TIM_GetHardwareInfo = lib.TIM_GetHardwareInfo
TIM_GetHardwareInfo.restype = c_short
TIM_GetHardwareInfo.argtypes = [
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

TIM_GetHardwareInfoBlock = lib.TIM_GetHardwareInfoBlock
TIM_GetHardwareInfoBlock.restype = c_short
TIM_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

TIM_GetJogParameters = lib.TIM_GetJogParameters
TIM_GetJogParameters.restype = c_short
TIM_GetJogParameters.argtypes = [TIM_JogMode, c_int32, c_int32, c_int32, POINTER(c_char), TIM_Channels]
# &jogMode, &jogStepAcceleration, &jogStepRate, &jogStepSize, *serialNo, channel

TIM_GetJogParametersStruct = lib.TIM_GetJogParametersStruct
TIM_GetJogParametersStruct.restype = c_short
TIM_GetJogParametersStruct.argtypes = [TIM_JogParameters, POINTER(c_char), TIM_Channels]
# &jogParameters, *serialNo, channel

TIM_GetLEDBrightness = lib.TIM_GetLEDBrightness
TIM_GetLEDBrightness.restype = c_short
TIM_GetLEDBrightness.argtypes = [POINTER(c_char)]
# *serialNo

TIM_GetMaxPotStepRate = lib.TIM_GetMaxPotStepRate
TIM_GetMaxPotStepRate.restype = c_int32
TIM_GetMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_GetNextMessage = lib.TIM_GetNextMessage
TIM_GetNextMessage.restype = c_bool
TIM_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

TIM_GetSoftwareVersion = lib.TIM_GetSoftwareVersion
TIM_GetSoftwareVersion.restype = c_ulong
TIM_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

TIM_GetStatusBits = lib.TIM_GetStatusBits
TIM_GetStatusBits.restype = c_ulong
TIM_GetStatusBits.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_HasLastMsgTimerOverrun = lib.TIM_HasLastMsgTimerOverrun
TIM_HasLastMsgTimerOverrun.restype = c_bool
TIM_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

TIM_Home = lib.TIM_Home
TIM_Home.restype = c_short
TIM_Home.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_Identify = lib.TIM_Identify
TIM_Identify.restype = c_void_p
TIM_Identify.argtypes = [POINTER(c_char)]
# *serialNo

TIM_LoadNamedSettings = lib.TIM_LoadNamedSettings
TIM_LoadNamedSettings.restype = c_bool
TIM_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

TIM_LoadSettings = lib.TIM_LoadSettings
TIM_LoadSettings.restype = c_bool
TIM_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

TIM_MessageQueueSize = lib.TIM_MessageQueueSize
TIM_MessageQueueSize.restype = c_int
TIM_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

TIM_MoveAbsolute = lib.TIM_MoveAbsolute
TIM_MoveAbsolute.restype = c_short
TIM_MoveAbsolute.argtypes = [POINTER(c_char), TIM_Channels, c_int32]
# *serialNo, channel, position

TIM_MoveJog = lib.TIM_MoveJog
TIM_MoveJog.restype = c_short
TIM_MoveJog.argtypes = [POINTER(c_char), TIM_Channels, TIM_Direction]
# *serialNo, channel, jogDirection

TIM_MoveStop = lib.TIM_MoveStop
TIM_MoveStop.restype = c_short
TIM_MoveStop.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_Open = lib.TIM_Open
TIM_Open.restype = c_short
TIM_Open.argtypes = [POINTER(c_char)]
# *serialNo

TIM_PersistSettings = lib.TIM_PersistSettings
TIM_PersistSettings.restype = c_bool
TIM_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

TIM_PollingDuration = lib.TIM_PollingDuration
TIM_PollingDuration.restype = c_long
TIM_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

TIM_RegisterMessageCallback = lib.TIM_RegisterMessageCallback
TIM_RegisterMessageCallback.restype = c_void_p
TIM_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]
# *serialNo, void

TIM_RequestButtonParameters = lib.TIM_RequestButtonParameters
TIM_RequestButtonParameters.restype = c_short
TIM_RequestButtonParameters.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_RequestCurrentPosition = lib.TIM_RequestCurrentPosition
TIM_RequestCurrentPosition.restype = c_short
TIM_RequestCurrentPosition.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_RequestDriveOPParameters = lib.TIM_RequestDriveOPParameters
TIM_RequestDriveOPParameters.restype = c_short
TIM_RequestDriveOPParameters.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_RequestJogParameters = lib.TIM_RequestJogParameters
TIM_RequestJogParameters.restype = c_short
TIM_RequestJogParameters.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_RequestMaxPotStepRate = lib.TIM_RequestMaxPotStepRate
TIM_RequestMaxPotStepRate.restype = c_short
TIM_RequestMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels]
# *serialNo, channel

TIM_RequestSettings = lib.TIM_RequestSettings
TIM_RequestSettings.restype = c_short
TIM_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

TIM_RequestStatus = lib.TIM_RequestStatus
TIM_RequestStatus.restype = c_short
TIM_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

TIM_RequestStatusBits = lib.TIM_RequestStatusBits
TIM_RequestStatusBits.restype = c_short
TIM_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

TIM_Reset = lib.TIM_Reset
TIM_Reset.restype = c_short
TIM_Reset.argtypes = [POINTER(c_char)]
# *serialNo

TIM_SetButtonParameters = lib.TIM_SetButtonParameters
TIM_SetButtonParameters.restype = c_short
TIM_SetButtonParameters.argtypes = [POINTER(c_char), TIM_ButtonsMode, TIM_Channels, c_int32, c_int32]
# *serialNo, buttonMode, channel, position1, position2

TIM_SetButtonParametersStruct = lib.TIM_SetButtonParametersStruct
TIM_SetButtonParametersStruct.restype = c_short
TIM_SetButtonParametersStruct.argtypes = [TIM_ButtonParameters, POINTER(c_char), TIM_Channels]
# &buttonParameters, *serialNo, channel

TIM_SetDriveOPParameters = lib.TIM_SetDriveOPParameters
TIM_SetDriveOPParameters.restype = c_short
TIM_SetDriveOPParameters.argtypes = [POINTER(c_char), TIM_Channels, c_int16, c_int32, c_int32]
# *serialNo, channel, maxVoltage, stepAcceleration, stepRate

TIM_SetDriveOPParametersStruct = lib.TIM_SetDriveOPParametersStruct
TIM_SetDriveOPParametersStruct.restype = c_short
TIM_SetDriveOPParametersStruct.argtypes = [TIM_DriveOPParameters, POINTER(c_char), TIM_Channels]
# &driveOPParameters, *serialNo, channel

TIM_SetJogParameters = lib.TIM_SetJogParameters
TIM_SetJogParameters.restype = c_short
TIM_SetJogParameters.argtypes = [POINTER(c_char), TIM_Channels, TIM_JogMode, c_int32, c_int32, c_int32]
# *serialNo, channel, jogMode, jogStepAcceleration, jogStepRate, jogStepSize

TIM_SetJogParametersStruct = lib.TIM_SetJogParametersStruct
TIM_SetJogParametersStruct.restype = c_short
TIM_SetJogParametersStruct.argtypes = [TIM_JogParameters, POINTER(c_char), TIM_Channels]
# &jogParameters, *serialNo, channel

TIM_SetLEDBrightness = lib.TIM_SetLEDBrightness
TIM_SetLEDBrightness.restype = c_short
TIM_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]
# *serialNo, brightness

TIM_SetMaxPotStepRate = lib.TIM_SetMaxPotStepRate
TIM_SetMaxPotStepRate.restype = c_short
TIM_SetMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels, c_int32]
# *serialNo, channel, maxPotStepRate

TIM_SetPosition = lib.TIM_SetPosition
TIM_SetPosition.restype = c_short
TIM_SetPosition.argtypes = [POINTER(c_char), TIM_Channels, c_long]
# *serialNo, channel, position

TIM_StartPolling = lib.TIM_StartPolling
TIM_StartPolling.restype = c_bool
TIM_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

TIM_StopPolling = lib.TIM_StopPolling
TIM_StopPolling.restype = c_void_p
TIM_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

TIM_TimeSinceLastMsgReceived = lib.TIM_TimeSinceLastMsgReceived
TIM_TimeSinceLastMsgReceived.restype = c_bool
TIM_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

TIM_WaitForMessage = lib.TIM_WaitForMessage
TIM_WaitForMessage.restype = c_bool
TIM_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
