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


class LitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lit"

    @property
    def original_file_name(self) -> "str":
        return "lit.svg"

    @property
    def title(self) -> "str":
        return "Lit"

    @property
    def primary_color(self) -> "str":
        return "#324FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lit</title>
     <path d="M2.4 9.6l4.8 4.8V24l-4.8-4.8V9.6zm4.8-4.8v9.6L12
 9.6V0L7.2 4.8zM12 9.6v9.6l4.8-4.8V4.8L12 9.6zm4.8
 4.8V24l4.8-4.8V9.6l-4.8 4.8z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/lit/lit.dev/blob/5e59bdb00
b7a261d6fdcd6a4ae529e17f6146ed3/packages/lit-dev-content/site/images/f'''

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
