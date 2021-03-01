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
from ..sdtype import SDType
from .sdmdlvalue import SDMDLValue
from ..sdapiobject import SDAPIObject
from ..sdtype import SDTypeModifier
from ..sdapiobject import SDApiError
from ..apiexception import APIException

class SDMDLValueParameterReference(SDMDLValue):
    """
    Class used to store information about a MDL parameter reference value
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDMDLValueParameterReference
        """
        SDMDLValue.__init__(self, APIContext, handle, *args, **kwargs)

    def getReferencedType(self):
        """
        Get the type of the referenced item

        :rtype: SDType
        """
        outSDType = ctypes.c_void_p()
        _res = self.mAPIContext.SDMDLValueParameterReference_getReferencedType(self.mHandle, ctypes.byref(outSDType))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outSDType, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outSDType.value, ownHandle=True)

