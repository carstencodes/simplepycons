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


class RocketIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rocket"

    @property
    def original_file_name(self) -> "str":
        return "rocket.svg"

    @property
    def title(self) -> "str":
        return "Rocket"

    @property
    def primary_color(self) -> "str":
        return "#D33847"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rocket</title>
     <path d="M23.735.238V.236a.248.248 0 0
 0-.2-.188c-.256-.04-6.336-.924-14.17 7.051a28.44 28.44 0 0 0-2.12
 2.576l-4.047 1.166a.246.246 0 0 0-.124.08l-2.856 3.5a.248.248 0 0 0
 .126.394l3.887
 1.096.484-.566c.178-.208.37-.4.574-.58l.54-.472-.38.608a5.556 5.556 0
 0 1-.482.66l-.52.606c.008.79.214 1.488.62 2.068L3.68
 19.653c-.148.16-.036.272.12.428l1.11
 1.086c.153.16.255.258.41.1l1.505-1.534c.34.122 1.162.334
 2.4.14l.75-.576c.212-.164.438-.312.672-.442l.644-.36-.514.53c-.187.192-.387.37-.6.534l-.62.476
 1.424 3.804a.246.246 0 0 0 .404.09l3.242-3.144a.248.248 0 0 0
 .072-.136l.698-4.108c.884-.78 1.78-1.686 2.66-2.694 5.072-5.806
 5.798-10.315 5.78-12.487-.008-.702-.094-1.094-.1-1.122h-.002zM16.49
 11.165c-1.274 1.296-3.1
 1.564-4.082.6-.98-.962-.744-2.794.53-4.09s3.1-1.566
 4.08-.602c.982.964.746 2.796-.528 4.092z" />
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
