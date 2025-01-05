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


class FaunaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fauna"

    @property
    def original_file_name(self) -> "str":
        return "fauna.svg"

    @property
    def title(self) -> "str":
        return "Fauna"

    @property
    def primary_color(self) -> "str":
        return "#3A1AB6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fauna</title>
     <path d="M17.864 5.034c-1.454.496-2.155 1.385-2.632
 2.77-.123.369-.43.778-.777 1.053l1.193 1.306-3.787-2.706L1.411 0s.754
 5.003 1.015 6.844c.185 1.298.5 1.88 1.5 2.47l.401.22
 1.724.928-1.024-.543 4.726 2.636-.031.07-5.087-2.407c.27.944.793
 2.761 1.016 3.564.238.865.508 1.18 1.331
 1.487l1.516.566.94-.378-1.194.81L2.28 24c3.963-3.76 7.319-5.097
 9.774-6.19 3.132-1.385 5.018-2.274 6.249-5.468.877-2.242 1.562-5.113
 2.432-6.222l1.855-2.423s-3.84 1.039-4.726 1.337z" />
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
