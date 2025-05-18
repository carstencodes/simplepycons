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


class GoogleTvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googletv"

    @property
    def original_file_name(self) -> "str":
        return "googletv.svg"

    @property
    def title(self) -> "str":
        return "Google TV"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google TV</title>
     <path d="M3.11 3.245A3.117 3.117 0 0 0 0 6.355V13.7a1.87 1.87 0 0
 0 1.878 1.878h2.588V5.124c0-.73.313-1.399.814-1.879zm3.944 0a1.87
 1.87 0 0 0-1.879 1.879V7.71h16.947v.021c.73 0 1.398.313
 1.878.814v-2.19a3.117 3.117 0 0 0-3.11-3.11zm12.48 5.176v10.455c0
 .73-.313 1.399-.814 1.879h2.17a3.117 3.117 0 0 0 3.11-3.11V10.3a1.87
 1.87 0 0 0-1.878-1.878zM0 15.475v2.17a3.117 3.117 0 0 0 3.11
 3.11h13.836a1.87 1.87 0 0 0 1.878-1.879V16.29H1.878c-.73
 0-1.398-.314-1.878-.814" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://partnermarketinghub.withgoogle.com/br'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partnermarketinghub.withgoogle.com/br'''

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
