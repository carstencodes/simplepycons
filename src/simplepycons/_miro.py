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


class MiroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "miro"

    @property
    def original_file_name(self) -> "str":
        return "miro.svg"

    @property
    def title(self) -> "str":
        return "Miro"

    @property
    def primary_color(self) -> "str":
        return "#050038"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Miro</title>
     <path d="M17.392 0H13.9L17 4.808 10.444 0H6.949l3.102 6.3L3.494
 0H0l3.05 8.131L0 24h3.494L10.05 6.985 6.949 24h3.494L17 5.494 13.899
 24h3.493L24 3.672 17.392 0z" />
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
