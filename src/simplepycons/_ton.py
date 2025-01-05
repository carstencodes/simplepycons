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


class TonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ton"

    @property
    def original_file_name(self) -> "str":
        return "ton.svg"

    @property
    def title(self) -> "str":
        return "TON"

    @property
    def primary_color(self) -> "str":
        return "#0098EA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TON</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zM7.902 6.697h8.196c1.505 0 2.462 1.628 1.705
 2.94l-5.059 8.765a.86.86 0 0 1-1.488 0L6.199
 9.637c-.758-1.314.197-2.94 1.703-2.94zm4.844 1.496v7.58l1.102-2.128
 2.656-4.756a.465.465 0 0 0-.408-.696h-3.35zM7.9 8.195a.464.464 0 0
 0-.408.694l2.658 4.754 1.102 2.13V8.195H7.9z" />
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
