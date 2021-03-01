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
from .sdtype import *
from .sdtypematrix import *
from .sdvalue import *
from .sdapiobject import *
from .sdtype import *
from .sdapiobject import *
from .apiexception import APIException

class SDValueMatrix(SDValue):
    """
    Class used to store the data of a matrix
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDValueMatrix
        """
        SDValue.__init__(self, APIContext, handle, *args, **kwargs)

    @staticmethod
    def sNew(itemType, columnCount, rowCount):
        """
        Create a new SDValueMatrix

        :param itemType: The type if the items of the matrix
        :type itemType: SDType
        :param columnCount: The number of the column of the new matrix
        :type columnCount: int
        :param rowCount: The number of the row of the new matrix
        :type rowCount: int
        :rtype: SDValueMatrix
        """
        outValueMatrix = ctypes.c_void_p()
        _res = sd.getContext().SDValueMatrix_sNew(itemType.mHandle, columnCount, rowCount, ctypes.byref(outValueMatrix))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outValueMatrix, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outValueMatrix.value, ownHandle=True)

    @staticmethod
    def sNewFromSDTypeMatrix(sdTypeMatrix):
        """
        Create a new SDValueMatrix from a SDTypeMatrix

        :param sdTypeMatrix: The type of the new matrix
        :type sdTypeMatrix: SDTypeMatrix
        :rtype: SDValueMatrix
        """
        outValueMatrix = ctypes.c_void_p()
        _res = sd.getContext().SDValueMatrix_sNewFromSDTypeMatrix(sdTypeMatrix.mHandle, ctypes.byref(outValueMatrix))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = sd.getContext().mTypeMap[SDAPIObject(sd.getContext(), outValueMatrix, ownHandle=False).getClassName()]
        return constructor(sd.getContext(), outValueMatrix.value, ownHandle=True)

    def getItem(self, columnIndex, rowIndex):
        """
        Get the value of the specified item

        :param columnIndex: The index of the column
        :type columnIndex: int
        :param rowIndex: The index of the row
        :type rowIndex: int
        :rtype: SDValue
        """
        outValue = ctypes.c_void_p()
        _res = self.mAPIContext.SDValueMatrix_getItem(self.mHandle, columnIndex, rowIndex, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        constructor = self.mAPIContext.mTypeMap[SDAPIObject(self.mAPIContext, outValue, ownHandle=False).getClassName()]
        return constructor(self.mAPIContext, outValue.value, ownHandle=True)

    def setItem(self, columnIndex, rowIndex, newItemValue):
        """
        Set the value of the specified item

        :param columnIndex: The index of the column
        :type columnIndex: int
        :param rowIndex: The index of the row
        :type rowIndex: int
        :param newItemValue: The new value of the item
        :type newItemValue: SDValue
        :rtype: None
        """
        _res = self.mAPIContext.SDValueMatrix_setItem(self.mHandle, columnIndex, rowIndex, newItemValue.mHandle)
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return None

    def getColumnCount(self):
        """
        Get the number of column of the matrix

        :rtype: int
        """
        outValue = ctypes.c_size_t()
        _res = self.mAPIContext.SDValueMatrix_getColumnCount(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value

    def getRowCount(self):
        """
        Get the number of row of the matrix

        :rtype: int
        """
        outValue = ctypes.c_size_t()
        _res = self.mAPIContext.SDValueMatrix_getRowCount(self.mHandle, ctypes.byref(outValue))
        if _res != SDApiError.NoError.value:
            if _res == SDApiError.NoErrorOutputParamNotSet.value:
                return None
            raise APIException(SDApiError(_res))
        return outValue.value

