#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class MdblistIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mdblist"

    @property
    def original_file_name(self) -> "str":
        return "mdblist.svg"

    @property
    def title(self) -> "str":
        return "MDBList"

    @property
    def primary_color(self) -> "str":
        return "#4284CA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MDBList</title>
     <path d="M1.928.029A2.47 2.47 0 0 0 .093
 1.673c-.085.248-.09.629-.09 10.33s.005 10.08.09 10.33a2.51 2.51 0 0 0
 1.512 1.558l.276.108h20.237l.277-.108a2.51 2.51 0 0 0
 1.512-1.559c.085-.25.09-.63.09-10.33s-.005-10.08-.09-10.33A2.51 2.51
 0 0 0 22.395.115l-.277-.109L12.117 0C6.615-.004 2.032.011
 1.929.029m7.48 8.067 2.123 2.004v1.54c0 .897-.02 1.536-.043
 1.527s-.92-.845-1.995-1.86c-1.071-1.01-1.962-1.84-1.977-1.84s-.024
 1.91-.024 4.248v4.25H4.911V6.085h1.188l1.183.006zm9.729
 3.93v5.94h-2.63l-.01-4.25-.013-4.25-1.907 1.795a367 367 0 0 1-1.98
 1.864c-.076.056-.08-.047-.08-1.489v-1.555l2.127-1.995 2.122-1.995
 1.187-.005h1.184z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://mdblist.com/static/safari-pinned-tab.'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
