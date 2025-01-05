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


class VibloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "viblo"

    @property
    def original_file_name(self) -> "str":
        return "viblo.svg"

    @property
    def title(self) -> "str":
        return "Viblo"

    @property
    def primary_color(self) -> "str":
        return "#5387C6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Viblo</title>
     <path d="M10.569 19.68h2.904L21.621.018 18.705 0l-4.428
 10.668H9.705L5.295 0H2.379l8.19 19.68zm-7.02
 1.854h16.908V24H3.549v-2.466z" />
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
