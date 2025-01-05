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


class ThreeMIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "3m"

    @property
    def original_file_name(self) -> "str":
        return "3m.svg"

    @property
    def title(self) -> "str":
        return "3M"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>3M</title>
     <path d="M18.903 5.954L17.17 13.03l-1.739-7.076h-5.099v2.613C9.72
 6.28 7.56 5.706 5.558 5.674 3.12 5.641.563 6.701.469
 9.936h3.373c0-.977.747-1.536 1.588-1.523 1.032-.008 1.508.434 1.533
 1.124-.036.597-.387 1.014-1.525 1.014H4.303V12.9h1.03c.584 0
 1.399.319 1.431 1.155.04.995-.652 1.435-1.501
 1.443-1.517-.053-1.763-1.225-1.763-2.23H0c.015.677-.151 5.091 5.337
 5.059 2.629.025 4.464-1.085 5.003-2.613v2.342h3.455v-7.632l1.867
 7.634h3.018l1.875-7.626v7.634H24V5.954h-5.097zm-8.561
 7.06c-.429-.893-1.034-1.284-1.376-1.407.714-.319 1.09-.751
 1.376-1.614v3.021z" />
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
