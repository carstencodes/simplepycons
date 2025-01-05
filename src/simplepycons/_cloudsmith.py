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


class CloudsmithIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudsmith"

    @property
    def original_file_name(self) -> "str":
        return "cloudsmith.svg"

    @property
    def title(self) -> "str":
        return "Cloudsmith"

    @property
    def primary_color(self) -> "str":
        return "#2A6FE1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cloudsmith</title>
     <path d="M24 10.667v2.667L13.333 24h-2.666L0 13.334v-2.667L10.667
 0h2.666L24 10.667Zm-12 6.869a5.535 5.535 0 1 0 0-11.07 5.535 5.535 0
 0 0 0 11.07Z" />
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
