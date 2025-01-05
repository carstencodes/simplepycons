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


class DatadotaiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "datadotai"

    @property
    def original_file_name(self) -> "str":
        return "datadotai.svg"

    @property
    def title(self) -> "str":
        return "data.ai"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>data.ai</title>
     <path d="M8.12 1.744.015 10.009 0 10.023l11.986 12.219.014.015
 11.986-12.22.014-.014-8.115-8.273-.006-.006Zm1.207 1.02h5.326L11.99
 5.41zm3.422 3.43 3.027-3.053L22.081 9.5h-6.054ZM8.211 3.14l3.04
 3.072L7.999 9.5h-6.08Zm.62 6.977L12 6.876l3.169 3.242L12
 19.842zm7.328.402h5.862l-8.793 9.005Zm-14.24 0h5.915l2.958 9.006Z" />
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
