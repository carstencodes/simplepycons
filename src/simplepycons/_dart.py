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


class DartIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dart"

    @property
    def original_file_name(self) -> "str":
        return "dart.svg"

    @property
    def title(self) -> "str":
        return "Dart"

    @property
    def primary_color(self) -> "str":
        return "#0175C2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dart</title>
     <path d="M4.105 4.105S9.158 1.58 11.684.316a3.079 3.079 0 0 1
 1.481-.315c.766.047 1.677.788 1.677.788L24
 9.948v9.789h-4.263V24H9.789l-9-9C.303 14.5 0 13.795 0
 13.105c0-.319.18-.818.316-1.105l3.789-7.895zm.679.679v11.787c.002.543.021
 1.024.498 1.508L10.204 23h8.533v-4.263L4.784
 4.784zm12.055-.678c-.899-.896-1.809-1.78-2.74-2.643-.302-.267-.567-.468-1.07-.462-.37.014-.87.195-.87.195L6.341
 4.105l10.498.001z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dart-lang/site-shared/tree'''

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
