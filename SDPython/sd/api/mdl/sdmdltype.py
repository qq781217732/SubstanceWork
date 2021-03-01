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
from ..sdapiobject import SDAPIObject
from ..sdtype import SDTypeModifier
from ..sdapiobject import SDApiError
from ..apiexception import APIException

class SDMDLType(SDType):
    """
    Class used to store information about a MDL type
    """
    def __init__(self, APIContext, handle, *args, **kwargs):
        """
        Constructor

        :rtype: SDMDLType
        """
        SDType.__init__(self, APIContext, handle, *args, **kwargs)

