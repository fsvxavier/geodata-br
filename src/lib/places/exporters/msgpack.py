#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Paulo Freitas
# MIT License (see LICENSE file)
'''
MessagePack file exporter module
'''
from __future__ import absolute_import

# Imports

# External dependencies

import io
import msgpack

# Package dependencies

from places.exporters import Exporter
from places.formats.msgpack import MessagePackFormat

# Classes


class MessagePackExporter(Exporter):
    '''
    MessagePack exporter class.
    '''

    # Exporter format
    _format = MessagePackFormat

    def export(self, **options):
        '''
        Exports the data into a MessagePack file-like stream.

        Arguments:
            options (dict): The exporting options

        Returns:
            io.BytesIO: A MessagePack file-like stream

        Raises:
            ExportError: When data fails to export
        '''
        unpacked = self._data.normalize()
        packed = msgpack.packb(unpacked, use_bin_type=False)

        return io.BytesIO(packed)