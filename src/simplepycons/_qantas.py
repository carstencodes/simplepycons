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


class QantasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qantas"

    @property
    def original_file_name(self) -> "str":
        return "qantas.svg"

    @property
    def title(self) -> "str":
        return "Qantas"

    @property
    def primary_color(self) -> "str":
        return "#E40000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qantas</title>
     <path d="M0 3.47l.218.572c1.925 5.006 5.566 2.689 10.415
 7.139l.056.05c.652.599 1.1.044.888-.306a.76.76 0 0 1-.165-.532 6.7
 6.7 0 0 1 2.606 1.369l-.06.126c-.366.73-3.959.421-4 1.943a.969.969 0
 0 0 .607.923l.71.287a17.34 17.34 0 0 1 6.086 4.146.086.086 0 0
 1-.063.147.079.079 0 0 1-.054-.018 17.32 17.32 0 0
 0-8.173-3.61.467.467 0 0
 1-.39-.41c-.548-5.089-5.575-5.434-7.492-8.705l5.313 13.94H24L9.979
 6.449a10.022 10.022 0 0 0-7.045-2.98Z" />
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
