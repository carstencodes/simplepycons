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


class OnestreamIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "onestream"

    @property
    def original_file_name(self) -> "str":
        return "onestream.svg"

    @property
    def title(self) -> "str":
        return "OneStream"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OneStream</title>
     <path d="M23.457 8.42h-2.311a9.79 9.79 0 0 1 .676 3.58c0
 5.425-4.397 9.822-9.822 9.822a9.767 9.767 0 0 1-4.98-1.357 9.12 9.12
 0 0 0 5.625-6.457l.817-3.529a6.918 6.918 0 0 1 2.488-3.903 6.221
 6.221 0 0 1 1.52-.87 7.616 7.616 0 0 1 2.765-.51l1.642-.003C19.711
 2.063 16.094 0 12 0 5.372 0 0 5.373 0 12c0 1.247.19 2.448.543
 3.579h2.31A9.79 9.79 0 0 1 2.179 12c0-5.424 4.398-9.822 9.822-9.822
 1.819 0 3.52.495 4.98 1.357a9.118 9.118 0 0 0-5.625 6.457l-.816
 3.53a6.917 6.917 0 0 1-2.488 3.903 6.22 6.22 0 0
 1-1.52.869c-.737.295-1.655.51-2.887.51l-1.522.002C4.288 21.936 7.906
 24 12 24c6.628 0 12-5.373 12-12a12 12 0 0 0-.543-3.58Z" />
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
