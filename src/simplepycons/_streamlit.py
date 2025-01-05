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


class StreamlitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "streamlit"

    @property
    def original_file_name(self) -> "str":
        return "streamlit.svg"

    @property
    def title(self) -> "str":
        return "Streamlit"

    @property
    def primary_color(self) -> "str":
        return "#FF4B4B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Streamlit</title>
     <path d="M16.673
 11.32l6.862-3.618c.233-.136.554.12.442.387L20.463
 17.1zm-8.556-.229l3.473-5.187c.203-.328.578-.316.793-.028l7.886
 11.75zm-3.375 7.25c-.28
 0-.835-.284-.993-.716l-3.72-9.46c-.118-.331.139-.614.48-.464l19.474
 10.306c-.149.147-.453.337-.72.334z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
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
