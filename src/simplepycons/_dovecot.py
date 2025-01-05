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


class DovecotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dovecot"

    @property
    def original_file_name(self) -> "str":
        return "dovecot.svg"

    @property
    def title(self) -> "str":
        return "Dovecot"

    @property
    def primary_color(self) -> "str":
        return "#54BCAB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dovecot</title>
     <path d="M 8.784 8.39 C 8.581 8.391 8.382 8.458 8.22 8.582 L
 0.118 14.772 C -0.04 14.897 -0.04 15.138 0.118 15.262 L 0.457 15.515
 C 0.61 15.635 0.825 15.635 0.98 15.515 L 4.998 12.454 C 5.22 12.286
 5.526 12.286 5.748 12.454 L 8.407 14.487 C 8.628 14.655 8.934 14.655
 9.156 14.487 L 12.671 11.804 C 12.902 11.636 12.902 11.291 12.671
 11.122 L 9.349 8.582 C 9.187 8.458 8.988 8.39 8.784 8.39 Z M 18.082
 8.39 C 17.878 8.39 17.68 8.458 17.519 8.582 L 9.417 14.778 C 9.255
 14.901 9.255 15.144 9.417 15.267 L 9.752 15.522 C 9.908 15.638 10.124
 15.638 10.279 15.522 L 14.914 11.989 C 15.136 11.823 15.442 11.823
 15.662 11.989 L 20.189 15.441 C 20.41 15.61 20.718 15.61 20.939
 15.441 L 23.828 13.228 C 24.057 13.056 24.057 12.712 23.828 12.54 L
 18.647 8.582 C 18.485 8.458 18.286 8.39 18.082 8.39 Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Dovec'''

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
