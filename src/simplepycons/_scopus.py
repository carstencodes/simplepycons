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


class ScopusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scopus"

    @property
    def original_file_name(self) -> "str":
        return "scopus.svg"

    @property
    def title(self) -> "str":
        return "Scopus"

    @property
    def primary_color(self) -> "str":
        return "#E9711C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Scopus</title>
     <path d="M24 19.059l-.14-1.777c-1.426.772-2.945 1.076-4.465
 1.076-3.319 0-5.96-2.782-5.96-6.475 0-3.903 2.595-6.31 5.633-6.31
 1.917 0 3.39.303 4.792 1.075L24
 4.895c-1.286-.608-2.337-.889-4.698-.889-4.534 0-7.97 3.53-7.97 8.017
 0 5.12 4.09 7.924 7.9 7.924 1.916 0 3.506-.257
 4.768-.888zm-14.954-3.46c0-2.22-1.964-3.225-3.857-4.347C3.716 10.364
 2.15 9.756 2.15 8.12c0-1.215.889-2.548 2.642-2.548 1.519 0 2.57.234
 3.903 1.029l.117-1.847c-1.239-.514-2.127-.748-4.137-.748C1.8
 4.006.047 5.876.047 8.26c0 2.384 2.103 3.413 4.02 4.581 1.426.865
 2.922 1.45 2.922 2.992 0 1.496-1.333 2.571-2.922 2.571-1.566
 0-2.594-.35-3.786-1.075L0 19.176c1.215.56 2.454.818 4.16.818 2.385 0
 4.885-1.473 4.885-4.395z" />
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
