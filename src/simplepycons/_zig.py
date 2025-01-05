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


class ZigIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zig"

    @property
    def original_file_name(self) -> "str":
        return "zig.svg"

    @property
    def title(self) -> "str":
        return "Zig"

    @property
    def primary_color(self) -> "str":
        return "#F7A41D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zig</title>
     <path d="m23.53 1.02-7.686 3.45h-7.06l-2.98 3.452h7.173L.47
 22.98l7.681-3.607h7.065v-.002l2.978-3.45-7.148-.001 12.482-14.9zM0
 4.47v14.901h1.883l2.98-3.45H3.451v-8h.942l2.824-3.45H0zm22.117 0-2.98
 3.608h1.412v7.844h-.942l-2.98 3.45H24V4.47h-1.883z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ziglang/logo/blob/6446ba8e'''

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
