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


class MdxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mdx"

    @property
    def original_file_name(self) -> "str":
        return "mdx.svg"

    @property
    def title(self) -> "str":
        return "MDX"

    @property
    def primary_color(self) -> "str":
        return "#1B1F24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MDX</title>
     <path d="M.79 7.12h22.42c.436 0 .79.355.79.792v8.176c0
 .436-.354.79-.79.79H.79a.79.79 0 0 1-.79-.79V7.912a.79.79 0 0 1
 .79-.791V7.12Zm2.507 7.605v-3.122l1.89 1.89L7.12
 11.56v3.122h1.055v-5.67l-2.99 2.99L2.24
 9.056v5.67h1.055v-.001Zm8.44-1.845-1.474-1.473-.746.746 2.747 2.747
 2.745-2.747-.746-.746-1.473 1.473v-4h-1.054v4Zm10.041.987-2.175-2.175
 2.22-2.22-.746-.746-2.22 2.22-2.22-2.22-.747.746 2.22 2.22-2.176
 2.177.746.746 2.177-2.177 2.176 2.175.745-.746Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mdx-js/mdx/blob/b8a76c95de'''

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
