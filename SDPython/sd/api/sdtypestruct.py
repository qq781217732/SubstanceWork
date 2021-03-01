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
from .sdarray import SDArray
from .sdproperty import SDProperty
from .sdtype import SDType
from .sdapiobject import SDAPIObject
from .sdproperty import SDPropertyCategory
from .sdproperty import SDPropertyInheritanceMethod
from .sdtype import SDTypeModifier
from .sdapiobject import SDApiError
from .apiexception import APIException

class SDTypeStruct(SDType):
    """
    Class used to store information about a structure type
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDTypeStruct
        """
        SDType.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sNew(sdTypeStructId):
        """
        Create a new SDTypeStruct from the specified type Id

        :param sdTypeStructId: The Id of the SDTypeStruct type to retrieve
        :type sdTypeStructId: string
        :rtype: SDTypeStruct
        """
        outSDTypeStruct = ctypes.c_void_p()
        _res = sd.getContext().SDTypeStruct_sNew(ctypes.create_string_buffer(sdTypeStructId.encode('utf-8')), ctypes.byref(outSDTypeStruct))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outSDTypeStruct, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outSDTypeStruct.value, ownHandle=True)

    def getMembers(self):
        """
        Get the members of the struct

        :rtype: SDArray[SDProperty]
        """
        outProperties = ctypes.c_void_p()
        _res = self.mAPIContext.SDTypeStruct_getMembers(self.mHandle, ctypes.byref(outProperties))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outProperties, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outProperties.value, ownHandle=True)

