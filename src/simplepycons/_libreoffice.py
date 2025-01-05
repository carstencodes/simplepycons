#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
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


class LibreofficeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "libreoffice"

    @property
    def original_file_name(self) -> "str":
        return "libreoffice.svg"

    @property
    def title(self) -> "str":
        return "LibreOffice"

    @property
    def primary_color(self) -> "str":
        return "#18A303"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LibreOffice</title>
     <path d="M16.365 0a.597.597 0 00-.555.352.582.582 0
 00.128.635l4.985 4.996a.605.605 0 00.635.133.59.59 0
 00.363-.53V.577A.605.605 0 0021.335 0zM2.661 0a.59.59 0
 00-.582.59v22.82a.59.59 0 00.582.59h18.67a.59.59 0
 00.59-.59V8.716a.59.59 0 00-.17-.42L13.674.182a.59.59 0
 00-.42-.181zm.59 1.184h9.754l7.733 7.77v13.863H3.251z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://wiki.documentfoundation.org/Marketing'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://wiki.documentfoundation.org/Marketing'''

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
