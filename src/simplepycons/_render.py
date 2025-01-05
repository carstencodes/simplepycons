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


class RenderIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "render"

    @property
    def original_file_name(self) -> "str":
        return "render.svg"

    @property
    def title(self) -> "str":
        return "Render"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Render</title>
     <path d="M18.263.007c-3.121-.147-5.744 2.109-6.192
 5.082-.018.138-.045.272-.067.405-.696 3.703-3.936 6.507-7.827
 6.507-1.388 0-2.691-.356-3.825-.979a.2024.2024 0 0
 0-.302.178V24H12v-8.999c0-1.656 1.338-3 2.987-3h2.988c3.382 0
 6.103-2.817 5.97-6.244-.12-3.084-2.61-5.603-5.682-5.75" />
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
