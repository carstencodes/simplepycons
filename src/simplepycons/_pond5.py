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


class PondFiveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pond5"

    @property
    def original_file_name(self) -> "str":
        return "pond5.svg"

    @property
    def title(self) -> "str":
        return "Pond5"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pond5</title>
     <path d="M21.504 11.385h.755c.92 0 1.747.286 1.741 1.388 0
 1.047-.932 1.412-1.717 1.412-.993
 0-1.75-.359-1.754-1.37v-.14h.944v.14c0 .384.442.53.798.53.233 0
 .784-.085.784-.572.006-.475-.508-.572-.797-.572h-1.644V9.875h3.146v.853h-2.256Zm-4.167
 2.745h-1.76V9.87h1.76c1.478 0 2.134.985 2.134 2.1 0 1.113-.632
 2.16-2.134 2.16zm0-3.402h-.816v2.526h.816c.932 0 1.19-.682 1.19-1.297
 0-.615-.295-1.23-1.19-1.23zm-6.055 1.14v2.262h-.955V9.81l.134-.023
 2.598 2.33V9.869h.957v4.333l-.1.017-2.634-2.351zm-4.431 2.367c-1.374
 0-2.319-.848-2.319-2.235 0-1.388.945-2.235 2.319-2.235 1.373 0
 2.318.847 2.318 2.235 0 1.387-.944 2.234-2.318 2.234zm0-3.618c-.816
 0-1.38.61-1.38 1.382 0 .798.564 1.376 1.38 1.376.834 0 1.38-.584
 1.38-1.376 0-.779-.546-1.382-1.38-1.382zm-4.827
 2.308h-.587v-.87h.587c.46 0 .686-.299.686-.64
 0-.34-.232-.645-.686-.645H.957v3.36H0V9.87h2.024c1.097 0 1.642.705
 1.642 1.527 0 .852-.552 1.516-1.643 1.528z" />
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
