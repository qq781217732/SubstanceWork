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
from .sddefinition import SDDefinition
from .sdapiobject import SDAPIObject
from .sdresource import SDResource
from .sdapiobject import SDApiError
from .sdresource import EmbedMethod
from .apiexception import APIException

class SDResourceScene(SDResource):
    """
    A scene or mesh resource as it can be found in a SDPackage
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDResourceScene
        """
        SDResource.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sGetAvailablePrimitiveDefinitions():
        """
        Get all available primitive definitions. A primitive is a predefined scene provided by Designer (Cube, Sphere, Plane, ...)

        :rtype: SDArray[SDDefinition]
        """
        outArray = ctypes.c_void_p()
        _res = sd.getContext().SDResourceScene_sGetAvailablePrimitiveDefinitions(ctypes.byref(outArray))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outArray, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outArray.value, ownHandle=True)

    @staticmethod
    def sNewFromPrimitiveId(parent, primitiveId):
        """
        Create a new SDResourceScene from the specified primitive Id

        :param parent: The parent data that will contains the newly created Resource. Can be SDPackage or SDResourceFolder
        :type parent: SDAPIObject
        :param primitiveId: The primitive id (See 'sGetAvailablePrimitiveDefinitions' for available primitive definitions)
        :type primitiveId: string
        :rtype: SDResourceScene
        """
        outResource = ctypes.c_void_p()
        _res = sd.getContext().SDResourceScene_sNewFromPrimitiveId(parent.mHandle, ctypes.create_string_buffer(primitiveId.encode('utf-8')), ctypes.byref(outResource))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outResource, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outResource.value, ownHandle=True)

    @staticmethod
    def sNewFromFile(parent, filePath, embedMethod):
        """
        Create a new SDResourceScene from the specified file. The resource will reference this file

        :param parent: The parent data that will contains the newly created Resource. Can be SDPackage or SDResourceFolder
        :type parent: SDAPIObject
        :param filePath: The scene file path
        :type filePath: string
        :param embedMethod: The embed method. The only supported method is Linked
        :type embedMethod: EmbedMethod
        :rtype: SDResourceScene
        """
        outResource = ctypes.c_void_p()
        _res = sd.getContext().SDResourceScene_sNewFromFile(parent.mHandle, ctypes.create_string_buffer(filePath.encode('utf-8')), embedMethod.value, ctypes.byref(outResource))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outResource, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outResource.value, ownHandle=True)

