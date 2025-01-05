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


class ChakraUiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chakraui"

    @property
    def original_file_name(self) -> "str":
        return "chakraui.svg"

    @property
    def title(self) -> "str":
        return "Chakra UI"

    @property
    def primary_color(self) -> "str":
        return "#319795"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chakra UI</title>
     <path d="M12 0C5.352 0 0 5.352 0 12s5.352 12 12 12 12-5.352
 12-12S18.648 0 12 0zm2.8 4.333c.13-.004.248.136.171.278l-3.044
 5.58a.187.187 0 00.164.276h5.26c.17 0 .252.207.128.323l-9.22
 8.605c-.165.154-.41-.063-.278-.246l4.364-6.021a.187.187 0
 00-.151-.296H6.627a.187.187 0 01-.131-.32l8.18-8.123a.182.182 0
 01.125-.056z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/chakra-ui/chakra-ui/blob/3'''

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
