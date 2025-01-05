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


class AutoprefixerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "autoprefixer"

    @property
    def original_file_name(self) -> "str":
        return "autoprefixer.svg"

    @property
    def title(self) -> "str":
        return "Autoprefixer"

    @property
    def primary_color(self) -> "str":
        return "#DD3735"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Autoprefixer</title>
     <path d="M5.87 21.045h2.923l.959-3.068h4.503l.949
 3.068h2.922L11.94 2.955l-6.07 18.09zm6.162-10.12 1.543
 4.917h-3.153l1.553-4.916h.057zM24 17.617l-.378-1.182-6.266-.59.733
 2.127 5.91-.354zM6.644 15.843l-6.266.591L0
 17.616l5.911.355.733-2.128z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/postcss/autoprefixer/blob/'''

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
