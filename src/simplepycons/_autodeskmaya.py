#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class AutodeskMayaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "autodeskmaya"

    @property
    def original_file_name(self) -> "str":
        return "autodeskmaya.svg"

    @property
    def title(self) -> "str":
        return "Autodesk Maya"

    @property
    def primary_color(self) -> "str":
        return "#37A5CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Autodesk Maya</title>
     <path d="M4.348 0 .69
 2.203v16.875l3.657-2.203h17.297V1.219c0-.67-.551-1.219-1.22-1.219H4.349zm18.297
 3.75v14.125H4.627l-1.943 1.17v3.736c0 .67.55 1.219 1.218
 1.219H23.31V3.75h-.664zm-14.471.025h2.937l1.885 7.508
 1.977-7.48-.012-.028h2.857v9.354h-2.216v-6.04l-1.565
 6.026v.014h-2.203l-1.656-6.28v6.28H8.174V3.775zm1.33
 14.762h1.18l1.068
 3.543h-.902l-.217-.773H9.568l-.197.773h-.88l1.013-3.543zm1.918
 0h.932l.648 1.494.643-1.494h.894l-1.113
 2.133v1.41h-.887v-1.406l-1.117-2.137zm3.826 0h1.18l1.068
 3.543h-.9l-.217-.773h-1.065l-.197.773h-.88l1.011-3.543zm-5.156.582-.362
 1.53h.73l-.368-1.53zm5.744 0-.36 1.53h.73l-.37-1.53z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://area.autodesk.com/learn/courses/maya-'''

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