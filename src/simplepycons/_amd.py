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


class AmdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amd"

    @property
    def original_file_name(self) -> "str":
        return "amd.svg"

    @property
    def title(self) -> "str":
        return "AMD"

    @property
    def primary_color(self) -> "str":
        return "#ED1C24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AMD</title>
     <path d="M18.324 9.137l1.559 1.56h2.556v2.557L24 14.814V9.137zM2
 9.52l-2 4.96h1.309l.37-.982H3.9l.408.982h1.338L3.432 9.52zm4.209
 0v4.955h1.238v-3.092l1.338
 1.562h.188l1.338-1.556v3.091h1.238V9.52H10.47l-1.592 1.845L7.287
 9.52zm6.283 0v4.96h2.057c1.979 0 2.88-1.046 2.88-2.472
 0-1.36-.937-2.488-2.747-2.488zm1.237.91h.792c1.17 0 1.63.711 1.63
 1.57 0 .728-.372 1.572-1.616 1.572h-.806zm-10.985.273l.791
 1.932H2.008zm17.137.307l-1.604 1.603v2.25h2.246l1.604-1.607h-2.246z"
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
