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

class SDValueDouble4(SDValueVector):
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDValueDouble4
        """
        SDValueVector.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sNew(value):
        """
        Create new SDValueDouble4

        :param value: The name of the enum type
        :type value: double4
        :rtype: SDValueDouble4
        """
        outSDValueDouble4 = ctypes.c_void_p()
        _res = sd.getContext().SDValueDouble4_sNew(ctypes.byref(value), ctypes.byref(outSDValueDouble4))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outSDValueDouble4, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outSDValueDouble4.value, ownHandle=True)

    def get(self):
        """
        Get the base type value as double4

        :rtype: double4
        """
        outValue = double4()
        _res = self.mAPIContext.SDValueDouble4_get(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue

