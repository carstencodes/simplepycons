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


class McdonaldsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mcdonalds"

    @property
    def original_file_name(self) -> "str":
        return "mcdonalds.svg"

    @property
    def title(self) -> "str":
        return "McDonald's"

    @property
    def primary_color(self) -> "str":
        return "#FBC817"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>McDonald's</title>
     <path d="M17.243 3.006c2.066 0 3.742 8.714 3.742
 19.478H24c0-11.588-3.042-20.968-6.766-20.968-2.127 0-4.007 2.81-5.248
 7.227-1.241-4.416-3.121-7.227-5.231-7.227C3.031 1.516 0 10.888 0
 22.476h3.014c0-10.763 1.658-19.47 3.724-19.47 2.066 0 3.741 8.05
 3.741 17.98h2.997c0-9.93 1.684-17.98 3.75-17.98Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.mcdonalds.com/gb/en-gb/newsroom.h'''

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
