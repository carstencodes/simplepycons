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


class PenpotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "penpot"

    @property
    def original_file_name(self) -> "str":
        return "penpot.svg"

    @property
    def title(self) -> "str":
        return "Penpot"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Penpot</title>
     <path d="M7.654 0 5.13 3.554v2.01L2.934
 6.608l-.02-.009v13.109l8.563 4.045L12 24l.523-.247
 8.563-4.045V6.6l-.017.008-2.196-1.045V3.555l-.077-.108L16.349.001l-2.524
 3.554v.004L11.989.973l-1.823 2.566-.065-.091zm.447 2.065.976
 1.374H6.232l.964-1.358zm8.694 0 .976
 1.374h-2.845l.965-1.358zm-4.36.971.976 1.375h-2.845l.965-1.359zM5.962
 4.132h1.35v4.544l-1.35-.638Zm2.042 0h1.343v5.506l-1.343-.635zm6.652
 0h1.35V9l-1.35.637V4.132zm2.042
 0h1.343v3.905l-1.343.634zm-6.402.972h1.35v5.62l-1.35-.638zm2.042
 0h1.343v4.993l-1.343.634zm6.534 1.493 1.188.486-1.188.561zM5.13
 6.6v1.047l-1.187-.561ZM3.96 8.251l7.517
 3.55v10.795l-7.516-3.55zm16.08 0v10.794l-7.517 3.55V11.802z" />
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
