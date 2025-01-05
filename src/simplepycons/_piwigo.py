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


class PiwigoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "piwigo"

    @property
    def original_file_name(self) -> "str":
        return "piwigo.svg"

    @property
    def title(self) -> "str":
        return "Piwigo"

    @property
    def primary_color(self) -> "str":
        return "#FF7700"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Piwigo</title>
     <path d="M16.712 12.777A4.713 4.713 0 0 1 12 17.49a4.713 4.713 0
 0 1-4.713-4.713A4.713 4.713 0 0 1 12 8.066a4.713 4.713 0 0 1 4.712
 4.711zm2.4-12.776c-2.572.058-2.358 1.544-8.237 1.555h-4.15A5.947
 5.947 0 0 0 .777 7.503v10.55A5.947 5.947 0 0 0 6.725 24h10.55a5.947
 5.947 0 0 0 5.948-5.947V4.081l-.008-.018c0-.014.004-.028.004-.043
 0-2.227-1.88-4.02-4.108-4.02zm.09 2.545a1.409 1.409 0 0 1 1.407
 1.41A1.409 1.409 0 0 1 19.2 5.364a1.409 1.409 0 0 1-1.41-1.408 1.409
 1.409 0 0 1 1.41-1.41zM12 6.12a6.656 6.656 0 0 1 6.656 6.655A6.656
 6.656 0 0 1 12 19.434a6.656 6.656 0 0 1-6.656-6.657A6.656 6.656 0 0 1
 12 6.122z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Piwigo/piwigodotorg/blob/6'''

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
