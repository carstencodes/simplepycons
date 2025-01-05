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


class FlatpakIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flatpak"

    @property
    def original_file_name(self) -> "str":
        return "flatpak.svg"

    @property
    def title(self) -> "str":
        return "Flatpak"

    @property
    def primary_color(self) -> "str":
        return "#4A90D9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Flatpak</title>
     <path d="M12 0c-.556 0-1.111.144-1.61.432l-7.603 4.39a3.217 3.217
 0 0 0-1.61 2.788v8.78c0 1.151.612 2.212 1.61 2.788l7.603 4.39a3.217
 3.217 0 0 0 3.22 0l7.603-4.39a3.217 3.217 0 0 0 1.61-2.788V7.61a3.217
 3.217 0 0 0-1.61-2.788L13.61.432A3.218 3.218 0 0 0 12 0Zm0 2.358c.15
 0 .299.039.431.115l7.604 4.39c.132.077.24.187.315.316L12
 12v9.642a.863.863 0 0 1-.431-.116l-7.604-4.39a.866.866 0 0
 1-.431-.746V7.61c0-.153.041-.302.116-.43L12 12Z" />
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
