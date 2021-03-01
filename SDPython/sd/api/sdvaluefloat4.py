# ADOBE CONFIDENTIAL
#
# Copyright 2020 Adobe
# All Rights Reserved.
#
# NOTICE:  Adobe permits you to use, modify, and distribute this file in
# accordance with the terms of the Adobe license agreement accompanying it.
# If you have received this file from a source other than Adobe,
# then your use, modification, or distribution of it requires the prior
# written permission of Adobe.
#
# Autogenerated by ipa. Don't edit directly, edit the definitions and regenerate it when changing
#

import ctypes
import base64
import sd
from .sdvaluevector import *
from .sdapiobject import *
from .sdbasetypes import *
from .sdapiobject import *
from .apiexception import APIException

class SDValueFloat4(SDValueVector):
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDValueFloat4
        """
        SDValueVector.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sNew(value):
        """
        Create new SDValueFloat4

        :param value: The name of the enum type
        :type value: float4
        :rtype: SDValueFloat4
        """
        outSDValueFloat4 = ctypes.c_void_p()
        _res = sd.getContext().SDValueFloat4_sNew(ctypes.byref(value), ctypes.byref(outSDValueFloat4))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outSDValueFloat4, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outSDValueFloat4.value, ownHandle=True)

    def get(self):
        """
        Get the base type value as float4

        :rtype: float4
        """
        outValue = float4()
        _res = self.mAPIContext.SDValueFloat4_get(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue

