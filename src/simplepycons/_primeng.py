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


class PrimengIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "primeng"

    @property
    def original_file_name(self) -> "str":
        return "primeng.svg"

    @property
    def title(self) -> "str":
        return "PrimeNG"

    @property
    def primary_color(self) -> "str":
        return "#DD0031"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PrimeNG</title>
     <path d="M12 0 .784 3.984l1.711 14.772L12 24l9.506-5.244
 1.71-14.772ZM8.354 4.212h1.674L9.19 6.124l-2.51-.24Zm2.032
 0h1.315v6.812h-.717L5.843 9.112l-.717-2.988 4.308.35Zm1.794
 0h1.314l.953 2.261 4.427-.349-.717 2.988-5.14 1.912h-.837Zm1.673
 0h1.674L17.2 5.885l-2.51.239zM5.963 9.59l1.315.478 1.315 1.315
 1.076-.24-.837 1.196v3.704l-2.87-2.39zm11.955 0v4.063l-2.87
 2.39v-3.704l-.837-1.195 1.077.239 1.314-1.315zm-7.786
 1.536.596.36h2.384l.597-.36.953 1.437v5.388l-.715
 1.078-.835.838h-2.384l-.834-.838-.715-1.078v-5.388zm-2.854 4.08 1.554
 1.315v1.793L7.278 16.76Zm9.324 0v1.554l-1.553 1.554V16.52z" />
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
