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


class EventbriteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eventbrite"

    @property
    def original_file_name(self) -> "str":
        return "eventbrite.svg"

    @property
    def title(self) -> "str":
        return "Eventbrite"

    @property
    def primary_color(self) -> "str":
        return "#F05537"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Eventbrite</title>
     <path d="M10.542 5.81c2.653-.6 5.3.487 6.775 2.54L5.591
 11c.405-2.479 2.298-4.591 4.951-5.19zm6.84 9.746a6.47 6.47 0 0
 1-3.919 2.634c-2.67.604-5.335-.501-6.804-2.582l11.763-2.657
 1.915-.433L24 11.691a11.57 11.57 0 0 0-.305-2.333C22.205 3.04
 15.76-.9 9.303.558 2.846 2.017-1.18 8.322.31 14.642c1.491 6.319 7.935
 10.259 14.392 8.8 3.805-.86 6.765-3.402 8.25-6.638z" />
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
