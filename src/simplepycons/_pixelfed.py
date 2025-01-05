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


class PixelfedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pixelfed"

    @property
    def original_file_name(self) -> "str":
        return "pixelfed.svg"

    @property
    def title(self) -> "str":
        return "Pixelfed"

    @property
    def primary_color(self) -> "str":
        return "#6366F1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pixelfed</title>
     <path d="M12 24C5.3726 24 0 18.6274 0 12S5.3726 0 12 0s12 5.3726
 12 12-5.3726 12-12 12m-.9526-9.3802h2.2014c2.0738 0 3.7549-1.6366
 3.7549-3.6554S15.3226 7.309 13.2488 7.309h-3.1772c-1.1964
 0-2.1663.9442-2.1663 2.1089v8.208z" />
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
