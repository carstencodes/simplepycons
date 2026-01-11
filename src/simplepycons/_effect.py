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


class EffectIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "effect"

    @property
    def original_file_name(self) -> "str":
        return "effect.svg"

    @property
    def title(self) -> "str":
        return "Effect"

    @property
    def primary_color(self) -> "str":
        return "#FFFFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Effect</title>
     <path d="M11.846.007a.8.8 0 0 0-.312.103L.454 6.346a.8.8 0 0
 0-.397.855.8.8 0 0 0 .408.78L3.99 9.976 1.033 11.64a.76.76 0 0
 0-.374.838c-.033.265.07.541.378.715l10.546 5.967a.8.8 0 0 0
 .61.073.8.8 0 0 0
 .27-.094l10.548-5.968c.31-.175.412-.454.376-.72a.76.76 0 0
 0-.383-.79l-3.01-1.693 3.554-2.012a.8.8 0 0 0 .399-.836.8.8 0 0
 0-.412-.753L12.455.13a.8.8 0 0 0-.28-.097.8.8 0 0 0-.227-.033m6.482
 10.853 2.78 1.566-9.205 5.21-9.21-5.213 2.76-1.554 5.99 3.387a.83.83
 0 0 0 .638.076.8.8 0 0 0 .285-.098zm3.572 6.03a.75.75 0 0
 0-.35.098l-9.67 5.47-9.635-5.45a.75.75 0 0 0-1.01.267.717.717 0 0 0
 .27.99l9.976 5.644a.75.75 0 0 0 .372.098c.079 0
 .294-.026.46-.117l9.978-5.645a.716.716 0 0 0 .27-.99.75.75 0 0
 0-.661-.364" />
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
