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


class ZodIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zod"

    @property
    def original_file_name(self) -> "str":
        return "zod.svg"

    @property
    def title(self) -> "str":
        return "Zod"

    @property
    def primary_color(self) -> "str":
        return "#3E67B1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zod</title>
     <path d="M19.088 2.477 24 7.606 12.521 20.485l-.925 1.038L0
 7.559l5.108-5.082h13.98Zm-17.434 5.2 6.934-4.003H5.601L1.619
 7.636l.035.041Zm12.117-4.003L3.333 9.7l2.149 2.588
 10.809-6.241-.2-.346 2.851-1.646-.365-.381h-4.806Zm7.52 2.834L8.257
 14.034h5.101v-.4h3.667l5.346-5.998-1.08-1.128Zm-7.129
 10.338H9.268l2.36 2.843 2.534-2.843Z" />
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
