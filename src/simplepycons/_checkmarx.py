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


class CheckmarxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "checkmarx"

    @property
    def original_file_name(self) -> "str":
        return "checkmarx.svg"

    @property
    def title(self) -> "str":
        return "Checkmarx"

    @property
    def primary_color(self) -> "str":
        return "#54B848"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Checkmarx</title>
     <path d="M6.544.12A6.553 6.553 0 0 0 0 6.664v10.674a6.551 6.551 0
 0 0 6.544 6.542h10.912A6.551 6.551 0 0 0 24 17.338v-.831a2.193 2.193
 0 0 0-4.388 0v.83c0 1.19-.967 2.157-2.156 2.157H6.544a2.16 2.16 0 0
 1-2.158-2.156V6.748c0-1.19.969-2.16 2.158-2.16 3.843.004 7.814-.009
 11.612.001.556.138.892.445 1.058.848.193.47.343 1.118-.404
 1.748l-6.26 4.596-1.892-2.441a2.191 2.191 0 0 0-3.075-.391 2.191
 2.191 0 0 0-.391 3.076l3.198 4.133a2.197 2.197 0 0 0
 3.035.424l7.252-5.301a56.68 56.68 0 0 0 1.22-.977c2.106-1.926
 2.517-4.393 1.627-6.553C22.603 1.51 20.268.12 17.435.12Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.checkmarx.com/resources/datasheet'''

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
