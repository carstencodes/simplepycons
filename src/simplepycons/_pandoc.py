#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class PandocIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pandoc"

    @property
    def original_file_name(self) -> "str":
        return "pandoc.svg"

    @property
    def title(self) -> "str":
        return "Pandoc"

    @property
    def primary_color(self) -> "str":
        return "#4093DA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pandoc</title>
     <path d="M4.259 0a.95.95 0 0 0-.925.837.74.74 0 0 0
 .75.837h1.953L3.778 23.163a.74.74 0 0 0 .75.837.95.95 0 0 0
 .924-.837l2.26-21.489h2.51Q9.095 12.419 7.964 23.163a.74.74 0 0 0
 .75.837.95.95 0 0 0 .925-.837l.997-9.489h8.372a.95.95 0 0 0
 .925-.837l.733-6.977a.76.76 0 0 0-.182-.591L15.988.245A.75.75 0 0 0
 15.422 0Zm7.638 1.674H14.9l.06.068-.403 3.84a.494.494 0 0 0
 .5.558h3.84l.06.067-.61 5.793h-7.534z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tarleb/pandoc-logo/blob/1c'''

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
