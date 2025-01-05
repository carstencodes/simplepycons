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


class ProtonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "proton"

    @property
    def original_file_name(self) -> "str":
        return "proton.svg"

    @property
    def title(self) -> "str":
        return "Proton"

    @property
    def primary_color(self) -> "str":
        return "#6D4AFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Proton</title>
     <path d="M2.474
 17.75V24h4.401v-5.979c0-.582.232-1.14.645-1.551a2.204 2.204 0 0 1
 1.556-.643h4.513a7.955 7.955 0 0 0 5.612-2.318 7.907 7.907 0 0 0
 2.325-5.595 7.91 7.91 0 0 0-2.325-5.596A7.958 7.958 0 0 0 13.587
 0H2.474v7.812h4.401V4.129h6.416c.995 0 1.951.394 2.656 1.097.704.7
 1.1 1.653 1.101 2.646a3.742 3.742 0 0 1-1.101 2.648 3.766 3.766 0 0
 1-2.656 1.097H8.627a6.158 6.158 0 0 0-4.352 1.795 6.133 6.133 0 0
 0-1.801 4.338Z" />
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
