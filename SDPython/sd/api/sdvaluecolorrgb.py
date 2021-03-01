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

class SDValueColorRGB(SDValueVector):
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDValueColorRGB
        """
        SDValueVector.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sNew(value):
        """
        Create new SDValueColorRGB

        :param value: The name of the enum type
        :type value: ColorRGB
        :rtype: SDValueColorRGB
        """
        outSDValueColorRGB = ctypes.c_void_p()
        _res = sd.getContext().SDValueColorRGB_sNew(ctypes.byref(value), ctypes.byref(outSDValueColorRGB))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outSDValueColorRGB, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outSDValueColorRGB.value, ownHandle=True)

    def get(self):
        """
        Get the base type value as ColorRGB

        :rtype: ColorRGB
        """
        outValue = ColorRGB()
        _res = self.mAPIContext.SDValueColorRGB_get(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue

