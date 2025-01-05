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


class ClickupIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "clickup"

    @property
    def original_file_name(self) -> "str":
        return "clickup.svg"

    @property
    def title(self) -> "str":
        return "ClickUp"

    @property
    def primary_color(self) -> "str":
        return "#7B68EE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ClickUp</title>
     <path d="M2 18.439l3.69-2.828c1.961 2.56 4.044 3.739 6.363 3.739
 2.307 0 4.33-1.166 6.203-3.704L22 18.405C19.298 22.065 15.941 24
 12.053 24 8.178 24 4.788 22.078 2 18.439zM12.04 6.15l-6.568
 5.66-3.036-3.52L12.055 0l9.543 8.296-3.05 3.509z" />
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
