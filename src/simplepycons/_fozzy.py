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


class FozzyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fozzy"

    @property
    def original_file_name(self) -> "str":
        return "fozzy.svg"

    @property
    def title(self) -> "str":
        return "Fozzy"

    @property
    def primary_color(self) -> "str":
        return "#F15B29"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fozzy</title>
     <path d="M14.494 20.48l-.998-2.095 5.787-11.273c.897 1.396 1.496
 3.092 1.496 4.888 0 3.99-2.594 7.382-6.285
 8.48zM12.998.029C5.615-.471-.47 5.615.028 12.998c.5 5.786 5.188
 10.475 10.974 10.973 7.383.5 13.468-5.586 12.97-12.969C23.471 5.216
 18.783.527 12.997.03zM7.112 4.717c1.297-.897 2.793-1.396
 4.39-1.496L8.807 8.409 7.112 4.717zm3.491 7.383l4.19-8.38c.798.3
 1.497.598 2.195 1.097L11.9 14.793 10.603 12.1zM3.221
 12c0-1.796.599-3.492 1.496-4.888l6.485 13.667C6.712 20.38 3.22 16.589
 3.22 12z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://fozzy.com/partners.shtml?tab=material'''

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
