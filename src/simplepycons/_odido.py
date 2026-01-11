#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class OdidoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "odido"

    @property
    def original_file_name(self) -> "str":
        return "odido.svg"

    @property
    def title(self) -> "str":
        return "Odido"

    @property
    def primary_color(self) -> "str":
        return "#2C72FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Odido</title>
     <path d="M20.923 15.077a3.077 3.077 0 1 0 0-6.154 3.077 3.077 0 0
 0 0 6.154m-17.846 0a3.077 3.077 0 1 0 0-6.154 3.077 3.077 0 0 0 0
 6.154m3.692 0a3.077 3.077 0 0 0 0-6.154zm10.462 0a3.077 3.077 0 0 1
 0-6.154zm-3.693-6.154h-3.077v6.154h3.077z" />
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
