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


class SuzukiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "suzuki"

    @property
    def original_file_name(self) -> "str":
        return "suzuki.svg"

    @property
    def title(self) -> "str":
        return "Suzuki"

    @property
    def primary_color(self) -> "str":
        return "#E30613"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Suzuki</title>
     <path d="M17.369 19.995C13.51 22.39 12 24 12 24L.105
 15.705s5.003-3.715 9.186-.87l5.61 3.882.683-.453L.106 7.321s2.226-.65
 6.524-3.315C10.49 1.609 12 0 12 0l11.895 8.296s-5.003
 3.715-9.187.87L9.1 5.281l-.683.454L23.893 16.68s-2.224.649-6.524
 3.315Z" />
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
