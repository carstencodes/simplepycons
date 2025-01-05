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


class LibreofficeCalcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "libreofficecalc"

    @property
    def original_file_name(self) -> "str":
        return "libreofficecalc.svg"

    @property
    def title(self) -> "str":
        return "LibreOffice Calc"

    @property
    def primary_color(self) -> "str":
        return "#007C3C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LibreOffice Calc</title>
     <path d="M9 13H7v-1h2v1zm6-3h-2v1h2v-1zm-6 0H7v1h2v-1zm3
 0h-2v1h2v-1zm3-10 7 7V0h-7zM9 14H7v1h2v-1zm5 3h1v-3h-1v3zm2
 0h1v-1h-1v1zm-4 0h1v-2h-1v2zm1-17 9 9v12c0 1.662-1.338 3-3 3H5c-1.662
 0-3-1.338-3-3V3c0-1.662 1.338-3 3-3h8zm5
 13h-7v5h7v-5zm-2-4H6v7h4.5v-1H10v-1h.5v-1H10v-1h2v.5h1V12h2v.5h1V9z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://wiki.documentfoundation.org/Design/Br'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/LibreOffice/help/blob/02fa
eab6e7b014ca97a8c452e829af4522dadfc8/source/media/navigation/libo-calc'''

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
