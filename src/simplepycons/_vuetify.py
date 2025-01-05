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


class VuetifyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vuetify"

    @property
    def original_file_name(self) -> "str":
        return "vuetify.svg"

    @property
    def title(self) -> "str":
        return "Vuetify"

    @property
    def primary_color(self) -> "str":
        return "#1867C0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vuetify</title>
     <path d="M6.312 12.564 12.636 1.2H0l6.312 11.364ZM14.94 1.2 7.464
 14.64 12 22.8 24 1.2h-9.06Zm4.98 2.4L12 17.856l-1.788-3.216L16.344
 3.6h3.576ZM6.312 7.62 4.08 3.6h4.476L6.312 7.62Z" />
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
