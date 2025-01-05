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


class SamsClubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "samsclub"

    @property
    def original_file_name(self) -> "str":
        return "samsclub.svg"

    @property
    def title(self) -> "str":
        return "Sam's Club"

    @property
    def primary_color(self) -> "str":
        return "#0067A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sam's Club</title>
     <path d="m14.275 1.71 9.403 9.504a1.119 1.119 0 0 1 .001
 1.569l-9.401 9.507-1.624-1.64a1.136 1.136 0 0 1 0-1.596L19.631
 12l-6.917-6.99a1.225 1.225 0 0 1 0-1.72l1.56-1.579zm-3.026
 1.572L9.695 1.71.34 11.17a1.186 1.186 0 0 0 0 1.663l9.356 9.457
 1.553-1.57a1.237 1.237 0 0 0 0-1.737L4.341 12l6.909-6.985a1.235 1.235
 0 0 0-.001-1.734z" />
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
