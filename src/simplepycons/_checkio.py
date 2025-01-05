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


class CheckioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "checkio"

    @property
    def original_file_name(self) -> "str":
        return "checkio.svg"

    @property
    def title(self) -> "str":
        return "CheckiO"

    @property
    def primary_color(self) -> "str":
        return "#008DB6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CheckiO</title>
     <path d="M10.846 8.886L24 2.932v13.82L9.621 21.068 0
 14.09l3.35-9.956 7.496 4.751v.001zm-4.582
 2.067l3.923-1.768-6.065-3.85 2.142 5.618zm-5.393
 2.44l4.842-2.187-2.179-5.717-2.662 7.904H.871zm22.526
 2.54V4.256l-5.96 7.37 5.96 4.307zm-12.865
 4.233l12.497-3.758-5.973-4.316-6.524 8.074zM.94 14.029l8.092
 5.867-3.106-8.124L.94 14.029zm21.722-9.826c-5.085 2.296-10.163
 4.6-15.25 6.895l9.445.284 5.805-7.178v-.001zM9.775
 20.143l6.608-8.173-9.844-.29 3.236 8.462v.001z" />
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
