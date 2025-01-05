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


class TomlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "toml"

    @property
    def original_file_name(self) -> "str":
        return "toml.svg"

    @property
    def title(self) -> "str":
        return "TOML"

    @property
    def primary_color(self) -> "str":
        return "#9C4121"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TOML</title>
     <path d="M.014 0h5.34v2.652H2.888v18.681h2.468V24H.015V0Zm17.622
 5.049v2.78h-4.274v12.935h-3.008V7.83H6.059V5.05h11.577ZM23.986
 24h-5.34v-2.652h2.467V2.667h-2.468V0h5.34v24Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/toml-lang/toml/blob/625f62'''

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
