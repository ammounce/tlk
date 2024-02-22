from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_uint, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (SC_OperatingModes, SC_OperatingStates)
from .definitions.structures import (SC_CycleParameters, TLI_DeviceInfo, TLI_HardwareInformation)
from pathlib import Path


lib_path = Path("C:/Program Files/Thorlabs/Kinesis/")
device_manager = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path / "Thorlabs.MotionControl.TCube.Solenoid.DLL")
SC_CheckConnection = lib.SC_CheckConnection
SC_CheckConnection.restype = c_bool
SC_CheckConnection.argtypes = [POINTER(c_char)]
# *serialNo

SC_ClearMessageQueue = lib.SC_ClearMessageQueue
SC_ClearMessageQueue.restype = None
SC_ClearMessageQueue.argtypes = [POINTER(c_char)]
# *serialNo

SC_Close = lib.SC_Close
SC_Close.restype = None
SC_Close.argtypes = [POINTER(c_char)]
# *serialNo

SC_EnableLastMsgTimer = lib.SC_EnableLastMsgTimer
SC_EnableLastMsgTimer.restype = None
SC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
# *serialNo, enable, lastMsgTimeout

SC_GetCycleParams = lib.SC_GetCycleParams
SC_GetCycleParams.restype = c_short
SC_GetCycleParams.argtypes = [c_uint, c_uint, c_uint, c_uint, c_uint, POINTER(c_char)]
# *numCycles, *offTime, *onTime, *pClosedTime, *pOpenTime, *serialNo

SC_GetCycleParamsBlock = lib.SC_GetCycleParamsBlock
SC_GetCycleParamsBlock.restype = c_short
SC_GetCycleParamsBlock.argtypes = [SC_CycleParameters, POINTER(c_char)]
# *cycleParams, *serialNo

