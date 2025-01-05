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


class ElasticsearchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "elasticsearch"

    @property
    def original_file_name(self) -> "str":
        return "elasticsearch.svg"

    @property
    def title(self) -> "str":
        return "Elasticsearch"

    @property
    def primary_color(self) -> "str":
        return "#005571"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Elasticsearch</title>
     <path d="M13.394 0C8.683 0 4.609 2.716 2.644 6.667h15.641a4.77
 4.77 0 0 0 3.073-1.11c.446-.375.864-.785 1.247-1.243l.001-.002A11.974
 11.974 0 0 0 13.394 0zM1.804 8.889a12.009 12.009 0 0 0 0
 6.222h14.7a3.111 3.111 0 1 0 0-6.222zm.84 8.444C4.61 21.283 8.684 24
 13.395 24c3.701 0 7.011-1.677 9.212-4.312l-.001-.002a9.958 9.958 0 0
 0-1.247-1.243 4.77 4.77 0 0 0-3.073-1.11z" />
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
