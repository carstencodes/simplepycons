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


class BluesoundIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bluesound"

    @property
    def original_file_name(self) -> "str":
        return "bluesound.svg"

    @property
    def title(self) -> "str":
        return "Bluesound"

    @property
    def primary_color(self) -> "str":
        return "#0F131E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bluesound</title>
     <path d="m14.327 14.893-8.396.003a4.549 4.549 0 0 0-4.546 4.543c0
 2.05.007 3.737.007 3.737V24h12.955l.191-.002c4.678-.099 8.077-3.577
 8.077-8.273a8.733 8.733 0 0 0-.805-3.721 8.77 8.77 0 0 0
 .805-3.724c0-4.695-3.399-8.173-8.084-8.275L1.392 0v.833s-.007
 1.681-.007 3.733a4.548 4.548 0 0 0 4.546 4.541l8.399.013c2.375 0
 4.392 1.048 5.567 2.884-1.178 1.838-3.197 2.889-5.57
 2.889m.219-7.452-8.615.002a2.88 2.88 0 0
 1-2.879-2.877V1.665H14.33c3.835 0 6.62 2.782 6.62 6.615 0 .681-.092
 1.339-.271 1.97-1.47-1.726-3.669-2.75-6.133-2.809m6.133
 6.314c.179.629.271 1.29.271 1.97 0 3.831-2.785 6.611-6.62
 6.611l-11.278.002v-2.899a2.882 2.882 0 0 1
 2.879-2.879h8.446l.288-.015c2.412-.084 4.564-1.088 6.014-2.79" />
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
