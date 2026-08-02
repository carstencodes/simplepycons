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


class ZxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zx"

    @property
    def original_file_name(self) -> "str":
        return "zx.svg"

    @property
    def title(self) -> "str":
        return "zx"

    @property
    def primary_color(self) -> "str":
        return "#F11A7B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>zx</title>
     <path d="M22.036 18.327v5.673h-20.072v-5.673l6.152-6.56L2.4
 5.673V0h19.156v5.673l-5.716 6.094 6.153
 6.56h0.043Zm-10.058-10.677l1.855-1.977h-3.709l1.854 1.977Zm0
 8.235l-2.291 2.442h4.582l-2.291-2.442Z" />
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
