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


class RumahwebIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rumahweb"

    @property
    def original_file_name(self) -> "str":
        return "rumahweb.svg"

    @property
    def title(self) -> "str":
        return "Rumahweb"

    @property
    def primary_color(self) -> "str":
        return "#2EB4E3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rumahweb</title>
     <path d="M0
 12.149c.028-.275.148-.543.36-.753l7.182-7.092a.972.972 0 0 1
 .103-.091c.308-.265 1.807-1.473 3.743-1.553h.402c1.126.047 2.374.5
 3.61 1.731 2.534 2.542 5.076 5.077 7.615 7.615 1.14 1.14 1.198
 2.585.642 3.795a4.043 4.043 0 0 1-.819 1.173 3.973 3.973 0 0
 1-1.188.823c-1.208.537-2.646.458-3.86-.753l-.053-.056-6.222-6.061a.93.93
 0 0 0-1.03-.207 1.6 1.6 0 0
 0-.499.325c-.15.141-.272.304-.352.473-.136.291-.141.627.085.907l6.806
 6.802c.483.485.481 1.27-.005 1.752a1.246 1.246 0 0
 1-1.758-.004l-6.889-6.89c-.999-1.138-1.021-2.48-.488-3.614a4.087
 4.087 0 0 1 2.185-2.05c1.183-.468 2.553-.365 3.679.731 2.103 2.044
 4.197 4.098 6.304 6.138.359.356.76.392 1.085.248a1.6 1.6 0 0 0
 .76-.763c.154-.335.148-.726-.146-1.018-2.54-2.533-5.07-5.077-7.615-7.605-1.977-1.973-4.04-.345-4.347-.082l-7.178
 7.086a1.245 1.245 0 0 1-1.757-.003A1.248 1.248 0 0 1 0 12.402v-.253Z"
 />
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
