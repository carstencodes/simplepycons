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


class FigmaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "figma"

    @property
    def original_file_name(self) -> "str":
        return "figma.svg"

    @property
    def title(self) -> "str":
        return "Figma"

    @property
    def primary_color(self) -> "str":
        return "#F24E1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Figma</title>
     <path d="M15.852 8.981h-4.588V0h4.588c2.476 0 4.49 2.014 4.49
 4.49s-2.014 4.491-4.49 4.491zM12.735 7.51h3.117c1.665 0 3.019-1.355
 3.019-3.019s-1.355-3.019-3.019-3.019h-3.117V7.51zm0
 1.471H8.148c-2.476 0-4.49-2.014-4.49-4.49S5.672 0 8.148
 0h4.588v8.981zm-4.587-7.51c-1.665 0-3.019 1.355-3.019 3.019s1.354
 3.02 3.019 3.02h3.117V1.471H8.148zm4.587 15.019H8.148c-2.476
 0-4.49-2.014-4.49-4.49s2.014-4.49 4.49-4.49h4.588v8.98zM8.148
 8.981c-1.665 0-3.019 1.355-3.019 3.019s1.355 3.019 3.019
 3.019h3.117V8.981H8.148zM8.172 24c-2.489
 0-4.515-2.014-4.515-4.49s2.014-4.49 4.49-4.49h4.588v4.441c0
 2.503-2.047 4.539-4.563 4.539zm-.024-7.51a3.023 3.023 0 0 0-3.019
 3.019c0 1.665 1.365 3.019 3.044 3.019 1.705 0 3.093-1.376
 3.093-3.068v-2.97H8.148zm7.704 0h-.098c-2.476
 0-4.49-2.014-4.49-4.49s2.014-4.49 4.49-4.49h.098c2.476 0 4.49 2.014
 4.49 4.49s-2.014 4.49-4.49 4.49zm-.097-7.509c-1.665 0-3.019
 1.355-3.019 3.019s1.355 3.019 3.019 3.019h.098c1.665 0 3.019-1.355
 3.019-3.019s-1.355-3.019-3.019-3.019h-.098z" />
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
