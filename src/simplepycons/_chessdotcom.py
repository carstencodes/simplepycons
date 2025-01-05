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


class ChessdotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chessdotcom"

    @property
    def original_file_name(self) -> "str":
        return "chessdotcom.svg"

    @property
    def title(self) -> "str":
        return "Chess.com"

    @property
    def primary_color(self) -> "str":
        return "#81B64C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chess.com</title>
     <path d="M12 0a3.85 3.85 0 0 0-3.875 3.846A3.84 3.84 0 0 0 9.73
 6.969l-2.79 1.85c0 .622.144 1.114.434
 1.649H9.83c-.014.245-.014.549-.014.925 0 .025.003.048.006.071-.064
 1.353-.507 3.472-3.62 5.842-.816.625-1.423 1.495-1.806 2.533a.33.33 0
 0 0-.045.084 8.124 8.124 0 0 0-.39 2.516c0 .1.216 1.561 8.038
 1.561s8.038-1.46
 8.038-1.561c0-2.227-.824-4.048-2.24-5.133-4.034-3.08-3.586-5.74-3.644-6.838h2.458c.29-.535.434-1.027.434-1.649l-2.79-1.836a3.86
 3.86 0 0 0 1.604-3.123A3.873 3.873 0 0 0
 13.445.275c-.004-.002-.01.004-.015.004A3.76 3.76 0 0 0 12 0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.chess.com/article/view/chess-com-'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.chess.com/article/view/chess-com-'''

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
