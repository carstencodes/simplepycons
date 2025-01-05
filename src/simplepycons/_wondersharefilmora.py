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


class WondershareFilmoraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wondersharefilmora"

    @property
    def original_file_name(self) -> "str":
        return "wondersharefilmora.svg"

    @property
    def title(self) -> "str":
        return "Wondershare Filmora"

    @property
    def primary_color(self) -> "str":
        return "#07273D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wondershare Filmora</title>
     <path d="M5.475 0A5.463 5.463 0 0 0 0 5.475v13.05A5.463 5.463 0 0
 0 5.475 24h13.05A5.463 5.463 0 0 0 24 18.525V5.475A5.463 5.463 0 0 0
 18.525 0H5.475Zm4.552 3.6 4.026 4.029-4.617 4.623-.022-.023a1.088
 1.088 0 0 0-.158-1.339L5.999 7.63l4.028-4.03ZM14.528 8l4.027
 4.03-8.528 8.536L6 16.536 14.528 8Z" />
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
