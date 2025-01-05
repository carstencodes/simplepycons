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


class IconifyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iconify"

    @property
    def original_file_name(self) -> "str":
        return "iconify.svg"

    @property
    def title(self) -> "str":
        return "Iconify"

    @property
    def primary_color(self) -> "str":
        return "#1769AA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Iconify</title>
     <path d="M12 19.5c3.75 0 7.159-3.379 6.768-4.125-.393-.75-2.268
 1.875-6.768 1.875s-6-2.625-6.375-1.875S8.25 19.5 12
 19.5zm4.125-12c.623 0 1.125.502 1.125 1.125v1.5c0 .623-.502
 1.125-1.125 1.125A1.123 1.123 0 0115 10.125v-1.5c0-.623.502-1.125
 1.125-1.125zm-8.25 0C8.498 7.5 9 8.002 9 8.625v1.5c0 .623-.502
 1.125-1.125 1.125a1.123 1.123 0 01-1.125-1.125v-1.5c0-.623.502-1.125
 1.125-1.125zM12 0C5.381 0 0 5.381 0 12s5.381 12 12 12 12-5.381
 12-12S18.619 0 12 0zm0 1.5c5.808 0 10.5 4.692 10.5 10.5S17.808 22.5
 12 22.5 1.5 17.808 1.5 12 6.192 1.5 12 1.5Z" />
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
