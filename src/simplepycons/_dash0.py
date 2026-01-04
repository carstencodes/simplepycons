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


class DashZeroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dash0"

    @property
    def original_file_name(self) -> "str":
        return "dash0.svg"

    @property
    def title(self) -> "str":
        return "Dash0"

    @property
    def primary_color(self) -> "str":
        return "#EA3D3B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dash0</title>
     <path d="M0 4.421c4.883 0 8.842 3.393 8.842 7.579S4.883 19.579 0
 19.579zm16.421 0C20.608 4.421 24 7.814 24 12s-3.392 7.579-7.579
 7.579S8.842 16.186 8.842 12s3.393-7.579 7.579-7.579" />
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
