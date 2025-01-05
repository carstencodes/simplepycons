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


class RemovedotbgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "removedotbg"

    @property
    def original_file_name(self) -> "str":
        return "removedotbg.svg"

    @property
    def title(self) -> "str":
        return "remove.bg"

    @property
    def primary_color(self) -> "str":
        return "#54616C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>remove.bg</title>
     <path d="m23.729 13.55-1.903-.995-9.134 4.776a1.497 1.497 0 0
 1-1.383.002l-9.137-4.778-1.903.995a.5.5 0 0 0 0 .888l11.499
 6.011a.495.495 0 0 0 .462 0l11.499-6.011a.5.5 0 0 0 0-.888zM.269
 10.447l11.499 6.013a.495.495 0 0 0 .462 0l11.499-6.013a.5.5 0 0 0
 0-.887l-11.5-6.012a.505.505 0 0 0-.462 0L.268 9.559a.5.5 0 0 0
 .001.887z" />
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
