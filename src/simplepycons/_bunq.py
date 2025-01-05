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


class BunqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bunq"

    @property
    def original_file_name(self) -> "str":
        return "bunq.svg"

    @property
    def title(self) -> "str":
        return "bunq"

    @property
    def primary_color(self) -> "str":
        return "#3394D7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>bunq</title>
     <path d="M16.414 14.62h1.103v-2.896a2.484 2.484 0 0 0-2.483-2.483
 2.484 2.484 0 0 0-2.482 2.483v2.897h1.103v-2.897c0-.837.618-1.517
 1.38-1.517.76 0 1.379.68 1.379 1.517zm-6.07-5.24h1.104v2.896a2.484
 2.484 0 0 1-2.482 2.483 2.484 2.484 0 0
 1-2.483-2.483V9.379h1.103v2.897c0 .837.618 1.517 1.38 1.517.76 0
 1.379-.68 1.379-1.517zM0 7.034V12c0
 .046.001.093.004.139H0v2.482h.965l.055-.48A2.76 2.76 0 0 0 5.518
 12a2.76 2.76 0 0 0-4.414-2.208V7.035zm2.69 3.172c.951 0 1.724.803
 1.724 1.793 0 .99-.773 1.793-1.725 1.793-.951
 0-1.724-.803-1.724-1.793 0-.99.773-1.793
 1.724-1.793zm18.552-.965A2.76 2.76 0 0 0 18.482 12a2.76 2.76 0 0 0
 4.414 2.207v2.758H24V12a2.15 2.15 0 0
 0-.004-.139H24V9.38h-.965l-.055.48a2.741 2.741 0 0
 0-1.738-.617zm.069.965c.951 0 1.724.803 1.724 1.793 0 .99-.773
 1.793-1.724 1.793-.952 0-1.725-.803-1.725-1.793 0-.99.773-1.793
 1.725-1.793Z" />
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
