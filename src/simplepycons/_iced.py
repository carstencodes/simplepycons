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


class IcedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iced"

    @property
    def original_file_name(self) -> "str":
        return "iced.svg"

    @property
    def title(self) -> "str":
        return "Iced"

    @property
    def primary_color(self) -> "str":
        return "#3645FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Iced</title>
     <path d="m22.605 0-6.023 6.123 1.313 1.291 6.023-6.123L22.605
 0zm-5.638.047L7.932 9.232l1.312 1.29 9.035-9.184L16.967.047zM9.699
 1.775c-2.337 2.377-3.477 3.528-4.617 4.68a1972.17 1972.17 0 0 0-4.621
 4.686l-.379.384 2.867 9.772L12.762 24l10.511-10.5-1.3-1.3-9.02
 9.007-1.908-6.83 5.559-5.65-1.311-1.291-5.559 5.65-6.845-1.79C4.506
 9.655 5.449 8.703 6.39 7.75c1.14-1.153 2.282-2.305 4.62-4.684L9.7
 1.776zM21.605 6.73l-1.53 1.53-6.458 6.565 1.313 1.291 6.45-6.558
 1.528-1.528-1.303-1.3zM2.46 13.088l6.812 1.781 1.895
 6.783-6.738-1.857-1.969-6.707z" />
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
