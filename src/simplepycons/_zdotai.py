#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class ZdotaiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zdotai"

    @property
    def original_file_name(self) -> "str":
        return "zdotai.svg"

    @property
    def title(self) -> "str":
        return "Z.ai"

    @property
    def primary_color(self) -> "str":
        return "#2D2D2D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Z.ai</title>
     <path d="M12.606 1.806l-1.677 2.388c-0.258 0.374-0.697
 0.606-1.161 0.606h-9.162V1.794C0.594 1.806 12.606 1.806 12.606
 1.806zM24 1.806L9.6 22.206 0 22.206 14.4 1.806zM11.394
 22.206l1.69-2.4c0.258-0.374 0.697-0.606
 1.161-0.606h9.149v3.006H11.394z" />
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