SC_GetHardwareInfo = lib.SC_GetHardwareInfo
SC_GetHardwareInfo.restype = c_short
SC_GetHardwareInfo.argtypes = [
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

SC_GetHardwareInfoBlock = lib.SC_GetHardwareInfoBlock
SC_GetHardwareInfoBlock.restype = c_short
SC_GetHardwareInfoBlock.argtypes = [TLI_HardwareInformation, POINTER(c_char)]
# *hardwareInfo, *serialNo

SC_GetHubBay = lib.SC_GetHubBay
SC_GetHubBay.restype = POINTER(c_char)
SC_GetHubBay.argtypes = [POINTER(c_char)]
# *serialNo

SC_GetLEDswitches = lib.SC_GetLEDswitches
SC_GetLEDswitches.restype = c_long
SC_GetLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

SC_GetNextMessage = lib.SC_GetNextMessage
SC_GetNextMessage.restype = c_bool
SC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

SC_GetOperatingMode = lib.SC_GetOperatingMode
SC_GetOperatingMode.restype = SC_OperatingModes
SC_GetOperatingMode.argtypes = [POINTER(c_char)]
# *serialNo

SC_GetOperatingState = lib.SC_GetOperatingState
SC_GetOperatingState.restype = SC_OperatingStates
SC_GetOperatingState.argtypes = [POINTER(c_char)]
# *serialNo

SC_GetSoftwareVersion = lib.SC_GetSoftwareVersion
SC_GetSoftwareVersion.restype = c_ulong
SC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
# *serialNo

SC_GetSolenoidState = lib.SC_GetSolenoidState
SC_GetSolenoidState.restype = SC_SolenoidStates
SC_GetSolenoidState.argtypes = [POINTER(c_char)]
# *serialNo

SC_GetStatusBits = lib.SC_GetStatusBits
SC_GetStatusBits.restype = c_ulong
SC_GetStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

SC_HasLastMsgTimerOverrun = lib.SC_HasLastMsgTimerOverrun
SC_HasLastMsgTimerOverrun.restype = c_bool
SC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
# *serialNo

SC_Identify = lib.SC_Identify
SC_Identify.restype = None
SC_Identify.argtypes = [POINTER(c_char)]
# *serialNo

SC_LoadNamedSettings = lib.SC_LoadNamedSettings
SC_LoadNamedSettings.restype = c_bool
SC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
# *serialNo, *settingsName

SC_LoadSettings = lib.SC_LoadSettings
SC_LoadSettings.restype = c_bool
SC_LoadSettings.argtypes = [POINTER(c_char)]
# *serialNo

SC_MessageQueueSize = lib.SC_MessageQueueSize
SC_MessageQueueSize.restype = c_int
SC_MessageQueueSize.argtypes = [POINTER(c_char)]
# *serialNo

SC_Open = lib.SC_Open
SC_Open.restype = c_short
SC_Open.argtypes = [POINTER(c_char)]
# *serialNo

SC_PersistSettings = lib.SC_PersistSettings
SC_PersistSettings.restype = c_bool
SC_PersistSettings.argtypes = [POINTER(c_char)]
# *serialNo

SC_PollingDuration = lib.SC_PollingDuration
SC_PollingDuration.restype = c_long
SC_PollingDuration.argtypes = [POINTER(c_char)]
# *serialNo

SC_RegisterMessageCallback = lib.SC_RegisterMessageCallback
SC_RegisterMessageCallback.restype = None
SC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
# *serialNo, void

SC_RequestCycleParams = lib.SC_RequestCycleParams
SC_RequestCycleParams.restype = c_short
SC_RequestCycleParams.argtypes = [POINTER(c_char)]
# *serialNo

SC_RequestHubBay = lib.SC_RequestHubBay
SC_RequestHubBay.restype = c_short
SC_RequestHubBay.argtypes = [POINTER(c_char)]
# *serialNo

SC_RequestLEDswitches = lib.SC_RequestLEDswitches
SC_RequestLEDswitches.restype = c_short
SC_RequestLEDswitches.argtypes = [POINTER(c_char)]
# *serialNo

SC_RequestOperatingMode = lib.SC_RequestOperatingMode
SC_RequestOperatingMode.restype = c_short
SC_RequestOperatingMode.argtypes = [POINTER(c_char)]
# *serialNo

SC_RequestOperatingState = lib.SC_RequestOperatingState
SC_RequestOperatingState.restype = c_short
SC_RequestOperatingState.argtypes = [POINTER(c_char)]
# *serialNo

SC_RequestSettings = lib.SC_RequestSettings
SC_RequestSettings.restype = c_short
SC_RequestSettings.argtypes = [POINTER(c_char)]
# *serialNo

SC_RequestStatus = lib.SC_RequestStatus
SC_RequestStatus.restype = c_short
SC_RequestStatus.argtypes = [POINTER(c_char)]
# *serialNo

SC_RequestStatusBits = lib.SC_RequestStatusBits
SC_RequestStatusBits.restype = c_short
SC_RequestStatusBits.argtypes = [POINTER(c_char)]
# *serialNo

SC_SetCycleParams = lib.SC_SetCycleParams
SC_SetCycleParams.restype = c_short
SC_SetCycleParams.argtypes = [POINTER(c_char), c_uint, c_uint, c_uint, c_uint, c_uint]
# *serialNo, closedTime, numCycles, offTime, onTime, openTime

SC_SetCycleParamsBlock = lib.SC_SetCycleParamsBlock
SC_SetCycleParamsBlock.restype = c_short
SC_SetCycleParamsBlock.argtypes = [SC_CycleParameters, POINTER(c_char)]
# *cycleParams, *serialNo

SC_SetLEDswitches = lib.SC_SetLEDswitches
SC_SetLEDswitches.restype = c_short
SC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]
# *serialNo, LEDswitches

SC_SetOperatingMode = lib.SC_SetOperatingMode
SC_SetOperatingMode.restype = c_short
SC_SetOperatingMode.argtypes = [POINTER(c_char), SC_OperatingModes]
# *serialNo, mode

SC_SetOperatingState = lib.SC_SetOperatingState
SC_SetOperatingState.restype = c_short
SC_SetOperatingState.argtypes = [POINTER(c_char), SC_OperatingStates]
# *serialNo, state

SC_StartPolling = lib.SC_StartPolling
SC_StartPolling.restype = c_bool
SC_StartPolling.argtypes = [POINTER(c_char), c_int]
# *serialNo, milliseconds

SC_StopPolling = lib.SC_StopPolling
SC_StopPolling.restype = None
SC_StopPolling.argtypes = [POINTER(c_char)]
# *serialNo

SC_TimeSinceLastMsgReceived = lib.SC_TimeSinceLastMsgReceived
SC_TimeSinceLastMsgReceived.restype = c_bool
SC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
# &lastUpdateTimeMS, *serialNo

SC_WaitForMessage = lib.SC_WaitForMessage
SC_WaitForMessage.restype = c_bool
SC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
# *messageData, *messageID, *messageType, *serialNo

TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = [None, None]
# , void

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
TLI_GetDeviceListSize.argtypes = [None]
#

TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = None
TLI_InitializeSimulations.argtypes = [None]
#
