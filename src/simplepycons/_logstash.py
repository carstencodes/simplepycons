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


class LogstashIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "logstash"

    @property
    def original_file_name(self) -> "str":
        return "logstash.svg"

    @property
    def title(self) -> "str":
        return "Logstash"

    @property
    def primary_color(self) -> "str":
        return "#005571"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Logstash</title>
     <path d="M13.745 24h8.291v-9.164h-8.29zm-2.618
 0h.437v-9.164h-9.6A9.163 9.163 0 0011.127
 24m.438-9.164h-9.6V0h.873a8.727 8.727 0 018.727 8.727z" />
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
