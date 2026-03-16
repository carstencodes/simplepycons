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


class DicebearIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dicebear"

    @property
    def original_file_name(self) -> "str":
        return "dicebear.svg"

    @property
    def title(self) -> "str":
        return "DiceBear"

    @property
    def primary_color(self) -> "str":
        return "#0284C7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DiceBear</title>
     <path d="M1.5 0A1.5 1.5 0 0 0 0 1.5v21A1.5 1.5 0 0 0 1.5
 24h12.84a.99.99 0 0 0
 .87-1.468c-.986-1.777-1.929-3.346-2.523-4.024-1.69-1.933-9.626-.13-9.877-6.435-.016-.415.262-.777.655-.908l3.872-1.29c.226-.076.418-.23.547-.43.365-.569
 1.182-1.768 1.928-2.375.707-.574 1.85-1.301
 3.936-1.636.417-.067.749-.379.952-.75.488-.89 1.457-1.432 2.478-1.285
 1.332.192 2.249 1.483 2.048 2.883a.3.3 0 0 0 .094.276c.889.794 1.829
 1.894 2.759 3.137.596.797 1.921.393 1.921-.602V1.5A1.5 1.5 0 0 0 22.5
 0zm9.375 9.625a1.25 1.25 0 1 0 2.5 0 1.25 1.25 0 1 0-2.5 0" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dicebear/brand/blob/f14718'''

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
