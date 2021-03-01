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
from .sdapiobject import SDAPIObject
from .sdapiobject import SDApiError
from .apiexception import APIException

class SDUsage(SDAPIObject):
    """
    Description of an input or output usage
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDUsage
        """
        SDAPIObject.__init__(self, APIContext, handle, *args, **kwargs)

    def getName(self):
        """
        Get the usage name

        :rtype: string
        """
        outValue = ctypes.c_char_p()
        _res = self.mAPIContext.SDUsage_getName(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value.decode('utf-8')

    def getComponents(self):
        """
        Get the components associated to the current usage (R, G, B, A, RGB or RGBA)

        :rtype: string
        """
        outValue = ctypes.c_char_p()
        _res = self.mAPIContext.SDUsage_getComponents(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value.decode('utf-8')

    def getColorSpace(self):
        """
        Get the color space associated to the current usage (sRGB, linear, ...)

        :rtype: string
        """
        outValue = ctypes.c_char_p()
        _res = self.mAPIContext.SDUsage_getColorSpace(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value.decode('utf-8')

    @staticmethod
    def sNew(name, components, colorSpace):
        """
        Create a new SDUsage

        :param name: The name of the usage
        :type name: string
        :param components: The components of the usage
        :type components: string
        :param colorSpace: The color space of the usage
        :type colorSpace: string
        :rtype: SDUsage
        """
        outSDUsage = ctypes.c_void_p()
        _res = sd.getContext().SDUsage_sNew(ctypes.create_string_buffer(name.encode('utf-8')), ctypes.create_string_buffer(components.encode('utf-8')), ctypes.create_string_buffer(colorSpace.encode('utf-8')), ctypes.byref(outSDUsage))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outSDUsage, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outSDUsage.value, ownHandle=True)

