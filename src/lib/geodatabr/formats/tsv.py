#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Paulo Freitas
# MIT License (see LICENSE file)
'''
TSV file format package
'''
# Imports

# Package dependencies

from geodatabr.core.helpers.decorators import classproperty
from geodatabr.formats import Format

# Classes


class TsvFormat(Format):
    '''
    The file format class for TSV file format.
    '''

    @classproperty
    def name(self):
        '''
        The file format name.
        '''
        return 'tsv'

    @classproperty
    def friendlyName(self):
        '''
        The file format friendly name.
        '''
        return 'TSV'

    @classproperty
    def extension(self):
        '''
        The file format extension.
        '''
        return '.tsv'

    @classproperty
    def type(self):
        '''
        The file format type.
        '''
        return 'Tabular Text'

    @classproperty
    def mimeType(self):
        '''
        The file format media type.
        '''
        return 'text/tab-separated-values'

    @classproperty
    def info(self):
        '''
        The file format reference info.
        '''
        return 'https://en.wikipedia.org/wiki/Tab-separated_values'

    @classproperty
    def isExportable(self):
        '''
        Tells whether the file format is exportable or not.
        '''
        return True