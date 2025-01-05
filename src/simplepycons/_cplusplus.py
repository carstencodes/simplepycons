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


class CplusplusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cplusplus"

    @property
    def original_file_name(self) -> "str":
        return "cplusplus.svg"

    @property
    def title(self) -> "str":
        return "C++"

    @property
    def primary_color(self) -> "str":
        return "#00599C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>C++</title>
     <path d="M22.394
 6c-.167-.29-.398-.543-.652-.69L12.926.22c-.509-.294-1.34-.294-1.848
 0L2.26 5.31c-.508.293-.923 1.013-.923 1.6v10.18c0
 .294.104.62.271.91.167.29.398.543.652.69l8.816 5.09c.508.293 1.34.293
 1.848
 0l8.816-5.09c.254-.147.485-.4.652-.69.167-.29.27-.616.27-.91V6.91c.003-.294-.1-.62-.268-.91zM12
 19.11c-3.92 0-7.109-3.19-7.109-7.11 0-3.92 3.19-7.11 7.11-7.11a7.133
 7.133 0 016.156 3.553l-3.076 1.78a3.567 3.567 0 00-3.08-1.78A3.56
 3.56 0 008.444 12 3.56 3.56 0 0012 15.555a3.57 3.57 0
 003.08-1.778l3.078 1.78A7.135 7.135 0 0112
 19.11zm7.11-6.715h-.79v.79h-.79v-.79h-.79v-.79h.79v-.79h.79v.79h.79zm2.962
 0h-.79v.79h-.79v-.79h-.79v-.79h.79v-.79h.79v.79h.79z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/isocpp/logos/tree/64ef0370'''

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
