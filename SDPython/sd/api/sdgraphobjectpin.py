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
from .sdgraph import SDGraph
from .sdgraphobject import SDGraphObject
from .sdapiobject import SDAPIObject
from .sdapiobject import SDApiError
from .apiexception import APIException

class SDGraphObjectPin(SDGraphObject):
    """
    Class managing a Pin object in the graph
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDGraphObjectPin
        """
        SDGraphObject.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sNew(sdGraph):
        """
        Create a new SDGraphObjectPin instance in the specified graph

        :param sdGraph: The SDGraph that should contains the new SDGraphObjectPin
        :type sdGraph: SDGraph
        :rtype: SDGraphObjectPin
        """
        outSDGraphObjectPin = ctypes.c_void_p()
        _res = sd.getContext().SDGraphObjectPin_sNew(sdGraph.mHandle, ctypes.byref(outSDGraphObjectPin))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outSDGraphObjectPin, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outSDGraphObjectPin.value, ownHandle=True)

