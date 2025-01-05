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


class DrizzleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "drizzle"

    @property
    def original_file_name(self) -> "str":
        return "drizzle.svg"

    @property
    def title(self) -> "str":
        return "Drizzle"

    @property
    def primary_color(self) -> "str":
        return "#C5F74F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Drizzle</title>
     <path d="M5.353 11.823a1.036 1.036 0 0 0-.395-1.422 1.063 1.063 0
 0 0-1.437.399L.138 16.702a1.035 1.035 0 0 0 .395 1.422 1.063 1.063 0
 0 0 1.437-.398l3.383-5.903Zm11.216 0a1.036 1.036 0 0 0-.394-1.422
 1.064 1.064 0 0 0-1.438.399l-3.382 5.902a1.036 1.036 0 0 0 .394
 1.422c.506.283 1.15.104 1.438-.398l3.382-5.903Zm7.293-4.525a1.036
 1.036 0 0 0-.395-1.422 1.062 1.062 0 0 0-1.437.399l-3.383 5.902a1.036
 1.036 0 0 0 .395 1.422 1.063 1.063 0 0 0
 1.437-.399l3.383-5.902Zm-11.219 0a1.035 1.035 0 0 0-.394-1.422 1.064
 1.064 0 0 0-1.438.398l-3.382 5.903a1.036 1.036 0 0 0 .394
 1.422c.506.282 1.15.104 1.438-.399l3.382-5.902Z" />
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
