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


class FritzIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fritz"

    @property
    def original_file_name(self) -> "str":
        return "fritz.svg"

    @property
    def title(self) -> "str":
        return "FRITZ!"

    @property
    def primary_color(self) -> "str":
        return "#E2001A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FRITZ!</title>
     <path d="M13.495 19.183 17.37
 24l4.817-3.903-3.875-4.817zM23.571.692 16.097.111l-.914 15.003
 6.118.221zM6.962
 5.564v4.097l5.62-.055v5.37H7.016v8.055H.43V.277L13.024 0V5.51z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://business.avm.de/de/data/allgemeine-nu'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
