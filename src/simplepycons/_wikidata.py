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


class WikidataIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wikidata"

    @property
    def original_file_name(self) -> "str":
        return "wikidata.svg"

    @property
    def title(self) -> "str":
        return "Wikidata"

    @property
    def primary_color(self) -> "str":
        return "#006699"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wikidata</title>
     <path d="M0 4.583v14.833h.865V4.583zm1.788
 0v14.833h2.653V4.583zm3.518 0v14.832H7.96V4.583zm3.547
 0v14.834h.866V4.583zm1.789 0v14.833h.865V4.583zm1.759
 0v14.834h2.653V4.583zm3.518 0v14.834h.923V4.583zm1.788
 0v14.833h2.653V4.583zm3.64 0v14.834h.865V4.583zm1.788
 0v14.834H24V4.583Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Wikid'''

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
