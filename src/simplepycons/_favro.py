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


class FavroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "favro"

    @property
    def original_file_name(self) -> "str":
        return "favro.svg"

    @property
    def title(self) -> "str":
        return "Favro"

    @property
    def primary_color(self) -> "str":
        return "#512DA8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Favro</title>
     <path d="M11.586 1.655a6.623 6.623 0 0 0-6.62 6.62v.773a7.503
 7.503 0 0 1 3.31 3.269V8.276a3.302 3.302 0 0 1 3.31-3.31A1.66 1.66 0
 0 0 13.24 3.31a1.66 1.66 0 0 0-1.656-1.655zm-9.93 7.448A1.66 1.66 0 0
 0 0 10.758c0 .91.745 1.655 1.655 1.655a3.302 3.302 0 0 1 3.31
 3.31v4.966c0 .91.745 1.655 1.655 1.655a1.66 1.66 0 0 0
 1.655-1.655v-4.966a6.623 6.623 0 0 0-6.62-6.621zm15.724 0a6.623 6.623
 0 0 0-6.622 6.621 6.623 6.623 0 0 0 6.622 6.621 6.583 6.583 0 0 0
 3.462-.979c.262.58.84.98 1.503.98A1.66 1.66 0 0 0 24 20.69v-9.93a1.66
 1.66 0 0 0-1.655-1.655c-.676 0-1.241.4-1.503.979a6.574 6.574 0 0
 0-3.462-.98zm0 3.311a3.303 3.303 0 0 1 3.31 3.31 3.303 3.303 0 0
 1-3.31 3.31 3.302 3.302 0 0 1-3.31-3.31 3.303 3.303 0 0 1 3.31-3.31z"
 />
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
