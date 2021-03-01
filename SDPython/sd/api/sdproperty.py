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
from enum import Enum
from .sdarray import SDArray
from .sdtype import SDType
from .sdvalue import SDValue
from .sdapiobject import SDAPIObject
from .sdtype import SDTypeModifier
from .sdapiobject import SDApiError
from .apiexception import APIException

class SDPropertyCategory(Enum):
    Annotation = 0
    Input = 1
    Output = 2

class SDPropertyInheritanceMethod(Enum):
    """Property value is relative to the node that is connected to this input property"""
    RelativeToInput = 0
    """Property value is relative to the graph containing the node of this input property"""
    RelativeToParent = 1
    """Property value is not relative"""
    Absolute = 2

class SDProperty(SDAPIObject):
    """
    Description of property defined by an identifier, a type, and some additional information
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDProperty
        """
        SDAPIObject.__init__(self, APIContext, handle, *args, **kwargs)

    def getId(self):
        """
        Get the identifier of the property. The identifier is unique in the current category.

        :rtype: string
        """
        outId = ctypes.c_char_p()
        _res = self.mAPIContext.SDProperty_getId(self.mHandle, ctypes.byref(outId))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outId.value.decode('utf-8')

    def getTypes(self):
        """
        Get all types supported by this property

        :rtype: SDArray[SDType]
        """
        outSDArrayOfSDType = ctypes.c_void_p()
        _res = self.mAPIContext.SDProperty_getTypes(self.mHandle, ctypes.byref(outSDArrayOfSDType))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outSDArrayOfSDType, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outSDArrayOfSDType.value, ownHandle=True)

    def getType(self):
        """
        Get the first type of all available types returned by getTypes() (defined for convenience)

        :rtype: SDType
        """
        outType = ctypes.c_void_p()
        _res = self.mAPIContext.SDProperty_getType(self.mHandle, ctypes.byref(outType))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outType, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outType.value, ownHandle=True)

    def getDefaultValue(self):
        """
        Get the default value of the property

        :rtype: SDValue
        """
        outValue = ctypes.c_void_p()
        _res = self.mAPIContext.SDProperty_getDefaultValue(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outValue, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outValue.value, ownHandle=True)

    def getLabel(self):
        """
        Get the label of the property

        :rtype: string
        """
        outLabel = ctypes.c_char_p()
        _res = self.mAPIContext.SDProperty_getLabel(self.mHandle, ctypes.byref(outLabel))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outLabel.value.decode('utf-8')

    def getDescription(self):
        """
        Get the description of the property

        :rtype: string
        """
        outDescription = ctypes.c_char_p()
        _res = self.mAPIContext.SDProperty_getDescription(self.mHandle, ctypes.byref(outDescription))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outDescription.value.decode('utf-8')

    def getCategory(self):
        """
        Get the category of the property (see SDPropertyCategory)

        :rtype: SDPropertyCategory
        """
        outSDPropertyCategory = ctypes.c_int()
        _res = self.mAPIContext.SDProperty_getCategory(self.mHandle, ctypes.byref(outSDPropertyCategory))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return SDPropertyCategory(outSDPropertyCategory.value)

    def isConnectable(self):
        """
        Indicates whether the property is connectable (i.e. if another node's property can be connected to it)

        :rtype: bool
        """
        outValue = ctypes.c_bool()
        _res = self.mAPIContext.SDProperty_isConnectable(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value

    def isReadOnly(self):
        """
        Indicates whether the property is readonly

        :rtype: bool
        """
        outValue = ctypes.c_bool()
        _res = self.mAPIContext.SDProperty_isReadOnly(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value

    def isVariadic(self):
        """
        Indicates whether the property is variadic. If True, this parameter will be represented as multiple properties on the instance

        :rtype: bool
        """
        outValue = ctypes.c_bool()
        _res = self.mAPIContext.SDProperty_isVariadic(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value

    def isPrimary(self):
        """
        Indicates whether the property is the primary property in its category

        :rtype: bool
        """
        outValue = ctypes.c_bool()
        _res = self.mAPIContext.SDProperty_isPrimary(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value

    def isFunctionOnly(self):
        """
        Indicates if the property value is only controlled by a function. If so calling getPropertyValue/setPropertyValue is not allowed

        :rtype: bool
        """
        outValue = ctypes.c_bool()
        _res = self.mAPIContext.SDProperty_isFunctionOnly(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value

