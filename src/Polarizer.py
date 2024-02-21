from c_types import (POINTER, c_bool, c_char, c_double, c_int, c_int32, c_int64, c_long, c_short, c_ulong, cdll)
from .safearray import SafeArray
from .definitions.enumerations import (MOT_TravelDirection, POL_PaddleBits, POL_Paddles, PolarizerParameters)
from .definitions.structures import (TLI_DeviceInfo)
from pathlib import Path


class Polarizer(object):

    def __init__(self, lib_path="C:/Program Files/Thorlabs/Kinesis/"):
        self.lib_path = Path(lib_path)

        self.device_manager = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

        self.lib = cdll.LoadLibrary(
            self.lib_path + "Thorlabs.MotionControl.Polarizer.DLL")

        self.MPC_CheckConnection = self.lib.MPC_CheckConnection
        self.MPC_CheckConnection.restype = c_bool
        self.MPC_CheckConnection.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_ClearMessageQueue = self.lib.MPC_ClearMessageQueue
        self.MPC_ClearMessageQueue.restype = None
        self.MPC_ClearMessageQueue.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_Close = self.lib.MPC_Close
        self.MPC_Close.restype = None
        self.MPC_Close.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_EnableLastMsgTimer = self.lib.MPC_EnableLastMsgTimer
        self.MPC_EnableLastMsgTimer.restype = None
        self.MPC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]
        # *serialNo, enable, lastMsgTimeout

        self.MPC_GetEnabledPaddles = self.lib.MPC_GetEnabledPaddles
        self.MPC_GetEnabledPaddles.restype = POL_PaddleBits
        self.MPC_GetEnabledPaddles.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_GetFirmwareVersion = self.lib.MPC_GetFirmwareVersion
        self.MPC_GetFirmwareVersion.restype = c_ulong
        self.MPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_GetHardwareInfo = self.lib.MPC_GetHardwareInfo
        self.MPC_GetHardwareInfo.restype = c_short
        self.MPC_GetHardwareInfo.argtypes = [
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
        # *firmwareVersion, *hardwareVersion, *modelNo, *modificationState, *notes, *numchannels, *serialNo, *type, sizeOfModelNo, sizeOfNotes

        self.MPC_GetHomeOffset = self.lib.MPC_GetHomeOffset
        self.MPC_GetHomeOffset.restype = c_double
        self.MPC_GetHomeOffset.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_GetJogSize = self.lib.MPC_GetJogSize
        self.MPC_GetJogSize.restype = c_double
        self.MPC_GetJogSize.argtypes = [POINTER(c_char), POL_Paddles]
        # *serialNo, paddle

        self.MPC_GetMaxTravel = self.lib.MPC_GetMaxTravel
        self.MPC_GetMaxTravel.restype = c_double
        self.MPC_GetMaxTravel.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_GetNextMessage = self.lib.MPC_GetNextMessage
        self.MPC_GetNextMessage.restype = c_bool
        self.MPC_GetNextMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
        # *messageData, *messageID, *messageType, *serialNo

        self.MPC_GetPaddleCount = self.lib.MPC_GetPaddleCount
        self.MPC_GetPaddleCount.restype = c_int
        self.MPC_GetPaddleCount.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_GetPolParams = self.lib.MPC_GetPolParams
        self.MPC_GetPolParams.restype = c_short
        self.MPC_GetPolParams.argtypes = [PolarizerParameters, POINTER(c_char)]
        # *polParams, *serialNo

        self.MPC_GetPosition = self.lib.MPC_GetPosition
        self.MPC_GetPosition.restype = c_double
        self.MPC_GetPosition.argtypes = [POINTER(c_char), POL_Paddles]
        # *serialNo, paddle

        self.MPC_GetSoftwareVersion = self.lib.MPC_GetSoftwareVersion
        self.MPC_GetSoftwareVersion.restype = c_ulong
        self.MPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_GetStatusBits = self.lib.MPC_GetStatusBits
        self.MPC_GetStatusBits.restype = c_ulong
        self.MPC_GetStatusBits.argtypes = [POINTER(c_char), POL_Paddles]
        # *serialNo, paddle

        self.MPC_GetStepsPerDegree = self.lib.MPC_GetStepsPerDegree
        self.MPC_GetStepsPerDegree.restype = c_double
        self.MPC_GetStepsPerDegree.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_GetVelocity = self.lib.MPC_GetVelocity
        self.MPC_GetVelocity.restype = c_short
        self.MPC_GetVelocity.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_HasLastMsgTimerOverrun = self.lib.MPC_HasLastMsgTimerOverrun
        self.MPC_HasLastMsgTimerOverrun.restype = c_bool
        self.MPC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_Home = self.lib.MPC_Home
        self.MPC_Home.restype = c_short
        self.MPC_Home.argtypes = [POINTER(c_char), POL_Paddles]
        # *serialNo, paddle

        self.MPC_Identify = self.lib.MPC_Identify
        self.MPC_Identify.restype = None
        self.MPC_Identify.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_IsPaddleEnabled = self.lib.MPC_IsPaddleEnabled
        self.MPC_IsPaddleEnabled.restype = c_bool
        self.MPC_IsPaddleEnabled.argtypes = [POINTER(c_char), POL_Paddles]
        # *serialNo, paddle

        self.MPC_Jog = self.lib.MPC_Jog
        self.MPC_Jog.restype = c_short
        self.MPC_Jog.argtypes = [POINTER(c_char), MOT_TravelDirection, POL_Paddles]
        # *serialNo, direction, paddle

        self.MPC_LoadNamedSettings = self.lib.MPC_LoadNamedSettings
        self.MPC_LoadNamedSettings.restype = c_bool
        self.MPC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]
        # *serialNo, *settingsName

        self.MPC_LoadSettings = self.lib.MPC_LoadSettings
        self.MPC_LoadSettings.restype = c_bool
        self.MPC_LoadSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_MessageQueueSize = self.lib.MPC_MessageQueueSize
        self.MPC_MessageQueueSize.restype = c_int
        self.MPC_MessageQueueSize.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_MoveRelative = self.lib.MPC_MoveRelative
        self.MPC_MoveRelative.restype = c_short
        self.MPC_MoveRelative.argtypes = [POINTER(c_char), POL_Paddles, c_double]
        # *serialNo, paddle, position

        self.MPC_MoveToPosition = self.lib.MPC_MoveToPosition
        self.MPC_MoveToPosition.restype = c_short
        self.MPC_MoveToPosition.argtypes = [POINTER(c_char), POL_Paddles, c_double]
        # *serialNo, paddle, position

        self.MPC_Open = self.lib.MPC_Open
        self.MPC_Open.restype = c_short
        self.MPC_Open.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_PersistSettings = self.lib.MPC_PersistSettings
        self.MPC_PersistSettings.restype = c_bool
        self.MPC_PersistSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_PollingDuration = self.lib.MPC_PollingDuration
        self.MPC_PollingDuration.restype = c_long
        self.MPC_PollingDuration.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_RegisterMessageCallback = self.lib.MPC_RegisterMessageCallback
        self.MPC_RegisterMessageCallback.restype = None
        self.MPC_RegisterMessageCallback.argtypes = [POINTER(c_char), None]
        # *serialNo, void

        self.MPC_RequestPolParams = self.lib.MPC_RequestPolParams
        self.MPC_RequestPolParams.restype = c_short
        self.MPC_RequestPolParams.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_RequestSettings = self.lib.MPC_RequestSettings
        self.MPC_RequestSettings.restype = c_short
        self.MPC_RequestSettings.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_RequestStatus = self.lib.MPC_RequestStatus
        self.MPC_RequestStatus.restype = c_short
        self.MPC_RequestStatus.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_ResetParameters = self.lib.MPC_ResetParameters
        self.MPC_ResetParameters.restype = c_bool
        self.MPC_ResetParameters.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_SetEnabledPaddles = self.lib.MPC_SetEnabledPaddles
        self.MPC_SetEnabledPaddles.restype = c_int
        self.MPC_SetEnabledPaddles.argtypes = [POINTER(c_char), POL_PaddleBits]
        # *serialNo, paddles

        self.MPC_SetHomeOffset = self.lib.MPC_SetHomeOffset
        self.MPC_SetHomeOffset.restype = c_short
        self.MPC_SetHomeOffset.argtypes = [POINTER(c_char), c_double]
        # *serialNo, homeOffset

        self.MPC_SetJogSize = self.lib.MPC_SetJogSize
        self.MPC_SetJogSize.restype = c_short
        self.MPC_SetJogSize.argtypes = [POINTER(c_char), c_double, POL_Paddles]
        # *serialNo, jogSize, paddle

        self.MPC_SetPolParams = self.lib.MPC_SetPolParams
        self.MPC_SetPolParams.restype = c_short
        self.MPC_SetPolParams.argtypes = [PolarizerParameters, POINTER(c_char)]
        # *polParams, *serialNo

        self.MPC_SetVelocity = self.lib.MPC_SetVelocity
        self.MPC_SetVelocity.restype = c_short
        self.MPC_SetVelocity.argtypes = [POINTER(c_char), c_short]
        # *serialNo, velocity

        self.MPC_StartPolling = self.lib.MPC_StartPolling
        self.MPC_StartPolling.restype = c_bool
        self.MPC_StartPolling.argtypes = [POINTER(c_char), c_int]
        # *serialNo, milliseconds

        self.MPC_Stop = self.lib.MPC_Stop
        self.MPC_Stop.restype = c_short
        self.MPC_Stop.argtypes = [POINTER(c_char), POL_Paddles]
        # *serialNo, paddle

        self.MPC_StopPolling = self.lib.MPC_StopPolling
        self.MPC_StopPolling.restype = None
        self.MPC_StopPolling.argtypes = [POINTER(c_char)]
        # *serialNo

        self.MPC_TimeSinceLastMsgReceived = self.lib.MPC_TimeSinceLastMsgReceived
        self.MPC_TimeSinceLastMsgReceived.restype = c_bool
        self.MPC_TimeSinceLastMsgReceived.argtypes = [c_int64, POINTER(c_char)]
        # &lastUpdateTimeMS, *serialNo

        self.MPC_WaitForMessage = self.lib.MPC_WaitForMessage
        self.MPC_WaitForMessage.restype = c_bool
        self.MPC_WaitForMessage.argtypes = [c_ulong, c_long, c_long, POINTER(c_char)]
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
