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


class OpenrouterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openrouter"

    @property
    def original_file_name(self) -> "str":
        return "openrouter.svg"

    @property
    def title(self) -> "str":
        return "OpenRouter"

    @property
    def primary_color(self) -> "str":
        return "#94A3B8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenRouter</title>
     <path d="M16.778
 1.844v1.919q-.569-.026-1.138-.032-.708-.008-1.415.037c-1.93.126-4.023.728-6.149
 2.237-2.911 2.066-2.731 1.95-4.14
 2.75-.396.223-1.342.574-2.185.798-.841.225-1.753.333-1.751.333v4.229s.768.108
 1.61.333c.842.224 1.789.575 2.185.799 1.41.798 1.228.683 4.14 2.75
 2.126 1.509 4.22 2.11 6.148 2.236.88.058 1.716.041
 2.555.005v1.918l7.222-4.168-7.222-4.17v2.176c-.86.038-1.611.065-2.278.021-1.364-.09-2.417-.357-3.979-1.465-2.244-1.593-2.866-2.027-3.68-2.508.889-.518
 1.449-.906 3.822-2.59 1.56-1.109 2.614-1.377 3.978-1.466.667-.044
 1.418-.017 2.278.02v2.176L24 6.014Z" />
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
